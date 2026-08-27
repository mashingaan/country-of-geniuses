# San Francisco Muni accessibility pack

Status: `tested-read`

Checked: 2026-08-27

Scope: City and County of San Francisco, California, United States

Primary language: English. SFMTA pages expose additional language options and SF 311 is the general city service channel.

## Official sources

- [SFMTA Muni Metro Elevator Status](https://www.sfmta.com/travel-updates/muni-metro-elevator-status)
- [SFMTA live elevator status endpoint](https://www.sfmta.com/elevator-status/elevatorstatus.php?src=prod)
- [SFMTA contact page](https://www.sfmta.com/contact-us)
- [SFMTA Muni Feedback](https://www.sfmta.com/getting-around/muni/muni-feedback)
- [SF 311 cases dataset](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/about_data)
- [SF 311 Socrata API](https://data.sfgov.org/resource/vw6y-z8j6.json)

## Read-only capabilities

| Capability | Method | Evidence from this pack |
| --- | --- | --- |
| Elevator status discovery | `GET` SFMTA status page and embedded endpoint | HTTP 200 and current station-by-station status were observed on 2026-08-27 |
| Service routing | Read SFMTA contact and Muni Feedback pages | Both pages identify SFMTA Muni feedback and 311 as public contact routes |
| Duplicate search | `GET` SF 311 Socrata API | A bounded query for elevator cases at Powell or Hallidie returned zero rows for the selected recent window |
| Submit Muni report | Not tested | No write capability is claimed |

## Routing rules

- An out-of-service Muni elevator belongs to SFMTA Muni service and accessibility handling.
- The status page tells users in a station to notify the nearest Station Agent. It also directs people outside a station to 311.
- The SFMTA contact page publishes the Muni Feedback form and the city 311 phone route. The exact channel should remain visible in the action draft.

## Duplicate and freshness rules

- Search SF 311 for `service_name = Muni Service Feedback`, `service_details = elevators_escalators`, the specific public facility or nearby public intersection, and a bounded recent window.
- A zero result means no matching public case was found in the selected dataset and window. It does not prove that no internal maintenance case exists.
- Preserve older closed matches as context rather than treating them as an active duplicate.
- The status feed includes a page-valid timestamp and a per-elevator `Last Changed` value. Do not interpret an old `Last Changed` value as proof that the outage began on that date.
- The station summary may still say `Accessible` when one elevator is out of service because alternate elevators remain available.

## Authentication and approval

The tested status and duplicate-search paths are unauthenticated reads. The SFMTA contact and Muni Feedback pages were read but no form submission was attempted. Any future submission needs a current preview, duplicate recheck, explicit human confirmation, and a local receipt record.

## Privacy boundary

Keep names, contact details, exact private addresses, photos, tokens, case references, and private correspondence outside the repository. A public station name and a public facility label are sufficient for this pack.

## Maintainer and recheck

Maintainer: Country of Geniuses maintainers

Next recheck: 2026-09-10
