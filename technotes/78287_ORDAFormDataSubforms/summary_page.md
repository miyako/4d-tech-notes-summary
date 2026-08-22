# Tech Note 19-12: Using ORDA with Form Data and Subforms

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** July 19, 2019 | **Product/Version:** 4D v17 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78287
**Download:** https://kb.4d.com/DLTN/TN/2019/19-12_ORDA_FormData_Subforms.zip

## Proposition
ORDA enables a fully object-oriented form design where data flows through `Form` objects rather than process variables, but this creates non-obvious scoping and timing rules between parent forms and subforms that developers need to understand to avoid null-reference errors and stale UI state.

## Key Points
- **Scope rule:** the parent form can read/write both its own and its subform's data; a subform can only see its own data.
- **Event order matters:** form data must be initialized as an object during the `DIALOG` call (Event 1), before Event 2 (subform On Load), Event 3 (subform container On Load), and Event 4 (parent On Load).
- **Green-triangle gotcha:** launching a form via the direct execute-method button (bypassing `DIALOG`) leaves `Form.Subform1` null unless initialized defensively in `On Load`.
- **`OBJECT SET SUBFORM`** is required to force a listbox to pick up a reassigned subform object reference — **but is no longer needed starting v17R6**, per the note itself.
- **Parent updates subform:** direct object notation (`Form.Subform1.LB.push(...)`) works for data; `EXECUTE METHOD IN SUBFORM` is needed only for widget-specific actions (e.g., highlighting a row) that must execute in the subform's own context.
- **Subform updates parent:** requires `CALL SUBFORM CONTAINER` with a negative (or >59) custom event number, caught by the parent's subform container method, since the subform has no direct access to parent data.

## Featured Technology
- ORDA, `Form` object notation
- `OBJECT SET SUBFORM`, `EXECUTE METHOD IN SUBFORM`, `CALL SUBFORM CONTAINER`
- Collection-based list boxes

## Best Practices Highlighted
1. Always initialize subform form-data objects during the `DIALOG` call rather than relying solely on `On Load`.
2. Prefer opening forms via a method that passes form data (not the direct execute button) to guarantee correct initialization order.
3. Use `EXECUTE METHOD IN SUBFORM` only for widget-specific operations, not general data updates.
4. Use negative (or >59) custom event numbers with `CALL SUBFORM CONTAINER` to avoid colliding with reserved form events.

## Context / Positioning
This note reflects 4D's mid-2019 emphasis on ORDA as not just a data-access layer but a design philosophy — "everything is an object" — extending object notation into form/subform architecture, a natural companion to other 2019 tech notes on ORDA-driven UI patterns.

## Historical Commentary
**Status:** Still relevant

This remains an accurate and useful explanation of parent/subform data flow in ORDA-based 4D forms; the object-oriented approach it describes is still 4D's current, recommended architecture. Notably, the note itself flags that its central workaround (`OBJECT SET SUBFORM`) became unnecessary starting in v17R6, since collection/entity-based list boxes now auto-refresh their object reference — so a developer reading this today on a modern 4D version can skip that specific line of code while still following the rest of the guidance on event order and CALL SUBFORM CONTAINER for parent-child communication.
