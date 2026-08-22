# Tech Note 24-05: Pop-Up Menu Utility

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** March 26, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79402
**Download:** https://kb.4d.com/DLTN/TN/2024/24-05_PopupMenuUtility.zip

## Proposition
4D's native `Pop up menu` and `Dynamic pop up menu` commands work well for simple cases but require verbose imperative code (`Create menu`, `APPEND MENU ITEM`, `SET MENU ITEM PARAMETER`) for multi-level menus, and provide no automatic handling of selection state such as checkmarks. This note offers a reusable, data-driven utility that turns menu building into declaring a collection.

## Key Points
- **Native command limitations:** Building nested menus with `Dynamic pop up menu` requires manual, repetitive calls to append items and set parameters for every level.
- **Collection-based menu definition:** A popup menu is defined as a single collection of strings; a submenu is an object whose property name holds a nested collection of its items.
- **Three required methods:** `inCollection` (generic lookup via `findIndex`), `buildPopupMenu` (constructs the in-memory menu from the definition), and `popup` (the public entry point).
- **Inline attribute markers:** A leading "(" disables an item; appended `<B`, `<I`, `<U` codes apply bold/italic/underline text styling.
- **Checkmark state via control characters:** Appending `Char(1)` to a submenu's property name enables single-selection ("radio") checkmark switching among its children; appending `Char(2)` to an item enables independent toggle-style checkmarks.
- **`popup()` API:** Signature `popup(menuDefinition : Collection{; coordinateDefinition : Object}) -> selected : Text`; returns the selected label, or a "/"-delimited path when the choice comes from a submenu (e.g., "Arrange By/Size").
- **Flexible positioning:** An optional coordinate-definition object (built with `OBJECT GET COORDINATES` and `OBJECT Get name`) anchors the popup to one of four corners (top-left/right, bottom-left/right) of a target object instead of the mouse cursor.

## Featured Technology
- **Pop up menu / Dynamic pop up menu:** Native 4D commands underlying the utility's implementation.
- **Create menu / APPEND MENU ITEM / SET MENU ITEM PARAMETER:** Lower-level menu-building commands wrapped by `buildPopupMenu`.
- **OBJECT GET COORDINATES / OBJECT Get name:** Used to compute anchor points for object-relative menu positioning.
- **4D Collections and Objects:** Used as the declarative data structure describing menu hierarchy, styles, and state.
- **Control characters (Char(1)/Char(2)):** Embedded markers driving automatic checkmark behavior.

## Best Practices Highlighted
1. Separate menu structure (data) from menu-building logic to simplify maintenance and reduce boilerplate.
2. Use consistent inline markers (disable, style, checkmark) rather than parallel state-tracking variables.
3. Provide an optional, well-defined coordinate API so menus can be anchored predictably relative to UI objects.

## Context / Positioning
Published as part of 4D's ongoing series of practical developer productivity tools, this note reflects a broader pattern in 4D Tech Notes of wrapping verbose native APIs with higher-level, object/collection-driven utility layers — consistent with 4D's continued embrace of modern object and collection syntax introduced in recent major versions.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
