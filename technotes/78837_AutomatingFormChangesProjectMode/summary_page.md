# Tech Note 21-23: Automating Form Changes in Project Mode

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** December 20, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78837
**Download:** https://kb.4d.com/DLTN/TN/2021/21-23_AutomatingFormChanges.zip

## Proposition
Because project-mode forms are stored as readable JSON, this note shows how to script bulk changes across every form in a database (e.g., restyling all buttons matching a pattern) instead of editing each form manually in the Form editor.

## Key Points
- **.4DForm is JSON**: project mode stores every form as human-readable JSON, unlike binary mode's opaque structure records.
- **Folder layout**: Project/Sources/Forms/{name}/ for project forms, Project/Sources/TableForms/{tableNum}/{name}/ for table forms.
- **Form JSON schema**: a `pages` collection holds per-page `objects`, each keyed by object name with its own property attributes (type, dimensions, text, events, etc.).
- **applyFormChangesByAttribute method**: enumerates all form paths via FORM GET NAMES/GET TABLE TITLES, then bulk-applies a collection of property changes to every object matching a name or type filter.
- **Demo 1**: restyles every button whose name matches '3D@' into a custom raised button with a background image across the entire project in one method call.
- **Demo 2 (log-driven variant)**: applies form fixes based on entries from a conversion error log rather than manual name/type criteria, directly aiding binary-to-project migration cleanup.
- **Round-trip persistence**: JSON Parse → modify in memory → JSON Stringify → TEXT TO DOCUMENT writes changes back to disk.

## Featured Technology
- Project mode .4DForm JSON files
- JSON Parse / JSON Stringify
- FORM GET NAMES / GET TABLE TITLES
- TEXT TO DOCUMENT

## Best Practices Highlighted
1. Back up (or use version control on) the Project/Sources folder before running bulk JSON-editing scripts against forms.
2. Prefer matching by object type when the same fix should apply broadly, and by name pattern for narrower, intentional targeting.
3. Pair form-JSON automation with the project mode conversion log (see TN 22-03) to resolve migration warnings/errors at scale.

## Context / Positioning
This note exemplifies one of project mode's most practical developer-experience benefits — plain-text, scriptable forms — and shows 4D actively encouraging developers to treat forms as data (JSON) that can be manipulated with code, a capability entirely unavailable in binary mode.

## Historical Commentary
**Status:** Current

Fully current: project-mode forms are still plain .4DForm JSON files, and the JSON Parse/JSON Stringify + FORM GET NAMES approach shown here works unchanged on modern 4D versions. If anything, this is a good illustration of a durable capability that is unique to (and only possible because of) project mode, and it remains a recommended technique for large-scale form maintenance or binary-to-project migration cleanup today.
