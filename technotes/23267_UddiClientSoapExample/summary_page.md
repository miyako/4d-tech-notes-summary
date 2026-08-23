# Tech Note 03-12: UDDI Client as a SOAP Example (API inquiry)

- **Asset ID:** 23267
- **Tech Note #:** 03-12
- **Published:** March 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Julien Feasson
- **Page URL:** https://kb.4d.com/assetid=23267
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_11-15_(MAR)/03-12_UDDI_Client_and_SOAP.hqx

## Overview

Julien Feasson (4D, Inc.) demonstrates building a UDDI Inquiry client in 4D 2003 — the first of a two-part series — using 4D's newly built-in SOAP Web Service Client and XML parsing commands to query a UDDI registry for web services by keyword, retrieving and displaying tModel details from servers such as xMethods.net.

## Key Points

- UDDI is described as a protocol layered on SOAP (UDDI → SOAP → XML → HTTP), and the note focuses solely on the Inquiry API (`find_xx`/`get_xx` calls), leaving the Publisher's API for Part II.
- A Preferences panel stores a list of UDDI servers to query; the demo's UDDI Search Assistant sends `find_tModel` and `get_tModelDetail` SOAP requests to every server in the list for a keyword search.
- Because UDDI is a Doc-style SOAP API, the request XML must be built by hand: `myxml:="<find_tModel xmlns=\"urn:uddi-org:api\" generic=\"1.0\">"+"<name>"+$1+"</name>"...`, converted to a blob with `TEXT TO BLOB`, then sent via `SET WEB SERVICE PARAMETER("BlobAsXMLIn";myblob)` and `CALL WEB SERVICE`.
- The raw XML SOAP response is retrieved with `GET WEB SERVICE RESULT` and walked as a DOM tree using `Parse XML variable`, `Get First XML element`, `Get Next XML element`, and `GET XML ATTRIBUTE BY NAME` to extract tModel UUIDs and names into arrays.
- A second request (`get_tModelDetail`) fetches full details for each cached UUID — author, operator, name, description, overview URL, category/identifier bags — parsed via a `Case of`/`Repeat...Until` loop into a 2D array for display.
- The author warns that many public UDDI servers (Microsoft, IBM) were already becoming stale/unreliable by 2003 and recommends xMethods.net as the most usable registry for testing.

## Featured Technology

- UDDI Inquiry API (find_tModel, get_tModelDetail)
- 4D 2003 built-in SOAP Web Service Client (CALL WEB SERVICE)
- SET WEB SERVICE PARAMETER / GET WEB SERVICE RESULT
- 4D XML parsing commands (Parse XML variable, Get First/Next XML element, GET XML ATTRIBUTE BY NAME)
- Doc-style SOAP request construction
- TEXT TO BLOB for building raw XML SOAP payloads

## Historical Commentary

**Status:** Obsolete

This note is the first of a two-part series showing how 4D 2003's newly built-in SOAP Web Service Client and XML parsing commands could be used to query a UDDI registry (find_tModel/get_tModelDetail) for web service discovery. UDDI as a technology and public registry infrastructure (Microsoft's, IBM's, and eventually xMethods.net's UDDI servers) has been dead for well over a decade, so the specific subject matter is entirely obsolete. However, the demonstrated 4D mechanics — building a Doc-style SOAP XML payload manually, sending it with CALL WEB SERVICE, and parsing the raw XML response by walking the DOM tree with Get First/Next XML element — were standard techniques for any non-RPC-style SOAP integration in that era and were themselves eventually superseded by 4D's more modern SOAP/REST web service tooling.

References to newer/updated information:
- UDDI has been effectively abandoned industry-wide; the public UDDI Business Registry (Microsoft, IBM, xMethods) was shut down years ago
- Modern service discovery uses different mechanisms such as API gateways, service meshes, and OpenAPI-based directories
- 4D's SOAP client and XML DOM-parsing commands used here have since been supplemented by 4D's native XML/JSON and HTTP client commands, reducing the need for manual Doc-style SOAP envelope construction
