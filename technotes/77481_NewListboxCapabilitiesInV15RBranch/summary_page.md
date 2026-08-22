# Tech Note 16-02: New Listbox Capabilities in v15 R Branch

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** February 26, 2016 | **Product/Version:** 4D v15 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77481
**Download:** https://kb.4d.com/DLTN/TN/2016/16-02_ListboxIn15R3AndR4.zip

## Proposition
This note surveys four listbox UX enhancements introduced in 4D v15 R3/R4: single-click cell editing, ellipsis-based text truncation, automatic hiding of trailing blank rows, and a row control array for setting per-row hidden/disabled/non-selectable states.

## Key Points
- **Single-Click Edit (R3):** lets users enter cell-edit mode with one click instead of requiring double-click or select-then-type.
- **Selection-mode interaction:** documents how single-click edit behaves alongside listbox selection modes and the On Click event.
- **Per-cell control:** single-click edit can be enabled selectively on specific cells rather than the whole listbox.
- **Truncate with ellipsis (R4):** overflowing cell text is visibly clipped with "..." instead of being silently cut off, with configurable clipping location.
- **Hiding extra blank rows (R4):** removes trailing empty rows past the last real record, driven by specific form events.
- **Row Control Array (R4):** a new mechanism to mark individual rows as hidden, disabled, or non-selectable, including combining multiple states per row.
- **Configuration UI included** for setting row control array properties interactively.

## Featured Technology
- 4D classic Listbox form object (v15 R3/R4)
- Row Control Array
- Listbox form events (On Click, etc.)

## Best Practices Highlighted
1. Use ellipsis truncation rather than silent text clipping to signal to users that content is cut off.
2. Combine row control array options thoughtfully to express complex per-row states (e.g., disabled AND non-selectable) without extra code.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

Classic array/selection-based listboxes were never deprecated in 4D even as ORDA and collection-type listboxes were introduced later, so the specific v15 R3/R4 features covered here — single-click edit, ellipsis truncation, hidden blank rows, and row control arrays — remain valid and usable in current 4D versions largely unchanged. The note predates ORDA-based and collection-type listboxes introduced from v16 R5 onward, which offer additional modern alternatives, but does not conflict with them.
