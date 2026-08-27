---
name: open311-read-only-discovery
description: Use when an agent needs to investigate a public-service signal through an Open311-compatible endpoint without submitting a request.
---

# Open311 read-only discovery

Use this skill to turn a bounded Open311 search into evidence for `civic-problem-triage`. It covers service discovery, public request lookup, currentness, duplicate checks, and safe redaction. It does not authorize POST requests, API-key creation, form submission, or any other external write.

## Before calling the endpoint

1. Define the jurisdiction, problem category, public location precision, and a time window no longer than the endpoint permits.
2. Read the matching jurisdiction pack and integration manifest. If either is missing, stale, contradictory, or marked `planned`, stop or label the result as unverified.
3. Record the exact base URL, query parameters, access time, and permitted read methods. Do not copy credentials into the card or repository.

## Read-only sequence

1. Call `GET /services.json` and record the HTTP status, response format, access time, and relevant service names and codes.
2. If the service has a definition endpoint, call its `GET` method and record only fields needed to understand routing or required request data.
3. Query `GET /requests.json` with the narrowest supported service, date, status, and page parameters. Respect the jurisdiction's documented date window and rate limit. Do not substitute generic pagination parameters without checking the local documentation.
4. Use `GET /requests/{service_request_id}.json` only for a public record that is relevant to the bounded signal.
5. Treat a zero-result query as a bounded observation. It does not prove that no internal, phone, web-form, capital-project, or maintenance record exists.

## Evidence and privacy

Keep separate timestamps for direct observation, request creation, source update, and API access. A request update timestamp is not an observation timestamp.

Open311 responses may contain addresses, coordinates, descriptions, media URLs, account fields, and tokens. Keep those fields in the participant's private local record unless a public redacted artifact proves they are necessary. Never place an API key, token, private response, or identifying media in the repository.

## Routing and action boundary

Use the service definition and the jurisdiction pack to support the responsible service. Check the asset owner and any active accessibility, construction, capital, or maintenance project before treating an empty request search as a new problem.

If an existing request matches, stop with `status: discarded` and a structured `duplicate` reason. If the route or currentness is unclear, stop with a structured reason instead of guessing.

If no duplicate is found and the problem is sufficiently supported, produce a privacy-safe card and a human-reviewable draft. Set `human_confirmation_required` to `true`. Stop before any POST, form submission, message, or write-capable connector call.

## Output

Return one of the following:

- A validated problem card with the exact read-only evidence and a draft that is visibly waiting for human confirmation.
- A validated `discarded` card with the evidence checked, uncertainty, and structured stop reason.

Run the repository validator against the output card. Keep the local raw response and any private notes outside the repository.
