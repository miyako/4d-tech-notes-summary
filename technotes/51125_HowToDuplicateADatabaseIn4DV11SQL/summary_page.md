# Tech Note: How to Duplicate a Database in 4D v11 SQL

## Overview
........................................................................................................... 3 Introduction ..................................................................................................... 3 Steps for moving objects between 4D v11 SQL instances ..................................... 3 Step 1: Running two instances of 4D v11 SQL.................................................. 4 Step 2: Handling Tables in the Trash ............................................................... 5 Step 3: Exporting/Importing the Database structure......................................... 7 Step 4: The Resource File (Converted databases) ............................................. 8 Step 5: The Tool Box ..................................................................................... 9 Users and Groups ....................................................................................... 9 Menus ........................................................................................................ 9 Pictures/Help Tips/Lists/Filters/Resources ..................................................... 9 Style Sheets ............................................................................................... 9 Important note before going further ........................................................... 10 Step 6: Moving forms................................................................................... 11 List Forms ................................................................................................ 11 Detail Forms ............................................................................................. 11 Set Input/Output forms ............................................................................. 11 Step 7: Methods .......................................................................................... 12 Project Methods ........................................................................................ 12 Database/Trigger Methods ......................................................................... 12 Step 8: Plug-ins........................................................................................... 13 Conclusion ..................................................................................................... 14 Related Resources .......................................................................................... 14 2 Abstract ------------------------------------------------------------------------------------------------------------------------------------------------------------------ This Technical Note will demonstrate the correct steps to successfully duplicate a database in 4D v11 SQL using the new XML structure import/export feature and the Drag and Drop mechanism between 2 instances of 4D v11 SQL.

## Key Points
- Published September 24, 2008 as Technical Note 08-34.
- Targets 4D v11.2 on Mac &amp; Win.
- Author: Silvio Belini, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
