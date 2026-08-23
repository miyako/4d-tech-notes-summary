# Tech Note: 4D Blogger and SOAP Part II

- **Asset ID:** 27707
- **Tech Note #:** 03-23
- **Published:** May 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri, Technical Support Engineer
- **Page URL:** https://kb.4d.com/assetid=27707
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_21-25_(MAY)/03-23_4D Blogger_&_SOAP_II.hqx

## Overview

Jamras Komoncharoensiri continues from Part I's discussion of the SOAP protocol between the 4D Blogger WebLog Server and WebLog Client, focusing this time on the client interface implementation and the new features shipped in 4D Blogger v2: a visual calendar, automatic background updates, multi-category support, user self-signup, and new search/display options.

## Key Points

- The WebLog calendar is built from seven coordinated form-object groups: prev/next arrow buttons, a `vMonthYear` label, a 7-item day-name header row, a 6x7 grid of oval "log exists" indicator objects, a matching 6x7 grid of day-number display variables, and a front-layer 6x7 grid of invisible click buttons -- managed by `GEN4D_CleanCalendar` (reset/hide) and `GEN4D_UpdateVisibleLog` (highlight days with posts).
- Automatic updates run via a background process, `GEN4D_GetMostCurrentData`, which loops calling `SOAP_GetVisibleLogOnCalendar` and other SOAP calls every 10 seconds (`DELAY PROCESS(Current process;60*10)`), refreshing arrays of available dates, archived months, admin usernames/IDs, and categories.
- Cross-process UI refresh is done via `CALL PROCESS(Process number("Client Panel"))`, handled in the client form's `On Outside Call` event to redraw the calendar and category list with the newly polled data.
- Multi-category support (new in v2) lets the Blog Master create, rename, or delete WebLog categories via SOAP methods `SOAP_AddCategoryName`, `SOAP_RenameCategory`, and `SOAP_RemoveCategoryName`, each pausing the background poller (`PAUSE PROCESS`) during the SOAP round-trip and resuming it (`RESUME PROCESS`) afterward, then calling `GEN4D_SetCategoryVariables` to refresh the UI.
- Category administration privileges can be assigned to a specific WebLog member via `SOAP_SetCategoryAdmin`, distinct from the single overall Blog Master account.
- New user self-signup flow validates username/password/first name/last name/email fields locally before calling `SOAP_SaveNewUser`, which returns a nonzero User ID on success (auto-login) or 0 if the username is taken.
- New search/display options add category-based browsing (`SOAP_GetLogByCategory`) and a "my logs" view of the current user's own not-yet-archived posts (`SOAP_GetMyLogs`), on top of the existing date/keyword search from Part I.
- At least one blog category must exist before any new blog post can be created, since the category selector in the Blog editor requires a populated list.

## Featured Technology

- SOAP-based WebLog Client/Server architecture
- 4D Blogger v2 sample application
- Background process polling via RESUME PROCESS/PAUSE PROCESS/DELAY PROCESS
- On Outside Call cross-process UI updates
- Custom calendar UI built from grid form objects
- SOAP category/user-management methods (SOAP_AddCategoryName, SOAP_SaveNewUser, etc.)

## Historical Commentary

**Status:** Historical interest only

This second-part note by Jamras Komoncharoensiri builds out the WebLog Client interface for the 4D Blogger v2 demo application, showing a hand-built calendar UI driven by a background polling process, multi-category blog administration, self-service user signup, and category-filtered search, all communicating with the WebLog Server over SOAP. 4D Blogger as a demo product and its SOAP client/server plumbing are long retired, and virtually all real-world blogging platforms and integrations moved to REST/JSON APIs many years ago, so the specific SOAP methods shown are of historical interest only. The generic implementation techniques on display -- background-process polling with RESUME PROCESS/PAUSE PROCESS, updating a foreground process via On Outside Call, and building a calendar from grid-arranged form objects -- remain conceptually valid 4D patterns, though modern 4D offers more capable ways to build such UIs (e.g., list boxes, richer object arrays) and to integrate with external services (native HTTP client and JSON commands) than shelling everything through SOAP.

References to newer/updated information:
- 4D Blogger and its SOAP-based WebLog Client/Server protocol are long discontinued; modern blogging and web-service integrations use REST/JSON, typically via 4D's native HTTP Client and JSON parsing commands rather than SOAP
- The general background-process polling and On Outside Call cross-process update patterns shown here are still valid 4D techniques, though current 4D also offers list boxes and richer object/array-driven UI controls that can simplify a custom calendar like the one built here
