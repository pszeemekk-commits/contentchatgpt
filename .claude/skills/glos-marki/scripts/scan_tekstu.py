#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scan mechaniczny tekstu marki "Niedzwiedz na Szlaku".

Po co to istnieje: model nie potrafi rzetelnie policzyc wzorcow we wlasnym
tekscie. W tescie z 2026-08-05 model zadeklarowal 1 kontrast "X, nie Y",
a w tekscie byly 2. Liczenie oddajemy skryptowi, zeby wynik nie zalezal od
tego, czy ten sam proces, ktory napisal tekst, uczciwie sie z niego rozliczy.

Uzycie:
    python scan_tekstu.py plik.md
    python scan_tekstu.py plik.md --od 215 --do 349     # tylko zakres linii
    cat tekst.txt | python scan_tekstu.py               # ze stdin

WAZNE: skanuj wylacznie sam tekst docelowy (slajdy + opis pod post).
Sekcje robocze - pakiet wsadu, cytaty ze zrodel, kontrola - zawieraja cudze
slowa i naglowki, ktore zafalszuja wynik. Do tego sluza --od / --do.

Kod wyjscia: 0 = wszystkie twarde limity spelnione, 1 = cos przekroczone.
"""

import argparse
import io
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MARKETINGOWE = r"wyjątkow|niesamowit|unikaln|przełomow|rewolucyjn|niezwykł"
AI_JARGON = r"adres uwagi|przestrzeń decyzyjn|w dzisiejszych czasach|kluczowe jest|warto pamiętać"
MINDFULNESS = (
    r"oddech|napięci\w* w ciele|tu i teraz|uważność|"
    r"zauważ,? (jak|kiedy)|złap się|poczuj,? jak"
)
ABSTRAKCJE = (
    r"mechanizm|wzorzec|zapis|schemat|rana|podswiadomość|podświadomość|"
    r"umysł|lęk|wstyd|nawyk|program|silnik|trauma|ładun\w*|emocj\w*|napięci\w*"
)

# Kalka z angielskiego: abstrakcja + czasownik miejsca. "Wiedza siedzi w glowie",
# "emocja lezy glebiej", "rozumienie mieszka w ciele" - po angielsku naturalne,
# po polsku brzmi jak tlumaczenie. Przemek zglaszal to wielokrotnie.
# Wyjatek: "co siedzi pod spodem" to jego potwierdzona fraza (KOR-020) - nie liczymy.
KALKA_MIEJSCA = (
    r"(?:" + ABSTRAKCJE + r"|wiedz\w*|rozumieni\w*|emocj\w*|ładun\w*|"
    r"napięci\w*|problem\w*|reakcj\w*|prawd\w*|odpowiedź|impuls\w*)"
    r"\s+(?:\w+\s+){0,2}?(?:siedzi|siedzą|leży|leżą|mieszka|mieszkają|"
    r"znajduje się|znajdują się)(?!\s+pod\s+spodem)"
    # "w tobie siedzi cos" - ta sama kalka z zaimkiem zamiast rzeczownika,
    # i przy okazji abstrakcja: czytelnik nie wie, co to "cos"
    r"|siedzi\s+coś|siedzą\s+w\s+tobie"
    # "emocja, ktora nie wyszla" - emocja nie jest podmiotem, ktory sam wychodzi.
    # Po polsku to czlowiek jej z siebie nie wypuscil.
    r"|(?:emocj|napięci|złoś|żal|ból)\w*[^.!?]{0,30}?nie\s+wysz\w+"
)

# Deiktyki, ktore czytelnik moze odczytac tylko wtedy, gdy zgadnie, o co chodzi.
# Nie wszystkie sa bledem - "sam tam nie zejdziesz" Przemek zatwierdzil.
# Dlatego miekkie: skrypt wypisuje, decyzje podejmujesz przy Tescie nazwania.
DEIKTYKI = (
    r"\b(?:tam na dole|na dole|to drugie|tym drugim|ta sama|tej samej|"
    r"to wszystko|czegoś takiego|coś takiego|tej pracy|tego procesu|"
    r"po tej stronie|po drugiej stronie|tamtej sytuacji|tamtego momentu|"
    r"tamtej chwili|tamtym miejscu|w tym miejscu|tamtej rzeczy)\b"
)


def zdania(t):
    parts = re.split(r"(?<=[.!?])\s+", t)
    return [p.strip() for p in parts if p.strip()]


def ctx(t, m, pad=45):
    a = max(0, m.start() - pad)
    b = min(len(t), m.end() + pad)
    return "..." + " ".join(t[a:b].split()) + "..."


FUNKCYJNE = {
    "nie", "do", "na", "w", "we", "z", "ze", "o", "po", "za", "przy", "od",
    "dla", "i", "a", "to", "się", "tak", "tylko", "już", "ci", "cię", "mi",
    "ten", "ta", "te", "tym", "tej", "go", "mu", "jak", "co", "być",
}


def klasyfikuj_nie(t, m):
    """Odroznia kontrast 'X, nie Y' od anafory 'nie X, nie X'.

    Powtorzenie tego samego czasownika to rytm (i czesto potwierdzona fraza
    Przemka), nie zakazana dychotomia - nie liczymy go do limitu.

    Przyimki i zaimki trzeba odfiltrowac, inaczej 'daza do spojnosci ...,
    nie do sukcesu' wyglada jak powtorzenie przez wspolne 'do' - a jest
    dokladnie tym kontrastem, ktorego limit pilnujemy.
    """
    przed = [w for w in re.findall(r"\w+", t[max(0, m.start() - 70):m.start()].lower())
             if w not in FUNKCYJNE and len(w) > 2]
    po = [w for w in re.findall(r"\w+", t[m.start():m.start() + 70].lower())
          if w not in FUNKCYJNE and len(w) > 2]
    if przed and po and po[0] in przed[-5:]:
        return "powtorzenie"
    return "kontrast"


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("plik", nargs="?", help="plik z tekstem; brak = stdin")
    ap.add_argument("--od", type=int, default=1, help="pierwsza linia zakresu")
    ap.add_argument("--do", type=int, default=None, help="ostatnia linia zakresu")
    ap.add_argument("--cicho", action="store_true", help="bez cytatow, sama tabela")
    a = ap.parse_args()

    if a.plik:
        with io.open(a.plik, encoding="utf-8") as f:
            linie = f.readlines()
        linie = linie[a.od - 1:a.do]
        t = "".join(linie)
    else:
        t = sys.stdin.read()

    # naglowki markdown i separatory nie sa tekstem docelowym
    tekst = "\n".join(
        l for l in t.splitlines()
        if not l.lstrip().startswith("#") and l.strip() not in ("---", "___")
    )

    znaleziska = []

    def sprawdz(nazwa, limit, matches, twarde=True):
        znaleziska.append((nazwa, limit, matches, twarde))

    sprawdz("dlugi myslnik —", 0,
            list(re.finditer(r"—", tekst)))
    sprawdz("'ale'", 1,
            list(re.finditer(r"(?<![\wĄ-ż])ale(?![\wĄ-ż])", tekst, re.I)))
    sprawdz("'Ze' na poczatku zdania", 0,
            list(re.finditer(r"(?:^|(?<=[.!?]\s))Że\s", tekst)))
    sprawdz("'To nie X. To Y.'", 0,
            list(re.finditer(r"[Tt]o nie [^.!?]{1,90}[.!?]\s+To\s", tekst)))
    sprawdz("'nie dlatego... tylko'", 0,
            list(re.finditer(r"nie dlatego[^.!?]{0,70}tylko", tekst, re.I)))

    nie_all = list(re.finditer(r",\s*nie\s+\w", tekst))
    kontrasty = [m for m in nie_all if klasyfikuj_nie(tekst, m) == "kontrast"]
    powtorzenia = [m for m in nie_all if klasyfikuj_nie(tekst, m) == "powtorzenie"]
    sprawdz("kontrast 'X, nie Y'", 1, kontrasty)

    sprawdz("przymiotniki marketingowe", 0,
            list(re.finditer(MARKETINGOWE, tekst, re.I)))
    sprawdz("AI-jargon", 0, list(re.finditer(AI_JARGON, tekst, re.I)))
    sprawdz("rejestr mindfulness (wrog marki)", 0,
            list(re.finditer(MINDFULNESS, tekst, re.I)))
    sprawdz("emoji / wykrzykniki", 0,
            list(re.finditer(r"[\U0001F300-\U0001FAFF☀-➿!]", tekst)))
    sprawdz("kalka 'X siedzi/lezy w Y'", 0,
            list(re.finditer(KALKA_MIEJSCA, tekst, re.I)))
    sprawdz("deiktyki bez nazwy (do oceny)", 0,
            list(re.finditer(DEIKTYKI, tekst, re.I)), twarde=False)

    # abstrakcja jako podmiot czasownika akcji
    abstr = list(re.finditer(
        r"(?:^|(?<=[.!?]\s)|(?<=\bTwoj[aeą]\s)|(?<=\bTwój\s))(?:[TtNn]?[oena]\s+|Ten\s+)?"
        r"(?:" + ABSTRAKCJE + r")\w*\s+(?!się\s+nazywa)\w+(?:e|a|ą|ają|uje|i)\b",
        tekst, re.I))
    sprawdz("abstrakcja jako podmiot (do oceny)", 0, abstr, twarde=False)

    # wyliczanka: 3+ kolejne zdania ponizej 5 slow
    zd = zdania(tekst)
    seria, serie = 0, 0
    for z in zd:
        if len(z.split()) < 5:
            seria += 1
            if seria == 3:
                serie += 1
        else:
            seria = 0
    # Miekkie, nie twarde: seria krotkich zdan to takze autentyczny rejestr
    # Przemka z GLOS_SUROWY ("Mniejsza. I popatrz na to.", "Dzis bedzie
    # niegrzecznie. Do dziela."). Test z 2026-08-10 pokazal, ze twardy limit
    # oblewa jego wlasne, kanoniczne teksty. GLOS_SUROWY jest zrodlem nadrzednym
    # wobec sformulowania reguly, wiec skrypt wypisuje serie do oceny,
    # a Ty rozstrzygasz, czy to rytm (zostaw) czy staccato AI (przepisz).
    znaleziska.append(("wyliczanka krotkich zdan (3+ pod rzad)", 0, [None] * serie, False))

    print("\n=== SCAN MECHANICZNY ===")
    print(f"{'kryterium':42s} {'limit':>6s} {'jest':>6s}  wynik")
    print("-" * 72)
    blad = False
    for nazwa, limit, ms, twarde in znaleziska:
        n = len(ms)
        ok = n <= limit
        if not ok and twarde:
            blad = True
        status = "ok" if ok else ("PRZEKROCZONE" if twarde else "sprawdz recznie")
        print(f"{nazwa:42s} {limit:>6d} {n:>6d}  {status}")

    if powtorzenia:
        print(f"\n(pominieto {len(powtorzenia)} powtorzen 'nie X, nie X' - to rytm/anafora,")
        print(" nie zakazana dychotomia; sprawdz ponizej, czy klasyfikacja sie zgadza)")

    if not a.cicho:
        for nazwa, limit, ms, twarde in znaleziska:
            realne = [m for m in ms if m is not None]
            if len(realne) > limit:
                print(f"\n--- {nazwa} ---")
                for m in realne:
                    print("  " + ctx(tekst, m))
        for m in powtorzenia:
            print("\n--- pominiete jako powtorzenie ---\n  " + ctx(tekst, m))

    zd_dl = [len(z.split()) for z in zd]
    if zd_dl:
        print(f"\nZdan: {len(zd)}, srednia dlugosc: {sum(zd_dl)/len(zd_dl):.1f} slow, "
              f"najkrotsze {min(zd_dl)}, najdluzsze {max(zd_dl)}")
        print("Porownaj te liczby z cytatem rytmu z GLOS_SUROWY.md wybranym w Bramce Glosu.")

    print("\nWynik: " + ("SA PRZEKROCZENIA - popraw i przeskanuj ponownie"
                         if blad else "wszystkie twarde limity spelnione"))
    return 1 if blad else 0


if __name__ == "__main__":
    sys.exit(main())
