# Tech Note 04-15: Returning Pictures Through SOAP

**Author:** Not specified in source teaser
**Published:** April 15, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32222
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_10-15_(MAR)/04-15_Pictures_Through_SOAP.exe

## Overview
This Tech Note explains how to work around a limitation of 4th Dimension 2003's SOAP Web Services support — the inability to return picture data directly — by converting images to BLOBs before including them in a SOAP response.

## Key Points
- 4D 2003+ Web Services (SOAP) responses natively support nearly all 4D data types except pictures.
- BLOBs are supported in SOAP responses, so pictures can be sent by first converting them with `PICTURE TO BLOB`.
- Explains the mechanics of converting and packaging images for SOAP/XML transport.
- Ships with an example database implementing a simple SOAP-based image-serving system.
- Offers suggestions for extending the basic example toward more sophisticated functionality.

## Featured Technology
- 4D Web Services (SOAP over the native 4D Web server)
- `PICTURE TO BLOB` command
- BLOB encoding within SOAP/XML responses

## Historical Context
Only the on-page teaser paragraph for this asset was recoverable (the full archived PDF could not be retrieved in this environment), so this summary is limited to the note's stated purpose and cannot describe its exact example code. The picture-to-BLOB SOAP workaround it documents is tied to 4D's early, now largely legacy SOAP Web Services implementation; modern 4D applications serving images over an API overwhelmingly rely on REST/JSON approaches instead, making this specific technique of historical interest only.
