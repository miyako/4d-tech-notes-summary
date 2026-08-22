# Tech Note 07-39: Hierarchical Lists in 4D v11 SQL

**Author:** Thomas Fitch, Technical Support Engineer, 4D Inc.
**Published:** October 3, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47652
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_39-42_(OCT)/07-39_4D_v11_SQL_HList.zip

## Overview
This note documents a major improvement to Hierarchical List form objects in 4D v11 SQL: a single underlying list can now be displayed through multiple independent form objects, each with its own selection, expand/collapse state, and scroll position.

## Key Points
- Previously, a Hierarchical List's language object (list reference ID) could only back one form object at a time; v11 SQL removes that restriction.
- Per-form-object-unique properties: current selection, expanded/collapsed state of items, and scroll cursor position; other properties remain shared across all representations.
- Existing commands (`SET LIST ITEM`, `GET LIST ITEM`, `SELECT LIST ITEMS BY POSITION`, `Count list items`, `Selected list items`, `List item parent`, `List item position`, `SET/GET LIST ITEM PROPERTIES`, and renamed `DELETE FROM LIST`/`INSERT IN LIST`) gain an optional `(*;"objectname";...)` syntax to target a specific form object.
- New commands introduced: `SET LIST ITEM FONT`, `Get list item font`, `Find in list`, `SET LIST ITEM ICON`, `GET LIST ITEM ICON`, `SET LIST ITEM PARAMETER`, `GET LIST ITEM PARAMETER`.
- Object-name references support a wildcard suffix (e.g. `"HL@"`) to match multiple form objects by name prefix.
- Precedence rule: once a Hierarchical List command sets a display property on a form object, it overrides Property List (Design mode) or general Object Properties theme settings (`FONT`, `FONT STYLE`, `FONT SIZE`), which now also apply to Hierarchical List objects.
- Sample database demonstrates two form objects tied to the same list with independently different selections and expand/collapse states.

## Featured Technology
- Hierarchical List form objects (multi-form-object support)
- `SET/GET LIST ITEM` command family with optional object-name targeting
- New v11 commands: `SET LIST ITEM FONT/ICON/PARAMETER`, `Find in list`
- Renamed commands: `DELETE FROM LIST` (was `DELETE LIST ITEM`), `INSERT IN LIST` (was `INSERT LIST ITEM`)

## Historical Context
Published in October 2007 as part of the 4D v11 SQL release, this note documents a substantive UI/UX enhancement to a long-standing 4D form control, delivered alongside the version's headline SQL engine addition, at a time when 4D databases were built exclusively in binary Design Mode.

## Historical Commentary
**Status:** Still relevant

Hierarchical List form objects and their `SET/GET LIST ITEM` command family remain part of current 4D, and the multiple-form-object display capability documented here is still a valid and useful technique today. The main historical nuance is that the "new for v11" framing is now simply how Hierarchical Lists have always worked for the last many versions, and 4D has continued to add further list-related capabilities since 2007.
