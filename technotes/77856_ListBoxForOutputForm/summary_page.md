# Tech Note 17-17: List Box for Output form

**Author:** Sara NAKKACH, Technical Services Engineer, 4D Inc.
**Published:** September 26, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77856
**Download:** https://kb.4d.com/DLTN/TN/2017/17-17_ListboxForOutputForm.zip

## Proposition
This Tech Note demonstrates converting a traditional List-form Output form into a List Box-based form, explaining List Box's history and automatic UI features, and providing a step-by-step migration guide.

## Key Points
- **List Box history:** introduced in 4D 2004 (arrays only), enhanced in v11 with field/expression columns and current/named selection data sources.
- **Automatic features:** built-in column sorting, movable columns, resizable columns without custom code.
- **Dynamic control:** shows manipulating List Box behavior and content programmatically via 4D Language.
- **Step-by-step conversion:** a detailed walkthrough converting an existing Output form to List Box.
- **Rationale:** List Box reduces the coding burden compared to traditional Output forms while offering richer UX.
- **Target audience:** developers maintaining legacy List-form-based Output forms.

## Featured Technology
- List Box form object
- Output form / List form
- Named selections and current selection as data sources
- 4D Language list box control commands

## Best Practices Highlighted
1. Prefer List Box over classic List form for new Output form designs.
2. Leverage List Box's automatic sorting/resizing features instead of hand-coding them.
3. Use named or current selections as List Box data sources for record navigation.

## Context / Positioning
Published in 2017 for 4D v16, this is a classic Design Mode-era UI modernization note, predating Project Mode, ORDA, and 4D View Pro. It reflects a period when List Box was already mature but many databases still used older List-form Output forms.

## Historical Commentary
**Status:** Still relevant

The core recommendation — use List Box instead of legacy List-form Output forms — remains sound advice in current 4D, where List Box (and later 4D View Pro for spreadsheet-like grids) is the standard mechanism for tabular record display. The step-by-step conversion guidance and the described automatic UI features are still applicable to current-generation 4D applications with little to no adjustment needed.
