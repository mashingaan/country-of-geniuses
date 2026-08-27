---
name: civic-problem-triage
description: Use when an agent is asked to investigate a potentially unresolved public-service problem, combine public signals, identify a responsible service, prepare a human-reviewable request, or track a public outcome with Country of Geniuses.
---

# Civic problem triage

Turn a public-service signal or a person's request into a privacy-safe, evidence-based action draft. The output is a problem card or a clear stop reason. External submission always remains behind human confirmation.

## 1. Bound the request

Write down the jurisdiction, problem type, location precision, time window, permitted sources, and requested outcome. For proactive work, use a bounded city or service area and a narrow time window. Completion means the search scope is explicit.

## 2. Build the evidence set

Collect public URLs, source types, published or observed times, access times, and one sentence describing what each source supports. Separate official records, official service pages, public reports, news, community reports, and direct observations. Preserve uncertainty and conflicting evidence. Completion means each material claim has a source or is labeled as unverified.

## 3. Check currentness and duplicates

Look for a newer observation, an existing public request, and a matching private request in the participant's local record. Cluster multiple signals into one candidate. A stale report, duplicate, or unsupported claim becomes `discarded` with a reason. Completion means the card states what was checked and what remains unknown.

## 4. Route to a responsible service

Use an official directory, service page, or locally verified jurisdiction pack. Record the service name, routing basis, contact method, and confidence. Treat undocumented or contradictory routing as a stop condition. Completion means the proposed recipient is supported by a source and the confidence is visible.

## 5. Assess safety and privacy

Remove names, contact details, exact private addresses, credentials, identifying media, and private correspondence from the public artifact. Escalate urgent danger and pause for human help for medical, legal, law-enforcement, electoral, immigration, vulnerable-person, or identifiable-person cases. Completion means the public card passes the privacy boundary and no high-risk branch is hidden.

## 6. Prepare the action

Draft the smallest useful request. Show the recipient, channel, exact content, evidence basis, data that would leave the local environment, possible duplicate risk, and expected response. Set `human_confirmation_required` to `true`. Completion means a person can understand and approve or reject the exact action without reconstructing the investigation.

## 7. Wait for confirmation

Present the draft and stop. Do not send, publish, or call a write-capable connector until the participant explicitly confirms the exact action. If the participant declines or the facts change, update the card or mark it `discarded`.

## 8. Track and verify

If a person confirms submission, record the channel and local time. Keep private reference numbers outside the repository unless they are already public. Distinguish `submitted`, `acknowledged`, `resolved`, and `closed`. A service closure is not proof of a real-world fix. Completion means the outcome is either verified by a named evidence type or clearly marked `not_verified`.

## Output contract

Use `schemas/problem-card.schema.json`. The public artifact must contain:

- A stable `cog-` identifier
- A bounded summary and status
- A privacy-safe jurisdiction
- At least one evidence item
- A sourced responsible service
- A human-reviewable action draft
- A privacy assertion and audit checks

Use `examples/problem-card.example.json` as a shape reference. Keep private evidence and credentials in the participant's local environment.
