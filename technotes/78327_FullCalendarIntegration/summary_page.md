# Tech Note 19-17: FullCalendar Integration

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** September 25, 2019 | **Product/Version:** 4D v17 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78327
**Download:** https://kb.4d.com/DLTN/TN/2019/19-17_fullcalendarintegration.zip

## Proposition
Rather than building a native calendar UI from scratch, 4D applications can embed the open-source FullCalendar JavaScript framework in a Web Area and bridge its events back to ORDA-based 4D methods, gaining a mature, well-supported calendar widget with minimal custom code.

## Key Points
- **Framework placement:** FullCalendar's `js`/`packages` folders live in the Database Resources folder so they deploy correctly to 4D Remote clients.
- **HTML template + glue code:** a `#calendar` div hosts the widget; JS functions `change()`, `getTitle()`, and `updateEventData()` configure and re-render the calendar.
- **Dynamic content injection:** `<!--#4DTEXT ...-->` tags are resolved via `PROCESS 4D TAGS` before the HTML is loaded into the Web Area.
- **4D → JS calls:** `WA EXECUTE JAVASCRIPT FUNCTION` triggers view/date changes on the calendar from 4D code.
- **JS → 4D callbacks:** the `$4d` bridge object (`waCallBackEventEdit`, `waCallBackEventUpdate`) is called on `eventClick`, `eventDrop`, and `eventResize`.
- **ORDA data access:** callback methods use `ds.Events.query(...)` and `entity.save()` to read/update event records.
- **Multi-user support:** the demo layers calendar sharing/permissions on top via `openCalendarMainWindow`, `openCalendarPermission`, and a `setupUserListForCalendar` hook.

## Featured Technology
- FullCalendar 4.3.1 (JavaScript, MIT licensed)
- 4D Web Area, `WA EXECUTE JAVASCRIPT FUNCTION`, `PROCESS 4D TAGS`
- ORDA (`ds.Events.query`, `entity.save()`)

## Best Practices Highlighted
1. Keep framework asset folders intact in Resources to ensure correct client/server distribution.
2. Use a dedicated JS↔4D bridge object (`$4d`) rather than ad hoc scripting for event callbacks.
3. Centralize calendar re-rendering logic in one JS function (`updateEventData`) to keep state consistent.

## Context / Positioning
This note is part of 4D's recurring "integrate a popular open-source library" series, illustrating how 4D's Web Area and ORDA together let developers avoid reinventing complex UI widgets, consistent with 4D's broader v17 R-release push toward object-notation-driven, web-technology-friendly development.

## Historical Commentary
**Status:** Partially superseded

The Web Area JS-bridging technique (`WA EXECUTE JAVASCRIPT FUNCTION`, the `$4d` callback object, `PROCESS 4D TAGS`) and the ORDA data access pattern (`ds.Events.query()`, `.save()`) are both still valid and commonly used in 4D applications today. However, FullCalendar itself has moved on considerably — the specific version (4.3.1) and some of its API details (e.g., the `defaultView`/`defaultDate` property names, plugin array style) are from FullCalendar's v4 line and have since been superseded by newer major versions (v5, v6) with revised configuration APIs. A developer implementing this today should pull the current FullCalendar release and adapt the JS glue code accordingly, or consider a Qodly-based web calendar component for pure ORDA/REST web apps.
