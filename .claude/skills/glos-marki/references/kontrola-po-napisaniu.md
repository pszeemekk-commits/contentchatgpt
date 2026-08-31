# Kontrola po napisaniu

Przejdź to po napisaniu draftu, przed pokazaniem czegokolwiek Przemkowi. Każdy punkt jako osobny, wypisany wynik — nie „w głowie". Sens tego kroku polega na tym, że wynik jest widoczny: kontrola, której nie widać, nie odróżnia się od kontroli, której nie było.

## 1. Test ruchu myślowego

Zadeklarowałeś w Bramce Głosu jeden ruch z `WZORZEC_MYSLENIA.md`. Sprawdź, czy faktycznie zaszedł:

- **Wskaż konkretny slajd/akapit**, zacytuj z niego zdanie i dopisz jednym zdaniem, na czym tam polega ten ruch.
- „Cały tekst jest w tym duchu" nie jest odpowiedzią. Ruch myślowy dzieje się w konkretnym miejscu albo nie dzieje się wcale.

## 2. Frazy

Czy obie frazy z tabeli `FRAZY_PRZEMKA.md` są w tekście dosłownie, czy zostały po drodze wygładzone? Wygładzona fraza to fraza nieużyta — cała jej wartość leży w tym, że to jego sformułowanie, nie Twoje.

## 3. Rytm

Przeczytaj cytat z `GLOS_SUROWY.md` i swój tekst po kolei. Nazwij różnicę konkretnie — długość zdań, tempo, gdzie stoją kropki. „Brzmi podobnie" nie jest obserwacją. Jeśli u niego zdania mają po 15-25 słów, a u Ciebie po cztery, pocięte kropkami dla efektu, to jest różnica, którą słychać.

## 4. Korekta

Czy błąd z pary AI→Przemek, którą wybrałeś, wrócił mimo wszystko? Zacytuj miejsce, jeśli tak.

## 5. Zero-Fiction

Każdy szczegół z życia Przemka musi mieć pokrycie w `material/CONTENT_MACHINE.md`, `wiedza/BANK_CASE_STUDIES.md`, `tozsamosc/PERSONA_I_GLOS.md` albo bezpośrednio od niego w tej rozmowie.

- Fakt bez pokrycia: usuń albo uogólnij.
- **Motywacji i emocji nigdy się nie domyślasz.** Fakt możesz znać z pliku; co ten fakt dla niego znaczył — pytasz. „Zrobił to, bo się bał" bez potwierdzenia to zmyślenie, nawet jeśli brzmi prawdopodobnie.
- To samo dotyczy avatara: opisuj postawę i priorytet wynikające z `AVATAR.md`, nie wymyśloną scenkę z jego poranka.

## 6. Jedna nić

Wypisz wszystkie metafory i systemy pojęć użyte w tekście. Zostaje jeden — ten z pakietu. Każdy inny: czy tłumaczy pojęcie centralne (zostaje), czy jest osobnym systemem, który sam siebie tłumaczy i konkuruje o uwagę (wytnij)?

To, że coś jest prawdziwą tezą marki, nie znaczy, że pasuje do tego tekstu. `BRAND.md` ma wiele prawdziwych, osobnych wątków — jeden tekst niesie jeden z nich. Kilka kanonicznych metafor w jednym tekście czyta się jak przypadkowe skoki, choć każdy skok da się formalnie uzasadnić cytatem.

## 7. Test nieznajomego

Czytelnik widzi wyłącznie ten jeden tekst. Nie zna plików źródłowych, nie zna życia Przemka, nie czytał poprzednich postów.

