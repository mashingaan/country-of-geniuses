# Jurisdiction packs

A jurisdiction pack is a small, reviewable description of how to investigate and route public-service problems in a country, region, city, or service area.

## Add a pack

Create a directory with a stable identifier such as `jurisdictions/us/boston/` or `jurisdictions/fi/helsinki/`. Keep the pack focused on public information.

Include:

- Geographic scope and language
- Official service directories
- Public source URLs and access dates
- Service categories and routing rules
- Whether each source is read-only, submission-capable, or unknown
- Authentication and approval requirements
- Rate limits, terms, and known failure modes
- A maintainer and a recheck date

Use `status: draft` until another contributor verifies the material. A pack is knowledge and routing context. It is not evidence that the country or city participates in this project.

## Privacy

Do not include resident records, private contact details, real case identifiers, credentials, or screenshots containing personal data. Use fictional examples and general locations in tests.
