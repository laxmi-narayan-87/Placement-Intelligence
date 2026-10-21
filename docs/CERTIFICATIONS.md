# Certification database

The source of truth is [\`data/certifications.yml\`](../data/certifications.yml). It preserves the supplied inventory and tags records for job-description relevance matching.

## Record fields

- \`id\`: stable unique lowercase kebab-case identifier.
- \`title\`: credential/course title as supplied.
- \`issuer\`: organization/brand shown in the inventory.
- \`platform\`: learning or issuing platform recorded in the inventory.
- \`date\`: \`YYYY-MM\`, retained at month-level precision.
- \`tags\`: normalized lowercase kebab-case labels used for matching.
- \`link\`: a direct HTTPS credential/verification URL, or \`null\` when no URL was supplied.

A \`null\` link does **not** mean the credential is invalid or not earned; it means this inventory does not have a link. Do not invent certificate URLs, credential IDs, exact days, or provider details. Repeated titles from different providers are retained and warned about rather than automatically deduplicated.

## Validate

\`\`\`bash
python -m pip install PyYAML==6.0.3
python scripts/validate_certifications.py
python -m unittest discover -s tests -v
\`\`\`

Errors fail validation. Missing links, future dates, and repeated titles are reported as warnings for manual review.

## Match a job description

\`\`\`bash
python scripts/match_certifications.py --jd-file /path/to/job-description.txt
python scripts/match_certifications.py --text "Python, SQL and machine learning"
python scripts/match_certifications.py --tag python --tag sql --tag machine-learning
python scripts/match_certifications.py --jd-file /path/to/job-description.txt --require-link --json
\`\`\`

The matcher is deterministic keyword/tag overlap. It shows which tags matched each entry, and whether a URL was supplied. It is a relevance aid—not a ranking of credential quality, proof of practical skills, or an eligibility decision. Review each credential and employer requirements before using it in a resume.

## Link-verification work still to do

The inventory includes three non-empty credential URLs and 53 missing links. The validator checks URL syntax, not whether an issuer currently serves or authenticates the page. Link reachability and award details have not been confirmed by this script. Add direct credential pages as they become available.
