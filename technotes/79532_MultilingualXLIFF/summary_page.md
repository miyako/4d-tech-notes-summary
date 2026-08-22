# Tech Note 24-11: Multilingual Support in 4D Databases with XLIFF Integration

**Author:** Karim MEGHRAOUI, Technical Support Engineer, 4D Morocco.
**Published:** September 25, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79532
**Download:** https://kb.4d.com/DLTN/TN/2024/24-11_MultilingualWithXLIFF.zip

## Proposition
Reaching a global audience requires more than translating displayed text — it demands a maintainable localization architecture. This note shows how 4D uses the OASIS XLIFF standard to centralize translations, letting applications dynamically switch languages per user or deployment without code changes.

## Key Points
- **XLIFF replaces legacy resource files:** Modern 4D favors XLIFF (.xlf) and .png files in a Resources folder over the older .RSR/.4DR resource file formats, aligning with Apple's current guidelines.
- **trans-unit structure with resname keys:** Each translatable string is a `<trans-unit>` element with a unique resname (e.g., "day_1"), referenced in 4D form objects via `:xliff:day_1` syntax instead of hardcoded text.
- **lproj folder convention drives language switching:** Placing XLIFF files inside en.lproj/es.lproj/fr.lproj folders lets 4D automatically pick the right translation set per active language.
- **Four-tier language resolution priority:** System language (macOS) → current 4D application language → English default → first lproj folder found, illustrated with three real deployment scenarios.
- **SET DATABASE LOCALIZATION overrides automatic selection:** Using RFC 3066/ISO639/ISO3166 codes (e.g., "fr"), developers can force a specific interface language at runtime, with Get database localization to read the current setting.
- **Get localized string retrieves specific translations:** Given a resName like "month_1", the command returns the translation matching the current active language.
- **4D's own UI stays in the build language:** Query editor, sort dialogs, and Quick Reports always render in the language the application was originally built in, regardless of database localization — requiring custom UI for full localization.
- **Asian/Arabic language support notes:** Windows IME support in the code editor, macOS's now-universal MeCab library for Japanese, and a UTF-8 import procedure for Arabic Excel data via DOCUMENT TO BLOB/Convert to text.

## Featured Technology
- **XLIFF (.xlf) files** — OASIS-standard XML format centralizing translation data.
- **lproj folders** — per-language resource folder convention (en.lproj, fr.lproj, es.lproj, etc.).
- **SET DATABASE LOCALIZATION** — forces the active interface language for a database session.
- **Get database localization** — retrieves the currently active language.
- **Get localized string** — retrieves a specific translated string by resName.
- **Unicode / UTF-8** — underlying character encoding enabling multilingual text storage and interoperability.

## Best Practices Highlighted
1. Keep resname/id values consistent across all language XLIFF files for the same UI element.
2. Leave 4D's code editor on the default "English-US" setting to keep methods portable and version-control-friendly.
3. Ensure the current data file's text comparison language is set correctly (e.g., Arabic) before importing non-Latin script data.
4. Remove references to legacy .RSR/.4DR resource files when converting older databases to XLIFF-based localization.

## Context / Positioning
Published as 4D continues modernizing its resource management to match Apple's evolving platform guidelines, this note supports 4D's broader localization/internationalization push — helping developers deliver applications tailored to increasingly diverse, global user bases while staying aligned with current OS-level language and Unicode standards.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
