# Russian Federation routing overlay

Status: `draft`

Checked: 2026-08-27

Scope: a federal routing overlay for the Russian Federation. This is not a complete pack for any specific region or municipality. A city or region needs its own maintained pack before an agent should claim a tested route.

Primary language: Russian. Shared repository documentation remains in English unless a localized file is the subject of the change.

## Core official entrypoints

| Layer | Official entrypoint | Use in this project | Boundary |
| --- | --- | --- | --- |
| Housing and utilities | [GIS ЖКХ](https://dom.gosuslugi.ru/) and [official open-part help](https://cdn.dom.gosuslugi.ru/webhelp/topics/housings/housings_och/t_view-och.html) | Read public house, managing-organization, inspection, interruption, tariff, and capital-repair context | An account-gated appeal is a participant action. No API or unattended write is claimed. |
| Federal services | [Gosuslugi](https://www.gosuslugi.ru/) | Use an exact official service page when the problem matches a defined e-service | Do not assume an anonymous issue list or Open311-compatible API. |
| Federal open data | [Data.gov.ru](https://data.gov.ru/?language=ru) | Find published datasets that can support discovery and evidence | A dataset is not a complaint channel and does not prove a local problem is current. |
| Saint Petersburg city messages | [Наш Санкт-Петербург](https://gorod.gov.spb.ru/about/) | Check city-service categories, public results, and handling context | Applies to Saint Petersburg only. Submission and account actions require the participant. |
| Saint Petersburg formal appeals | [Electronic reception](https://letters.gov.spb.ru/) | Consider only when the official route and escalation level fit the issue | Human action channel. Do not automate login or sending. |
| Moscow city resources | [Наш город](https://gorod.mos.ru/) and [Moscow open data](https://data.mos.ru/) | Starting points for a future Moscow-specific pack | Current method-level behavior must be rechecked from a participant environment. |

## Routing rules

1. Start with the exact region and municipality. This overlay does not assume one nationwide public 311 endpoint.
2. Identify the asset owner from an official source before drafting a message.
3. For ЖКХ, use the public GIS ЖКХ record to identify the house and managing organization, then check inspections, planned interruptions, and capital-repair programs.
4. Check an applicable city portal's public history before treating an empty result as a new issue.
5. Use Gosuslugi or a regional electronic reception only when the exact official service matches the issue. Keep identity and private evidence local.
6. Use Data.gov.ru and other open-data portals for evidence and discovery, never as proof of ownership or as a submission channel.
7. If the official sources disagree or the local route is not maintained, mark the route `unverified` and stop before preparing an action.

## Account and privacy boundary

The participant must control ESIA or other account access. Never request or store passwords, one-time codes, cookies, personal documents, personal account numbers, apartment details, meter serials, private correspondence, or identifying media in this repository.

An exact public facility or house address may be recorded only when it is already public, necessary for routing, and safe to publish. A participant's private address remains local.

## Source notes

The [Russia entrypoint research note](../../docs/research/russia-public-service-entrypoints-2026-08-27.md) records the source basis, current verification limits, and the difference between public read context and account-gated action. No write capability is claimed for this overlay.

## Maintainer and recheck

Maintainer: Country of Geniuses maintainers

Next recheck: 2026-09-10
