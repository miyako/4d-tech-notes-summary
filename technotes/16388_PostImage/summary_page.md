# Tech Note: PostImage

- **Asset ID:** 16388
- **Tech Note #:** 01-32
- **Published:** July 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Chiheb Nasr
- **Page URL:** https://kb.4d.com/assetid=16388
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_31-35_(JUL)/01-32_PostImage.hqx

## Overview

Chiheb Nasr (Technical Support Engineer, 4D S.A.) demonstrates uploading a picture from a web browser form to a 4D database and storing it directly in a Picture field, framed as an easy technique even beginners can integrate into an existing database. It requires QuickTime 4.0 on the Windows side to function.

## Key Points

- The HTML upload form must use `Enctype="multipart/form-data"` and an `<INPUT Type="file" Name="vblobimage" size="35">` field posting to a `4DACTION` (e.g., `/4daction/WebH_Reception`) rather than a `4DCGI` action.
- The uploaded BLOB variable name (`vBlobImage`) must be declared with `C_BLOB` in the `Compiler_Web` method — skipping this step results in only the file's path or name being received, not its contents.
- The received BLOB is split at the `CR+LF+CR+LF` boundary (expressed in 4D as `2*(Char(13)+Char(10))`), separating the multipart header from the actual picture data.
- The header is parsed by `WebH_BlobImageHeaderProc`, with `WebH_ExtractPictureName` and `WebH_ExtractPictureType` extracting the file's name and MIME/file type; if the uploaded file is not a picture, `WebH_ExtracErrorType` reports the actual type back to the caller.
- A valid picture is stored via `WebH_Reception` into a picture field in the `[Pictures]` table, and a confirmation message is sent back to the browser.

## Featured Technology

- multipart/form-data HTML file upload (4DACTION)
- 4D built-in Web Server BLOB reception
- Compiler_Web BLOB variable declaration
- CR+LF+CR+LF BLOB header delimiter parsing
- WebH_ExtractPictureName / WebH_ExtractPictureType
- Picture field storage from uploaded BLOB

## Historical Commentary

**Status:** Partially superseded

Accepting image uploads from a web client into a 4D database is still a common requirement, but this note's specific mechanism — manually parsing a raw multipart/form-data BLOB via a 4DACTION method and delimiter-searching for CR+LF+CR+LF boundaries — reflects the constraints of 4D's original built-in Web Server. Modern 4D applications handle equivalent scenarios through REST/ORDA endpoints and more capable native multipart/file-upload support, making the hand-rolled BLOB-header-parsing approach shown here largely unnecessary today, even though the underlying built-in Web Server commands referenced still exist.

**References to newer/updated information:**
- 4D's REST/ORDA APIs now provide more modern mechanisms for handling file/image uploads from web and mobile clients
- 4D's built-in Web Server has gained more native multipart/form-upload handling since 2001, reducing the need for manual BLOB header parsing
