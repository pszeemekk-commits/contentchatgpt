---
name: feedback-otwarte-pytania-wydobywanie
description: "Gdy Przemek daje explicit instrukcję wzorować się na konkretnym, nazwanym mechanizmie (np. innym skillu) - trzymaj się DOKŁADNIE tego, nie podmieniaj go po drodze na własną, 'lepszą' architekturę, nawet jeśli wydaje się bardziej rygorystyczna"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f9551f94-f568-4ab0-b31d-d98703c60c39
  modified: 2026-07-31T13:55:08.466Z
---

## Rdzeń lekcji (po ~17 rundach poprawek na skillu `wydobywanie-tematow`)

Przemek na starcie dał precyzyjną instrukcję: mechanika rozmowy skilla `wydobywanie-tematow` ma być wzorowana na `klarowanie-perspektywy` (jedno pytanie naraz, budowane WYŁĄCZNIE z tego co użytkownik właśnie powiedział, nigdy z gotowego pomysłu Claude'a; pogłębianie: dlaczego/co z tego wynika/skąd się bierze/przykład z życia) + filtr konkret/truizm z `karuzele-z-wsadu`. Nic więcej.

W trakcie budowy skilla po cichu podmieniłem tę instrukcję na inną: zacząłem "operacjonalizować" `AGENT_DORADCA.md` (MODUŁ, warunki konieczne, sekwencja "BRAND.md jako weryfikacja nie źródło") — dokument realny i wartościowy, ale NIE ten, o który Przemek prosił dla tego skilla. Efekt: ~15 rund poprawek próbujących naprawić coraz to nowe objawy (zamknięte pytania, kwestionariusz, scenariusze z wymyśloną trzecią osobą, gotowe tezy do podpisania, batch 15 pytań z "tarciem" i "zakotwiczeniem w domenie") — wszystkie były próbami załatania architektury, której Przemek nigdy nie zamówił. Przemek finalnie: "dlaczego ty wciąż się wzorujesz na Agencie Doradcy, kiedy mówiłem że masz się wzorować na klarowaniu perspektywy."

**Why to ważne:** żadna ilość analizy plików projektowych (Human Design, ENTP, WZORZEC_MYSLENIA.md, AGENT_DORADCA.md) nie zastąpi trzymania się wprost tego, o co poproszono. Dogłębna wiedza o projekcie jest pomocna do WYPEŁNIANIA instrukcji (np. dobór treści, ton), nie do jej PODMIENIANIA na własną architekturę, choćby wydawała się bardziej rygorystyczna czy "kompletna".

**How to apply:** gdy użytkownik wskazuje konkretny, nazwany wzorzec do naśladowania (inny plik, inny skill, konkretna metoda) — trzymaj się GO, nie zbaczaj w stronę innego, choćby powiązanego dokumentu, bez wyraźnej zgody na zmianę kierunku. Jeśli w trakcie pracy zauważysz że sięgasz po inne źródło niż wskazane na starcie — zatrzymaj się i zapytaj, zanim zbudujesz na tym kolejne rundy poprawek.

## Finalna architektura skilla (stan po korekcie, `wydobywanie-tematow` v10)

Krok 1: jedno proste pytanie otwierające (co ma teraz w głowie / co go ostatnio zajmuje) — nie batch, nie bank, nie zaproszenie inżynierowane pod "tarcie" czy "domenę". Pogłębianie: jedno pytanie naraz, budowane wyłącznie z ostatniej odpowiedzi Przemka, cztery kąty z klarowania-perspektywy (dlaczego / co z tego wynika / skąd się bierze / przykład z życia). Filtr konkret/truizm z karuzele-z-wsadu przed zapisaniem tematu. Filar/Klarowna Transformacja sprawdzane po fakcie (weryfikacja), nigdy jako źródło pytania. Jeśli po kilku próbach naprawdę nic nie wychodzi — powiedzieć to wprost, nie forsować.

## Podlekcje, które przetrwały mimo zmiany architektury (przydatne gdzie indziej, niekoniecznie w tym skillu)

- **Test na żywo > teoretyzowanie nad plikami.** Żadna ilość analizy dokumentów nie zastępuje sprawdzenia czy coś faktycznie działa w realnej rozmowie z Przemkiem.
- **Nie zadawaj pytań meta, których odpowiedź niczego nie zmienia w dalszym toku pracy** (np. "ile tematów dziś potrzebujesz", skoro sesja i tak kończy się gdy powie "starczy").
- **Gdy poprawka nie działa, sprawdź czy problem jest w ZDANIU czy w ARCHITEKTURZE** — jeśli kolejna wersja to wariacja tej samej wadliwej struktury, cofnij się zamiast pisać kolejną.
- Obserwacje o Przemku (Generator/autorytet sakralny, ENTP — `WZORZEC_MYSLENIA.md`, `material/CONTENT_MACHINE.md`) są prawdziwe i mogą być przydatne w innych kontekstach, ale NIE uzasadniają automatycznie odchodzenia od jawnie wskazanej metody rozmowy w konkretnym skillu.
