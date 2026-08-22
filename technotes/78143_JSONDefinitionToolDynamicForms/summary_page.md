# Tech Note 18-18: JSON Definition Tool for Dynamic Forms

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** October 31, 2018 | **Product/Version:** 4D v17 (requires v17 HF3/R2 or later) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78143
**Download:** https://kb.4d.com/DLTN/TN/2018/18-18_DynamicFormObjectDefinition.zip

## Proposition
4D v17's Dynamic Forms let developers build forms purely from a JSON definition, but the official documentation at the time only covered a minimal example. This note exhaustively documents the JSON schema for every major 4D form object type and ships a visual "JSON Definition Tool" to generate/inspect these definitions hands-on.

## Key Points
- **Basic form skeleton:** a form is `New object("pages"; New collection(Null; $page))` where `$page` holds an `"objects"` property; rendered with `Open form window($form)` or embedded via `OBJECT SET SUBFORM`.
- **Rendering paths differ:** `Open form window` requires `DIALOG` to refresh screen data from the data source; `OBJECT SET SUBFORM` (used for the bundled tool) does not, since the subform is already inside a running parent form.
- **List box variants covered:** array-based, current-selection-based, collection-based, and entity-selection-based list boxes each get their own JSON property breakdown.
- **Broad object coverage:** text/group boxes, fields/variables, hierarchical lists, combo boxes and pop-up menus (including hierarchical and picture pop-ups), all button styles, radio buttons, check boxes, progress indicators, rulers, drawing shapes, splitters, tab controls.
- **Container objects included:** subforms, web areas, 4D Write Pro areas, and 4D View Pro areas each have documented minimal JSON (e.g., `"type":"webArea"`, `"type":"view"`).
- **Sample "JSON Definition Tool":** a bundled database provides a UI to visually build/edit form-object JSON and preview it live via `OBJECT SET SUBFORM`.
- **Version requirement:** the techniques require 4D v17 HF3 (Build 228509) or v17 R2 (227970+).

## Featured Technology
- 4D Dynamic Forms (JSON-based form definitions)
- `Open form window`, `OBJECT SET SUBFORM`, `DIALOG`
- `New object` / `New collection` object-notation form construction
- Per-object-type JSON schemas (list boxes, buttons, pop-ups, drawing shapes, subform/web area/Write Pro/View Pro containers)

## Best Practices Highlighted
1. Use `OBJECT SET SUBFORM` instead of `Open form window` when embedding a dynamic form inside another form, to avoid unnecessary `DIALOG` calls.
2. Reference the bundled JSON Definition Tool as a living, testable catalog rather than memorizing every object's JSON schema.
3. Verify the target 4D build meets the v17 HF3/R2+ requirement before relying on documented JSON properties, since Dynamic Forms were still being actively extended at this point.

## Context / Positioning
Released as Dynamic Forms (introduced in v16R6) matured through v17, this note reflects 4D Technical Services filling a real documentation gap for a powerful but sparsely-documented feature, aimed at developers building metadata-driven, generated, or highly dynamic UIs rather than hand-designed forms.

## Historical Commentary
**Status:** Still relevant

The core mechanism — defining forms as JSON/object structures and rendering them via `Open form window` or `OBJECT SET SUBFORM` — remains fully current in 4D today, and this became even more broadly relevant once 4D moved from Design Mode (binary structure files) to Project Mode (v17-18+), where forms are stored as JSON on disk by default, making JSON form literacy a mainstream rather than niche skill.

4D's official documentation for Dynamic Forms has expanded considerably since 2018 and now likely covers more object types and properties than this note's catalog, so it should be treated as a strong historical reference and learning aid rather than the single source of truth — but nothing here has been deprecated, and the fundamental approach is unchanged.
