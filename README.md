## Engineering focus

Placement Intelligence is designed as a **research and verification workflow**, not a generic job-search scraper.

### Workflow

```text
Fresh sources
    ↓
Candidate hiring signals
    ↓
Source verification
    ↓
Role / eligibility / deadline checks
    ↓
Deduplication
    ↓
Action-oriented briefing
```

### What it demonstrates

- Retrieval of recent hiring information
- Preference for official company/application sources
- Verification of role and application details
- Deduplication of reposted opportunities
- Structured summaries designed around the next action

### Design principle

The system separates **finding information** from **verifying information**. A hiring signal is treated as useful only after relevant details such as role, eligibility, location, deadline, or application status have been checked where possible.

---

# Placement Intelligence

A personal placement-intelligence plugin for fresh, verified, actionable India software and technology hiring information.

## What it does

- Finds recent India software/technology hiring updates
- Verifies roles, eligibility, deadlines, locations, assessments, and application status
- Prioritizes official company and application sources
- Deduplicates reposted opportunities
- Tracks campus, off-campus, OA, interview, and hiring-challenge updates
- Produces concise, action-oriented placement briefings

## Plugin structure

- `plugin.json` — plugin manifest
- `.codex-plugin/plugin.json` — ChatGPT/Codex plugin interface metadata
- `skills/placement-intelligence/SKILL.md` — placement research workflow

This repository mirrors the private Placement Intelligence plugin configuration.

> Never commit API keys, OAuth tokens, passwords, or other secrets.


## Certification-aware role matching

A curated credential database is available for job-description relevance matching:

- \`data/certifications.yml\` — 56 records from the supplied inventory, with normalized tags.
- \`scripts/validate_certifications.py\` — validates required fields, IDs, dates, tags, URL syntax and missing data.
- \`scripts/match_certifications.py\` — matches JD wording to known tags and explains which tags matched each record.
- \`tests/test_certifications.py\` and \`.github/workflows/validate-certifications.yml\` — regression tests and CI validation.
- \`docs/CERTIFICATIONS.md\` — schema and usage examples.

Run \`python scripts/match_certifications.py --jd-file /path/to/job-description.txt\` to retrieve relevant records. The matcher reports tag overlap only; it does not rank credential quality, assert eligibility, or prove a skill. Missing credential URLs are stored as \`null\` and are never fabricated. See the documentation before using the output in a resume.
