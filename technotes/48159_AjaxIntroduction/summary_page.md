# Tech Note 07-44: An Introduction to Ajax

**Author:** Joe Resuello, Technical Marketing Engineer, 4D Inc.
**Published:** November 21, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=48159
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_42-45_(NOV)/07-44_Ajax_Intro.pdf

## Overview
This note gives a beginner-level explanation of Ajax for 4D developers with little web experience, then introduces the 4D Ajax Framework (4DAF) as 4D's own way to add Web 2.0-style browser interactivity to a 4D database.

## Key Points
- Dispels misconceptions: Ajax is not a plug-in technology, not a new programming language, and not a proprietary product (unlike Flash).
- Defines Ajax as a technique combining JavaScript, XML, HTML, and CSS to build interactive web apps using open standards, compatible with browsers of the era (IE 5.0+, Mozilla 1.0+, Firefox 1.0+, Netscape 7.0+, Safari 1.2+).
- Credits Jesse James Garrett's February 18, 2005 essay for coining the term "Ajax," amid buzz from early Ajax-style Google apps (Google Maps, Google Suggest).
- Characterizes Ajax applications by their lack of full-page reloads and desktop-like responsiveness.
- Introduces the 4D Ajax Framework (4DAF) with its layered architecture: 4DAF Client (plug-and-play), 4DAF Libraries (custom embedding), and Data Services/Server layers for browser-database communication.
- Highlights prebuilt 4DAF UI objects (e.g. Image Matrix, Calendar) that visually and asynchronously represent 4D table data.
- Notes ease of integration: often only a line or two of JavaScript, or none at all via the "4D Ajax for Dreamweaver" point-and-click extension.
- Points to further resources: Daxipedia.com and related Technical Notes (e.g. 07-24 "4DAF Video Player").

## Featured Technology
- Ajax (JavaScript, XML, HTML, CSS technique)
- 4D Ajax Framework (4DAF) — client, libraries, data services, server layers
- 4DAF prebuilt objects: Image Matrix, Calendar
- 4D Ajax for Dreamweaver extension

## Historical Context
Published in November 2007, just before 4D's SQL-focused notes for the new 4D v11 SQL engine, this note reflects the pre-ORDA, pre-Project-Mode era in which 4D paired its classic Design-Mode desktop database engine with the 4DAF component to reach the emerging Web 2.0 / Ajax trend, using tools like Dreamweaver integration and prebuilt widget objects that were considered cutting-edge web UI techniques at the time.

## Historical Commentary
**Status:** Superseded

The general explanation of what Ajax is and why it mattered remains historically accurate and reasonably clear even today, but the 4D Ajax Framework it promotes has been discontinued, along with the Dreamweaver-based, plug-and-play integration workflow it describes. Modern 4D web development instead relies on 4D's built-in Web Server exposing REST/ORDA APIs, consumed by contemporary JavaScript frameworks rather than the 4DAF's bundled widget library.
