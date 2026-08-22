# Tech Note: Components in 4D v11 SQL

## Overview
4D Components since their inception have represented the most flexible and secure way to create and distribute additional functionalities to be installed in other databases. 4D v11 SQL introduces a new Component Architecture. Components are now easier to develop and install; however, the changes are significant enough that the previous versions of components are no longer supported. The goal of this Technical Note is to examine the new Component mechanism in 4D v11 SQL and its advantages, compare the previous implementation with the current, and analyze a component database example included with this Technical Note.

## Key Points
- Published March 5, 2008 as Technical Note 08-08.
- Targets 4D Developer v11 on Mac &amp; Win.
- Author: Luis Pineiros, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D Components
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
