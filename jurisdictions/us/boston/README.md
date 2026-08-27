# Boston Open311 read-only pack

Status: `tested-read`

Checked: 2026-08-27

Scope: City of Boston, Massachusetts, United States

## Official sources

- [BOS:311 API page](https://311.boston.gov/open311)
- [BOS:311 API documentation](https://311.boston.gov/open311/docs)
- [Open311 service catalog](https://311.boston.gov/open311/v2/services.json)
- [Open311 server directory](https://wiki.open311.org/GeoReport_v2/Servers/)

## Read-only capabilities

| Capability | Method | Evidence from this pack |
| --- | --- | --- |
| Service discovery | `GET /open311/v2/services.json` | HTTP 200 with 10 service categories on 2026-08-27 |
| Request listing | `GET /open311/v2/requests.json` | HTTP 200 with `per_page=3` and `page=1` |
| Request lookup | `GET /open311/v2/requests/{service_request_id}.json` | HTTP 200 for public request `101006740558` |
| Create request | Not tested | No write capability is claimed |

The public catalog currently includes `Damaged Sign` with service code `Transportation - Traffic Division:Signs & Signals:Sign Repair` and `Traffic Signal` with service code `Transportation - Traffic Division:Signs & Signals:Traffic Signal Inspection`.

## Method-level constraints

The official documentation describes API keys and default rate limiting. These requirements must be checked against the exact method being called. A public service catalog response does not prove that request creation is available to an unauthenticated client.

The documentation describes `per_page` and `page` for request listing. A probe using an unsupported `limit=3` parameter returned 50 records, so a connector must not assume that generic pagination parameters are honored.

The documentation also describes a 90-day limit for date-based request filters. Keep search windows bounded and record the exact query.

## Privacy boundary

Public request responses can contain an address, coordinates, media URL, description, and a token. A public problem card must keep only the minimum needed for routing and duplicate detection. Omit those fields from committed examples unless a separate privacy review proves they are necessary.

## Safe use in this project

This pack supports read-only discovery and duplicate detection. It does not authorize submission. Any future write connector needs method-level documentation, explicit approval, a preview, human confirmation, duplicate protection, rate limits, and a safe test procedure.
