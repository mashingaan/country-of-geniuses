# Initial research scan

Checked 2026-08-27. This is a shortlist for future skills and integration work, not a claim that any connector is live in this repository.

## Government APIs and MCP

### Open311 GeoReport v2

- Official references: [developer resources](https://www.open311.org/develop/), [GeoReport v2 server directory](https://wiki.open311.org/GeoReport_v2/Servers/)
- Relevance: a common vocabulary for public-service requests and a directory of jurisdiction-specific endpoints
- Capability boundary: the directory shows example production and test endpoints, but an entry does not prove current availability, authentication, or write permission
- Skill implication: a jurisdiction pack should discover service definitions first, record the exact endpoint and jurisdiction, then check duplicate and submission rules
- Verification needed: endpoint health, official terms, rate limits, service categories, authentication, and a permitted non-production write test

### Boston BOS:311 Open311

- Official references: [BOS:311 API page](https://311.boston.gov/open311), [API documentation](https://311.boston.gov/open311/docs)
- Relevance: a concrete city implementation with service-request behavior, JSON and XML formats, API keys, and documented rate limiting
- Capability boundary: method-level behavior matters. On 2026-08-27, an anonymous `GET https://311.boston.gov/open311/v2/services.json` returned HTTP 200 with 10 service categories. The official page also documents API keys and default rate limiting for broader use. Catalog readability does not prove write permission
- Skill implication: check the exact method before acting, surface auth and rate limits for that method, and inspect service definitions before preparing a request
- Verification needed: current endpoint behavior, create-request fields, test environment, duplicate semantics, and a safe permissioned test

### GovInfo MCP

- Official references: [GovInfo Developer Hub](https://www.govinfo.gov/developers), [official MCP documentation](https://github.com/usgpo/api/blob/main/docs/mcp.md), [official API repository](https://github.com/usgpo/api)
- Relevance: a government-published MCP example for agent access to official content and metadata
- Capability boundary: the cited preview exposes read-oriented tools such as `searchGovInfo` and `describePackageOrGranule`. It requires an API key and uses `https://api.govinfo.gov/mcp`. It is useful for policy and document research, not direct service-request submission
- Skill implication: use source provenance, official publication dates, and package metadata as evidence fields rather than treating model output as authoritative
- Verification needed: preview status, current tool list, key limits, terms, and behavior on missing or ambiguous queries

## Open-source analogs

### FixMyStreet

- Official repository: [mysociety/fixmystreet](https://github.com/mysociety/fixmystreet)
- Relevance: an established open-source platform that maps street problems to the appropriate authority and can use email or Open311
- Transferable pattern: location and problem type drive routing, public visibility helps reveal duplicates, and the platform can be reused for different regions
- Boundary: this is a complete reporting platform, not a plug-in for Country of Geniuses. We should borrow patterns and avoid pretending to replace its operational deployment model

### Alaveteli

- Official repository: [mysociety/alaveteli](https://github.com/mysociety/alaveteli)
- Relevance: an internationalized open-source platform for Freedom of Information requests in different countries
- Transferable pattern: jurisdiction-specific procedures, public request history, and community-maintained local deployment knowledge
- Boundary: information-access requests have different legal and privacy risks from street-service reports. They need a separate skill family

### Ushahidi

- Official repository: [ushahidi/platform](https://github.com/ushahidi/platform)
- Relevance: open-source collection, categorization, geolocation, visualization, and REST API patterns for public signals
- Transferable pattern: source ingestion and human review can be separated from publication and map display
- Boundary: incoming reports can contain sensitive material. Any reuse needs a strict private store and moderation path

### Decidim

- Official repository: [decidim/decidim](https://github.com/decidim/decidim)
- Relevance: open-source participatory democracy infrastructure with community governance and public participation modules
- Transferable pattern: long-term community rules and institutional feedback can be treated as project infrastructure, not only as software features
- Boundary: this is a governance platform, not a public-service connector. It belongs in the long-term community layer

## Immediate research order

1. Define the integration manifest and verification states before adding live endpoints.
2. Build a read-only Open311 discovery skill around service definitions and endpoint evidence.
3. Select one jurisdiction from the official directory and verify it manually.
4. Keep submission behind human confirmation until duplicate, privacy, auth, and failure behavior are documented.
5. Add separate skill families for official-document research, information-access requests, and public-signal intake only after the first workflow is reproducible.
