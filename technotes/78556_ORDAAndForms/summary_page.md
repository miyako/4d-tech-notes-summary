# Tech Note 20-16: ORDA and Forms

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** September 30, 2020 | **Product/Version:** 4D v18 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78556
**Download:** https://kb.4d.com/DLTN/TN/2020/20-16_ORDAandForms.zip

## Proposition
With ORDA (introduced in v17) offering a modern, object-based way to access and manipulate 4D data, this Tech Note shows developers how to wire ORDA directly into 4D Forms to build a simple, complete CRUD application — creating, reading, updating, and deleting records through entity and entity-selection member functions.

## Key Points
- **Creating records**: `ds.Table_1.new()` returns a new entity, whose properties are set directly before calling `.save()`.
- **Reading/selecting records**: `.all()` returns every record; `.query("field = :1"; value)` returns a filtered entity selection.
- **Updating records**: query for the entity, take `.first()`, modify a property, then `.save()` again.
- **List box binding**: assigning an entity selection to `Form.selection` and setting the list box's data source to Entity Selection with `This.FieldName` column expressions is the core UI pattern.
- **Create-record UX**: double-clicking an empty list box row or a dedicated button opens a sheet-form dialog fed a `.new()` entity via `DIALOG`, saving with `.save()` on Accept.
- **Update-record UX**: double-clicking an existing row opens the same dialog pre-loaded with `Form.selection[$row-1]`.
- **Delete-record UX**: `.drop()` deletes the selected entity, but `Form.selection` must be reassigned afterward to remove the now-stale entity from memory/display.
- **Consistent refresh pattern**: after any save/drop operation, reassigning `Form.selection := ds.Table_1.all()` keeps the UI in sync with the datastore.

## Featured Technology
- ORDA entity/entity-selection functions: `.new()`, `.save()`, `.query()`, `.all()`, `.drop()`
- Form.selection bound to a list box (Entity Selection data source)
- `This.FieldName` list box column expressions
- DIALOG command with sheet-form windows for CRUD dialogs

## Best Practices Highlighted
1. Reuse one dialog form (e.g., `AddNewPerson`) for both create and update flows by feeding it either a `.new()` or an existing entity.
2. Always refresh the bound entity selection (`Form.selection`) after save/drop operations to keep the list box display accurate.
3. Check `$dropInfo.success` after `.drop()` before assuming the deletion completed and refreshing the UI.

## Context / Positioning
This note is a core, evergreen ORDA onboarding resource from the period when 4D was actively encouraging developers to rebuild their data-access layer and forms around ORDA rather than classic record-pointer-based commands, demonstrating that the new object-oriented API was not just for REST/web use cases but was equally suited to traditional desktop 4D forms.

## Historical Commentary
**Status:** Current

This Tech Note describes exactly the pattern 4D developers still use today: ORDA's entity/entity-selection functions (`.new()`, `.save()`, `.query()`, `.all()`, `.drop()`) and binding a list box directly to an entity selection via `Form.selection` remain the current, unchanged, recommended way to build ORDA-driven CRUD forms in 4D. Nothing in this note has been superseded — it is one of the more durable, foundational Tech Notes in this era precisely because it documents core ORDA usage rather than a specific feature or workaround likely to be replaced.
