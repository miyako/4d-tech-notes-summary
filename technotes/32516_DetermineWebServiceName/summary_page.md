# Tech Note 04-18: Determining the Name of a Requested Web Service

**Author:** Not specified in source teaser
**Published:** May 6, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32516
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_16-20_(APR)/04-18_Determine_WS_Name.exe

## Overview
This Tech Note addresses how a 4D method published as a SOAP Web Service can determine the name of the method or service that was actually requested by a client — information useful for developers implementing custom security, logging, or routing logic around Web Services calls.

## Key Points
- 4th Dimension 2003+ can publish project methods as SOAP Web Services served through the native 4D Web server.
- SOAP requests conventionally include the name of the requested method, and sometimes the Web Service name.
- The built-in `Get Soap info` command provides some of this information, but has behavioral limits described in the note.
- Custom code is provided to extract the method/service name directly from the `SoapAction` HTTP header when present, supplementing `Get Soap info`.
- A downloadable example database (Windows/Mac) demonstrates the technique.

## Featured Technology
- 4D Web Services (SOAP over the native 4D Web server)
- `Get Soap info` language command
- Manual HTTP header (`SoapAction`) parsing

## Historical Context
Published only a few months into 4D's SOAP Web Services era, this note reflects a period when developers regularly had to work around gaps in 4D's built-in Web Services introspection by manipulating raw HTTP/SOAP headers. Since only the on-page teaser text was recoverable for this asset (the full archived PDF could not be retrieved in this environment), this summary is necessarily limited to the note's stated purpose and cannot describe the exact custom code shown. SOAP-based Web Services, and the specific header-parsing workaround described here, are now of historical interest only, given 4D's subsequent shift toward REST/JSON web services and more complete built-in request-handling commands.
