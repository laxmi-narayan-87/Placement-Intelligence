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

The inventory keeps the three personal credential URLs supplied in the source file and does not infer personal credential links from public pages. Public course/catalog pages are mapped only for records with a confidently matched official provider page. The validator checks URL syntax and date fields, not live HTTP reachability or whether a specific learner earned a credential. Add a personal credential URL from the learner’s certificate/share page after confirming it.


The matcher returns matched tags, personal credential URL status, and the mapped public course page when available. `--require-link` filters for records with a supplied personal credential URL; a course page alone does not verify completion.


## Public course URL review log

See [COURSE_URL_REVIEW.md](COURSE_URL_REVIEW.md) for the 24 public course/catalog pages mapped on 2026-10-22 and the remaining verification work.
