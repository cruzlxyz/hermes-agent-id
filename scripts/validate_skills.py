#!/usr/bin/env python
"""Validate Hermes SKILL.md files in this repo."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MAX_DESCRIPTION_LENGTH = 1024
MAX_NAME_LENGTH = 64
MAX_SKILL_CHARS = 100_000


def parse_frontmatter(content: str, path: Path) -> tuple[dict, str]:
    if not content.startswith("---"):
        raise ValueError("file harus dimulai langsung dengan ---")

    match = re.search(r"\n---\s*\n", content[3:])
    if not match:
        raise ValueError("frontmatter penutup --- tidak ditemukan")

    end = match.start() + 3
    raw_frontmatter = content[3:end]
    body = content[end + len(match.group(0)) - 1 :]

    if yaml is not None:
        data = yaml.safe_load(raw_frontmatter)
    else:
        # Fallback minimal kalau PyYAML belum ada: cukup ambil key top-level sederhana.
        data = {}
        for line in raw_frontmatter.splitlines():
            if ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"\'')

    if not isinstance(data, dict):
        raise ValueError("frontmatter harus berupa YAML mapping")

    return data, body


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")

    if len(content) > MAX_SKILL_CHARS:
        errors.append(f"file terlalu besar: {len(content)} chars > {MAX_SKILL_CHARS}")

    try:
        meta, body = parse_frontmatter(content, path)
    except Exception as exc:  # noqa: BLE001 - validation script should collect all errors
        return [str(exc)]

    name = meta.get("name")
    desc = meta.get("description")

    if not name:
        errors.append("frontmatter wajib punya name")
    elif len(str(name)) > MAX_NAME_LENGTH:
        errors.append(f"name terlalu panjang: {len(str(name))} chars > {MAX_NAME_LENGTH}")

    if not desc:
        errors.append("frontmatter wajib punya description")
    elif len(str(desc)) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"description terlalu panjang: {len(str(desc))} chars > {MAX_DESCRIPTION_LENGTH}")

    if not body.strip():
        errors.append("body setelah frontmatter tidak boleh kosong")

    if any(secret_word in content.lower() for secret_word in ["private_key=", "seed phrase", "api_key=", "password="]):
        errors.append("kemungkinan ada secret hardcoded; cek manual")

    return errors


def main() -> int:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("Tidak ada skill di folder skills/")
        return 1

    failed = False
    for path in skill_files:
        rel = path.relative_to(ROOT)
        errors = validate_skill(path)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
