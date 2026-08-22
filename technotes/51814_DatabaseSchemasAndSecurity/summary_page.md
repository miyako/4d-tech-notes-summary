# Tech Note: Database Schemas and Security

## Overview
4D v11 SQL Release 3 introduces many improvements and features to the 4D v11 SQL line of products. One particularly useful feature is the support of schemas in 4D’s integrated SQL engine. The implementation of this feature has resulted in modifications to the interface and the introduction of new SQL commands. This technical note describes the changes to the interface as well as the new SQL commands. A sample database component is included.

## Key Points
- Published December 10, 2008 as Technical Note 08-43.
- Targets 4D v11.3 on Mac &amp; Win.
- Author: Timothy Aaron Penner, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
