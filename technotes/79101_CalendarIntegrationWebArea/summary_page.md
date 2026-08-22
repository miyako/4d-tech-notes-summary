# Tech Note 23-02: 4D for Mobile: Calendar Integration via Web Area

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** January 23, 2023 | **Product/Version:** 4D for Mobile v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79101
**Download:** https://kb.4d.com/DLTN/TN/2023/23-02_4DforMobileWebArea.zip

## Proposition
4D for Mobile's built-in view templates cover common UI patterns but not everything a mobile app might need, such as a rich calendar view. The new Open URL action in v19R7 lets developers embed custom HTML/JS views (via a web area) directly in a mobile app, unlocking far greater UI flexibility.

## Key Points
- **Open URL action:** new in 4D v19R7, links an HTML document to a mobile action so it renders inside a native mobile web area.
- **Demo app "PTOgo":** an iOS manager tool for approving/denying employee PTO requests (Name, Date, Hours, Status), used to motivate the calendar feature.
- **Third-party FullCalendar library:** the calendar UI itself is not native to 4D — it's the free FullCalendar JS bundle, embedded via a script tag pointing to `index.global.js` in the project's WebFolder.
- **Server-side templating:** `template.html` uses 4D's HTML tag syntax (`<!--#4DCODE-->`, `<!--#4DEACH-->`, `<!--#4DTEXT-->`) to inject a dynamically generated events array from 4D data.
- **Data pipeline:** a `loadDataToCal` method queries `ds.Requests.all()`, builds a color-coded event collection (orange=Pending, green=Approved, Denied omitted), and merges it into the template with `PROCESS 4D TAGS`, writing the result as `calendar.html`.
- **Refresh triggers:** the calendar HTML is regenerated on `On Mobile App Authentication` (login) and `On Mobile App Action` (after approve/deny), keeping the view current.
- **Mobile-side wiring:** an "Open URL" preset action in the Mobile Project editor points to `/calendar.html` to load it into the web area.
- **Native/web bridging:** `$4d.mobile.dismiss()` called from an HTML "CLOSE CALENDAR" button lets the web view hand control back to the native mobile UI.

## Featured Technology
- **Open URL action (4D for Mobile)** — the core v19R7 feature enabling custom HTML views inside a mobile web area.
- **FullCalendar JS library** — third-party calendar rendering engine embedded in the mobile web area.
- **PROCESS 4D TAGS** — merges 4D data into an HTML template using 4D's tag syntax.
- **$4d.mobile.dismiss()** — JavaScript bridge function that closes the current web area view and returns to native mobile UI.
- **Mobile web area** — the native container that hosts the custom HTML/JS view within the 4D for Mobile app.

## Best Practices Highlighted
1. Regenerate template-derived HTML (e.g., calendar.html) at natural data-change points (login, record updates) rather than statically, so the mobile view stays in sync with the database.
2. Provide an explicit UI affordance (e.g., a close button wired to `$4d.mobile.dismiss()`) so users can always return from a custom web view to native navigation.
3. Treat Open URL + web area as a general-purpose extension mechanism, not limited to calendars — any HTML/CSS/JS UI can be embedded this way.

## Context / Positioning
Released with 4D v19R7, this note reflects 4D for Mobile's maturation strategy: rather than building every possible UI widget natively, 4D exposes an escape hatch (Open URL + web area) that lets developers leverage the vast web/JS ecosystem for specialized UI needs within native mobile apps.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
