# San Francisco Muni elevator prepared run

Date: 2026-08-27

## Objective

Find one current non-emergency accessibility problem without a matching current public SF 311 request, identify the responsible service, and prepare an exact draft for human review. No external submission is part of this run.

## Signal and currentness

The official SFMTA live elevator status endpoint was fetched at 2026-08-27T17:05:56Z. It returned HTTP 200 and said the feed was valid as of 9:58 AM on 2026-08-27. It listed the Powell Station `Hallidie Plaza - Street Elevator` as `Out of service` with `Last Changed` shown as 1/16/20 at 2:55 PM.

The source does not establish whether the equipment has been continuously broken since 2020 or whether the source's per-elevator timestamp is stale. The current status is the evidence. The station remained marked accessible because other Powell elevators were listed as in service.

## Duplicate check

The SF 311 Socrata API was queried at 2026-08-27T17:06:24Z for Muni elevator cases opened from 2026-05-29 through the check time and with an address containing Powell or Hallidie. The result was `count: 0`.

The same query without the recent date filter returned five historical Powell-related elevator records. All had status `Closed`. The newest was opened on 2025-10-15 and last updated on 2025-10-16. These historical records are retained as duplicate context and do not prove that the current outage has no maintenance history.

The check means `no matching current public 311 case found in the selected window`. It does not prove that no internal SFMTA maintenance case exists, that the public dataset has zero delay, or that a new report will be accepted.

## Routing

SFMTA Muni is the proposed recipient. The official elevator status page says to notify the nearest Station Agent or call 311 when an elevator is out of service. The SFMTA contact page lists the Muni Feedback form for Muni service concerns. The selected draft channel is the Muni Feedback form, with 311 as the fallback if the form cannot handle the report.

## Prepared action

The exact draft is stored in `examples/san-francisco-muni-elevator.json`. It asks the service to:

1. Confirm whether an active maintenance case already exists for the specific elevator.
2. If no active case exists, open a maintenance request for the current out-of-service condition.
3. Provide the public case reference and expected restoration date if available.
4. Correct the public status page if its current state is stale.

The draft does not include a person's name, contact details, exact private address, photo, token, or historical case identifier. It requires explicit human confirmation and was not submitted.

## No-write boundary

- Status pages were read only.
- The SF 311 API was read only.
- No SFMTA feedback form was opened for submission.
- No message, case, or public report was sent.
