# Tech Note: Dynamic Translation of Fields' Labels

- **Asset ID:** 30138
- **Tech Note #:** 03-47
- **Published:** October 31, 2003
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Bertrand Soubeyrand
- **Page URL:** https://kb.4d.com/assetid=30138
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_44-47_(OCT)/03-47_Dynamic_Transmission.hqx

## Overview

Bertrand Soubeyrand, a 4D Developer, shows in about 15 lines of code how to build a virtual, renameable structure layer on top of any 4D database using SET TABLE TITLES and SET FIELD TITLES, paired with the two commands new in 4D 2003 — GET FIELD TITLES and GET TABLE TITLES — which extend where those custom names can be displayed (search/sort editors, forms, Quick Report, import/export dialogs). Custom names are stored in 4D choice lists (one per table) so they can be edited via the built-in list editor and reordered by drag-and-drop, then applied at On Startup.

## Key Points

- GET FIELD TITLES and GET TABLE TITLES, new in 4D 2003, extend SET TABLE TITLES/SET FIELD TITLES's reach to the Search editor, Sort editor, dynamic form labels, Quick Report editor, and Import/Export dialogs
- Custom names are stored one choice list per table (e.g. 'SV_Table1'), where element 0 is reserved for the table's own custom name and subsequent elements map to field creation numbers
- Uses ARRAY TO LIST's optional reference-number parameter to keep each list entry synchronized with its field's actual creation-order number, so drag-and-drop reordering in the choice-list editor doesn't break the mapping
- A 4DSV_Rename method run from the On Startup database method reads every stored choice list with LIST TO ARRAY and applies it via SET FIELD TITLES / SET TABLE TITLES before any process starts
- 4DFIELD_ReadSV accepts a generic pointer (via RESOLVE POINTER) to any table or field and returns its current custom label, useful for building generic, renaming-aware messages
- Includes a parallel implementation for 4D 6.x databases (using Table name/Field name/Count tables/Count fields) for developers who don't yet have the 2003 GET TITLES commands
- Notes that user edits to a choice list must be re-imported into the development structure via 4D Insider, or persisted to the data file directly, to avoid losing changes

## Featured Technology

- SET TABLE TITLES / SET FIELD TITLES
- GET TABLE TITLES / GET FIELD TITLES (new in 4D 2003)
- 4D choice lists as a renaming data store
- RESOLVE POINTER for generic table/field lookup
- ARRAY TO LIST / LIST TO ARRAY
- Table() / Field() pointer commands

## Historical Commentary

**Status:** Partially Superseded

The SET/GET TABLE TITLES and SET/GET FIELD TITLES commands featured here are still part of the current 4D language and still work as described for classic-mode structures, so the mechanics of this note remain technically valid. In practice, though, modern 4D applications built on ORDA and current form/list-box objects increasingly rely on the data model's own titles, computed attributes, and resource-based localization rather than runtime table/field-title renaming, so this specific technique is now more of a classic-mode-era pattern than the default approach to multilingual UI in current 4D.

**References to newer/updated information:**
- SET/GET TABLE TITLES and SET/GET FIELD TITLES remain valid, supported 4D commands today
- Modern 4D applications built on ORDA and current form/list-box objects more commonly handle multilingual labeling through the data model's own titles or resource-based localization rather than runtime title renaming
