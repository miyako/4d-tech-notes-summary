# Tech Note 16-14: Manage 4D Mobile Session via 4D Language

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** September 12, 2016 | **Product/Version:** 4D Mobile v15 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77620
**Download:** https://kb.4d.com/DLTN/TN/2016/16-14_Manage4DMobileSession.zip

## Proposition
A 4D Mobile session differs structurally from a standard 4D web session: it consumes its own client license and can span multiple concurrent web processes. 4D v15 R4/R5 introduced new and extended WEB commands to properly retrieve and manage 4D Mobile session information, and this note demonstrates building a Wakanda-based session administration console on top of them.

## Key Points
- **Structural difference:** a Web session ties to exactly one web process; a 4D Mobile session can span several processes (one per method call), each reset after execution.
- **Pre-v15 R4 limitation:** standard web session commands like `WEB CLOSE SESSION` simply did not work on 4D Mobile sessions before this release — 4D managed them automatically and opaquely.
- **Extended commands:** `WEB Get Current Session ID`, `WEB CLOSE SESSION`, and `WEB GET SESSION EXPIRATION` gained 4D Mobile support.
- **New command:** `WEB Get session process count` returns the number of active processes tied to a given session.
- **Renamed method:** `On Web Close Process` (formerly `On Web Session Suspend`) is now called per related web process as it closes.
- **Admin console use case:** active 4D Mobile session IDs are stored in an interprocess array (added on login, removed on logout) and rendered in a live Wakanda web view, letting an administrator forcibly end a session and free its client license.

## Featured Technology
- 4D Mobile session management commands (WEB Get Current Session ID, WEB CLOSE SESSION, WEB GET SESSION EXPIRATION, WEB Get session process count)
- `On Web Close Process` database method
- Wakanda session model / web administration console pattern
- Interprocess arrays for cross-process session tracking

## Best Practices Highlighted
1. Track active sessions centrally (e.g., in an interprocess array) so an administrator can monitor and forcibly terminate sessions to reclaim client licenses.
2. Use the new process-count and expiration commands to build proactive session-health monitoring rather than relying on silent, automatic session expiry.

## Context / Positioning
Published September 2016 for 4D Mobile v15 R5, this note documents session-management plumbing specific to 4D's native mobile/web app framework of that era (built on the bundled Wakanda server), sitting apart from classic 4D desktop development and predating ORDA's maturation as the unified data-access layer.

## Historical Commentary
**Status:** Obsolete

4D Mobile and its underlying Wakanda server have been fully discontinued, so the 4D-Mobile-specific session behaviors and the Wakanda administration console pattern described here no longer apply to current 4D development. The general-purpose WEB session commands referenced still exist for 4D's own web server, but their 4D-Mobile-specific extensions are moot.

Session/connection management in modern 4D web applications is instead handled through ORDA-based REST sessions and standard web server session commands, without any dependency on the Wakanda-specific multi-process session model this note is built around. This is a clear example of a note whose entire use case has since disappeared along with the product it served.
