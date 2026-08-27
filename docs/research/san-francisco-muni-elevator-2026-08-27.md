# San Francisco Muni elevator signal research

Date: 2026-08-27

## Research question

Can a current public accessibility problem be verified from an official source, routed to the correct service, and checked against public SF 311 records before preparing a human-confirmed draft?

## Candidate selected

The SFMTA live elevator status endpoint returned HTTP 200 and reported `Hallidie Plaza - Street Elevator` at Powell Station as `Out of service`. The feed said the status was valid as of 9:58 AM on 2026-08-27. The station summary still marked Powell as accessible, which is consistent with the same feed showing other Powell elevators in service.

This is a current public-service signal. The per-elevator `Last Changed` value is 1/16/20, but that value is source metadata and does not prove that the fault began on that date. The draft therefore asks SFMTA to confirm the current maintenance state.

## Responsible service

SFMTA is the correct recipient because the official Muni Metro Elevator Status page describes the elevator inventory and directs people to a Station Agent or 311 when an elevator is out of service. The official SFMTA contact page also lists Muni Feedback as the online route for Muni service concerns.

## Duplicate search

The public SF 311 dataset was queried for:

- `service_name = Muni Service Feedback`
- `service_details = elevators_escalators`
- `requested_datetime >= 2026-05-29T00:00:00`
- an address containing `POWELL` or `HALLIDIE`

The query returned `count: 0` at 2026-08-27T17:06:24Z. A wider historical query found five matching Powell-related elevator cases. All were closed, and the newest was opened on 2025-10-15 and last updated on 2025-10-16. This supports `no current public duplicate found in the selected window`, not a claim that no internal SFMTA case exists.

The dataset API metadata reported `rowsUpdatedAt = 1787825825`, which is 2026-08-27T10:17:05Z. The dataset description says it is provided by San Francisco 311 and updated nightly. The duplicate result is therefore useful evidence, but it has a coverage and freshness boundary.

## Reproduction

Status fetch:

```powershell
$statusUri = 'https://www.sfmta.com/elevator-status/elevatorstatus.php?src=prod'
Invoke-WebRequest -UseBasicParsing -Uri $statusUri -Method Get
```

Duplicate count query:

```powershell
$base = 'https://data.sfgov.org/resource/vw6y-z8j6.json'
$duplicateQuery = '?$select=count(*) as count&$where=service_name=''Muni Service Feedback'' and service_details=''elevators_escalators'' and requested_datetime >= ''2026-05-29T00:00:00'' and (upper(address) like ''%POWELL%'' or upper(address) like ''%HALLIDIE%'')'
Invoke-RestMethod -Uri ($base + $duplicateQuery) -Method Get
```

Historical context query:

```powershell
$historyQuery = '?$select=service_request_id,requested_datetime,updated_datetime,status_description,address&$where=service_name=''Muni Service Feedback'' and service_details=''elevators_escalators'' and (upper(address) like ''%POWELL%'' or upper(address) like ''%HALLIDIE%'')&$order=requested_datetime desc&$limit=10'
Invoke-RestMethod -Uri ($base + $historyQuery) -Method Get
```

## Sources

- [SFMTA Muni Metro Elevator Status](https://www.sfmta.com/travel-updates/muni-metro-elevator-status) supports the purpose of the status page and the 311 or Station Agent route.
- [SFMTA live elevator status endpoint](https://www.sfmta.com/elevator-status/elevatorstatus.php?src=prod) supports the 2026-08-27 status and the Powell elevator detail.
- [SFMTA contact page](https://www.sfmta.com/contact-us) supports Muni Feedback, 311, and the public routing boundary.
- [SFMTA Muni Feedback](https://www.sfmta.com/getting-around/muni/muni-feedback) supports the selected public feedback channel.
- [SF 311 dataset description](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/about_data) supports the dataset owner, update process, and field meanings.
- [SF 311 duplicate count query](https://data.sfgov.org/resource/vw6y-z8j6.json?%24select=count%28%2A%29%20as%20count&%24where=service_name%3D%27Muni%20Service%20Feedback%27%20and%20service_details%3D%27elevators_escalators%27%20and%20requested_datetime%20%3E%3D%20%272026-05-29T00%3A00%3A00%27%20and%20%28upper%28address%29%20like%20%27%25POWELL%25%27%20or%20upper%28address%29%20like%20%27%25HALLIDIE%25%27%29) supports the zero-result recent duplicate check.
