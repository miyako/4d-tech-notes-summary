# Tech Note: Introduction to 4D Open

## Overview
- **Technical Note 00-44**
- **Author:** Aziz Elghomari, 4D S.A. Technical Support
- **Published:** September 1, 2000
- **Product/Version:** 4D Open v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is 4D S.A. Technical Support's introduction to 4D Open, the API that lets external client code communicate with a 4D Server, framing 4D Open's capabilities around four themes: access management (passwords and groups), structure access (retrieving table/field names, attributes, and properties), access to selections (searches, navigation), and data access (record creation, deletion, and modification in a multi-user context). This first installment deliberately scopes itself to the structure-access theme, explicitly deferring data access to 'a future technical note' (fulfilled a month later by the companion note archived here as asset 11987). It explains what an API fundamentally is in classic C/Pascal terms — a library exposing entry points that another application can call, with data exchanged across the boundary — and walks through the specific initialization sequence required before any 4D Open call can succeed: _4D_Init4DWS to prepare 4D Open's internal data, _4D_InitNetworkComponent to allocate a network-component memory block (citing ADSP and TCP/IP as the two example network components of the era), and _4D_Select4DServer to locate and select a specific 4D Server on the network by name. The featured technology is squarely 4D Open's connection-and-structure-access layer, an early precursor concept to today's REST/ORDA-based external access to 4D Server.

## Featured Technology
- 4D Open
- Structure access API
- Network components (ADSP/TCP)

## Historical Context
This is the first of a pair of introductory 4D Open notes (its data-access companion, also archived here as asset 11987, followed a month later), explaining 4D Open's four functional themes and walking through initializing a connection and retrieving structure information (tables, fields, attributes) from a 4D Server. 4D Open, described here as a C-style API with explicit entry points and network-component initialization calls, has been discontinued for many years; modern external programmatic access to 4D Server data is done through 4D's REST/ORDA web data server, which offers a fundamentally different, HTTP-based architecture rather than a linked C library.

## What's Changed Since
- 4D Open has been discontinued; there is no direct modern product carrying its name forward
- 4D's REST/ORDA data server is the modern replacement path for programmatic, cross-platform access to a 4D Server's structure and data

