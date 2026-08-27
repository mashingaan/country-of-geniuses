# Agent runbook

This is the shortest path for using Country of Geniuses as a participant. The repository supplies the skills, jurisdiction context, evidence contract, and safety boundary. The participant's agent performs the investigation locally.

## One read-only run

Install the small development dependency set and validate the repository:

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate-repo.py
```

Then give an agent the repository and a bounded request. This prompt is a starting point, not permission to contact a service:

```text
Use this repository as the civic investigation harness.

Load:
- AGENTS.md
- docs/trust-and-safety.md
- skills/civic-problem-triage/SKILL.md
- the relevant jurisdiction pack
- the relevant integration manifest

Investigate this bounded scope:
- jurisdiction: [country, city, or service area]
- problem type: [category]
- public location precision: [city, district, street, intersection, or public facility]
- time window: [start and end with timezone]
- permitted sources: [official pages, read-only APIs, public records]

Use read-only calls only. Do not POST, submit a form, send a message, or use a write-capable connector.
Check currentness, duplicates, the owning agency, and active projects before preparing any action.
Return either a privacy-safe problem card or a discarded card with a structured stop reason.
If a draft is justified, show the exact recipient, channel, text, evidence, data leaving the local environment, and duplicate risk. Mark it as requiring human confirmation.
Validate the resulting JSON with:
python scripts/validate-repo.py --card [local card path]
Keep raw responses, credentials, private evidence, and private notes outside the repository.
```

Save an output card and raw evidence in a local directory such as `local-output/`, which is ignored by Git. Do not put a real participant case into `examples/` unless it has been redacted and intentionally prepared as a public contribution.

## Open311 Boston example

The Boston pack and the `open311-read-only-discovery` skill provide a concrete tested-read path:

1. Read the service catalog and select an exact service code.
2. Query a bounded request window with the documented `per_page` and `page` parameters.
3. Inspect only a relevant public request when needed.
4. Remove addresses, coordinates, media URLs, descriptions, and tokens from a public card.
5. Stop on a matching open request, or prepare a draft only after the duplicate, owner, project, safety, and privacy checks pass.

The current Boston example is intentionally a duplicate stop. It proves the read-only and redaction path, not a submission or a government response by this project.

## Human boundary

The agent may prepare a draft. The participant must explicitly approve the exact external action after seeing its recipient, channel, content, evidence, data disclosure, and duplicate risk. The repository does not operate a central crawler, daemon, queue, or complaint cannon.

## Contributing the result

Use the [Civic signal issue form](https://github.com/mashingaan/country-of-geniuses/issues/new?template=signal.yml) for an honest public signal, or open a narrow pull request for a redacted card, jurisdiction correction, skill improvement, or integration note. Keep the raw local investigation private until the public artifact passes the privacy review.
