# Civic Signal Protocol

Status: `draft`

Version: `0.1`

The Civic Signal Protocol is a small structured handoff between a participant-side agent and a government agent or official service adapter. It is a protocol contract, not a conversation between two models and not a permission to send a request.

## Purpose

Country of Geniuses verifies a bounded signal before it crosses into another system:

`participant agent -> evidence and routing checks -> signal preview -> human confirmation -> government agent or official adapter -> receipt or structured response`

The public investigation remains represented by a problem card. The protocol envelope is a separate transport artifact because a handoff needs an idempotency key, a recipient, a human approval state, and a response contract without putting private credentials or personal data into the repository.

## Message artifacts

- [`schemas/civic-signal.schema.json`](../schemas/civic-signal.schema.json) defines a preview or confirmed `submit_civic_signal` envelope.
- [`schemas/civic-signal-response.schema.json`](../schemas/civic-signal-response.schema.json) defines structured responses.
- [`examples/civic-signal-preview.example.json`](../examples/civic-signal-preview.example.json) is fictional and unconfirmed.
- [`examples/civic-signal-response.example.json`](../examples/civic-signal-response.example.json) is fictional and demonstrates `needs_evidence`.

## Required handoff content

Every envelope records:

- the protocol version and stable client signal ID
- jurisdiction, public asset, problem summary, and observation time when known
- primary evidence URLs with source type, access time, and support statement
- responsible service, official routing basis, contact method, and confidence
- bounded duplicate search and active-project check
- overall confidence and the proposed action
- a privacy assertion and labels for any participant-controlled fields
- the exact fields reviewed by a person
- an idempotency key and request for a receipt

The public envelope contains field labels, not credentials or private values. A participant may add private data directly in an official channel after reviewing the action. That local step is outside the public packet.

## Lifecycle

1. The participant agent produces a `signal_preview`.
2. The agent shows the recipient, exact content, evidence, disclosure, duplicate risk, and project check to the participant.
3. Only after explicit approval is the same packet emitted as `submit_civic_signal` with `human_confirmation.confirmed: true`.
4. The receiving agent or adapter returns one structured response: `accepted`, `duplicate`, `needs_evidence`, or `rejected`.
5. An accepted response contains a receipt ID. Receipt creation is not proof that the underlying problem was fixed.
6. Later status responses can be `received`, `in_progress`, `resolved`, or `closed`. A closed service record still needs independent outcome verification before the problem card is closed.

An implementation must not turn a `duplicate`, `needs_evidence`, or `rejected` response into an automatic resend. A new outbound action requires a fresh preview and human confirmation.

## Capability contract

The protocol can be transported by MCP, HTTPS, a queue, or a participant-controlled form adapter. The transport must not change the packet semantics.

### `submit_civic_signal`

Input: a validated `submit_civic_signal` envelope.

Preconditions:

- the recipient is supported by an official source
- `duplicate_check.result` is `no_match_found`
- `project_check.result` is `no_active_project`
- `privacy.contains_personal_data` is `false` for the shared envelope
- human confirmation is true and includes a confirmation time and participant marker
- the idempotency key is stable for retries of the same exact packet

Output: a validated response with an explicit status. `accepted` means the receiving system created or recorded a signal. It does not mean the service accepted responsibility or completed work.

### `check_duplicate`

Read-only operation. It may be exposed by a receiving system before submission, but the participant agent must still record its own bounded search and active-project check. The result must state the search scope, access time, and whether the result is public or private.

### `get_signal_status`

Read-only operation using a receipt or public reference. The response must distinguish system status from a verified real-world outcome.

### `request_more_evidence`

Structured response from the receiving side. It names the missing field, explains why it matters, and states whether it is required. The participant agent presents the request to a person before collecting or disclosing anything private.

## Trust and safety

- The protocol never replaces the participant's decision about an external action.
- A government agent must be identified by an official endpoint, signed integration, or a participant-verified service boundary. A model name is not an identity proof.
- The receiving side must define authentication, rate limits, duplicate behavior, error handling, retention, and status semantics before a connector is labeled `tested-write`.
- No emergency, medical, legal, electoral, law-enforcement, immigration, vulnerable-person, or identifiable-person case should be routed through an unreviewed agent handoff.
- The protocol rewards useful abstention. A stop because of a duplicate, active project, wrong owner, missing evidence, or privacy risk is a valid outcome.
- Retries use the same idempotency key only for the same exact packet. Changed evidence or changed content creates a new preview.

## Compatibility

An MCP tool is an adapter to this contract, not the protocol itself. A service can implement the contract without MCP, and an MCP server can expose the contract without becoming an official government participant.

Version `0.1` is intentionally narrow. It does not define identity federation, payment, legal deadlines, a universal government directory, a public database, or autonomous follow-up.

## Adoption path

1. Validate local previews and responses against the schemas.
2. Run fictional and read-only interoperability tests between two independent implementations.
3. Add one official service adapter only after its exact endpoint, authentication, rate limits, duplicate behavior, privacy boundary, and human confirmation flow are verified.
4. Publish redacted receipts and outcomes without exposing participant credentials or private case data.
