# Tech Note 21-08: Enrich UX and UI with Unicode Special Characters

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** May 25, 2021 | **Product/Version:** 4D v18 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78711
**Download:** https://kb.4d.com/DLTN/TN/2021/21-08_EnrichUXwithUnicode.zip

## Proposition
Unicode symbols and Emoji can serve as free, zero-asset icons throughout a 4D application's UI. This note shows how to insert them correctly into different form objects and how to work around cross-platform rendering inconsistencies.

## Key Points
- **`Char(code)`** inserts any character below code point 65535 directly into static text or input objects.
- **Multi-style HTML spans** (`<span>&#x1F50D;</span>` processed with `ST Get plain text`) are required for characters above 65535, i.e. most Emoji.
- **Button titles** accept plain Unicode text directly via `OBJECT SET TITLE`.
- **Pop-up/drop-down icons** can be built by prefixing each menu choice string with a directional glyph, assembled via a collection and `.join(";")`.
- **Listbox selection indicators** (checkmark, arrow) swap in/out via a bound object property, updated on `On Clicked`, as an alternative to row highlighting.
- **Toolbar buttons** can be composed from a centered collection-based Listbox cell or a custom-style Button object sized to fit a large glyph.
- **Cross-platform rendering differs:** the same character can look 3D on macOS and flat/monochrome on Windows — font-size and even character choice may need per-OS branching (`If (Is Windows)`).
- **Character-to-picture conversion:** `SVG_New`/`SVG_New_text`/`SVG_Export_to_picture` renders a Unicode character into a bitmap picture for guaranteed visual consistency across platforms.

## Featured Technology
- Unicode / Emoji character ranges
- `Char` command
- Multi-style text spans + `ST Get plain text`
- SVG_ command family (character-to-picture conversion)

## Best Practices Highlighted
1. Use `Char()` for code points under 65535 and multi-style spans for higher code points (most Emoji).
2. Branch font-size/character choice by platform (`Is Windows`) when rendering consistency matters.
3. Convert critical icon glyphs to pictures via the SVG_ commands when cross-platform visual parity is required.
4. Ensure Listbox/button objects support both horizontal and vertical centered alignment before using them as icon containers.

## Context / Positioning
This is a UI craftsmanship tech note aimed at helping developers avoid purchasing or designing custom icon sets, leaning instead on the richness of native Unicode/Emoji support that 4D's text engine already provides — a low-cost, low-effort way to modernize an application's look and feel.

## Historical Commentary
**Status:** Still relevant

Every technique in this note — `Char`, multi-style spans via `ST Get plain text`, and the SVG_ character-to-picture conversion — remains available and functionally unchanged in current 4D versions; none of it depends on any deprecated feature. The cross-platform font rendering caveat is also still true today, since it stems from OS-level font differences rather than anything 4D-specific. This is a durable, still-useful how-to for any developer wanting quick, dependency-free icons in a 4D UI.
