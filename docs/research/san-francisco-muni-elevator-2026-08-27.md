# San Francisco Muni elevator signal research

Date: 2026-08-27

## Research question

Can a current public accessibility problem be verified from an official source, routed to the correct service, and checked against public SF 311 records and active project pages before preparing a human-confirmed draft?

## Candidate selected and initial error

The SFMTA live elevator status endpoint returned HTTP 200 and reported `Hallidie Plaza - Street Elevator` at Powell Station as `Out of service`. The feed said the status was valid as of 9:58 AM on 2026-08-27. The station summary still marked Powell as accessible, which is consistent with the same feed showing other Powell elevators in service.

This is a current public-service signal. The per-elevator `Last Changed` value is 1/16/20, but that value is source metadata and does not prove that the fault began on that date.

The initial draft incorrectly routed the condition to SFMTA Muni because the live status page is hosted by SFMTA. That was not enough to establish ownership.

## Ownership and project correction

SFMTA's accessibility strategy states that the Hallidie Plaza elevator between Market Street and the concourse is not functional and is in DPW jurisdiction. The official Public Works Hallidie Plaza project page says the elevator is decommissioned and will be permanently removed. The project will build accessible ramps between Market Street, plaza level, and the BART or Muni station level. Its published construction timeline is Summer 2027 through Spring 2028.

This project context means the issue is already known and assigned at the program level. A zero-result SF 311 query does not establish that the issue lacks an existing government response. The corrected disposition is `discarded` as a new repair candidate, with the routing error preserved for skill improvement.

## Responsible service after correction

San Francisco Public Works is the correct project owner for this asset. The SFMTA strategy is the ownership basis, and the Public Works project page is the active project route. The SFMTA status page remains useful as a discovery source and does not override the ownership statement.

## Duplicate search

The public SF 311 dataset was queried for:

- `service_name = Muni Service Feedback`
- `service_details = elevators_escalators`
- `requested_datetime >= 2026-05-29T00:00:00`
- an address containing `POWELL` or `HALLIDIE`

The query returned `count: 0` at 2026-08-27T17:06:24Z. A wider historical query found five matching Powell-related elevator cases. All were closed, and the newest was opened on 2025-10-15 and last updated on 2025-10-16. This supports `no current public duplicate found in the selected window`, not a claim that the underlying condition lacks an existing Public Works project or internal maintenance history.

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
- [SFMTA accessibility strategy: reliable elevators and escalators](https://www.sfmta.com/accessibility-strategy-needs-assessment-2024/muni-capital-projects/32-reliable-elevators-and-escalators) supports the DPW jurisdiction statement.
- [Public Works Hallidie Plaza Accessibility Improvements](https://sfpublicworks.org/HallidiePlaza) supports the decommissioned status, permanent removal, replacement ramps, project team, and construction timeline.
- [SF 311 dataset description](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/about_data) supports the dataset owner, update process, and field meanings.
- [SF 311 duplicate count query](https://data.sfgov.org/resource/vw6y-z8j6.json?%24select=count%28%2A%29%20as%20count&%24where=service_name%3D%27Muni%20Service%20Feedback%27%20and%20service_details%3D%27elevators_escalators%27%20and%20requested_datetime%20%3E%3D%20%272026-05-29T00%3A00%3A00%27%20and%20%28upper%28address%29%20like%20%27%25POWELL%25%27%20or%20upper%28address%29%20like%20%27%25HALLIDIE%25%27%29) supports the zero-result recent duplicate check.
