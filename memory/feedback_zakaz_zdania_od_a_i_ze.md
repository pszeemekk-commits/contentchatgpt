---
name: feedback-zakaz-zdania-od-a-i-ze
description: "Zdanie nie może zaczynać się od spójnika \"A\", \"I\" ani \"Że\" - scal je z poprzednim zdaniem przecinkiem albo usuń spójnik."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c65432b7-5946-4e31-b7e6-538a23e2d75e
  modified: 2026-08-16T07:34:11.600Z
---

Żadne zdanie w tekście dla marki Niedźwiedź na Szlaku nie zaczyna się od "A", "I" ani "Że". Dotyczy slajdów, opisu pod post, hooka i ziarenek.

**Why:** rozpoczęcie zdania spójnikiem to sztuczna pauza dramatyczna - ta sama rodzina błędu co dramatyczny myślnik i staccato z osobnych linijek. Przemek zgłosił to jako twardą zasadę po rolce o niezaspokojonych potrzebach: "Ona kocha cię jak dorosłego faceta. A ty czekasz..." i "I ona to robi, mówi ci to wprost". `MASTER_TOV.md` sekcja 7 miała dotąd tylko "Że" na początku zdania i skaner sprawdza wyłącznie ten jeden przypadek - "A" i "I" przechodziły przez kontrolę bez trafienia.

**How to apply:** dwie naprawy. Jeśli spójnik niesie kontrast albo ciąg dalszy, scal oba zdania przecinkiem ("Ona kocha cię jak dorosłego faceta, a ty czekasz na to, co dziecko dostaje od rodziców"). Jeśli spójnik jest tylko rozbiegiem, skasuj go i zostaw samo zdanie ("I ona to robi" -> "Ona to robi"). Przed oddaniem tekstu zrób `grep -nE "(^|[.!?] )(A|I|Że) " plik`, bo `scan_tekstu.py` łapie tylko "Że". Wyjątek do potwierdzenia u Przemka: jego własny, zatwierdzony CTA z KOR-020 zaczyna się od "A jeśli jesteś kobietą..." - nie przerabiaj jego zatwierdzonych fragmentów bez pytania, patrz [[feedback_no_retrofit_anafora_redakcja]].
