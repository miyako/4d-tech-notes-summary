# Tech Note: 4D ODBC in DataGrid's Enterprise Data Module - Beta 1

## Overview
- **Technical Note 00-40**
- **Author:** Sebastian Frey, Sextant Technologies, Inc.
- **Published:** August 1, 2000
- **Product/Version:** 4D ODBC v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the fifth installment in Sebastian Frey's series on the internals of DataGrid Beta 1, this time examining the 4D ODBC low-level layer of the application's Enterprise Data Module (EDM) framework. It opens with a grounding explanation of ODBC itself — Microsoft's standard for accessing any data source through a common driver-based middle layer — before describing 4D ODBC as the plug-in that lets 4th Dimension, 4D Runtime, or 4D Client act as an ODBC client, connecting to external ODBC data sources such as Microsoft SQL Server or Access to query, sort, receive, and modify records. A central proposition of the note is clearing up a common point of community confusion: 4D ODBC (which makes 4D an ODBC client) is an entirely different product from the ODBC Driver for 4D Server (which makes 4D Server itself an ODBC data source that third-party tools like Crystal Reports or Visual Basic can query), and the note explains why using both together in an all-Windows environment is tempting but limited by the ODBC Driver for 4D Server's incomplete ODBC compliance. The featured technology is the 4D ODBC connectivity plug-in as wired into DataGrid's EDM abstraction, illustrating how the broader 4D Connectivity Products suite of the era was meant to interoperate with third-party applications like DataGrid.

## Featured Technology
- 4D ODBC plug-in
- ODBC Driver for 4D Server
- DataGrid Enterprise Data Module (EDM)

## Historical Context
This note, the fifth in Sextant Technologies' DataGrid series, explains 4D ODBC (which lets 4D act as an ODBC client) as integrated into DataGrid's Enterprise Data Module, and it carefully distinguishes 4D ODBC from the separate ODBC Driver for 4D Server (which lets 4D act as an ODBC server for tools like Crystal Reports or Visual Basic) — a distinction that confused many developers even at the time. DataGrid itself is long defunct, and while ODBC connectivity concepts remain broadly relevant, 4D's own architecture for both consuming and exposing external data sources has evolved considerably since this Beta-1-era plug-in integration, making the specific implementation obsolete.

## What's Changed Since
- DataGrid and its Enterprise Data Module, the third-party application this note documents, are long discontinued
- 4D's own connectivity options for consuming external databases and exposing 4D data to other tools have significantly evolved since this 2000-era plug-in architecture

