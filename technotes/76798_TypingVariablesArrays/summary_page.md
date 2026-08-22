# Tech Note 13-04: Typing Variables and Arrays for Active Objects

**Author:** Aaron Smith, Technical Services Team Member, 4D Inc.
**Published:** March 29, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76798
**Download:** https://kb.4d.com/DLTN/TN/2013/13-04_DeclareVariable.pdf

## Proposition
This Tech Note is a reference guide covering exactly which 4D variable or array type should be declared for each kind of active form object — fields/variables, list objects, pop-ups, buttons, radio buttons, check boxes, progress indicators, tab controls, plug-in areas, and web areas — helping both new and experienced developers correctly type objects on a form.

## Key Points
- Explains why proper typing declaration matters before placing active objects on a form.
- Covers field and variable objects, distinguishing appropriate types for each.
- Documents list objects: hierarchical lists and list boxes, including array-based backing.
- Covers pop-up objects: combo box, pop-up/drop-down list, hierarchical pop-up menu, and picture pop-up menu.
- Covers button objects (standard, 3D, highlight, invisible, picture, button grid), radio objects, and check box objects (including 3D variants).
- Covers progress indicators (thermometer, dial, ruler), tab control objects, plug-in areas, and web areas.

## Featured Technology
- Active objects (form objects)
- Variable/array typing (C_TEXT, ARRAY commands, etc.)
- List objects (hierarchical list, list box)
- Pop-up/button/radio/checkbox/progress-indicator/tab-control/plug-in/web-area objects

## Best Practices Highlighted
1. Always explicitly declare (type) variables and arrays used by active objects rather than relying on defaults.
2. Match the object's expected data type precisely to avoid runtime display/behavior issues.

## Context/Positioning
Published for 4D v13.3 as an onboarding/reference resource, reflecting the breadth of classic 4D form object types available in the Design Mode form editor at the time.

## Historical Commentary
**Status:** Still Relevant

Most of the classic active-object types and their variable/array typing rules described here (buttons, radio buttons, check boxes, pop-ups, progress indicators) remain unchanged and fully applicable in current 4D versions, since 4D forms retain deep backward compatibility. The main evolution is in list boxes, where 4D now also supports object- and collection/entity-selection-based list boxes in addition to the classic array-based ones described here, giving developers a more ORDA-friendly alternative for that specific object type.