- Czy pada termin niewprowadzony wcześniej w tym tekście?
- Czy każdy zaimek i odniesienie („ona", „to", „wtedy") ma wcześniejsze zdanie, które go ustanawia?
- Czy zamknięcie ląduje na konkretnym fakcie, zachowaniu albo przyczynie — czy na poetyckiej metaforze, której nikt nie rozpakował?
- Czy zamknięcie korzysta wyłącznie z tego, co padło w TYM tekście? Prawdziwy mechanizm z bazy, wrzucony na końcu bez wcześniejszego wprowadzenia, czyta się jak wrzutka znikąd, mimo że ma pokrycie.
- Czy nazywasz rzeczy wprost? Peryfraza w rodzaju „to, czego on pilnuje" jest dla czytelnika pustką — nazwij to w tym samym zdaniu albo wytnij zdanie.

## 7a. Test nazwania (twardy)

Przejdź tekst zdanie po zdaniu i dla każdego „to", „tam", „go", „ten drugi", „ta sama X"
wskaż rzeczownik, do którego się odnosi, i numer zdania, w którym on stoi. Jeśli rzeczownik
jest dalej niż jedno zdanie wstecz albo nie ma go wcale — nazwij go w tym zdaniu.

Nagłówki traktuj osobno i surowiej: czyta się je pierwsze, więc zaimek w nagłówku
odnoszący się do czegoś z tekstu pod spodem jest zawsze błędem.

To jest osobny punkt od Testu nieznajomego, bo tam pytanie brzmi „czy termin był
wprowadzony", a tu „czy da się wskazać palcem słowo". Drugie wypada w praktyce częściej
i to ono w sesji z 10 sierpnia 2026 zawróciło cztery slajdy z rzędu.

## 8. Scan językowy

Zastosuj skill `natural-polish-copy-fable-updated` w całości — obowiązuje przy każdym polskim tekście, także bez wyraźnej prośby.

Wzorce mechaniczne liczy skrypt, nie Ty:

```bash
python .claude/skills/glos-marki/scripts/scan_tekstu.py <plik> --od <linia> --do <linia>
```

Zakres linii ma obejmować **wyłącznie tekst docelowy** — slajdy i opis pod post. Pakiet wsadu, cytaty ze źródeł i ta kontrola zawierają cudze słowa i zafałszują wynik.

Co sprawdza i jakie są limity: długi myślnik 0, „ale" maksymalnie 1, „Że" na początku zdania 0, „To nie X. To Y." 0, „nie dlatego… tylko" 0, kontrast „X, nie Y" maksymalnie 1 na cały tekst, przymiotniki marketingowe 0, AI-jargon 0, rejestr mindfulness 0, emoji i wykrzykniki 0, kalka „X siedzi/leży w Y" 0. Wyliczanka trzech krótkich zdań pod rząd jest od 10 sierpnia 2026 miękka, nie twarda: test na kanonicznych tekstach Przemka pokazał, że twardy limit oblewa jego własny rejestr („Mniejsza. I popatrz na to."). Skrypt ją wypisuje, Ty rozstrzygasz, czy to jego rytm, czy staccato AI.

Kalka miejsca ma limit zero, bo Przemek zgłaszał ją wielokrotnie w różnych tekstach: „wiedza siedzi w głowie", „rozumienie siedzi w głowie", „emocja leży głębiej". Po angielsku to naturalne, po polsku czyta się jak tłumaczenie. Wyjątkiem jest jego własne „co siedzi pod spodem" i skrypt je pomija.

Trzy rzeczy, które skrypt zostawia Twojej ocenie:

- **Deiktyki bez nazwy** wypisuje osobno, bo część z nich jest w porządku („sam tam nie zejdziesz" przeszło), a część to dziura („Tam na dole nie ma zdania"). Zestaw tę listę z Testem nazwania (punkt 7a) zamiast rozstrzygać na wyczucie.

- **Powtórzenia typu „nie X, nie X"** odfiltrowuje jako rytm, nie dychotomię — bo to często potwierdzona fraza Przemka. Wypisuje je osobno; sprawdź, czy klasyfikacja się zgadza.
- **Abstrakcja jako podmiot** jest oznaczona jako miękka. Wypisuje trafienia, decydujesz sam: część z nich to kanon marki (Komunikat 1 w `BRAND.md` sam brzmi „Podświadomość podpięła…"), a część to zwykłe uciekanie od podmiotu „Ty". Policz proporcję, zamiast rozstrzygać na wyczucie.

Skrypt podaje też liczbę zdań i średnią długość — zestaw to z cytatem rytmu z `GLOS_SUROWY.md`, który wybrałeś w Bramce Głosu. To jest twarda wersja punktu 3 tej listy.

Wynik niezerowy: popraw i przeskanuj ponownie. Nie negocjuj z licznikiem i nie tłumacz, dlaczego akurat ten przypadek się nie liczy — jeśli naprawdę się nie liczy, uzasadnij to jednym zdaniem w raporcie dla Przemka i zostaw jego decyzji.

## 9. Test lustra

Przeczytaj na głos. Brzmi jak Przemek przy ognisku, czy jak ktoś starający się brzmieć jak Przemek? Drugie — przepisz, i sprawdź, czy nie wróciłeś do wygładzonych, generycznych wzorców zamiast rytmu z `GLOS_SUROWY.md`.

To jest jedyny subiektywny punkt na tej liście i dlatego stoi na końcu, a nie na początku. Nie zastępuje żadnego z powyższych.
