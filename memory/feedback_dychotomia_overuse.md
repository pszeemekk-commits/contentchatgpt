---
name: feedback-dychotomia-overuse
description: "User flags repeated \"nie X, Y\" / \"To nie X. To Y.\" contrast pattern as an AI tell, even when individual instances are single-sentence compressed"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 22738e6d-7bf5-4111-a741-971d31fc3547
---

Even when a single "X, nie Y" contrast is technically compliant with the exception carved out in `material/KOREKTY_SUROWE.md` (KOR-001, KOR-002 - compressed single-sentence negation+affirmation is allowed, unlike the two-sentence "To nie X. To Y." form), using this device on **multiple slides within the same karuzela** still reads as AI-generated to Przemek. He flagged it directly: "uzywasz dychotomii to brzmi jak AI" after a draft that had the pattern on 4 of 12 slides (some as single compressed sentences, some as the fully banned two-sentence form I'd missed in self-review).

**Why:** the contrast-through-negation move is a low-effort default the model reaches for repeatedly. One clean instance can be genuine voice (matches a real Przemek correction like "Dopamina to hormon pragnienia, nie odczuwania"). Four instances in one piece is a crutch, not a style choice - it flattens into a recognizable formula regardless of each instance passing the "single sentence" technical test.

**How to apply:** when self-checking a draft against `format/TOV_KARUZELA.md` section 6 (scan mechaniczny, max 1 "to nie X, to Y" per całą karuzelę) - the limit of 1 applies to the *pattern family* broadly, not just the literal two-sentence form. Count every "nie X, Y" / "Nie X - Y" / "X, nie Y" contrast across the whole text, not just per-slide. If more than one shows up, cut all but the strongest and rewrite the rest as plain positive/causal statements - let the reader infer the negation themselves (this also matches the brand's own principle in `format/TOV_KARUZELA.md` section 6 SHIFT: "Czytelnik sam wyciąga wniosek - nie podawaj mu go na tacy").

Related: [[project-carousel-writing-protocol]] (if that memory exists) - this is a refinement of the mechanical scan step in `AGENT_PISARZ.md` Krok 3D / TOV_KARUZELA section 11.
