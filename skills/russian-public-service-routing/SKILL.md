---
name: russian-public-service-routing
description: Use when investigating a public-service problem in Russia and choosing an official federal, regional, municipal, or sector route without assuming a nationwide 311 API.
---

# Russian public-service routing

Use this skill with `civic-problem-triage` when the jurisdiction is the Russian Federation. It provides a routing overlay for official sources and account-gated channels. It does not create a universal Russian service directory and does not authorize a submission.

Read [the Russia jurisdiction pack](../../jurisdictions/ru/README.md) before choosing a route. Read [the dated research note](../../docs/research/russia-public-service-entrypoints-2026-08-27.md) when a source capability or account boundary is unclear.

## 1. Fix the jurisdiction first

Record the region, municipality, settlement, and public facility or asset. Do not treat `Russia` as a sufficient routing scope. If the location is missing or the issue crosses several authorities, keep the card at `candidate` or stop with a structured reason.

Completion means the responsible territorial level is explicit and the relevant regional or municipal pack has been found or is labeled `unverified`.

## 2. Choose the source layer

Use the narrowest official layer that matches the problem:

- For housing and utilities, inspect the public part of GIS ЖКХ for the house, managing organization, inspections, planned interruptions, tariffs, and capital-repair context.
- For a defined state or municipal e-service, inspect the exact Gosuslugi or regional service page and its stated recipient. The service page is a route, not proof that a public duplicate list or anonymous API exists.
- For published statistics, registers, budgets, transport, environment, or procurement data, use an official open-data dataset as evidence only.
- For city improvement, roads, public facilities, and similar issues, use the region's official city portal or electronic reception when the maintained jurisdiction pack identifies the category and recipient.
- For Moscow and Saint Petersburg, consult the city-specific portals listed in the Russia pack. Do not generalize their behavior to another region.

Completion means the chosen source layer is tied to the issue type and has an official URL or an explicit `unverified` label.

## 3. Establish ownership

Find the organization responsible for the exact asset or service from an official directory, sector registry, service definition, or local regulation. Check active capital, accessibility, construction, maintenance, and repair projects before treating an empty search result as a new problem.

A public portal that displays an outage or accepts a message does not by itself prove ownership. If the owner is contradictory or absent, stop before preparing an action.

Completion means the owner, routing basis, source URL, and confidence are recorded in the card or the card is discarded with a reason.

## 4. Check currentness and duplicates

Search the public history or result view of the applicable regional or city portal when one exists. For GIS ЖКХ, check the public record and active program context. For Gosuslugi or a personal cabinet, ask the participant to perform any private duplicate check locally rather than requesting credentials.

Keep separate timestamps for the person's observation, a source update, a request creation, and access to the source. A portal's update time is not the observation time.

Completion means the checked source, query or search scope, access time, result, and remaining unknowns are recorded.

## 5. Prepare only a human-reviewed route

If the issue is supported and no duplicate or active project explains it, prepare the smallest useful draft for the official route. Show the recipient, channel, exact text or fields, evidence, data that will leave the local environment, account requirement, and duplicate risk. Set `human_confirmation_required` to `true`.

Treat ESIA, Gosuslugi, phone numbers, email, personal documents, apartment details, meter numbers, and private photos as participant-controlled data. Keep them outside the public repository.

Stop before login, form submission, POST, message sending, or any write-capable connector call. The participant must approve the exact external action after reviewing it.

## Stop conditions

Return a structured stop reason when:

- the city or region has no current maintained route
- the owner conflicts across official sources
- a current project, planned work, or decommissioned asset already explains the signal
- the only possible route requires private data that the participant has not chosen to disclose
- the source is stale, inaccessible, or not sufficiently official
- the situation is an emergency or involves legal, medical, law-enforcement, electoral, immigration, vulnerable-person, or identifiable-person risk

For a stopped run, produce a validated `discarded` card when public evidence can be safely recorded. Otherwise keep the raw investigation local and return the reason to the participant.

## Output contract

Return a problem card validated with `python scripts/validate-repo.py --card [local card path]`, or return a clear stop report that explains why no public card is safe. Do not label a Russian route `tested-read` or `tested-write` unless the exact method, response, access time, account or rate boundary, and privacy review have been verified.
