# Tech Note 14-09: Web Area Inspector

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** June 2, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77066
**Download:** https://kb.4d.com/DLTN/TN/2014/14-09_WebAreaInspector.pdf

## Proposition
4D v14 exposes the WebKit Web Inspector inside the Web Area form object, giving developers a native way to debug load times, JavaScript, and console output for embedded web content without leaving 4D's context.

## Key Points
- The Web Area object (since v11 SQL Release 2) adopted the cross-platform WebKit rendering engine in v13; v14 adds access to its Web Inspector.
- Enabling it requires the integrated WebKit engine and Contextual Menu turned on at design time, plus a runtime call: `WA SET PREFERENCE(*;"WA";WA enable Web inspector;True)`.
- The **Network** tab surfaces load times, bottlenecks, and missing resources (timeline or sort-by-latency views).
- The **Scripts** tab supports breakpoints, step-over/into/out debugging of JavaScript running in the Web Area.
- The **Console** tab allows live JavaScript evaluation and can receive `console.log()` output triggered from 4D via `WA Evaluate JavaScript`.
- The Web Inspector can run as an undocked external window (useful with a second monitor).
- Deployment caution: the `$4d` object accessible via the console can enumerate and invoke any 4D method, including invisible ones — a security consideration for shipped applications.

## Featured Technology
- Web Area form object (integrated WebKit engine)
- `WA SET PREFERENCE`, `WA Evaluate JavaScript`
- WebKit Web Inspector (Network/Scripts/Console tabs)
- `$4d` JavaScript-to-4D method bridge object

## Best Practices Highlighted
1. Enable the Web Inspector only for development/debugging builds, not necessarily for end users.
2. Use the Network tab's latency sort to quickly find slow-loading resources.
3. Restrict or review 4D-method access granted to Web Areas before deployment, since the Inspector console can reach the `$4d` bridge.

## Context/Positioning
Published just after v14's release, this note showcased a debugging convenience that made 4D's embedded web content easier to troubleshoot at a time when Web Area/WebKit integration was still relatively new.

## Historical Commentary
**Status:** Partially superseded

Exposing WebKit's Web Inspector inside the Web Area was a genuinely useful improvement at the time, but 4D has since replaced the underlying WebKit rendering engine with a Chromium-based Web Area engine (around 4D v18), which surfaces Chromium's own DevTools rather than the legacy WebKit Web Inspector documented here. The specific commands and UI in this note are tied to the retired WebKit engine, though the underlying practice — enabling embedded browser dev tools and bridging JavaScript to native methods — remains conceptually current in 4D's newer Web Area implementation.
