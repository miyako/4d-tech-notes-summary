# Tech Note: New List Box Features in 4D v11 SQL – Part 2

## Overview
In September 2007 the first Technical Note on this topic was released, number 0738, New List Box Features in 4D v11 SQL. Part 2 of the topic, covered in this Technical Note, delves into manipulating the new features of List Boxes in code rather than via the Form Editor. The new data sources available for List Boxes in 4D v11 SQL, as well as changes to the commands used to manage List Box’s in code, provide powerful tools for the 4D developer to create dynamic List Box-based content. A sample database is included. Introduction ------------------------------------------------------------------------------------------------------------------------------------------------------------------ This Technical Note expands on how to use List Boxes in 4D v11 SQL. The first part of the Technical Note is an overview of the commands and features used to manage List Box form objects programmatically through 4D code. The second part of the Technical Note documents the sample database and the code it uses. There are main topics covered in this Technical Note and examples of each in the sample database: • • • • List Boxes from arrays (similar to previous versions of 4D) List Boxes from selection

## Key Points
- Published March 13, 2008 as Technical Note 08-09.
- Targets 4D Developer v11 on Mac &amp; Win.
- Author: Tom Fitch, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D List Box
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
