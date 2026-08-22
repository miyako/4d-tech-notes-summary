# Tech Note: Building Applications Examples – Part 1 XML Keys Editor

## Overview
4D 2004 features over 80 XML keys that can be used to build customized applications. The XML keys documentation gives basic information about what the keys do, but there are few examples. The goal of this series of Technical Notes is two-fold: • Provide examples for each XML key, on Mac OS X and Windows, to aid the 4D Developer in understanding what each key does. • To make editing the XML project file, used in building applications, an easier task by providing a GUI editor. In part 1 of this series a 4D application is presented, which provides a GUI editor for every XML key available. This makes editing and maintaining the project files a snap. Introduction ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 4D 2004 features the ability to control the application building process with the use of an XML project file. There are over 80 XML keys that can be used to build customized applications. The project file can contain some or all of these XML keys, as needed. These XML keys allow many parts of a 4D application to be customized; for example the application name c

## Key Points
- Published February 20, 2008 as Technical Note 08-07.
- Targets 4D v2004.7 on Mac &amp; Win.
- Author: Josh Fletcher, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- XML

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
