# Tech Note 14-11: Preserving Display State with Save Geometry

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** July 14, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77069
**Download:** https://kb.4d.com/DLTN/TN/2014/14-11_SaveGeometry.pdf

## Proposition
4D v14 introduces the Save Geometry form property, which automatically persists and restores a form's window position, geometry, and (via "Save Value") object states to a JSON preference file — removing the need to hand-code form-state persistence.

## Key Points
- **Save Geometry** memorizes window coordinates, object positions, and states at the time a form closes and restores them on reopen.
- Settings are stored as a **JSON preference file**, one of 4D's early user-visible uses of the JSON format.
- Must be enabled in the form's Property List and requires opening the form with **OPEN FORM WINDOW** using the `*` parameter.
- **Save Value** is a companion object property that persists last-entered/selected values for variables, list box headers, popups, tabs, and buttons/checkboxes.
- Behavior differs across 4D runtime modes: standalone/compiled, merged application, interpreted single-user, and interpreted client-server (each client keeps an independent preference file).
- Preference files live in per-platform, per-mode locations (e.g., `AppData\Roaming\<project>\4D Window Bounds v14` on Windows, `Library:Application Support:4D:...` on Mac) and can be manually inspected or restored.

## Featured Technology
- Save Geometry / Save Value form and object properties (4D v14)
- JSON-based window/form preference files
- `OPEN FORM WINDOW` with `*` parameter

## Best Practices Highlighted
1. Enable Save Geometry only where persistent display state genuinely improves user workflow, not for every form.
2. Understand mode-specific behavior (merged vs. interpreted vs. client/server) before relying on saved state in production.
3. Avoid manually editing the JSON preference file; treat it as an internal 4D-managed artifact.

## Context/Positioning
Published shortly after 4D v14's release, this note showcases a genuine quality-of-life feature that reduced boilerplate code 4D developers previously had to write by hand for every form.

## Historical Commentary
**Status:** Still relevant

Save Geometry solved a real and recurring problem, and the feature — along with its JSON preference-file mechanism — has persisted essentially unchanged as part of 4D's form engine for over a decade. The file-path conventions described are tied to the classic binary Design Mode database layout, but the feature's runtime behavior carries forward into Project Mode largely unaffected, since Project Mode changed how forms are stored (as JSON `.4DForm` files) rather than how their runtime state is remembered. This remains one of the more durable, "still current" utility features covered in this era's Tech Notes.
