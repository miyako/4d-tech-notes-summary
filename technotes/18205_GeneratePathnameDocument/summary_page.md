# Tech Note: How to generate a pathname document in 4D

- **Asset ID:** 18205
- **Tech Note #:** 01-42
- **Published:** September 30, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Pascal Pradier, 4D, S.A.
- **Page URL:** https://kb.4d.com/assetid=18205
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_41-45_(SEP)/01-42_Generate_Pathname_Doc.hqx

## Overview

Pascal Pradier (4D, S.A.) reverse-engineers the 148-byte binary layout of a 4D Client pathname (.PTH) connection document and shows a MakeKey method to generate one programmatically, so automatic-connection files can be produced at install time instead of only by hand through the 4D Password editor.

## Key Points

- A .PTH pathname document is exactly 148 bytes: bytes 0-79 hold an 80-byte Pascal string with the server address (TCP/AppleTalk/IPX, or database-name+Tab+machine-name for DHCP setups), bytes 52-82 hold a 31-byte Pascal-string username, bytes 72-92 hold a 31-byte Pascal-string password, and the final integer at offset 146 is the network-component resource ID (1=AppleTalk, 2=TCP/Windows, 4=IPX, 29=TCP/Mac).
- The MakeKey method builds this blob with SET BLOB SIZE(148) followed by TEXT TO BLOB calls at the three Pascal-string offsets and an INTEGER TO BLOB call for the component ID, using either Macintosh byte ordering or PC byte ordering depending on the target platform parameter.
- A file built for one platform's byte ordering cannot be used on the other platform -- the note is explicit that this makes the resulting document platform-specific despite the identical field layout.
- The generated blob is written with BLOB TO DOCUMENT, then on Mac the file must additionally be tagged with SET DOCUMENT TYPE ("path") and SET DOCUMENT CREATOR ("4D+6", or a custom OEM signature) since Mac OS identified the file type by these codes rather than by extension alone; on Windows, the .PTH extension alone suffices.
- The technique lets a developer generate connection documents automatically (e.g., at install time, or for a compiled application whose production database name differs from its interpreted-mode name), avoiding the previous requirement to create them manually from the 4D Password Editor dialog in 4D Client.

## Featured Technology

- TEXT TO BLOB / INTEGER TO BLOB binary layout construction
- SET BLOB SIZE for fixed 148-byte .PTH file format
- Pascal-string encoding of address/user/password
- Platform-specific byte ordering (Macintosh byte ordering / PC byte ordering)
- BLOB TO DOCUMENT plus SET DOCUMENT TYPE/CREATOR for Mac file typing

## Historical Commentary

**Status:** Obsolete

This note reverse-engineers the binary layout of a 4D Client "pathname" (.PTH) file -- a 148-byte structure holding a Pascal-string server address, username, and password plus a network-component ID with platform-specific byte ordering -- and shows a MakeKey method to generate one programmatically instead of relying on the 4D Password editor's manual export, so pathname documents can be generated on the fly (e.g., per customer or per server address) rather than only by hand. This is a low-level, format-specific hack tied to the legacy 4D Client/Server pathname-document mechanism and classic Mac file type/creator codes; while 4D Server/Client connections and stored-connection documents still exist in some form, this exact binary format and manual construction technique is now of largely historical interest given how connection setup has evolved since 4D v6.5.

References to newer/updated information:
- 4D client/server connection settings and remote connection handling have evolved substantially since 4D v6.5; automatic pathname-document construction by hand-built blob is no longer a standard technique
- Classic Mac OS file type/creator codes (SET DOCUMENT TYPE/CREATOR) are irrelevant on modern macOS, which identifies files by extension/UTI instead
