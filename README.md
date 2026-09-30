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
