# Workflow

## Problem lifecycle

| State | Meaning | Exit condition |
| --- | --- | --- |
| `signal` | A public or user-provided observation exists | It has a source or a clear request for more information |
| `candidate` | The signal may represent a current public-service problem | Currentness and duplicate checks are recorded |
| `verified` | The problem has enough evidence for a responsible routing decision | The responsible service and confidence are recorded |
| `prepared` | A human-readable action draft exists | Recipient, content, source basis, and risks are visible |
| `submitted` | A human explicitly approved and sent the action | The channel and submission time are recorded locally |
| `acknowledged` | The service provided a receipt or official reference | The reference is stored outside the public repository unless it is public |
| `resolved` | The service reports completion or a public source shows a change | A follow-up check is performed |
| `closed` | A person or reliable public evidence verifies the outcome | The public record contains a redacted outcome note |
| `discarded` | The case is not actionable, current, safe, or sufficiently supported | The reason to stop is recorded |

`resolved` does not automatically mean `closed`. A service may close a ticket without fixing the underlying problem.

## Proactive mode

Use proactive mode for a bounded question such as a city, a problem category, and a time window. Search only permitted public sources. Cluster possible duplicates before preparing any action. Prefer a small set of high-confidence candidates over a large stream of weak signals.

## User-request mode

Start from the person's description. Ask only for information needed to identify the service and prepare a request. Explain what will be sent and what is still unknown. Keep private evidence local.

## Stop conditions

Stop at `discarded` or request human help when the problem is urgent, the source is not reliable enough, the responsible service is unclear, the action could expose personal data, or the case would require legal, medical, law-enforcement, electoral, or political judgment.
