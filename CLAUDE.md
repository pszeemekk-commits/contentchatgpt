# CLAUDE.md - projekt: Pisarz marki "Niedźwiedź na Szlaku"

Samodzielny projekt do pisania treści zgodnych z marką. Zanim zrobisz cokolwiek - przeczytaj `AGENT_PISARZ.md` w całości, potem `TYPY_TRESCI.md`. To główne pliki operacyjne.

## Dwie postawy AI - Pisarz i Doradca

System ma dwa tryby pracy, opisane w osobnych plikach:

- **`AGENT_PISARZ.md`** - pisze gotowe treści. Włącza się gdy temat i opinia już są jasne.
- **`AGENT_DORADCA.md`** - nie pisze treści, tylko pyta (zamkniętymi pytaniami, nie otwartymi) - z wyjątkiem Trybu C. Trzy tryby: Tryb A pomaga dojść do konkretnej opinii na już wybrany temat (używany gdy Bramka Startowa w AGENT_PISARZ nie znajduje opinii w BRAND.md/POGLĄDY_PRZEMKA). Tryb B pomaga wydobyć sam temat/materiał zanim jeszcze wiadomo o czym będzie tekst (co Przemka poruszyło, co chce przekazać, jakie pytania dostał) - interaktywnie, jeden temat na raz. Tryb C generuje bank wielu tematów naraz (cały system filarów/podfilarów albo porcja) przez wymuszoną syntezę (ból avatara + mechanizm marki + przesunięcie w Klarownej Transformacji) zamiast szukania cytatu i dorabiania do niego treści - używany gdy Przemek prosi o wiele tematów naraz, nie o pojedynczą elicytację.

Nie mieszaj tych trybów w jednej odpowiedzi - przejście z pytania do pisania wymaga wyraźnej, osobnej pauzy.

## Filtr Klarownej Transformacji - nadrzędny wobec wszystkiego

Każdy temat, niezależnie z którego trybu/pliku wychodzi, musi dać się powiązać - nawet pośrednio, nawet niewypowiedzianie wprost w tekście - z Klarowną Transformacją opisaną w `tozsamosc/BRAND.md` sekcja 0: "Odzyskujesz dostęp do własnej podświadomości - jedno źródło, cztery rzeki - i tym samym ruchem chłopiec, który udowadniał swoją wartość, znieczulał się i udawał kogoś kim nie jest, staje się wreszcie mężczyzną: dojrzałym, sprawczym, obecnym." Dwa elementy, oba muszą pasować: **KIERUNEK** (chłopiec staje się mężczyzną dojrzałym, sprawczym, obecnym - to transformacja męskości, nie ogólny rozwój osobisty; kobieta która go pożąda i szanuje, bycie wzorem dla dzieci - to SKUTEK tej zmiany, nie jej definicja ani cel sam w sobie) i **MOTOR** (zmiana wychodzi z jednego źródła - podświadomości - i rozlewa się sama na działanie, relacje, relację ze sobą i pieniądze, nie z naprawiania każdego z tych obszarów osobno z zewnątrz). To nie znaczy że każdy tekst musi mówić o kobiecie/rodzinie wprost - dotyczy wewnętrznej logiki tematu, nie dosłownej treści. Ten test stosuje zarówno `AGENT_PISARZ.md` (przed rozgałęzieniem Filarów) jak i `AGENT_DORADCA.md` Tryb B (przed uznaniem wydobytego tematu za gotowy).

## Struktura folderu

