# Tech Note: Returning Pictures Through SOAP

- **Asset ID:** 32222
- **Tech Note #:** 04-15
- **Published:** April 15, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=32222
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_11-15_(APR)/04-15_Returning_Pictures_Through_SOAP.hqx

## Overview

David Adams shows how to work around 4th Dimension 2003's inability to include the Picture type directly in a SOAP response, by converting images to BLOBs with PICTURE TO BLOB before returning them, illustrated with a complete SOAP-based image server offering listing, format-discovery, and retrieval services.

## Key Points

- Every native 4D data type except Picture can be automatically bound into a SOAP response; the workaround is converting the picture to a BLOB with `PICTURE TO BLOB` before returning it, and converting back with `BLOB TO PICTURE` on the client.
- `GetPictureList` queries an `[Images]` table, sorts by name, and returns the names as a `SOAP DECLARATION`-bound String array output (`outPictureNames`), giving clients a discoverable catalog of available images.
- `GetPictureFormatList` returns platform-neutral MIME types (not 4D's native four-character QuickTime codes) by using `PICTURE TYPE LIST` at startup and a `[Picture_Format_Codes]` lookup table to convert QuickTime codes to MIME types, always ensuring GIF is included since it needs no QuickTime.
- `getPicture` takes a picture name and desired MIME type, queries the `[Images]` record, converts it with `PICTURE TO BLOB` using the resolved 4D format code, and returns the BLOB as a `SOAP DECLARATION`-bound output (`outPictureBlob`), with `SEND SOAP FAULT` used for error signaling.
- A client-side proxy method demonstrates the full round trip: `SET WEB SERVICE PARAMETER`, `CALL WEB SERVICE`, `GET WEB SERVICE RESULT` for the BLOB, and `BLOB TO PICTURE` to reconstruct the image, needing only one line of application code (`request_getPicture(...)`) to retrieve a picture.
- Extended commands in the sample (`getPictureData`, `getPictureListExtended`, `getPictureWithType`, `getThumbnail`) return picture metadata (size, width, height, authors, description) or thumbnails; the note also surveys alternative picture sources beyond table records (documents on disk/network, PICT resources, Picture Library, 4D Chart/4D Draw output).

## Featured Technology

- PICTURE TO BLOB / BLOB TO PICTURE commands
- SOAP DECLARATION with Is BLOB SOAP Output
- PICTURE TYPE LIST for enumerating QuickTime-supported formats
- SEND SOAP FAULT for SOAP error handling
- GET WEB SERVICE PARAMETER / SET WEB SERVICE PARAMETER
- Base64-encoded BLOB transport over SOAP

## Historical Commentary

**Status:** Obsolete

Since 4th Dimension's native SOAP binding didn't directly support the Picture data type, this note shows how to work around that gap by converting pictures to BLOBs with `PICTURE TO BLOB` before returning them as a SOAP output, and converting back with `BLOB TO PICTURE` on the client -- illustrated with a small SOAP-based image server offering picture listing, format discovery (via `PICTURE TYPE LIST` and a QuickTime-code-to-MIME-type lookup table), and image retrieval by name/format. It's a clear, well-engineered example of working around SOAP data-type limitations. Because it's built entirely on 4th Dimension's SOAP Web Service client/server system, which has been superseded by REST APIs on ORDA (2017+), and because it depends on QuickTime for non-GIF format conversion (QuickTime itself has since been discontinued on Windows and deprecated on macOS), both the transport approach and the picture-conversion mechanism are now largely of historical interest.

**References to newer/updated information:**
- 4D's SOAP-based Web Service publishing has been superseded by REST APIs built on ORDA (introduced 2017+), which handle binary/picture data more directly (e.g. via BLOB or file responses) without needing this BLOB workaround
- Apple QuickTime, which this note's image-format conversion depends on, has been discontinued on Windows and deprecated/removed on modern macOS, breaking part of the described format-conversion pipeline
- 4D's native picture-handling commands have expanded since 2004, reducing reliance on QuickTime for format conversion
