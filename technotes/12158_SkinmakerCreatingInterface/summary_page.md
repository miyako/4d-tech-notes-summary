# Tech Note: Skinmaker: Creating an Interface

- **Asset ID:** 12158
- **Tech Note #:** 01-5
- **Published:** January 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Gilles Mellot
- **Page URL:** https://kb.4d.com/assetid=12158
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_01-05_(JAN)/01-05_Skinmaker.hqx

## Overview

Gilles Mellot (4D S.A.) presents the SkinMaker example database, which builds a library of reusable form-background "skin" templates rather than static images, so a single defined interface skin can be dynamically composited to fit any form size at runtime and dropped into other custom databases with no code changes.

## Key Points

- Each skin is built from nine source pictures: four corners (`P_TR_Corner`, `P_TL_Corner`, `P_LR_Corner`, `P_LL_Corner`), four borders (`P_Left`, `P_Right`, `P_Top`, `P_Bottom`), and a center fill (`P_Center`) — a classic nine-slice composition approach.
- `Skin_VerifSize` computes the minimum overall picture size needed by reading each corner/border picture's `◊Width`/`◊Height` via `F_PictSize`, ensuring the assembled result matches or exceeds the target form's dimensions without distortion.
- Templates are saved by packing all nine picture variables sequentially into a single BLOB with repeated `VARIABLE TO BLOB(...;$blob;$offset)` calls, then storing that BLOB in a custom resource named "skin" via `SET RESOURCE`/`SET RESOURCE NAME`, keyed by a skin ID and name array.
- `Skin_Fill` reverses the process: `GET RESOURCE("skin";$1;$blob;◊LocalRessFile)` followed by matching `BLOB TO VARIABLE` calls restores the nine pictures, then `SET PICTURE TO LIBRARY(P_Center;1;"BackGround")` (or `REMOVE PICTURE FROM LIBRARY` if empty) loads the fill picture into the Picture Library for display.
- The final composited border/fill pictures are built using picture concatenation (`|`) and tiling logic that steps across the target width/height in increments of the border picture's own dimension, handling a final partial-width remainder tile with a computed scale coefficient.
- The `Test` object method opens a window sized to the user-specified Form Width/Height and immediately displays the composited skin via `Skin_Calc` and a `DIALOG([Interface];"INT_Skin")` call, letting a developer preview a skin at any target size before adopting it.

## Featured Technology

- Picture operators (concatenation |, division / for tiling)
- VARIABLE TO BLOB / BLOB TO VARIABLE
- SET RESOURCE / GET RESOURCE (Skin resource storage)
- SET PICTURE TO LIBRARY / REMOVE PICTURE FROM LIBRARY
- Nine-slice picture composition (4 corners, 4 borders, center fill)
- Dynamic form background templates (Skin_Fill / Skin_Calc)

## Historical Commentary

**Status:** Obsolete

Gilles Mellot's note shows a nine-slice interface-skinning technique -- four corner pictures, four border pictures, and a center fill, tiled and concatenated with 4D's picture operators into a single composite background matched to a form's exact size -- with each template persisted as a Blob in a custom "Skin" resource and reloaded via Skin_Fill/Skin_Calc. The underlying nine-slice composition idea is still a recognizable UI technique, but the specific implementation is deeply tied to obsolete Mac OS resource forks (SET RESOURCE/GET RESOURCE) and the classic Picture Library, both of which have been superseded by 4D's modern object/JSON-based settings storage and CSS-driven form styling, making this note's mechanics obsolete for current development even though the visual concept it automates persists in modern UI frameworks.

**References to newer/updated information:**
- 4D's classic resource-fork storage (SET RESOURCE/GET RESOURCE) is obsolete; modern 4D applications store structured data like this in objects/JSON or preference files instead
- Modern 4D form styling relies on CSS-based theming and form object properties rather than manually composited nine-slice picture backgrounds built from Picture Library entries
