# Tech Note 16-01: [3rd Party Tech Note] Migrating Away from the 4D Picture Library

**Author:** David Adams
**Published:** January 14, 2016 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77446
**Download:** https://kb.4d.com/DLTN/TN/2016/16-01_PictureLibrary.zip

## Proposition
This third-party note explains why 4D's legacy Picture Library (dating to 4D 6.5, based on old resource files) has been deprecated by 4D itself, and provides concrete migration tooling — PictureLibrary_DumpToDisk/DumpToTable methods, OBJECT SET FORMAT guidance, and missing-file detection — to move applications to external picture files.

## Key Points
- **Why migrate:** Mac OS moved away from resource files, cross-platform formats matured, and 4D itself stopped enhancing the Picture Library.
- **Legacy uses documented:** centralized image repository, picture buttons/graphic objects, and hierarchical list icons all historically relied on the Picture Library.
- **External file review:** covers picture storage/organization conventions and how references are set in the Form Editor.
- **Migration utilities:** PictureLibrary_DumpToDisk and PictureLibrary_DumpToTable methods extract images out of the Picture Library programmatically.
- **OBJECT SET FORMAT guidance:** includes a code generator to correctly wire external image paths to form objects, with notes on common pitfalls.
- **Missing-image handling:** provides code to detect and gracefully manage external image files that go missing from disk — a new failure mode external files introduce.
- **Design Mode picture handling** is specifically addressed as a related consideration during migration.

## Featured Technology
- 4D Picture Library (legacy, 4D 6.5+)
- External picture files
- OBJECT SET FORMAT command
- 4D Resource Viewer tool

## Best Practices Highlighted
1. Migrate images to external files and reference them via OBJECT SET FORMAT rather than embedding them in the Picture Library.
2. Always include explicit handling/detection code for missing external image files, since they can be deleted or moved outside 4D's control.
3. Use dump utilities (to disk or to a table) to make Picture Library migration a repeatable, programmatic process rather than manual re-creation.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

This note documents 4D's own long-running, deliberate deprecation of the Picture Library in favor of external picture files, a direction that has only strengthened over the subsequent decade; the guidance, migration utilities, and missing-file handling patterns remain directly applicable today, and any database still relying on the Picture Library should still follow essentially this same migration path.
