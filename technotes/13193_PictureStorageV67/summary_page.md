# Tech Note: Picture Storage

- **Asset ID:** 13193
- **Tech Note #:** 01-18
- **Published:** April 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=13193
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_16-20_(APR)/01-18_Picture_Storage.hqx

## Overview

Jamras Komoncharoensiri (4D, Inc.) documents 4D v6.7's new and renamed picture-handling commands -- several promoted directly from the old v6.5 ACI Pack plug-in -- and demonstrates their use through the "Pics Storage" example database, which supports importing, thumbnailing, viewing, resizing, moving, and exporting pictures stored in a 4D database.

## Key Points

- Several 4D v6.5/ACI Pack commands were renamed and folded into core 4D v6.7 (e.g., `PIC TO GIF` became `PICTURE TO GIF`), alongside new commands `PICTURE TO BLOB`, `BLOB TO PICTURE`, `WRITE PICTURE FILE`, `READ PICTURE FILE`, `PICTURE TYPE LIST`, and `CREATE THUMBNAIL`.
- QuickTime 4 or later must be installed for conversion commands like `WRITE PICTURE FILE`/`READ PICTURE FILE` to handle formats beyond PICT and GIF; the note lists QuickTime's standard format codes (PICT, PICS, GIFf, PNGf, TIFF, 8BPS, SGI, BMPf, JPEG, PNTG).
- The Pics Storage Thumbnail panel displays up to 21 pictures at a time with "Prev 21"/"Next 21" navigation, and double-clicking a thumbnail opens a full-size viewer window with zoom and directional-pan tools.
- Moving a displayed picture uses 4D's picture arithmetic operators — `vPicFrame+50`/`vPicFrame-50` for horizontal moves and `vPicFrame/40`/`vPicFrame/(-40)` for vertical moves — and requires the picture variable's display format be set to "On Background".
- Resizing uses the `*` operator with fixed ratios (e.g., `vPicFrame*(4/3)` to enlarge 33.33%, `vPicFrame*0.75` to reduce 25%) chosen so the picture can always be reverted to its original size.
- Exporting supports PICT/JPEG/BMP/TIFF directly via `WRITE PICTURE FILE`, while GIF requires an extra step — converting with `PICTURE TO GIF` into a BLOB and writing it out with `BLOB TO DOCUMENT` — since GIF is limited to 256 colors and 4D optimizes the palette from the source picture; saving a picture at its exact on-screen size uses a clipboard round-trip (`SET PICTURE TO CLIPBOARD` / `GET PICTURE FROM CLIPBOARD`).

## Featured Technology

- PICTURE TO GIF / PICTURE TO BLOB / BLOB TO PICTURE
- WRITE PICTURE FILE / READ PICTURE FILE (QuickTime-based conversion)
- PICTURE TYPE LIST / CREATE THUMBNAIL
- Picture arithmetic operators (+/-, /, *) for move and resize
- SET PICTURE TO CLIPBOARD / GET PICTURE FROM CLIPBOARD
- Pics Storage example database (import, thumbnail, export)

## Historical Commentary

**Status:** Superseded

Jamras Komoncharoensiri's note documents 4D v6.7's newly consolidated picture-handling commands (renamed and expanded from the old 6.5 ACI Pack, e.g. PIC TO GIF becoming PICTURE TO GIF), QuickTime's role in converting between formats like JPEG/PNG/BMP/TIFF, and the Pics Storage example database's import/thumbnail/export/resize/move features built on 4D's picture arithmetic operators. 4D's picture-handling APIs and storage engine have been substantially overhauled since v6.7 -- including broader native format support, list box picture columns, and no dependency on QuickTime -- making this note's specific v6.7-era commands and QuickTime-conversion caveats superseded, even though storing and displaying images in a 4D database remains a routine requirement today.

**References to newer/updated information:**
- 4D's picture commands and picture field storage have been substantially updated since v6.7, dropping the QuickTime dependency for format conversion and adding broader native format support
- List box picture columns and other modern form objects now offer more built-in ways to display and manage stored pictures than the v6.7-era commands and manual clipboard tricks shown here
