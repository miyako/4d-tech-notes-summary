# Tech Note: Object Storage in 4D v11 SQL Using Native Commands

## Overview
4D v11 SQL has extended the capabilities of hierarchical list items to allow storage of Object-like structures. The same hierarchical list item may have values of different types; i.e. numerical, string or boolean. In other words, you can associate a dictionary with each list item. Using the commands SET LIST ITEM PARAMETER and GET LIST ITEM PARAMETER, you can store Objects using native 4D v11 SQL Commands.

## Key Points
- Published May 14, 2008 as Technical Note 08-18.
- Targets 4D v11 on Mac &amp; Win.
- Author: Luis Pineiros Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
