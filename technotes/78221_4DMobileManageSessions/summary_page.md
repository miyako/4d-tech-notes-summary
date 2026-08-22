# Tech Note 19-04: Manage 4D Mobile sessions with $info parameter in V17

**Author:** Not specified in the available material
**Published:** February 28, 2019 | **Product/Version:** 4D Mobile v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78221
**Download:** https://kb.4d.com/DLTN/TN/2019/19-04_4DMobileManageSessions.zip

## Proposition
Only the setup/readme for this Tech Note's demo database was retrievable (the full PDF text was not available), so this summary is based on that readme. It shows a 4D v17 sample form that lists active 4D Mobile REST sessions and lets an admin terminate a selected session to free up a license connection slot.

## Key Points
- **Session listing form:** launches showing connected 4D Mobile sessions, distinguishing the "Is admin Session" entry from standard client sessions.
- **REST connection trigger:** opening `http://127.0.0.1/rest/$catalog` in a browser (or connecting from Wakanda) creates a new listed client session.
- **License-slot awareness:** a Developer Pro license defaults to 3 concurrent 4D Mobile sessions; the demo illustrates hitting that limit.
- **Manual session termination:** selecting a non-admin session and clicking "End Selected Session" removes it from the list and frees the slot.
- **Underlying methods:** `getRestSessions` and `closeRestSession` project methods implement the listing/termination logic; UI lives in the "MobileSession" project form.
- **Admin session lifecycle:** the admin session is only released when the form itself is closed.

## Featured Technology
- 4D Mobile (REST-based mobile client connections)
- 4D REST server (`$catalog` endpoint)
- 4D project methods and project forms

## Context / Positioning
This note fits within 4D's push (circa v17) to make the 4D Mobile product — REST-based data exchange with mobile/Wakanda clients — practical to administer, giving developers visibility into and control over the small number of concurrent mobile sessions permitted by a given license tier.

## Historical Commentary
**Status:** Obsolete

4D Mobile as a distinct product line, along with its Wakanda Enterprise Studio dependency, was discontinued well before 2026; 4D's mobile/web strategy moved to ORDA/REST-based responsive web apps and, more recently, the separate Qodly low-code platform. The specific UI and workflow in this note (an admin form listing 4D Mobile sessions with an "Is admin Session" flag) is no longer applicable to current 4D development.

The general underlying idea — that a 4D REST server tracks sessions and that administrators may need to inspect/force-close them — remains conceptually valid in modern 4D REST/ORDA server administration, but today's session APIs and management tools (e.g. `$info`, session force-login parameters in the current REST API, and Server Administration Window tooling) differ substantially from what this 2019 demo used, so the specific code shown should not be reused as-is.
