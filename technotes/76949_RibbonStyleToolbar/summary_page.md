# Tech Note 14-02: Creating a Ribbon-Style Toolbar in 4D

**Author:** Timothy Aaron Penner, Technical Services Engineer, 4D Inc.
**Published:** January 23, 2014 | **Product/Version:** 4D v13.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76949
**Download:** https://kb.4d.com/DLTN/TN/2014/14-02_RibbonStyleToolbar.zip

## Proposition
This note shows how to recreate a Microsoft-Office-style tabbed "Ribbon" toolbar in 4D using the new v13 `OBJECT SET SUBFORM` command, swapping between multiple dimension-matched project forms shown in a shared subform container.

## Key Points
- A Ribbon toolbar is simply a tabbed toolbar, a decades-old UI concept popularized by Microsoft Office 2007's naming.
- Benefits: groups related operations by function, uses screen space efficiently, and increases feature discoverability for new users.
- Build one project form per logical toolbar group (e.g., Main, Devices, Applications), all sharing identical dimensions and icon/text placement.
- Place a subform object beneath a row of tab buttons/tabs on the target form; use `OBJECT SET SUBFORM` in each tab's method to change the subform's source form.
- Polish trick: overlapping line objects along the top of the subform/buttons are selectively hidden/shown per active tab to create the illusion the active toolbar is "attached" while others look detached.
- Bundled sample database includes both a plain grey demo and a colorized demo of the same technique.

## Featured Technology
- `OBJECT SET SUBFORM` command (4D v13)
- Subform-based tabbed/ribbon UI pattern
- Multiple project forms as interchangeable toolbar "pages"

## Best Practices Highlighted
1. Keep all toolbar-page project forms pixel-matched in size and icon/text placement to avoid a jarring switch between tabs.
2. Use selective line-visibility toggling to visually connect the active tab to its toolbar content.
3. Decide on a default toolbar page early, since only one subform page displays at a time.

## Context/Positioning
Published for 4D v13.4, this note showcased a new sub-form command by applying it to a highly recognizable, desktop-application-grade UI pattern that many business application developers wanted to replicate.

## Historical Commentary
**Status:** Still relevant

Building a ribbon-style toolbar from a subform container whose source form is swapped via `OBJECT SET SUBFORM` is a classic-language UI trick that still works in current 4D versions, since subforms and this command remain part of the platform unchanged. The technique is dated in the sense that it requires manually crafting multiple pixel-matched project forms and toggling line visibility to fake a connected-tab look — a level of manual craftsmanship that modern HTML/CSS-based 4D forms (v18+) could reduce for teams willing to move away from classic form objects. As a classic Design Mode/Project Mode UI recipe, however, it remains directly applicable to today's forms.
