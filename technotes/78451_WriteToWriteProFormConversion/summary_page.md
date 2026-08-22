# Tech Note 20-06: 4D Write to 4D Write Pro Conversion Guidelines: Form and Off-screen areas

**Author:** Hamza Aharbil, Quality Support Engineer, 4D Morocco.
**Published:** April 22, 2020 | **Product/Version:** 4D Write Pro v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78451
**Download:** https://kb.4d.com/DLTN/TN/2020/20-06_4DWrite-to-4DWritePro.zip

## Proposition
With 4D's shift to 64-bit, the legacy 32-bit 4D Write plugin needed replacement by the fully-integrated 4D Write Pro. This note is a practical migration guide covering how to convert stored documents, off-screen areas, and form-based Write areas (including toolbar/menu functionality) to 4D Write Pro equivalents.

## Key Points
- **Document conversion**: `WP New([blobField])` converts Blob-stored 4D Write content directly; Picture-stored content must first pass through a 4D Write off-screen area and `WR Area to blob` before conversion.
- **Object field storage**: 4D Write Pro documents are stored in Object fields (a model dating to 4D v16), requiring structure changes (new field) rather than reusing old Blob/Picture fields.
- **Off-screen area replacement**: 4D Write Pro objects themselves replace the concept of off-screen areas — e.g., replacing `WR PRINT MERGE` batch merging with a per-record loop calling `WP PRINT`.
- **Command family mapping**: 4D Write Pro functionality spans four command themes — dedicated Write Pro commands, Objects (Forms) commands, Styled Text (`ST`) commands, and Objects (Language) commands.
- **Toolbar/menu equivalents**: classic actions like lock/unlock (`WR LOCK DOCUMENT` → `OBJECT SET ENTERABLE`), toggle references (`WR Get/SET DOC PROPERTY` → `ST GET/SET OPTIONS` with `ST Expressions display mode`), and find/replace all translated to Write Pro code.
- **No built-in menu bar**: 4D Write Pro areas ship without menu/toolbars by default; developers must add the Write Pro toolbar object from the Object library or build a custom one.

## Featured Technology
- 4D Write Pro (`WP` commands, object-based documents)
- Styled Text (`ST` commands)
- 4D Write classic (`WR` commands) — legacy, for reference only

## Best Practices Highlighted
1. Create a dedicated `WPOnErrorCall` empty method to suppress conversion errors during batch document migration.
2. Convert Picture-stored documents via an intermediate off-screen area rather than attempting a direct Blob conversion.
3. Rebuild custom toolbar actions using the flexible 4D Write Pro toolbar rather than assuming menu-bar parity out of the box.

## Context / Positioning
Published as 4D actively pushed developers off 32-bit technology, this note exemplifies the wave of "conversion guideline" tech notes from 2019-2020 aimed at helping long-time 4D shops retire legacy plugin-based tools (4D Write, and separately 4D View) in favor of the fully integrated, 64-bit-native Write Pro and View Pro components.

## Historical Commentary
**Status:** Obsolete

4D Write classic (the `WR` command family and its off-screen areas) is long discontinued — it was never available in 64-bit 4D and modern 4D versions do not support it at all, meaning any database still needing this conversion guide today is almost certainly running unsupported legacy tooling. 4D Write Pro (the `WP`/`ST` commands) has been the sole word-processing engine in 4D for many years now and has itself evolved substantially since v17 — gaining richer object/section models, deeper ORDA and forms integration, and expanded styled-text capabilities — so even the "target" technology described here is now several generations behind current 4D Write Pro. This note is useful today mainly as a historical record of the 4D Write → Write Pro transition rather than as an active how-to for current development.
