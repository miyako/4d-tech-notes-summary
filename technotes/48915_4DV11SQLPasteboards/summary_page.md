# Tech Note: 4D v11 SQL Pasteboards

## Overview
This Technical Note covers the new Pasteboard theme of 4D v11 SQL. This new theme encompasses the functionality of the previous Clipboard theme and adds new functionality. One of the more significant additions is the ability to now access drag-and-drop data from outside of 4D. This Technical Note will cover the different pasteboards available in 4D, what new functionality has been added, and what data types are supported. A sample database is included.

## Key Points
- Published February 13, 2008 as Technical Note 08-06.
- Targets 4D Developer v11 on Mac &amp; Win.
- Author: Jesse Piña, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- Clipboard/Pasteboard APIs

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
