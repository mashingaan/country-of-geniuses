# Country of Geniuses agent instructions

## Mission

Help participants investigate public-service problems and prepare accountable, evidence-based action. Treat the repository as a shared civic harness, not as an autonomous complaint cannon.

## Required reading by task

- Before changing an agent skill, read `docs/trust-and-safety.md` and the target skill.
- Before adding a jurisdiction pack, read `jurisdictions/README.md`.
- Before adding an API or MCP integration, read `integrations/README.md`.
- Before changing the problem-card shape, read `schemas/problem-card.schema.json` and `examples/problem-card.example.json`.

## Working loop

1. Define the jurisdiction, problem type, time window, and permitted sources.
2. Collect source URLs, timestamps, and a short explanation of what each source supports.
3. Check whether the problem is current and whether an existing request already covers it.
4. Identify the responsible public service from an official or locally verified source.
5. Produce a privacy-safe problem card or a clear reason to stop.
6. Prepare an action for human review. Report what would be sent, to whom, and why.
7. Record only public, redacted outcomes in the repository.

The task is complete when the card is ready for explicit human confirmation or is marked as stopped with a reason and evidence trail.

## Hard boundaries

- Keep names, phone numbers, email addresses, exact private addresses, access tokens, images with faces, and other personal data outside the repository.
- Keep credentials in the participant's local environment. Never add them to skills, examples, issues, or pull requests.
- Treat an unverified endpoint or routing rule as a draft. Do not use it for external submission.
- Do not send a request, publish a report, contact a person, or call a write-capable tool without explicit human confirmation.
- Do not infer wrongdoing from an anomaly. Use neutral language and preserve alternative explanations.
- Stop and ask for human help when a situation is urgent, dangerous, medical, legal, electoral, law-enforcement related, or materially affects a vulnerable person.

## Repository style

Use English for shared project documentation unless a localized file is the subject of the change. Use `e` rather than `ё` in Russian text. Avoid semicolon punctuation in project text and scripts.

Prefer one coherent pull request, a small reproducible example, and a test or validation check for each real behavior changed.
