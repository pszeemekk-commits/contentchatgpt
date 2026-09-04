"""Read-only validation of the ECS file graph and skill mirrors.

Run from any directory: python -X utf8 scripts/check_ecs.py
Before syncing a prepared mirror: --library .claude/skills --no-mirror
This checks files and routing integrity, not prose quality or audience response.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml


CORE = (
    "AGENTS.md", "CLAUDE.md", "SYSTEM_ECS.md", "TYPY_TRESCI.md",
    "PSYCHOLOGIA_I_WARTOSC.md", "format/TOV_KARUZELA.md", "format/TOV_STORIES.md",
    "narracja/TERAZ.md", "narracja/CONTENT_USAGE.md",
    "narracja/PAMIEC_NARRACJI.md",
)
PROJECT_PATH = re.compile(
    r"(?<![\w/])(?:tozsamosc|odbiorca|narracja|format|material|wiedza|skills)/"
    r"[^\s`<>|\[\](),;]+?\.md"
)
RESOURCE_PATH = re.compile(r"\b(?:references|assets)/[\w./-]+\.\w+")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path, library: Path, mirror: bool) -> dict:
    errors: list[str] = []
    checked: set[Path] = set()
    skills = sorted(p for p in library.iterdir() if (p / "SKILL.md").is_file())
    for relative in CORE:
        path = root / relative
        if path.is_file():
            checked.add(path)
        else:
            errors.append(f"Missing core file: {relative}")

    for skill in skills:
        path = skill / "SKILL.md"
        text = path.read_text(encoding="utf-8-sig")
        front = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
        try:
            data = yaml.safe_load(front.group(1)) if front else None
            if not isinstance(data, dict) or data.get("name") != skill.name:
                raise ValueError("name must match directory")
            description = data.get("description")
            if not isinstance(description, str) or not description.strip():
                raise ValueError("description is required")
            if len(description) > 1024:
                raise ValueError("description exceeds 1024 characters")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"Invalid skill {skill.name}: {exc}")
        for document in skill.rglob("*.md"):
            checked.add(document)
            body = document.read_text(encoding="utf-8-sig")
            for relative in RESOURCE_PATH.findall(body):
                if not (skill / relative).is_file():
                    errors.append(f"Missing resource in {skill.name}: {relative}")

    for path in sorted(checked):
        body = path.read_text(encoding="utf-8-sig")
        if "\ufffd" in body:
            errors.append(f"Replacement character: {path.relative_to(root)}")
        for relative in PROJECT_PATH.findall(body):
            if "_XX" not in relative and not (root / relative).is_file():
                errors.append(f"Missing project reference in {path.name}: {relative}")
        if re.search(r"python\s+\.Codex/skills", body, re.I):
            errors.append(f"Invalid scanner location in {path.relative_to(root)}")
        if "AGENT_PISARZ.md" in body:
            errors.append(f"Retired writer dependency in {path.relative_to(root)}")

    types = (root / "TYPY_TRESCI.md").read_text(encoding="utf-8-sig")
    identifiers = re.findall(r"^### (\d+\.\d+)\b", types, re.M)
    expected = {f"{pillar}.{i}" for pillar, count in ((1, 5), (2, 6), (3, 5), (4, 6))
                for i in range(1, count + 1)}
    if set(identifiers) != expected or len(identifiers) != len(expected):
        errors.append("Content types have missing or duplicate identifiers")

    scanner = library / "glos-marki/scripts/scan_tekstu.py"
    if not scanner.is_file():
        errors.append("Missing language scanner")
    mirror_files = 0
    if mirror:
        peer_root = root / ".claude/skills"
        main_root = root / ".agents/skills"
        skill_names = {p.name for p in main_root.iterdir() if (p / "SKILL.md").is_file()}
        skill_names |= {p.name for p in peer_root.iterdir() if (p / "SKILL.md").is_file()}
        for name in sorted(skill_names):
            main = main_root / name
            peer = peer_root / name
            files = {
                p.relative_to(main) for p in main.rglob("*")
                if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
            }
            files |= {
                p.relative_to(peer) for p in peer.rglob("*")
                if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
            }
            for relative in sorted(files):
                a, b = main / relative, peer / relative
                if not a.is_file() or not b.is_file() or digest(a) != digest(b):
                    errors.append(f"Skill mirrors differ: {name}/{relative.as_posix()}")
                mirror_files += 1
    return {
        "ok": not errors,
        "skills": len(skills),
        "documents_checked": len(checked),
        "content_types": len(identifiers),
        "mirror_files_checked": mirror_files,
        "errors": sorted(set(errors)),
        "scope": "File graph, metadata and mirror integrity; no audience or prose evaluation",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--library", type=Path, default=Path(".agents/skills"))
    parser.add_argument("--no-mirror", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    library = args.library if args.library.is_absolute() else root / args.library
    result = validate(root, library, not args.no_mirror)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
