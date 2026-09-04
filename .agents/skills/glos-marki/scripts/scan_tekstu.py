#!/usr/bin/env python
"""Mechaniczny skaner tekstu marki Niedźwiedź na Szlaku.

Skaner egzekwuje wyłącznie reguły, które da się rozpoznać mechanicznie i które
aktualny MASTER_TOV oznacza jako twarde. Przypadki wymagające rozumienia sensu
są raportowane do oceny i nie zmieniają kodu wyjścia.

Użycie:
    python scan_tekstu.py plik.md
    python scan_tekstu.py plik.md --od 20 --do 80
    python scan_tekstu.py plik.md --json
    type tekst.txt | python scan_tekstu.py

Kod wyjścia: 0 = brak naruszeń pewnych, 1 = co najmniej jedno naruszenie pewne.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from dataclasses import dataclass
from typing import Pattern


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


@dataclass(frozen=True)
class Rule:
    key: str
    label: str
    severity: str
    pattern: Pattern[str]
    guidance: str


HARD_RULES = (
    Rule(
        "long_dash",
        "długi myślnik",
        "hard",
        re.compile(r"—"),
        "Zamień go na krótki myślnik albo przebuduj zdanie.",
    ),
    Rule(
        "sentence_start_ze",
        "„Że” na początku zdania",
        "hard",
        re.compile(r"(?im)(?:^[ \t]*(?:[-*+]\s+|\d+[.)]\s+)?że\b|[.!?][ \t\r\n]+że\b)"),
        "Scal z poprzednim zdaniem albo przebuduj początek.",
    ),
    Rule(
        "marketing_adjective",
        "przymiotnik marketingowy",
        "hard",
        re.compile(r"\b(?:wyjątkow|niesamowit|unikaln|przełomow)\w*", re.I),
        "Nazwij konkretną cechę, zmianę albo rezultat.",
    ),
    Rule(
        "forbidden_term_1",
        "zakazane słowo z MASTER_TOV 9.1: pozycja 1",
        "hard",
        re.compile(r"(?<!\w)adres(?:u|owi|em|ie|y|ów|om|ami|ach)?(?!\w)", re.I),
        "Nazwij wprost przyczynę albo miejsce, którego dotyczy zdanie.",
    ),
    Rule(
        "forbidden_term_2",
        "zakazane słowo z MASTER_TOV 9.1: pozycja 2",
        "hard",
        re.compile(r"\bgł(?:ó|o)d\w*", re.I),
        "Opisz wprost, czego człowiek szuka i gdzie tego szuka.",
    ),
    Rule(
        "forbidden_term_3",
        "zakazane słowo z MASTER_TOV 9.1: pozycja 3",
        "hard",
        re.compile(r"\bawari\w*", re.I),
        "Użyj źródłowego sformułowania autora.",
    ),
    Rule(
        "decision_jargon",
        "żargon: „przestrzeń decyzyjna”",
        "hard",
        re.compile(r"\bprzestrze(?:ń|ni|nią)\s+decyzyjn\w*", re.I),
        "Napisz, jaką decyzję człowiek podejmuje i od czego ona zależy.",
    ),
    Rule(
        "location_calque",
        "kalka miejsca z abstrakcyjnym podmiotem",
        "hard",
        re.compile(
            r"\b(?:wiedz|rozumieni|emocj|napięci|problem|reakcj|prawd|odpowied|"
            r"impuls|mechanizm|wzorzec|schemat|rana|podświadomoś|umysł|lęk|wstyd|"
            r"nawyk|program|traum)\w*\s+(?:\w+\s+){0,2}(?:siedzi|siedzą|leży|"
            r"leżą|mieszka|mieszkają|znajduje\s+się|znajdują\s+się)\b|"
            r"\b(?:w\s+tobie|w\s+głowie)\s+(?:\w+\s+){0,2}(?:siedzi|siedzą|"
            r"leży|leżą|mieszka|mieszkają)\b",
            re.I,
        ),
        "Nazwij konkretnie, co dzieje się z człowiekiem.",
    ),
)


REVIEW_RULES = (
    Rule(
        "work_as_label",
        "słowo z MASTER_TOV 9.1 wymagające oceny użycia",
        "review",
        re.compile(r"\brobot(?:a|y|ę|ą|ą|cie|om|ami|ach)\b", re.I),
        "Sprawdź, czy to zwykłe słowo, czy nazwa pojęcia stworzona przez system.",
    ),
    Rule(
        "empty_dichotomy_candidate",
        "możliwa pusta dychotomia",
        "review",
        re.compile(r"\b[Tt]o\s+nie\s+[^.!?\n]{1,120}[.!?]\s+To\s+[^.!?\n]{1,120}[.!?]?"),
        "Sprawdź, czy drugie zdanie wnosi nowy fakt, argument albo obraz.",
    ),
    Rule(
        "abstract_object",
        "możliwy żargon: „obiekt”",
        "review",
        re.compile(r"\bobiekt\w*", re.I),
        "Jeśli to skrót myślowy, nazwij rzecz, której człowiek dotyka, doświadcza lub zaprzecza.",
    ),
)


def read_text(path: str | None, start: int, end: int | None) -> str:
    if path:
        with io.open(path, encoding="utf-8-sig") as handle:
            lines = handle.readlines()
        return "".join(lines[start - 1:end])
    return sys.stdin.read()


def target_text(raw: str) -> str:
    """Pomija nagłówki Markdown i samodzielne separatory dokumentacji."""
    return "\n".join(
        line
        for line in raw.splitlines()
        if not line.lstrip().startswith("#")
        and line.strip() not in {"---", "___", "```"}
    )


def context(text: str, match: re.Match[str], padding: int = 55) -> str:
    start = max(0, match.start() - padding)
    end = min(len(text), match.end() + padding)
    return "..." + " ".join(text[start:end].split()) + "..."


def sentence_stats(text: str) -> dict[str, float | int]:
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
    lengths = [len(re.findall(r"\b\w+\b", sentence)) for sentence in sentences]
    if not lengths:
        return {"sentences": 0, "average_words": 0.0, "shortest": 0, "longest": 0}
    return {
        "sentences": len(lengths),
        "average_words": round(sum(lengths) / len(lengths), 1),
        "shortest": min(lengths),
        "longest": max(lengths),
    }


def short_sentence_runs(text: str) -> int:
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
    run = 0
    findings = 0
    for sentence in sentences:
        if len(re.findall(r"\b\w+\b", sentence)) < 5:
            run += 1
            if run == 3:
                findings += 1
        else:
            run = 0
    return findings


def inspect(text: str) -> dict[str, object]:
    findings = []
    for rule in HARD_RULES + REVIEW_RULES:
        matches = list(rule.pattern.finditer(text))
        findings.append(
            {
                "key": rule.key,
                "label": rule.label,
                "severity": rule.severity,
                "count": len(matches),
                "guidance": rule.guidance,
                "contexts": [context(text, match) for match in matches],
            }
        )

    findings.append(
        {
            "key": "short_sentence_run",
            "label": "seria co najmniej trzech bardzo krótkich zdań",
            "severity": "review",
            "count": short_sentence_runs(text),
            "guidance": "Sprawdź, czy to żywy rytm autora, czy cięcie wykonane wyłącznie dla efektu.",
            "contexts": [],
        }
    )

    hard_count = sum(item["count"] for item in findings if item["severity"] == "hard")
    review_count = sum(item["count"] for item in findings if item["severity"] == "review")
    return {
        "ok": hard_count == 0,
        "hard_findings": hard_count,
        "review_findings": review_count,
        "findings": findings,
        "stats": {
            **sentence_stats(text),
            "ale": len(re.findall(r"(?<!\w)ale(?!\w)", text, re.I)),
            "exclamation_marks": text.count("!"),
            "emoji": len(re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", text)),
        },
    }


def print_report(report: dict[str, object], quiet: bool) -> None:
    print("\n=== SKAN TEKSTU ===")
    print(f"{'poziom':10s} {'wynik':>6s}  kryterium")
    print("-" * 72)
    for item in report["findings"]:
        count = item["count"]
        if count:
            print(f"{item['severity']:10s} {count:>6d}  {item['label']}")

    if not quiet:
        for item in report["findings"]:
            if not item["count"]:
                continue
            print(f"\n--- {item['label']} ---")
            print(item["guidance"])
            for sample in item["contexts"]:
                print("  " + sample)

    stats = report["stats"]
    print(
        "\nStatystyki neutralne: "
        f"zdania {stats['sentences']}, średnia {stats['average_words']} słowa, "
        f"najkrótsze {stats['shortest']}, najdłuższe {stats['longest']}, "
        f"ale {stats['ale']}, wykrzykniki {stats['exclamation_marks']}, emoji {stats['emoji']}."
    )
    if report["review_findings"]:
        print("Miejsca do oceny nie blokują tekstu; wymagają przeczytania w kontekście.")
    print("Wynik: " + ("brak naruszeń pewnych" if report["ok"] else "wykryto naruszenia pewne"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plik", nargs="?", help="plik UTF-8; brak oznacza stdin")
    parser.add_argument("--od", type=int, default=1, help="pierwsza linia zakresu")
    parser.add_argument("--do", type=int, default=None, help="ostatnia linia zakresu")
    parser.add_argument("--cicho", action="store_true", help="bez kontekstów trafień")
    parser.add_argument("--json", action="store_true", help="raport JSON")
    args = parser.parse_args()

    if args.od < 1 or (args.do is not None and args.do < args.od):
        parser.error("zakres linii jest nieprawidłowy")

    report = inspect(target_text(read_text(args.plik, args.od, args.do)))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report, args.cicho)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
