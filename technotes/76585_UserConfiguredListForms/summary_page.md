# Tech Note 12-10: User Configured List Forms

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** May 31, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76585
**Download:** https://kb.4d.com/DLTN/TN/2012/12-10_UserConfiguredListForms.zip

## Proposition
This Tech Note provides a proof-of-concept letting end users build, name, and save their own customized output list forms using 4D v13's significantly enhanced List Box object, in place of fixed native list forms.

## Key Points
- Leverages 4D v13's major List Box upgrade to fully replace native output list forms with a user-buildable equivalent.
- Stores each user's list form configuration (fields, layout) in a dedicated LSTFRM_Config table, defined via inline SQL DDL, keyed by user, browser, and configuration name.
- Persists the actual column/layout data as a BLOB and guards against duplicate configuration names per user via QUERY + DELETE SELECTION logic.
- Details careful List Box property setup: typed selection-based variables (C_LONGINT for "Current Selection" data source vs. ARRAY BOOLEAN for "Arrays"), zeroed initial columns to allow runtime construction, and manual OBJECT SET RGB COLORS for alternating row colors.
- Introduces supporting "List Form User Tools": a List Form Configuration Tool, a Records Selection Tool, and a List Form Column Formula Editor for interactively building column formulas.
- Packaged with component usage guidance so the mechanism can be reused across databases.

## Featured Technology
- 4D v13 enhanced selection-based List Box (programmatic column construction)
- OBJECT SET RGB COLORS
- Classic QUERY / DELETE SELECTION data access
- Inline SQL DDL (Begin SQL/End SQL) for schema definition
- BLOB storage for serialized layout configuration

## Best Practices Highlighted
1. Use typed variables matching the List Box's data source (Long Integer for selection-based, Boolean array for array-based) to avoid compiler issues.
2. Guard against duplicate per-user configuration names before saving.
3. Treat the prototype as a starting point — production adaptation requires addressing additional details beyond the POC.

## Context/Positioning
Published for 4D v13.0 in 2012, shortly after List Box gained major new capabilities, this note demonstrates an ambitious real-world application of the upgraded control: giving end users self-service control over their own data views.

## Historical Commentary
The self-service list-customization concept is still a valid and common feature pattern in business applications today, but the implementation techniques are dated: classic QUERY/DELETE SELECTION-based data access predates ORDA's entity-based dot notation, and manually zeroing/building List Box columns programmatically predates the object/collection-array-bound list boxes introduced in later 4D versions, both of which make dynamic, user-configurable list views considerably easier to implement now.

**Status:** Partially superseded
