# Tech Note: NULLS in 4D v11 SQL

## Overview
For all of the vast improvements that 4D v11 SQL provides over its predecessors with respect to performance and scalability, some of the more subtle aspects of this latest offering are worth spending some time with. Case in point is 4D’s support of NULL values. A NULL value is a value that exists, but its contents are unknown. This tech note covers the uses for NULL values, the language commands in 4D and SQL that developers can use to manipulate them and their behavior in 4D v11 SQL.

## Key Points
- Published October 30, 2008 as Technical Note 08-38.
- Targets 4D v11 on Mac &amp; Win.
- Author: Chris Visaya, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- SQL NULL handling

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
