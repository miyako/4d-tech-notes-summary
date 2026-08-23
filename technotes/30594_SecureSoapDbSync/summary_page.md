# Tech Note: Securely Synchronizing databases with dissimilar structures via SOAP

- **Asset ID:** 30594
- **Tech Note #:** 03-50
- **Published:** November 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=30594
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_48-51_(NOV)/03-50_Synchronizing_SOAP.hqx

## Overview

Kent Wilbur, Manager of Information Systems at 4D, Inc., presents a SOAP-based technique for synchronizing two 4D databases that have different (and potentially changing) structures, using a single secure entry-point method rather than a published, field-by-field WSDL. Instead of exposing individual fields as SOAP parameters, the sample Server/Client databases pack an entire record's worth of data into a text array, convert it to a BLOB, and transmit it through one method, SERVER4D_ConnectFromRemote, that has no discoverable WSDL.

## Key Points

- Uses one narrow SOAP entry point (SERVER4D_ConnectFromRemote, single BLOB in/out) instead of a discoverable, per-field WSDL, reducing the attack surface
- Packs an entire record's fields into a text array, then a BLOB, via VARIABLE TO BLOB / BLOB TO VARIABLE, so record shape can change without renegotiating the SOAP interface
- Authenticates each connection with a 4-element Connection Validation Array (Store ID, user name, password, requested function name) checked against the [Store] table before any data is returned
- Requests the server's current field order at runtime ('ReadCustomersArrayFormat') via a named choice list, so client and server stay in sync automatically as the structure evolves
- Returns descriptive errors to the caller with SEND SOAP FAULT and a custom SERVER_tErrorMessages lookup method (e.g., -28002 Invalid Store ID, -28003 invalid credentials)
- Optionally compresses BLOBs with COMPRESS BLOB/EXPAND BLOB and sketches true end-to-end security using GENERATE ENCRYPTION KEYPAIR with ENCRYPT BLOB/DECRYPT BLOB (public/private key pairs per side)
- Suggests obscuring credit-card data by scattering it across a large random-number array (PrivateBLOB) rather than storing it as a single value

## Featured Technology

- SOAP (4D 2003 Web Services)
- SEND SOAP FAULT
- BLOB packing via VARIABLE TO BLOB / BLOB TO VARIABLE
- COMPRESS BLOB / EXPAND BLOB
- GENERATE ENCRYPTION KEYPAIR (ENCRYPT BLOB / DECRYPT BLOB)
- Self-describing schema negotiation ('common vocabulary') via LIST TO ARRAY

## Historical Commentary

**Status:** Superseded

This note's core insight — negotiate a schema at runtime and transfer opaque BLOBs through a single secure entry point rather than exposing per-field SOAP parameters — was a clever, security-conscious pattern for 2003-era 4D SOAP web services. SOAP itself has since been broadly superseded as a transport by REST/JSON, and for 4D-to-4D scenarios specifically, ORDA's remote datastore access now offers a far simpler and more secure way to read and write data across databases without hand-rolled BLOB packing. The underlying goal of structure-agnostic, secure synchronization remains a live concern, but the concrete SOAP/BLOB mechanism described here is dated.

**References to newer/updated information:**
- ORDA and 4D's remote datastore capabilities (introduced starting with 4D v17/v18, 2018+) provide a modern way to read/write data across 4D databases, replacing the need for hand-built SOAP/BLOB synchronization
- REST/JSON has broadly replaced SOAP as the preferred data-interchange transport for new integrations
- 4D still supports SOAP/CALL WEB SERVICE commands for legacy interoperability, but they are not the recommended approach for new 4D-to-4D sync
