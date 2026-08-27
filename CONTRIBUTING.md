# Contributing

Country of Geniuses grows through small, verifiable contributions. Local knowledge is valuable, but an unverified procedure can cause real harm, so every contribution needs a clear evidence boundary.

## Good first contributions

- Add or correct a public source in a jurisdiction pack.
- Document how a service identifies its jurisdiction and request categories.
- Add a fictional example or a schema validation check.
- Improve a skill step, translation, or safety explanation.
- Add an integration manifest after checking the official documentation.

## Pull request expectations

1. Explain the user or contributor problem.
2. Keep the change narrow and identify every affected path.
3. Link to primary documentation or public source material.
4. State what was tested and what remains unverified.
5. Remove personal data, credentials, private correspondence, and identifying media.
6. For a write-capable integration, document the human confirmation gate, duplicate protection, rate limits, failure behavior, and rollback or follow-up path.

Do not claim that an integration is live when it has only been designed or read from documentation. Use the status vocabulary in `integrations/README.md`.

## Case contributions

Public case material must be redacted and reproducible from public sources. A case should explain what happened, how current it was, which service was responsible, what action was taken, and what outcome was actually verified.

Do not put a private case in GitHub. Keep the private record with the participant and publish only the minimum public evidence needed to audit the process.

## Review standard

Reviewers should check source provenance, currentness, routing, privacy, duplicate risk, and whether the proposed behavior can trigger an external action. A useful change request is specific, respectful, and tied to a reproducible risk.
