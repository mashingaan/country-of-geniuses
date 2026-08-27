# San Francisco Hallidie Plaza routing correction run

Date: 2026-08-27

## Objective

Find one current non-emergency accessibility problem, check for a matching public request, verify the owning agency and active project context, and stop if a new action would duplicate or misroute existing work. No external submission is part of this run.

## Signal and currentness

The official SFMTA live elevator status endpoint was fetched at 2026-08-27T17:05:56Z. It returned HTTP 200 and said the feed was valid as of 9:58 AM on 2026-08-27. It listed the Powell Station `Hallidie Plaza - Street Elevator` as `Out of service` with `Last Changed` shown as 1/16/20 at 2:55 PM.

The source does not establish whether the equipment has been continuously broken since 2020 or whether the source's per-elevator timestamp is stale. The current status is the evidence. The station remained marked accessible because other Powell elevators were listed as in service.

## Duplicate check

The SF 311 Socrata API was queried at 2026-08-27T17:06:24Z for Muni elevator cases opened from 2026-05-29 through the check time and with an address containing Powell or Hallidie. The result was `count: 0`.

The same query without the recent date filter returned five historical Powell-related elevator records. All had status `Closed`. The newest was opened on 2025-10-15 and last updated on 2025-10-16. These historical records are retained as duplicate context and do not prove that the current outage has no maintenance history.

The check means `no matching current public 311 case found in the selected window`. It does not prove that no internal SFMTA maintenance case exists, that the public dataset has zero delay, or that a new report will be accepted.

## Routing correction

The initial route to SFMTA Muni was incorrect for this asset. SFMTA's accessibility strategy explicitly says that the Hallidie Plaza elevator between Market Street and the concourse is not functional and is in DPW jurisdiction. The official Public Works project page says the elevator is decommissioned and will be permanently removed as part of an accessibility project with new ramps. Construction is listed for Summer 2027 through Spring 2028.

The live SFMTA status page was useful for discovering the condition, but it did not establish ownership. The public SF 311 zero-result query was also insufficient because the condition is already represented by a capital accessibility project rather than a new maintenance request.

## Disposition

The card is now `discarded` as a new repair candidate. It preserves the official status evidence, the earlier bounded duplicate check, the corrected Public Works route, and the reason no SFMTA draft should be sent.

The card does not include a person's name, contact details, exact private address, photo, token, or historical case identifier. No action draft is stored because the next useful action would be a separately scoped project-status inquiry, not a repair request.

## No-write boundary

- Status pages were read only.
- The SF 311 API was read only.
- No SFMTA feedback form was opened for submission.
- No message, case, or public report was sent.
