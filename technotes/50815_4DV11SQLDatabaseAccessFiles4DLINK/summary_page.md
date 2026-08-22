# Tech Note: 4D v11 SQL Database Access Files (4DLINK)

## Overview
........................................................................................................... 3 Introduction ..................................................................................................... 3 What are 4DLINK files? ..................................................................................... 3 Why Use Them?................................................................................................ 3 How does it work? ............................................................................................ 4 Creation of Files............................................................................................. 4 Using 4DLINK Files......................................................................................... 4 Anatomy of the 4DLINK file ............................................................................ 5 Attributes for all 4DLINK Files ...................................................................... 5 Attributes for Remote 4DLINK Files .............................................................. 5 Attributes for Local 4DLINK Files .................................................................. 6 4DLINK Examples ............................................................................................. 7 Example Database ............................................................................................ 9 Conclusion ..................................................................................................... 11 Related Resources .......................................................................................... 11 2 Abstract ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 4D v11 SQL features a new file type called “database access file” or simply, 4DLINK. This new file type allows 4D Developers to control the way in which 4D databases are launched, automatically log in users, automatically create a data file, etc. This feature goes beyond anything seen in both Path Documents and the CLI found in previous versions of 4D. This Technical Note outlines how these files can be created and used. A sample database for creating 4DLINK files is included.

## Key Points
- Published August 20, 2008 as Technical Note 08-30.
- Targets 4D v11.2 on Mac &amp; Win.
- Author: Timothy Penner, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
