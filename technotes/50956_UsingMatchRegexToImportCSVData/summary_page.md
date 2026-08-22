# Tech Note: Using Match regex to Import CSV data

## Overview
..................................................................................................... 3 Introduction ............................................................................................... 3 What Makes CSV Challenging?....................................................................... 4 CSV Rules ............................................................................................... 4 How Does 4D's Match regex Command Solve the Problem? ................................ 6 Introduction to, Listing, and Explanation of the 4D Code.................................... 7 Conclusion ............................................................................................... 11 Related Resources ..................................................................................... 11 2 Abstract ------------------------------------------------------------------------------------------------------------------------------------------------------------------ The complexities of importing a Comma-Separated Values (CSV) file are greatly simplified by using the Match regex command in 4D v11 SQL. This Technical Note presents a 4D method that can be used to parse CSV files, using the Match regex command. A sample database is included.

## Key Points
- Published September 4, 2008 as Technical Note 08-32.
- Targets 4D v11.2 on Mac &amp; Win.
- Author: Charles Vass, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- Regular expressions

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
