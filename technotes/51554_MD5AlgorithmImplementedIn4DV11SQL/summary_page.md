# Tech Note: MD5 Algorithm Implemented in 4D v11 SQL

## Overview
Nowadays more and more businesses are conducted over the internet, and security for changing information is becoming a problem. This is the time when encryption algorithms come in handy. 4D developers also want to implement some of the well known encryption algorithms in their databases. Some of these algorithms are already written in JavaScript code. 4D v11 SQL release 2 offers tools for developers to implement JavaScript code in a 4D database. This Technical Note explains how easy it is to implement JavaScript code in 4D. In our examples we use an MD5 encryption algorithm. The hash function of this algorithm is written in JavaScript and we will implement this function in 4D. There are two examples, and they show the algorithm in a 4D Web area and a 4D form.

## Key Points
- Published November 12, 2008 as Technical Note 08-39.
- Targets 4D v11 on Mac &amp; Win.
- Author: Atanas Atanassov, Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- MD5 hashing

## Historical Context
This 2008 Tech Note documents a feature of the then-new 4D v11 SQL engine or the 4D Ajax Framework (4DAF), both of which were central to 4D's product strategy at the time. The 4D v11 SQL engine itself was foundational and its core concepts (schemas, SQL access, list boxes, components) persist conceptually in modern 4D, though the specific syntax and interfaces have evolved substantially through later versions and ORDA (introduced 2018). 4DAF-based web UI techniques (Data Grids, YUI integration, custom AJAX components), by contrast, reflect a web-development approach that has been superseded by 4D's modern web server, web components, and Qodly Studio (2021+).

**Status:** superseded

**Related updates:**
- 4D v11 SQL's data access model has since been extended by ORDA (Object Relational Data Access, introduced in 4D v17, 2018), which is now the recommended API for data access
- Project Mode (introduced 4D v17, 2018) added a text-based alternative to the binary Design Mode structure file referenced implicitly in this era
