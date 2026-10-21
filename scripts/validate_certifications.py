#!/usr/bin/env python3
"""Validate the certification inventory without inventing missing credential data."""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = ROOT / "data" / "certifications.yml"
REQUIRED_FIELDS = {"id", "title", "issuer", "platform", "date", "tags", "link"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^(\d{4})-(\d{2})$")


def load_certifications(path: Path = DATABASE_PATH) -> list[dict]:
    """Load the YAML list safely and raise a readable error for invalid YAML."""
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("Database root must be a YAML list of certification records.")
    return data


def validate_records(records: list[dict]) -> tuple[list[str], list[str]]:
    """Return (errors, warnings); warnings do not fail validation."""
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()
    titles: dict[str, list[str]] = {}
    current_month = date.today().strftime("%Y-%m")

    if not records:
        errors.append("Database contains no records.")

    for index, record in enumerate(records, start=1):
        prefix = f"Entry {index}"
        if not isinstance(record, dict):
            errors.append(f"{prefix} must be a mapping/object.")
            continue

        keys = set(record)
        missing = REQUIRED_FIELDS - keys
        extra = keys - REQUIRED_FIELDS
        if missing:
            errors.append(f"{prefix} ({record.get('id', 'no id')}): missing fields: {', '.join(sorted(missing))}.")
        if extra:
            errors.append(f"{prefix} ({record.get('id', 'no id')}): unexpected fields: {', '.join(sorted(extra))}.")

        record_id = record.get("id")
        if not isinstance(record_id, str) or not ID_RE.fullmatch(record_id):
            errors.append(f"{prefix}: id must be a lowercase kebab-case string.")
        elif record_id in seen_ids:
            errors.append(f"{prefix}: duplicate id '{record_id}'.")
        else:
            seen_ids.add(record_id)

        for field in ("title", "issuer", "platform"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip() or value != value.strip():
                errors.append(f"{prefix} ({record_id or 'no id'}): '{field}' must be a non-empty, trimmed string.")

        title = record.get("title")
        if isinstance(title, str) and title.strip():
            titles.setdefault(title.strip().casefold(), []).append(str(record_id or index))

        month = record.get("date")
        match = DATE_RE.fullmatch(month) if isinstance(month, str) else None
        if not match:
            errors.append(f"{prefix} ({record_id or 'no id'}): date must use YYYY-MM format.")
        else:
            year, month_number = int(match.group(1)), int(match.group(2))
            if year < 1900 or not 1 <= month_number <= 12:
                errors.append(f"{prefix} ({record_id or 'no id'}): date has an invalid year or month.")
            elif month > current_month:
                warnings.append(f"{record_id}: date {month} is in the future; confirm it is intentional.")

        tags = record.get("tags")
        if not isinstance(tags, list) or not tags:
            errors.append(f"{prefix} ({record_id or 'no id'}): tags must be a non-empty list.")
        else:
            local_tags: set[str] = set()
            for tag in tags:
                if not isinstance(tag, str) or not TAG_RE.fullmatch(tag):
                    errors.append(f"{prefix} ({record_id or 'no id'}): tag {tag!r} must be lowercase kebab-case.")
                elif tag in local_tags:
                    errors.append(f"{prefix} ({record_id or 'no id'}): duplicate tag '{tag}'.")
                else:
                    local_tags.add(tag)

        link = record.get("link")
        if link is not None:
            if not isinstance(link, str) or not link.strip():
                errors.append(f"{prefix} ({record_id or 'no id'}): link must be null or a non-empty URL.")
            else:
                parsed = urlsplit(link)
                if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                    errors.append(f"{prefix} ({record_id or 'no id'}): link must be an absolute HTTPS URL without embedded credentials.")

    for title, ids in titles.items():
        if len(ids) > 1:
            warnings.append(
                f"Repeated title across records {', '.join(ids)}: matching titles are retained because providers may differ."
            )

    missing_links = [
        record.get("id", f"entry-{i}")
        for i, record in enumerate(records, start=1)
        if isinstance(record, dict) and record.get("link") is None
    ]
    if missing_links:
        warnings.append(
            f"{len(missing_links)} of {len(records)} records have no credential URL. Add only direct, verified links; none were fabricated."
        )

    return errors, warnings


def main() -> int:
    try:
        records = load_certifications()
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    errors, warnings = validate_records(records)
    for error in errors:
        print(f"FAIL: {error}")
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        print(f"\nValidation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    unique_tags = {tag for record in records for tag in record["tags"]}
    print(f"PASS: {len(records)} records; {len(unique_tags)} distinct tags; required fields and formats validated.")
    print(f"Warnings: {len(warnings)} (missing links and repeated titles require human review, not automatic correction).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
