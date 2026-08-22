# Tech Note 15-03: Breadcrumbs in 4D

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** February 9, 2015 | **Product/Version:** 4D v14 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77229
**Download:** https://kb.4d.com/DLTN/TN/2015/15-03_Breadcrumbs.zip

## Proposition
This note shows how to add breadcrumb-trail navigation to any 4D form by embedding a small reusable subform whose two shared arrays (labels and actions) drive both the visual crumbs and, via the newly-introduced 4DEVAL tag in `PROCESS 4D TAGS`, the code executed when a crumb is clicked.

## Key Points
- **New 4DEVAL tag** (added in v14 R4) lets a string of 4D code be evaluated on the fly through `PROCESS 4D TAGS`, unlocking dynamic, data-driven UI behaviors previously impossible.
- **Reusable project subform** for breadcrumbs can be dropped onto any parent form without modification.
- **Two shared arrays drive state:** `bc_label_at` holds crumb labels, `bc_action_at` holds either method names or raw 4D code (e.g. `FORM GOTO PAGE(2)`) to run when a crumb is clicked.
- **Event-driven update:** changing the shared arrays on the parent form triggers `On Bound Variable Change` in the subform, which redraws the breadcrumb trail.
- **Multiple visual styles compared:** equal-width color, equal-width white, dynamic-width color, and dynamic-width white variants, plus a File Manager-style example.
- **Sample database provided** demonstrating all the styles side by side.

## Featured Technology
- PROCESS 4D TAGS / 4DEVAL transformation tag
- Subforms with On Bound Variable Change
- Text arrays as shared subform state

## Best Practices Highlighted
1. Encapsulate reusable UI in a project subform rather than duplicating logic per form.
2. Drive dynamic subform behavior through shared arrays rather than hard-coding per-instance logic.
3. Use raw 4D code strings in the action array only when a full method would be overkill.

## Context / Positioning
Written for 4D v14 R5 in 2015, squarely in the classic binary Design Mode era. `PROCESS 4D TAGS`/4DEVAL is an HTML-templating mechanism tied to 4D's web area and HTML-based dynamic content — a technology line that predates the more modern approach of building rich UIs with native form objects, list boxes, or client-side JS frameworks fed by REST/ORDA.

## Historical Commentary
**Status:** Still Relevant

The 4DEVAL mechanism and `PROCESS 4D TAGS` command are still present and functional in current 4D versions, so this technique has not been removed — it's simply less central now that native 4D forms/list boxes and browser-based front ends (talking to 4D via REST/ORDA) have become the more common ways to build navigable UI.

The underlying idea — a reusable, array-driven breadcrumb subform — is architecture-agnostic and could be reimplemented today with 4D classes/collections instead of parallel text arrays, but the specific 4DEVAL-based plumbing described here is now a legacy-flavored approach rather than the default choice.
