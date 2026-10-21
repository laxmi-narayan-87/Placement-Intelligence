#!/usr/bin/env python3
"""Find credential records whose curated tags appear in a job description."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from validate_certifications import DATABASE_PATH, load_certifications

ALIASES: dict[str, tuple[str, ...]] = {
    "machine-learning": ("ml", "machine learning"),
    "artificial-intelligence": ("artificial intelligence",),
    "generative-ai": ("gen ai", "genai", "generative ai"),
    "llm": ("large language model", "large language models"),
    "software-engineering": ("software engineer", "software engineering", "swe"),
    "object-oriented-programming": ("object oriented programming", "object-oriented programming", "oop"),
    "data-science": ("data science",),
    "data-analysis": ("data analysis", "data analytics"),
    "deep-learning": ("deep learning",),
    "neural-networks": ("neural network", "neural networks"),
    "cloud-computing": ("cloud computing",),
    "project-management": ("project management",),
    "web-development": ("web development",),
    "prompt-engineering": ("prompt engineering",),
    "responsible-ai": ("responsible ai",),
}


def phrase_found(text: str, phrase: str) -> bool:
    parts = [re.escape(part) for part in re.split(r"[\s-]+", phrase.strip()) if part]
    if not parts:
        return False
    expression = r"(?<![a-z0-9])" + r"[\s-]+".join(parts) + r"(?![a-z0-9])"
    return bool(re.search(expression, text, re.IGNORECASE))


def extract_tags(jd_text: str, records: list[dict]) -> set[str]:
    text = jd_text.casefold()
    database_tags = {tag for record in records for tag in record["tags"]}
    found: set[str] = set()
    for tag in database_tags:
        phrases = (tag, tag.replace("-", " "), *ALIASES.get(tag, ()))
        if any(phrase_found(text, phrase) for phrase in phrases):
            found.add(tag)
    return found


def match_records(records: list[dict], requested_tags: set[str], limit: int = 10,
                  require_link: bool = False) -> list[dict]:
    matched = []
    for record in records:
        common = sorted(set(record["tags"]) & requested_tags)
        if not common or (require_link and not record.get("link")):
            continue
        matched.append({
            "id": record["id"],
            "title": record["title"],
            "issuer": record["issuer"],
            "platform": record["platform"],
            "date": record["date"],
            "matched_tags": common,
            "matched_tag_count": len(common),
            "link": record.get("link"),
            "link_status": "provided" if record.get("link") else "missing",
        })
    matched.sort(key=lambda item: (-item["matched_tag_count"], item["title"].casefold(), item["date"]))
    return matched[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--jd-file", type=Path, help="UTF-8 text file containing a job description")
    source.add_argument("--text", help="Job description text")
    source.add_argument("--tag", action="append", dest="tags", help="Use a database tag; repeat as needed")
    parser.add_argument("--limit", type=int, default=10, help="Maximum matches to print (default: 10)")
    parser.add_argument("--require-link", action="store_true", help="Only include records with a supplied credential URL")
    parser.add_argument("--json", action="store_true", help="Print JSON for programmatic use")
    parser.add_argument("--database", type=Path, default=DATABASE_PATH, help="Path to certifications.yml")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be at least 1")

    try:
        records = load_certifications(args.database)
        if args.jd_file:
            tags = extract_tags(args.jd_file.read_text(encoding="utf-8"), records)
        elif args.text is not None:
            tags = extract_tags(args.text, records)
        else:
            available = {tag for record in records for tag in record["tags"]}
            tags = {tag.strip().casefold() for tag in (args.tags or [])}
            unknown = tags - available
            if unknown:
                parser.error("Unknown tag(s): " + ", ".join(sorted(unknown)))
        results = match_records(records, tags, args.limit, args.require_link)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps({"matched_tags": sorted(tags), "matches": results}, ensure_ascii=False, indent=2))
        return 0

    print("Matched JD tags: " + (", ".join(sorted(tags)) if tags else "none"))
    if not results:
        print("No credential records matched the detected tags.")
        print("This is a tag match only; it is not proof of eligibility or practical proficiency.")
        return 0
    for number, item in enumerate(results, start=1):
        print(f"\n{number}. {item['title']} — {item['issuer']}")
        print(f"   Platform/date: {item['platform']} · {item['date']}")
        print(f"   Matching tags ({item['matched_tag_count']}): {', '.join(item['matched_tags'])}")
        print(f"   Credential link: {item['link'] or 'Not provided in database'}")
    print("\nNote: relevance is deterministic tag overlap, not a credential-quality score. Missing URLs are not inferred.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
