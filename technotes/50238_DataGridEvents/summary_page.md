# Tech Note: Data Grid Events

## Overview
The Data Grid supports a number of events that can be used for many purposes such as drag and drop functionality and passing custom values to and from 4D. For this Technical Note, we will go over the user interface events that fire when the end user interacts with the grid. We will also evaluate the information that becomes available once each event is triggered. A sample database is provided.

## Key Points
- Published June 26, 2008 as Technical Note 08-24.
- Targets 4D Web 2.0 Pack v11.2 on Mac &amp; Win.
- Author: Joe Resuello, Technical Marketing Engineer, 4D Inc..

## Featured Technology
- 4D v11 SQL
- Data Grid / 4DAF

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** obsolete

**Related updates:**
- 4D Ajax Framework (4DAF) has been discontinued; modern 4D web development uses 4D's built-in web server, REST/ORDA APIs, and Qodly Studio (2021+) for low-code web UI
- AJAX-era manual grid/component techniques have been superseded by modern JS frameworks and 4D web components
