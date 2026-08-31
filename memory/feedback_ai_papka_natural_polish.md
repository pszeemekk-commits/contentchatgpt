---
name: feedback-ai-papka-natural-polish
description: "Zawsze przepuszczaj finalny tekst stories/karuzeli przez checklistę natural-polish-copy (myślniki, negacja+twierdzenie, trójki) przed pokazaniem - AGENT_PISARZ scan mechaniczny tego nie łapie"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d64213c4-6346-4cd8-8fcf-6cecaa023c75
---

Scan mechaniczny z AGENT_PISARZ.md (sekcja 6) łapie długi myślnik "—" i "to nie X. to Y.", ale NIE łapie krótkiego myślnika "-" jako dramatycznej pauzy w środku zdania, konstrukcji "nie X. Y." (negacja + twierdzenie tej samej myśli), ani sztucznych dwukropków z wyliczeniem. To osobny zestaw reguł z pluginu `anthropic-skills:natural-polish-copy`.

**Why:** Przemek ocenił dopracowane już (teza + jedna oś + domknięcie) stories jako "AI papka" (2026-07-13) - błąd był czysto językowy/stylistyczny, nie strukturalny. Przykłady złapane po fakcie: "ta sama osoba - ten, który buduje obraz" (dramatyczny myślnik), "to nie były moje pragnienia. To był cudzy głos" (negacja+twierdzenie, powinno być jedno zdanie twierdzące).

**How to apply:** Przy KROK 3D (reguły stylistyczne) w AGENT_PISARZ, oprócz zakazów już tam wypisanych, przejdź tekst przez checklistę natural-polish-copy PRZED pokazaniem: (1) każdy krótki myślnik "-" w środku zdania - czy to dramatyczna pauza do usunięcia, czy prawdziwe wtrącenie; (2) każde zdanie z negacją "nie X" - czy następne zdanie mówi to samo na plus (wtedy scal w jedno twierdzenie); (3) potrójne wyliczenia bliskoznaczne dla rytmu; (4) sztuczne dwukropki z listą. To dotyczy KAŻDEGO tekstu w tym projekcie (karuzela i stories), nie tylko gdy user explicite poprosi o skill.
