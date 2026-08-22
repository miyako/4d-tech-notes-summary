# Tech Note 12-14: Programmable and Portable Component Subforms

**Author:** Bertrand Soubeyrand, Consultants
**Published:** August 8, 2012 | **Product/Version:** 4D v12.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76630
**Download:** https://kb.4d.com/DLTN/TN/2012/12-14_ComponentSubform.zip

## Proposition
This Tech Note explains how 4D v12's enhanced subform capabilities — combined with dynamic variables and new communication commands — make subforms distributed via components both reusable ("portable") and interactive ("programmable").

## Key Points
- Defines subform vocabulary: host form, subform, subform container, subform instance — a subform can be instantiated multiple times in one host form.
- Four key commands: CALL SUBFORM CONTAINER (event passing), OBJECT Get pointer / OBJECT Get name (retrieving pointers/names), EXECUTE METHOD IN SUBFORM (running code in a specific instance).
- Introduces 4D v12 "dynamic variables" — form variables 4D creates/destroys automatically per subform instance, replacing static process variables and saving memory.
- Demonstrates two-way communication: host-to-subform updates via container variable pointers, and subform-to-host custom event codes via CALL SUBFORM CONTAINER.
- Shows subform forms shared from components (via Explorer → Project Forms → Share) as well as a non-component variant for simpler use cases.

## Featured Technology
- 4D v12 subform containers (list & detail/page subforms)
- Dynamic (process-free) form variables
- CALL SUBFORM CONTAINER / OBJECT Get pointer / EXECUTE METHOD IN SUBFORM
- 4D components sharing forms across host databases

## Best Practices Highlighted
1. Prefer dynamic variables over static process variables in subforms to avoid per-instance memory duplication.
2. Use negative custom event codes when passing developer-defined events to avoid clashing with 4D's built-in codes.
3. Package reusable subforms as components with explicitly shared forms for portability across host databases.

## Context/Positioning
Published shortly after 4D v12 shipped, this note re-introduces subforms — a feature some developers considered outdated — as significantly more capable, encouraging their combination with 4D's growing component ecosystem for reusable UI.

## Historical Commentary
The subform communication commands and dynamic-variable concept described here remain part of the current classic 4D language and continue to be the standard technique for building reusable, interactive subforms — no newer mechanism has replaced pointer-based host/subform communication. What has changed is the surrounding context: forms and components at the time lived in binary Design Mode structures, whereas today's Project Mode stores forms as text files, and simple encapsulated logic might now be organized using 4D classes rather than solely pointer-passing between object methods.

**Status:** Still relevant
