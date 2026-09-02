# Dokumenty robocze w /narracja/

Pamięć tego skilla. Bez nich każda sesja zaczyna od zera, a `STORY_USAGE` — czyli jedyna realna ochrona przed powtarzaniem tych samych trzech historii — w ogóle nie działa.

Wszystko żyje w `/narracja/` w korzeniu projektu. Ten skill **nie pisze** do `/tozsamosc/`, `/odbiorca/` ani `/material/`; te pliki są autorstwa Przemka i zmienia je tylko on (`CLAUDE.md`).

## Pliki

| Plik | Co trzyma | Kiedy się zmienia |
|---|---|---|
| `NARRATIVE_MAP.md` | 12 sekcji mapy narracji | Nowy materiał podważa albo pogłębia rdzeń |
| `BELIEF_SYSTEM.md` | Filozofia: poziomy i tezy | Nowy belief, doprecyzowanie, zmiana zdania |
| `STORY_BANK.md` | Historie + znaczenia + status | Każda nowa historia z braindumpu |
| `STORY_USAGE.md` | Co poszło gdzie i w jakim znaczeniu | Po każdej publikacji |
| `PERSONAL_MAP.md` | Portret człowieka: rozdziały, potrzeby, paradoksy | Rzadko; przy dużych zmianach w życiu autora |
| `CONTENT_UNIVERSE.md` | Wątki i ich pojemność | Wątek się wyczerpuje albo pojawia nowy |
| `VOICE_NOTES.md` | Dosłowne sformułowania, metafory, rytm | Za każdym razem, gdy Przemek powie coś swoim językiem |
| `OPEN_LOOPS.md` | Pytania bez odpowiedzi | Pętla się otwiera albo domyka |

Nie zakładaj żadnego z nich „na zapas". Plik powstaje, gdy ma treść.

## Konwencja etykiet

Każde twierdzenie w każdym pliku dostaje etykietę:

```
[SOURCE] Ojciec nie odzywał się do niego przez trzy tygodnie po tej rozmowie.
  ↳ braindump, akapit o powrocie z wojska

[INTERPRETATION] Milczenie jako kara jest u niego pierwszym wzorcem tego,
  że bliskość ma warunki.
  ↳ wniosek z trzech scen: wojsko, rozstanie z A., kłótnia o pieniądze

[HYPOTHESIS] Może to tłumaczyć, dlaczego w relacjach wycofuje się pierwszy.
  ↳ NIEPOTWIERDZONE — zapytać
```

Kotwica (`↳`) jest obowiązkowa. Bez niej po miesiącu nikt nie odróżni jego zdania od twojego, a to jest dokładnie ten moment, w którym marka zaczyna mówić rzeczy, których autor nigdy nie pomyślał.

Hipoteza awansuje na interpretację albo źródło **tylko** wtedy, gdy Przemek to potwierdzi. Nie awansuje przez to, że dobrze pasuje do struktury.

---

## STORY_BANK.md — struktura wpisu

```markdown
## S-014 — Rozmowa z ojcem po powrocie z wojska

**Status:** centralna
**Ton:** cichy, bez dramatu, z niedopowiedzeniem
**Opis:** [SOURCE] dwa-trzy zdania, co się wydarzyło
  ↳ braindump, sekcja o rodzinie

**Co pokazuje:** [INTERPRETATION] ...
**Jakie przekonanie tłumaczy:** B-003, B-007

**Możliwe znaczenia:**
1. charakter — jak reaguje, gdy nie dostaje odpowiedzi  → UŻYTE (newsletter #4)
2. przekonanie — skąd wzięło się B-003                   → wolne
3. symbol większego problemu — milczenie między mężczyznami → wolne
4. bliskość — moment, w którym się pomylił              → wolne

**Warstwy:** PERSON mocna / PHILOSOPHY średnia / BRAND średnia
**Czego z tego nie robić:** nie używać jako dowodu skuteczności metody
```

Numeracja (`S-014`, `B-003`) jest po to, żeby dało się odwoływać między plikami bez przepisywania treści.

Historia **cudza** (klienta, znajomego) dostaje wyraźny znacznik `[CUDZA]` i notatkę o zgodzie — inne ryzyko, inne zasady użycia.

---

## STORY_USAGE.md — struktura wpisu

To jest plik, który realnie chroni markę przed powtarzalnością, więc uzupełniaj go nawet wtedy, gdy się spieszysz.

```markdown
## S-014
| Data | Gdzie | Jakie znaczenie | Forma |
|---|---|---|---|
| 2026-07-12 | newsletter #4 | charakter — reakcja na milczenie | esej osobisty |
| 2026-09-01 | pinned #1 | — planowane — | karuzela |
```

**Jak z tego korzystać.** Przed zaproponowaniem historii sprawdzasz jej wiersz. Jeśli była użyta niedawno, nie proponujesz jej automatycznie. Jeśli mimo to jest najlepszym materiałem, mówisz wprost: „to S-014, użyta w newsletterze #4 w znaczeniu 'charakter'; tym razem otwieram znaczenie 3 — milczenie między mężczyznami — i to jest inny tekst, nie ta sama historia drugi raz".

Zużywa się **znaczenie**, nie historia. To rozróżnienie jest całym sensem tego pliku: centralna historia z pięcioma znaczeniami wystarcza na lata, jeśli za każdym razem wchodzi się w nią z innej strony, i wyczerpuje się po trzech miesiącach, jeśli za każdym razem opowiada się ją tak samo.

---

## VOICE_NOTES.md

Zapisujesz **dosłownie**, w cudzysłowie, z kontekstem użycia. Sparafrazowane sformułowanie autora przestaje być jego.

```markdown
## Sformułowania
- „nie chodzi o to, żeby przestać — chodzi o to, żeby przestało być potrzebne"
  ↳ braindump, o nawykach. Używane, gdy odróżnia powstrzymywanie się od zmiany.

## Metafory
- szlak / droga — [SOURCE] jego własna, konsekwentna
- plecak, uwieranie — obrazy do myślenia, NIE pojęcia centralne marki.
  Nie budować na nich tekstu bez zgody.

## Rytm
- długie zdanie złożone, potem krótkie domknięcie. Nie trzy krótkie pod rząd.
- nie zaczyna zdań od „A", „I", „Że"
```

Uwaga o awansie obrazu na pojęcie: obraz, który w materiale służył do wytłumaczenia jednej rzeczy, nie staje się przez to centralnym pojęciem marki. To decyzja Przemka.

---

## Aktualizacja

Po każdej sesji, w której powstało coś nowego, dopisujesz zmiany i mówisz Przemkowi w jednym zdaniu, co się zmieniło. Nie przepisujesz plików od zera — dokładasz i poprawiasz punktowo, bo historia zmian w tych dokumentach sama w sobie jest informacją o tym, jak myślenie autora się przesuwa.

Gdy nowy materiał **podważa** coś zapisanego wcześniej, nie nadpisuj po cichu. Zostaw stare z datą i dopisz nowe obok — zmiana zdania jest materiałem na tekst, a skasowana nie istnieje.