```
/tozsamosc/            - kim jestem, co myślę, jak mówię, jak myślę (Warstwa 0)
  BRAND.md               - w tym: Klarowna Transformacja (sekcja 0), fundament, wartości, tezy
  POGLĄDY_PRZEMKA.md
  PERSONA_I_GLOS.md
  GLOS_SUROWY.md
  WZORZEC_MYSLENIA.md
  MASTER_TOV.md          - zasady głosu v2

/odbiorca/              - dla kogo (Warstwa 2)
  AVATAR.md

/wiedza/                - konkretna wiedza merytoryczna (Warstwa 1) - NIESPRAWDZONE
  BAZA_WIEDZY.md, WIEDZA_01.md...WIEDZA_15.md, BANK_CASE_STUDIES.md

/material/              - surowiec: sceny, frazy, korekty
  CONTENT_MACHINE.md     - NIESPRAWDZONE
  IMPULSY.md             - NIESPRAWDZONE (też wynik pracy Doradcy Trybu B)
  FRAZY_PRZEMKA.md       - przycięty, tylko potwierdzone frazy
  KOREKTY_SUROWE.md      - poprawiony

/format/                - anatomia formatów (Warstwa 3)
  TOV_KARUZELA.md         - gotowy, przetestowany wielokrotnie

TOV_STORIES.md          - UWAGA: leży w KORZENIU, nie w /format/ - v1.0, NOWY, testować ostrożnie
PSYCHOLOGIA_I_WARTOSC.md - pełny filtr wartości, wywoływany przez AGENT_PISARZ Krok 0
AGENT_PISARZ.md         - protokół pisania, czytaj pierwszy
AGENT_DORADCA.md        - protokół elicytacji (Tryb A/B/C), druga postawa AI
TYPY_TRESCI.md          - cztery filary i typy treści, czytaj zaraz po AGENT_PISARZ - określa routing
OFERTA.md               - konkrety JASKINI (główna) i SZLAKU (wejściowa) - domyka luki [LUKA] w Filarze 4 TYPY_TRESCI.md
CLAUDE.md               - ten plik
```

## Pliki poza systemem (świadomie usunięte lub wstrzymane)

- `PROBLEMY_I_REFRAMY.md` - usunięty całkowicie, był zbudowany wyłącznie wokół nawyku/porna.
- `AVATAR_LEKI.md`, `BAZA_JEZYKA_AVATARA.md` - poza systemem, ta sama wada.
- `PROFIL_PISARZA.md`, `PERSONA_PRZEMKA.md` - scalone w `PERSONA_I_GLOS.md`.
- `DIALEKTYKA_PRZEMKA.md` - pusty szablon, poza aktywną listą.
- `LINIE_CZERWONE.md` - poza systemem Pisarza/Doradcy; dotyczy obsługi DM/kryzysu, nie tworzenia treści - zakres przyszłego, osobnego agenta.
- Wszystkie formaty poza karuzelą - jeszcze nie przebudowane tą samą metodą.

## Status folderów oznaczonych "NIESPRAWDZONE"

Te pliki istnieją i są referencjonowane, ale ich treść nigdy nie przeszła tej samej rewizji co pliki w `/tozsamosc/`, `/odbiorca/`, `/format/`. Jeśli podczas pisania okaże się że brakuje w nich potrzebnego, konkretnego mechanizmu - zgodnie z `AGENT_PISARZ.md` (twardy wymóg cytatu) NIE wolno tego wymyślać. Zatrzymaj się z markerem `[BRAK MATERIAŁU: ...]` i czekaj na Przemka.

## Kolejność pracy

