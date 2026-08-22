# Tech Note 20-18: Introduction to Project Mode

**Author:** Rajae CHETOUANI, Quality Support Engineer, 4D Morocco
**Published:** October 26, 2020 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78575
**Download:** https://kb.4d.com/DLTN/TN/2020/20-18_IntroProjectMode.pdf

## Proposition
4D introduced Project mode (starting v17 R5) as a new, text-file-based database architecture designed for distributed teams and source control integration, contrasting with the traditional binary (.4DB) structure. This Tech Note gives a foundational tour of Project mode's file layout and explains, section by section, how tables, forms, methods, users, menus, and preferences are represented once a database is converted.

## Key Points
- **Creating/converting**: a new project is created via File > New > Database Project…, or an existing binary database is converted via File > Export > Structure to project…, producing a `.4DProject` folder and JSON conversion logs.
- **Tables**: schema now lives in an XML `catalog.4DCatalog` file.
- **Forms**: split into Project Forms and Table Forms, stored as individual `.4DForm` files including embedded 4D Write Pro zone properties.
- **Methods**: project methods, database methods, and triggers are stored as individual, human-readable `.4dm` text files (with comments preserved).
- **Trash**: deleted forms/methods/table forms are moved to a recoverable Trash folder rather than being purged.
- **Users & groups**: extracted from the binary structure into a `directory.json` file; single-user mode always defaults to "Designer," with real identification only mattering in Client/Server.
- **Menus, pictures, style sheets**: represented as `menu.json`, an exported picture folder (Picture Library deprecated), and platform-specific CSS files respectively.
- **User preferences**: breakpoints, window positions, and workspace state are stored as per-user JSON files.

## Featured Technology
- Project mode (.4DProject architecture)
- Binary-to-project "Structure to project" conversion + JSON conversion logs
- catalog.4DCatalog, folder.json, directory.json, menu.json
- .4dm method files / .4DForm form files
- Source-control-friendly plain-text project layout
- .4dz compiled/compressed deployment format

## Best Practices Highlighted
1. Review conversion log files (Info/Warning/Error) carefully after converting a binary database, especially Warnings that may change app behavior.
2. Treat Project mode's plain-text files as the natural basis for adopting a source control system (e.g., git) for 4D development.
3. Understand the single-user-mode authentication change (always "Designer") before relying on user/group logic that assumes classic binary-mode behavior.

## Context / Positioning
Written while Project mode was still a relatively new offering, this note served as an onboarding document for developers and teams considering the move away from binary/Design-mode databases. It reflects 4D's strategic bet — which paid off in subsequent years — that distributed, git-friendly, text-based project files would become the preferred way to build 4D applications, foreshadowing 4D's eventual full commitment to Project mode as the default architecture.

## Historical Commentary
**Status:** Still relevant

Project mode has gone on to become 4D's default and strongly recommended database architecture, and binary/.4DB Design mode is now considered legacy, relevant mainly to older, not-yet-converted databases. The core structural description in this note — catalog.4DCatalog for schema, .4dm/.4DForm text files for code and forms, directory.json for users/groups, menu.json for menus — remains an accurate account of how Project mode is organized today. What has evolved since this note was written is the surrounding tooling: 4D has since introduced more capable conversion assistants and considerably deeper git-workflow integration and documentation than existed in this early 2020 introduction, so while the concepts here are sound, developers converting today should also consult 4D's more current Project Mode and git-integration Tech Notes for the fuller, more mature tooling picture.
