# Tech Note 22-01: 4D for Android: Computed Attributes and More

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** January 24, 2022 | **Product/Version:** 4D v19 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78858
**Download:** https://kb.4d.com/DLTN/TN/2022/22-01_CumputedAttrib_4DforAndroid.zip

## Proposition
Demonstrates how to use 4D for Android's Mobile Project editor to build a full native Android app (schoolDB) with computed attributes exposed as publishable fields, custom data formatters, and authenticated per-role data filtering.

## Key Points
- **4D for Android**: a since-discontinued 4D product for generating native Android apps directly from a 4D structure, requiring the Android SDK/Android Studio.
- **exposed keyword**: marks a computed-attribute getter function so it can be published as a field in the Mobile Project's Structure section.
- **Custom data formatters**: manifest.json with a `choiceList` maps raw field values (e.g., integer grades) to custom display assets (letter-grade icon images).
- **Mobile Project editor sections**: Structure (publish fields), Forms (drag-and-drop list/detail templates), Labels & Icons, Publishing (authentication toggle), Data (filter query strings).
- **On Mobile App Authentication method**: authenticates users by email against Students/Teachers tables and returns a userInfo object used downstream for row-level filtering.
- **Role-based filter queries**: e.g., `email = :userEmail` for students vs. wildcard access for teachers, implemented via ORDA filter-query strings tied to the authenticated user's context.
- **Simulator testing**: apps are tested via an Android device simulator integrated into the Mobile Project editor's Build tab.

## Featured Technology
- 4D for Android (4D Mobile app generator)
- ORDA computed attributes (exposed getters)
- Custom data formatters (manifest.json)
- Mobile Project editor (Structure/Forms/Publishing sections)
- On Mobile App Authentication

## Best Practices Highlighted
1. Expose computed attributes with the `exposed` keyword specifically so they can serve as UI-ready mobile fields, keeping formatting logic out of the app's raw data model.
2. Implement authentication and per-role filter queries together so sensitive data (e.g., other users' records) is filtered server-side, not just hidden in the UI.
3. Use custom data formatters (manifest.json) to translate raw stored values into user-friendly icons/labels without altering the underlying schema.

## Context / Positioning
Published at the tail end of 4D's investment in native mobile app generation, this note shows the platform's mobile ambitions at their most developed (drag-and-drop native app building with ORDA-backed computed attributes) shortly before 4D pivoted its mobile/low-code strategy toward Qodly and responsive web/ORDA-REST apps instead of native app generation.

## Historical Commentary
**Status:** Obsolete

This is one of the clearer examples of technology obsolescence in this batch: 4D for Android/iOS (the native mobile app generator) was discontinued, and the specific Mobile Project editor workflow, manifest.json data-formatter mechanism, and On Mobile App Authentication method described here no longer apply to current 4D. Developers today needing mobile/responsive access to a 4D backend would instead build a web app using ORDA/REST (and increasingly Qodly Studio for low-code UI) rather than 4D's native app generator. That said, the underlying ORDA computed-attributes concept it demonstrates (exposed getter functions, per-role filter queries via `On Mobile App Authentication`-style logic) remains conceptually transferable to REST/ORDA web app authentication patterns even though the specific product vehicle is gone.
