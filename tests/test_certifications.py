from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from match_certifications import extract_tags, match_records  # noqa: E402
from validate_certifications import load_certifications, validate_records  # noqa: E402


class CertificationDatabaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_certifications()

    def test_database_schema_is_valid(self):
        errors, _warnings = validate_records(self.records)
        self.assertEqual(errors, [])

    def test_ids_are_unique_and_record_count_preserved(self):
        ids = [record["id"] for record in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(ids), 56)

    def test_missing_links_are_null_not_fake(self):
        self.assertTrue(all(record["link"] is None or record["link"].startswith("https://") for record in self.records))
        self.assertEqual(sum(record["link"] is None for record in self.records), 53)

    def test_course_page_urls_are_explicit_and_dated(self):
        linked = [record for record in self.records if record.get("course_url")]
        self.assertEqual(len(linked), 37)
        self.assertTrue(all(record["course_url"].startswith("https://") for record in linked))
        self.assertTrue(all(record["course_url_checked"] == "2026-10-22" for record in linked))
        self.assertTrue(all(record.get("course_url_checked") is None for record in self.records
                            if not record.get("course_url")))

    def test_job_description_tag_extraction(self):
        tags = extract_tags("We need Python, SQL and machine learning experience with neural networks.", self.records)
        self.assertIn("python", tags)
        self.assertIn("sql", tags)
        self.assertIn("machine-learning", tags)
        self.assertIn("neural-networks", tags)

    def test_match_results_include_reasons_and_missing_link_state(self):
        result = match_records(self.records, {"machine-learning", "python"}, limit=10)
        self.assertTrue(result)
        self.assertGreaterEqual(result[0]["matched_tag_count"], 1)
        self.assertIn("matched_tags", result[0])
        self.assertIn(result[0]["link_status"], {"provided", "missing"})
        self.assertIn(result[0]["course_page_status"], {"mapped", "not-mapped"})
        self.assertIn("course_url", result[0])

    def test_require_link_filters_missing_credential_urls(self):
        result = match_records(self.records, {"python"}, limit=50, require_link=True)
        self.assertTrue(all(record["link"] for record in result))

    def test_duplicate_title_from_different_sources_is_not_dropped(self):
        titles = [record["title"] for record in self.records]
        self.assertEqual(titles.count("Introduction to Artificial Intelligence"), 2)


if __name__ == "__main__":
    unittest.main()
