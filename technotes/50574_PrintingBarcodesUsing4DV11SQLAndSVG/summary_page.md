# Tech Note: Printing Barcodes using 4D v11 SQL and SVG

## Overview
Printing Barcodes using 4D v11 SQL and SVG By Thomas Maul, General Manager, 4D Germany TN 08-27 Introduction ------------------------------------------------------------------------------------------------------------------------------------------------------------------ This Technical Note updates Technical Note 05-08 for 4D v11 SQL. Using the new SVG features of 4D v11 SQL to replace 4D Chart to create bar codes, the result is much faster creation with higher quality. It also fixes a bug. See the original Technical Note for a description of the commands and features (included with this document and also available at): http://www.4d.com/knowledgebase?CaseID=36279 Example and Component ------------------------------------------------------------------------------------------------------

## Key Points
- Published July 30, 2008 as Technical Note 05-08.
- Targets 4D v11.2 on Mac &amp; Win.
- Author: Thomas Maul, General Manager, 4D Germany.

## Featured Technology
- 4D v11 SQL
- Barcode / SVG generation
- SVG

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
