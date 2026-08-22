# Tech Note 17-07: An Approach to Implementing a Panel Bar in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 20, 2017 | **Product/Version:** 4D v16 R2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77768
**Download:** https://kb.4d.com/DLTN/TN/2017/17-07_PanelBar.zip

## Proposition
This Tech Note presents a technique for building a vertical, menu-driven "panel bar" navigation control in 4D using a list box, motivated by the trend toward wider monitor aspect ratios favoring vertical over horizontal navigation bars.

## Key Points
- **Design rationale:** wider modern monitors favor vertical navigation bars over horizontal toolbars/menu bars.
- **List box as backbone:** the panel bar is implemented using a list box for its visual and interactive structure.
- **Menu parsing:** an existing menu structure is parsed into panel bar entries programmatically.
- **Form initialization method:** sets up the panel bar's initial state and content.
- **Applying functionality:** wires click/selection handling to trigger navigation actions.
- **Sizing and display formatting:** covers list box sizing and formatting choices needed for a polished navigation look.
- **Sample database:** provides a working example to adapt to other menu structures.

## Featured Technology
- List box form object
- Menu parsing logic
- Form initialization method
- List box sizing/display formatting

## Best Practices Highlighted
1. Favor vertical navigation panels over horizontal toolbars on modern widescreen displays.
2. Drive navigation UI content from existing menu definitions rather than duplicating menu structure by hand.
3. Tune list box sizing/formatting carefully to make it read as a dedicated navigation control rather than a generic list.

## Context / Positioning
Published in April 2017 for 4D v16 R2, this is a classic Design Mode-era custom-UI note, reflecting native list-box-based form design well before Project Mode, ORDA, or any web-based UI alternatives (Qodly) existed for 4D applications.

## Historical Commentary
**Status:** Partially superseded

The list-box-driven panel bar technique described remains technically workable in current 4D and the underlying menu-parsing/navigation logic is still sound. However, native 4D form and list box capabilities have continued to expand since 2017, and many modern 4D applications now build navigation UI for web-facing clients using HTML/CSS/JS or 4D View Pro/Qodly rather than a hand-rolled native list box panel bar, making this note's specific approach one option among several rather than the default recipe it may have been in 2017.
