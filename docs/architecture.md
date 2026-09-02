# Architecture

Country of Geniuses is a repository-first coordination layer. The participant's agent performs the work locally or on the participant's chosen platform. The repository provides shared knowledge and machine-readable contracts.

## Layers

### 1. Skills

Skills define an ordered investigation process. They tell an agent what to collect, when to stop, and how to present uncertainty. The first skill is `skills/civic-problem-triage/SKILL.md`.

### 2. Jurisdiction packs

Jurisdiction packs describe local service boundaries, official source locations, language, access requirements, and known limitations. They are context, not permission to submit.

### 3. Integration contracts

An integration manifest records what an API or MCP server is believed to support and how that claim was verified. A manifest can be useful before an executable connector exists. Status and evidence keep the distinction visible.

### 4. Problem cards

The problem card is the shared unit of work. It joins a signal, evidence, currentness checks, routing, proposed action, and public outcome without requiring private case data to be stored in GitHub.

### 5. Human action boundary

The repository can help an agent prepare an action. The participant remains the decision maker for external submission until a narrowly scoped automation has been separately reviewed and enabled.

### 6. Civic Signal Protocol

The protocol is a separate machine-readable handoff envelope for a future government agent or official service adapter. It keeps the problem card as the public investigation record while adding an idempotency key, explicit recipient, human approval state, receipt, and structured response statuses. It is transport agnostic, so MCP, HTTPS, a queue, or a participant-controlled form can act as an adapter without becoming the protocol itself. See [`docs/civic-signal-protocol.md`](civic-signal-protocol.md).

## Data flow

`public signal -> local evidence set -> problem card -> service routing -> signal preview -> human confirmation -> external channel -> receipt -> public redacted outcome`

The repository does not need to receive all source data or operate a central database to provide value. Its durable assets are tested procedures, source provenance, local service knowledge, and lessons from completed work.

## Planned extension points

- Read-only public data connectors
- Open311-compatible service profiles
- MCP tool contracts for discovery, routing, and status lookup
- Local stores for private evidence and credentials
- A deduplication index that never stores more personal data than required

Each extension must preserve the privacy and confirmation boundaries in `docs/trust-and-safety.md`.
