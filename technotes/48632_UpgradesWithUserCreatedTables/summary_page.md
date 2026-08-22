# Tech Note: Upgrades with User Created Tables

## Overview
This Technical Note prepares developers for creating a 4D application which allows end users to create their own tables. It includes two sample databases. One represents the current version of a database, just finished by the developer. The other represents the end user’s version of the same database, which the developer would like to upgrade to the new version. Because the end user has added some user created tables to the database the upgrade process is more complicated than if he or she did not have that option.

## Key Points
- Published January 17, 2008 as Technical Note 02-08.
- Targets 4D Developer v11 on Mac &amp; Win.
- Author: Thomas Fitch, Technical Support Engineer, 4D Inc..

## Featured Technology
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
