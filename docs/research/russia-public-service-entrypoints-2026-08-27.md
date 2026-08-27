# Russia public-service entrypoint research

Checked: 2026-08-27

Scope: official Russian entrypoints that can help an agent discover a public-service signal, identify an owner, check public context, and prepare a human-reviewed next step. This is a source note for the Russia skill, not a claim that any submission connector is live.

## Method and boundary

A free OpenCode research scout produced an initial lead list. The maintainers independently checked the useful claims against official pages and kept only the claims needed for routing. No form, POST request, credential, or external write was used.

The current environment does not provide a reliable in-country session for every Russian portal. A live page or account-gated action must be rechecked from an appropriate participant environment before the skill labels a method `tested-read` or prepares a real submission.

## Findings

### GIS ЖКХ

Official help describes an open part of the State Information System for Housing and Utilities. It says that some public information is available without an account, including information about homes, managing organizations, tariffs, and capital repairs.

Sources:

- [GIS ЖКХ housing registry](https://cdn.dom.gosuslugi.ru/webhelp/topics/housings/housings_och/c_housings-och.html)
- [How to view house information](https://cdn.dom.gosuslugi.ru/webhelp/topics/housings/housings_och/t_view-och.html)
- [How to create a housing and utilities appeal](https://cdn.dom.gosuslugi.ru/webhelp/topics/messages/sent/t_add-ov_otchet.html)
- [GIS ЖКХ appeals](https://cdn.dom.gosuslugi.ru/webhelp/sozhk/topics/messages/c_messages.html)

Routing implication: for a housing or utilities signal, first look up the public house record, managing organization, inspections, planned interruptions, and capital-repair context. Treat a personal appeal in GIS ЖКХ as account-gated and keep the participant's identity and private address local.

The official help describes a saved or sent appeal and says that the addressee can be selected from a directory. This supports preparation guidance only. It does not prove that an API or unattended submission path exists.

### Federal public-services portal

[Gosuslugi](https://www.gosuslugi.ru/) is the federal public-services entrypoint. This skill treats it as a service-specific route when an official service page provides the required form and recipient. It does not assume that Gosuslugi exposes an anonymous public list of civic service requests or an Open311-compatible API.

That API statement is a verification boundary, not a claim that no private or authenticated interfaces exist. Any request to use an account, ESIA, phone number, email address, or personal document must remain a participant-controlled action.

### Federal open data

[Data.gov.ru](https://data.gov.ru/?language=ru) describes itself as a centralized public access point for open government information. It is useful for finding datasets about transport, housing, environment, budgets, and inspections.

Routing implication: use an individual dataset as evidence about a published record or statistic. Do not treat the existence of a dataset as proof that a particular local problem exists, that the data is current, or that the dataset owner accepts service requests.

### Saint Petersburg

[Наш Санкт-Петербург](https://gorod.gov.spb.ru/about/) is an official city portal for messages about housing, utilities, city improvement, roads, sidewalks, public facilities, and other listed categories. The official page says that city services process messages within established periods and that users can follow handling and rate the response.

[The unified electronic reception](https://letters.gov.spb.ru/) is the official Saint Petersburg route for electronic appeals to executive bodies and municipal authorities. The page provides a submission route, status checking, and login options. The skill must treat this as a human action channel, not as a background connector.

Sources:

- [About Наш Санкт-Петербург](https://gorod.gov.spb.ru/about/)
- [Saint Petersburg electronic reception](https://letters.gov.spb.ru/)
- [Official city note about Наш Санкт-Петербург](https://www.gov.spb.ru/gov/otrasl/c_information/news/300760/)

### Moscow

Official Moscow material lists [Наш город](https://gorod.mos.ru/) and the [Moscow open-data portal](https://data.mos.ru/) as city digital resources. The portal itself and its submission rules need a current method-level check from a participant environment before a Moscow pack can claim a tested submission path.

Source:

- [Official Moscow transport portal partner links](https://transport.mos.ru/help/links)

## Implications for the Russia skill

1. Start with the exact region and municipality. Russia has no assumed national 311 workflow in this skill.
2. Identify the asset owner from an official service directory, sector registry, or municipal pack before drafting anything.
3. For housing and utilities, check GIS ЖКХ public records and active programs before treating an empty city-portal search as a new issue.
4. For Moscow and Saint Petersburg, check the public history or result view of the city portal before preparing a duplicate message.
5. Use Gosuslugi or a regional electronic reception only when the official route matches the problem and the participant can review the exact fields and data disclosure.
6. Use open-data portals for discovery and evidence. They are not complaint channels.
7. If the relevant city or region has no maintained pack, stop with `unverified` rather than guessing the recipient or inventing an API.

## Recheck requirements

The Russia jurisdiction pack should remain `draft` until a contributor with a suitable Russian-region session verifies a concrete city and method. Promotion to `tested-read` requires the exact URL or API method, response status, access time, observed capability, rate or account boundary, and privacy review. No write status can be assigned without explicit permission and a safe test.
