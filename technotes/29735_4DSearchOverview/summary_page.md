# Tech Note: 4D Search

- **Asset ID:** 29735
- **Tech Note #:** 03-37
- **Published:** August 29, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=29735
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_36-39_(AUG)/03-37_4D_Search.hqx

## Overview

Jean-Yves Fock-Hoon, QA Manager at 4D, Inc., explains the internals of the 4D Search sample database, which lets a 4D application query the indexes built by the 4D WebSTAR V web server's Search plug-in (including records published dynamically via the 4D Dynamic Data Indexer) and parse the XML results using 4D 2003's native Parse XML source command, rather than hand-rolling raw TCP socket calls.

## Key Points

- Connects to one or more 4D WebSTAR V servers via WSAPI_LoginDialog and retrieves available search index pages with WSAPI_WebSrv_GetSearchIndices (from the 4D WebSTAR API component, which requires the 4D Internet Command plug-in)
- Notes that since WebSTAR 5.3.1, the '4D Dynamic Data Indexer' lets index pages cover a SOAP-generated dynamic list of URLs, letting 4D Search index and expose 4D records published on the web (referenced to an August 2003 companion Tech Note)
- Resolves a raw index-page name to an absolute, usable URL by calling WSAPI_WebSrv_GetRouting (to confirm the realm and find its site/port) and, when the realm is generically configured (host '*', port 'Any'), falling back to WSAPI_WebSrv_GetWebListeners for the server's real listening IP/port
- Builds search request URLs like http://host/test.search?numdocs=9999&minscore=10&xml=1&geturl=1&getrelevance=1&gettitle=1&getsummary=1&query=keyword against each selected index page
- Because the target is 4th Dimension 2003 and the WebSTAR response is XML, the entire HTTP fetch-and-parse cycle is done with the single native Parse XML source command in M_ParseXMLSource, avoiding a hand-written TCP_Send/TCP_Receive component that older 4D versions would have required
- Categorizes stored results (HTML/PDF/text/all) by testing each URL's file extension and adding the record to a matching 4D set, switched between via tab controls with USE SET
- Opens a selected search result directly in the user's default browser via OPEN WEB URL
- Cites a live benchmark: searching 'ODBC' across the full 4D documentation set (100MB+ of HTML/PDF) and parsing the results took under two seconds

## Featured Technology

- 4D WebSTAR V Search plug-in / index pages
- 4D Dynamic Data Indexer (DDI, SOAP-driven URL lists)
- WSAPI_LoginDialog / WSAPI_WebSrv_GetSearchIndices
- WSAPI_WebSrv_GetRouting / WSAPI_WebSrv_GetWebListeners
- Parse XML source (native 4D XML/HTTP fetch)
- OPEN WEB URL for opening search results

## Historical Commentary

**Status:** Obsolete

This note showcases a smart use of 4D 2003's then-new native Parse XML source command to avoid hand-rolled TCP networking, but the product it's built around — the 4D WebSTAR V web server and its Search plug-in/Dynamic Data Indexer — has been discontinued for many years. A modern equivalent to full-text search over a document/record set would use a dedicated search engine (Elasticsearch, Algolia, or similar) fronted by 4D's current built-in web server and native HTTP client, rather than WebSTAR's proprietary indexing plug-in, making this note of historical interest only.

**References to newer/updated information:**
- 4D WebSTAR V, and its Search plug-in / Dynamic Data Indexer used throughout this note, have been discontinued
- Modern full-text search over documents or records would typically be built with a dedicated search engine (e.g., Elasticsearch, Algolia) fronted by 4D's current built-in web server and native HTTP client commands