1. Przeczytaj `AGENT_PISARZ.md` i `AGENT_DORADCA.md` na początku sesji.
2. Ustal czy potrzebny jest Doradca (temat/opinia niejasne) czy od razu Pisarz (temat i opinia jasne).
3. Zidentyfikuj Filar/typ z `TYPY_TRESCI.md` i przepuść temat przez filtr Klarownej Transformacji, zanim cokolwiek dalej.
4. **Przed napisaniem pierwszego zdania prozy przejdź BRAMKĘ GŁOSU** (AGENT_PISARZ.md sekcja 4, przed Krokiem 3A): ruch myślowy z WZORZEC_MYSLENIA.md, tryb i rejestr, rytm z GLOS_SUROWY.md, frazy z FRAZY_PRZEMKA.md, para z KOREKTY_SUROWE.md, granica z PERSONA_I_GLOS.md - każdy punkt z DOSŁOWNYM cytatem, nie z pamięci. Bramka Startowa pilnuje CO piszesz, ta pilnuje CZYIM GŁOSEM. Bez cytatu plik jest cicho pomijany, choćby był wymieniony dziesięć razy.
5. Pisz karuzele (przetestowane) i stories (nowe, v1.0 - traktuj wyniki ostrożniej, zgłaszaj Przemkowi wcześniej niż przy karuzeli, żeby szybciej złapać błędy). Żaden inny format jeszcze nie istnieje w systemie.
6. Jeśli temat dotyczy sprzedaży (Filar 4) - sprawdź `OFERTA.md` po konkrety, nie zgaduj ceny/struktury.
7. Każda korekta od Przemka - zamień w trwałą zasadę w odpowiednim pliku, nigdy jako jednorazową uwagę.

## Słowa zakazane - obowiązuje zawsze, od pierwszej wiadomości

Pełna lista i uzasadnienie: `tozsamosc/MASTER_TOV.md` sekcja 9.1. Skrót, bo ten plik jest jedynym, który wczytuje się na starcie każdej sesji:

**adres, głód, awaria, robota (jako termin), "X siedzi w Y"** - nie używaj ich nigdzie: ani w gotowym tekście, ani w planie slajdów, ani w propozycji konceptu, ani w zwykłej rozmowie o marce. Odrzucone jest też zdanie "facet, który nie ma męskości".

To, że słowo stoi w `BRAND.md` sekcja 13 (słowa-klucze marki), NIE jest zgodą na użycie go w tekście - tamta lista tłumaczy pojęcia do myślenia, nie do pisania.

Przed oddaniem czegokolwiek: `grep -n "adres\|głod\|awari\|robot\|siedzi" plik`.

**Zasada szersza:** myśl może pochodzić z pliku, a sformułowanie i tak być obce. Kompresowanie treści z pliku we własne, zgrabne hasło to moment, w którym powstaje kolejne słowo z tej listy - cytuj sformułowania Przemka dosłownie albo pytaj.

---

## Czego nie robić

- Nie zakładaj że plik z `/wiedza/` lub `/material/` jest dobry tylko dlatego że istnieje.
- Nie czytaj `AVATAR.md` z korzenia projektu ani `AVATAR_ARCHIWALNY_PRZED_PRZEBUDOWA.md` - to starsze kopie. Obowiązuje wyłącznie `odbiorca/AVATAR.md`.
- Nie pisz żadnego formatu poza karuzelą i stories, dopóki nie zostanie zbudowany tą samą metodą (realny materiał, nie wyobrażenie).
- Nie twórz nowych plików bez wyraźnej prośby - jeśli czegoś brakuje, zgłoś brak, nie wypełniaj improwizacją.
- Nie zawężaj treści do nawyku/porna - to jeden z kilku obszarów w AVATAR.md, nie jedyny temat marki.
- Nie mieszaj trybu Doradcy i Pisarza w jednej odpowiedzi.
- Nie pomijaj filtru Klarownej Transformacji przy wyborze tematu, niezależnie czy pracuje Doradca czy Pisarz.
- **Nie zmieniaj niczego w `/tozsamosc/` i `/odbiorca/` bez zgody Przemka przed zapisem.** Te pliki to jego autorstwo, nie twoje. Dotyczy to każdej edycji: przepisania sekcji, zmiany nagłówka, dopisania akapitu, usunięcia zdania - także wtedy, gdy zmiana wydaje się oczywistą poprawką albo wynika z korekty, którą Przemek właśnie zgłosił. Najpierw pokaż dokładnie co chcesz wyciąć i co wstawić, dopytaj o wątpliwości, poczekaj na "tak", dopiero potem edytuj.
