# Tech Note 16-05: Picture Collage in 4D

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** May 12, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77528
**Download:** https://kb.4d.com/DLTN/TN/2016/16-05_PictureCollageIn4D.zip

## Proposition
This note implements a Picture Collage component — a social-media-style photo grid layout — for classic 4D forms, using a reusable subform, dynamically duplicated picture objects, and JSON-based configuration, demonstrated inside a Car/Motorcycle inventory demo app.

## Key Points
- **Motivation:** replicate the picture-grid/collage UX popularized by Facebook, Instagram, and Pinterest inside a 4D application.
- **Subform-based component:** collage behavior is encapsulated in a reusable subform for easy integration into any host database.
- **Dynamic object duplication:** dsf_loadPictureCollage duplicates variable objects and computes layout positions to add pictures on the fly.
- **JSON-driven configuration:** collage layout/state is read from and serialized to JSON via dsf_getJSONSubformProperties.
- **Rich event wiring:** On Load, On Bound Variable Change, On Clicked, and On Getting Focus events drive the interactive behavior.
- **Demo app:** a Car/Motorcycle inventory database shows querying, selecting, and double-clicking collage items.

## Featured Technology
- 4D Subforms (classic Design Mode)
- JSON for component configuration
- Dynamic form-object duplication
- Variable and round rectangle form objects

## Best Practices Highlighted
1. Encapsulate visually complex, reusable UI patterns as subform-based components.
2. Drive component configuration through JSON rather than many discrete parameters for flexibility.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Obsolete

This component reflects the pre-web-UI era of 4D form design, where achieving a modern grid/collage layout required manually duplicating and positioning form objects rather than using CSS grid/flexbox. Contemporary 4D development would almost certainly implement this via a web area (HTML/CSS/JS) or a fully web-based front end, which handles responsive grid layouts natively and with far less custom code; the classic-form technique shown here is largely of historical interest.
