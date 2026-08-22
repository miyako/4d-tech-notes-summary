# Tech Note 21-17: Guide to Converting 4D Write to 4D Write Pro

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** September 20, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78783
**Download:** https://kb.4d.com/DLTN/TN/2021/21-17_4DWriteConversionGuide.pdf

## Proposition
With 4D v18 and later moving to 64-bit-only, the 32-bit-only 4D Write plugin can no longer run, forcing every database that still uses 4D Write areas, documents, or commands to migrate to 4D Write Pro. This note is a practical migration checklist covering document conversion, area replacement, and command translation.

## Key Points
- **Version dependency for conversion:** documents stored as `.4w6` or as Picture fields must be converted using a **32-bit** copy of 4D (17.5 or 17 R4 max), because `WR New offscreen area` doesn't exist in 64-bit builds.
- **Disk-based documents:** a sample method walks a folder, detects `.4w6`/`.4w7`/`.4wt` files, and converts them to `.4wp` via `WP Import document` / `WP EXPORT DOCUMENT`.
- **Datafile-based documents:** Picture fields must first become a BLOB (`WR Area to blob`) before conversion; BLOB fields go straight to `WP New`.
- **Command mapping is lossy:** 4D Write's generic `WR EXECUTE COMMAND` calls split into multiple discrete 4D Write Pro commands (`WP PRINT`, `ST FREEZE EXPRESSIONS`, etc.), and some commands (`WR LOCK COMMAND`, `WR ON COMMAND`) have **no equivalent**.
- **Area replacement options:** 4D Write Pro offers plain, control-dialog, and toolbar (MS Word-like) area variants from the object library.
- **Testing strategy:** keep both a 4D Write and 4D Write Pro area side-by-side on the same form during conversion, tested on the last 32-bit-capable 4D versions.
- **OS constraints:** 4D Write requires Windows 10 or macOS Mojave 10.14 or older; macOS Catalina 10.15+ dropped 32-bit app support entirely.

## Featured Technology
- 4D Write Pro (.wp documents, WP/ST command families)
- Legacy 4D Write plugin (32-bit only, WR command family)
- `WR New offscreen area`, `WP Import document`, `WP EXPORT DOCUMENT`

## Best Practices Highlighted
1. Identify storage format first (disk file vs. datafile field) before choosing a conversion path.
2. Use "Edit > Find in design" for the "WR " keyword to catalogue all 4D Write command usages before removal.
3. Build a documented equivalency table (4D Write command → 4D Write Pro command) per database, since 4D's own mapping is incomplete.
4. Test old and new areas in parallel before final removal to avoid runtime/syntax errors.

## Context / Positioning
This note reflects 4D's broader v17R5→v18 architectural shift to 64-bit-only builds, which forced deprecation of several 32-bit-only plugins beyond just 4D Write. It positions 4D Write Pro — already the modern, actively developed rich text engine — as the mandatory successor, and frames the tech note as damage control/migration guidance for the installed base still carrying legacy content forward.

## Historical Commentary
**Status:** Obsolete (as a forward-looking technique; historically significant as a one-time migration record)

By 2026 this conversion problem is effectively closed for any database still in active use — 4D Write has been unsupported for years, and any 4D app still running today either completed this migration long ago or was retired. The specific pain point described (needing a 32-bit copy of 4D 17.5/17R4, which itself requires pre-Catalina macOS or older Windows to run) has become progressively harder to satisfy as those OS versions age out of availability, making this note more of a historical curiosity than an actionable guide today.

4D Write Pro itself has continued to mature significantly since 2021 (more layout, style, and ORDA-object integration features), so a developer needing rich-text documents today should simply build on 4D Write Pro directly — there is no reason to have any residual 4D Write dependency in a current-generation 4D project.
