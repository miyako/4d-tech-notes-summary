# Tech Note: Exploring 4D Ajax Framework Offline Mode

## Overview
........................................................................................................... 3 Introduction ..................................................................................................... 3 Introduction to Offline Mode .............................................................................. 4 Using the 4D Ajax Framework Client................................................................ 4 Using the 4D Ajax Framework Libraries ........................................................... 6 Offline Browser Technology ............................................................................... 7 HTML5 .......................................................................................................... 7 Gears by Google ............................................................................................ 7 Troubleshooting Offline Mode Problems .............................................................. 9 Allowing Access for Gears ............................................................................... 9 Unsupported Browsers Without Gears.............................................................. 9 Offline Mode Status Indicator ........................................................................ 10 End of 4D Ajax Framework Session ............................................................... 10 Conclusion ..................................................................................................... 11 A Note about 4D Web 2.0 Pack ........................................................................ 11 Related Resources .......................................................................................... 11 2 Abstract ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 4D Ajax Framework v11 Release 2 (11.2) offers a great new feature: Offline Mode. With the new offline web browser technologies available, users can enter and save data in their browser while not connected to the internet, then automatically synchronize that data when they reconnect. This Technical Note will give a quick overview of the capabilities of Offline Mode, outline the new browser technologies behind the feature, and offer troubleshooting tips for developers implementing Offline Mode in a 4D Ajax Framework application.

## Key Points
- Published August 6, 2008 as Technical Note 08-28.
- Targets 4D Web 2.0 Pack v11.2 on Mac &amp; Win.
- Author: Thomas Fitch, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D Ajax Framework (4DAF)
- 4D v11 SQL

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** obsolete

**Related updates:**
- 4D Ajax Framework (4DAF) has been discontinued; modern 4D web development uses 4D's built-in web server, REST/ORDA APIs, and Qodly Studio (2021+) for low-code web UI
- AJAX-era manual grid/component techniques have been superseded by modern JS frameworks and 4D web components
