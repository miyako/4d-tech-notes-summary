# Tech Note 15-11: Adding Window Snapping to 4D

**Author:** Tai BUI, Technical Services Engineer, 4D Inc.
**Published:** June 23, 2015 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77315
**Download:** https://kb.4d.com/DLTN/TN/2015/15-11_WindowSnapping.zip

## Proposition
Windows OS offers native "window snapping" — docking and resizing a window to a screen edge via shortcuts or drag gestures — but 4D windows lacked this behavior natively. This note implements three alternative approaches to bring window-snapping convenience into a 4D application, with a sample database demonstrating each.

## Key Points
- **OS feature recap:** Windows-key + arrow shortcuts for half-screen/maximize/minimize, and drag-to-edge snapping, including multi-monitor and vertical full-height resize behavior.
- **Method 1 — menu bar shortcuts:** simplest to implement, but ignores form size restrictions and requires assigning the snapping menu to every form.
- **Method 2 — adaptive snapping via invisible buttons:** accounts for a form's minimum/maximum size restrictions, but requires adding invisible buttons to each form individually.
- **Method 3 — palette window + drag detection:** a always-open palette window listens for window drag/resize events and applies snapping globally to all forms without per-form setup, but without size-limit awareness.
- **Sample database with 5 demos:** walks through each snapping method's specific implementation and limitations concretely.
- **Explicit trade-off framing:** the conclusion directly compares simplicity vs. flexibility vs. universality across the three methods.

## Featured Technology
- Menu bar keyboard shortcuts
- Invisible form buttons (adaptive snapping trigger)
- Palette window + window-movement event handling
- Classic 4D window positioning/sizing commands

## Best Practices Highlighted
1. Choose the snapping implementation based on your application's needs: quick wins (shortcuts) vs. size-aware precision (invisible buttons) vs. universal coverage (palette window).
2. Account for form size restrictions explicitly if adaptive snapping behavior is required, since naive snapping can ignore minimum/maximum size constraints.

## Context / Positioning
A classic Design Mode-era UI convenience note (v14.x, 2015) working entirely within the traditional 4D forms/windows model, well before Project Mode or any newer 4D UI paradigm — a good example of period-typical "fill the gap the platform doesn't cover" tech notes.

## Historical Commentary
**Status:** Still relevant (as a technique), niche in practice

The three window-snapping techniques described here still function in current 4D for classic desktop windows, so nothing here is technically broken. That said, since this note was published, native OS-level window management (Windows Snap Assist, macOS Stage Manager/tiling, and various window managers) has become considerably more capable, reducing the practical need for applications to reimplement snapping themselves — most developers today would simply rely on the OS rather than replicate this functionality in-app.
