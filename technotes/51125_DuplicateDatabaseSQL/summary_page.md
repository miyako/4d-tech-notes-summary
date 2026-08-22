# Tech Note 08-34: How to Duplicate a Database in 4D v11 SQL

**Author:** Silvio Belini (Technical Services Team Member, 4D Inc.)  
**Published:** September 24, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51125  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_32-35_(SEP)/08-34_Duplicate_DB.pdf

## Overview

This Technical Note documents the correct procedure for successfully duplicating a database in 4D v11 SQL by leveraging the newly introduced drag-and-drop object copying mechanism and XML structure import/export capabilities. The guide addresses the critical challenge of preserving internal object numbering and referential integrity when copying database elements between two instances of 4D v11 SQL, which is essential for ensuring that the duplicated database remains fully functional.

## Key Points

**Step 1: Running Two Instances**  
Both instances of 4D v11 SQL must be running simultaneously on the same machine to enable drag-and-drop between them.

**Step 2: Table Trash Management**  
The Trash must be empty or cleared of any deleted tables before export. If tables have been deleted from the original database, remaining tables will be renumbered when structure is exported/imported, breaking any hardcoded table number references. Example: if Table_1, Table_3, Table_5 exist and Table_2, Table_4 are deleted, the exported structure will renumber them as Table_1, Table_2, Table_3 with new table numbers (1, 2, 3 instead of 1, 3, 5).

**Step 3: XML Structure Export/Import**  
Export the database structure via File > Export > Structure definition to XML file, then create a new database in the second instance using File > New > Database From Structure Definition, selecting the exported XML file. This automatically recreates tables with preserved relationships and field numbering. Simply dragging and dropping tables does not preserve relations and internal numbering.

**Step 4: Resource File Handling (Converted Databases)**  
For databases originally converted from 4D 2004, the .RSR resource file must be manually copied to the new database folder and opened in the On Startup Database method using the `Open Resource File` command to maintain compatibility with legacy resource references.

**Step 5: The Toolbox Migration**  
- **Users and Groups:** Cannot be dragged; must be recreated manually.
- **Menus:** Cannot be dragged; must be created manually in the same order and with matching reference numbers to preserve menu bar defaults.
- **Pictures, Help Tips, Lists, Filters, Resources, Style Sheets:** Can be dragged and dropped one at a time between open Toolbox windows.
- **Default Style Sheet:** Should be re-set in the new database rather than dragged.

**Step 6: Forms Migration**  
List forms, detail forms, and input/output forms can be dragged from the original to the new database while maintaining their structure.

**Step 7: Methods Migration**  
Project methods and database/trigger methods can be dragged and dropped between databases.

**Step 8: Plug-ins**  
Plug-in files must be copied to the new database's plug-in folder or re-registered in the new instance.

**Critical Principle:** Object references and internal numbering must remain intact. Deviating from this sequence risks breaking hardcoded references to table numbers, field IDs, method names, or resource IDs.

## Featured Technology

- XML structure import/export
- Drag-and-drop object copying between instances
- Table and field numbering preservation
- Resource file (.RSR) handling
- Referential integrity maintenance
- Database object migration

## Historical Context

Published in September 2008, this note addresses a common workflow during the 4D v11 SQL era when the XML-based structure export/import feature and enhanced drag-and-drop capabilities made it possible to consolidate or duplicate databases more efficiently than in earlier versions. The procedure represents a significant improvement over purely manual object recreation, though it still required careful sequencing and some manual steps (users, groups, menu bars).

## Historical Commentary

**Status:** Superseded

Modern 4D development (v17+) has replaced this manual duplication workflow with Project Mode, which stores database structure and objects as text files in a Git-compatible format, enabling true version control, branching, and collaborative development. Component packages and shared components provide modular reuse without the need for physical database duplication. Developers today would use Git for source control and component-based architecture rather than export/import procedures, making this note's step-by-step approach obsolete for contemporary 4D development practices.
