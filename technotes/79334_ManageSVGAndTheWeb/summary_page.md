# Tech Note 23-21: Managing SVG for images and the web within 4D (Revised on Nov 29th, 2023)

**Author:** Thomas SCHLUMBERGER, Technical Support Engineer, 4D SAS.
**Published:** November 28, 2023 | **Product/Version:** 4D v20.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79334
**Download:** https://kb.4d.com/DLTN/TN/2023/23-21_ManageSVGAndTheWeb_R2.zip

## Proposition
Modern displays span an enormous range of resolutions, DPI scaling, and light/dark themes, making fixed-resolution raster images increasingly impractical for forms and web content. This note explains why SVG — 4D's standard vector format since the retirement of 4D Draw — is a strong fit for this problem, and demonstrates how to construct, load, and manipulate SVG images inside a 4D application.

## Key Points
- **Historical context:** SVG replaced 4D Draw's proprietary vector format starting in 4D v11 SQL/v12, giving developers a standard, portable vector-drawing format.
- **Resolution independence:** As an XML-based format defining shapes mathematically rather than as pixels, SVG scales cleanly across UHD/4K/5K displays and DPI/scaling settings without quality loss.
- **Balanced pros/cons:** Benefits include editability (plain text/XML), interactivity/animation (JavaScript/CSS), accessibility (indexable, screen-reader compatible), and compactness; drawbacks include unsuitability for complex/photographic images, unprotected/openly readable content, script-based security risk in web areas, no built-in 4D SVG editor, and no default metadata support.
- **Dual display paths:** The sample database shows the same SVG (or HTML/GIF) file displayed simultaneously in a 4D Web Area (`WA OPEN URL`, with `WA ZOOM IN`/`WA ZOOM OUT`) and in a picture object (`READ PICTURE FILE`), noting some file types (e.g., HTML) can't render in a picture object.
- **External browser launching:** `OPEN URL` opens files in the platform default browser (Safari on macOS, Edge on Windows) or explicitly in Firefox, supporting cross-browser SVG compatibility checks.
- **Programmatic SVG generation:** The "Build 4D Logo SVG" button demonstrates generating SVG markup as text, writing it to a file with `File(...).setText()`, then loading it into both the web area and picture object.
- **ClassSVG color-editing example:** A custom class parses SVG/HTML/CSS text for unique hexadecimal colors ("#123456" pattern) via a `colorChanges` function and rewrites each occurrence via `colorChangesEach`, illustrating SVG's text-editability advantage.
- **Metadata handling:** `GET PICTURE METADATA`/`SET PICTURE METADATA` let developers add custom metadata (e.g., copyright `<desc>` tags) or strip sensitive metadata (date, camera model, location) from images served via the HTTP server.

## Featured Technology
- **SVG (Scalable Vector Graphics):** W3C-standard XML vector image format, the note's central subject.
- **4D Web Area commands:** `WA OPEN URL`, `WA ZOOM IN`/`WA ZOOM OUT` for rendering and navigating SVG/HTML content.
- **READ PICTURE FILE:** Loads SVG (and other image files) into a native 4D picture object.
- **GET PICTURE METADATA / SET PICTURE METADATA:** Native commands for reading/writing image metadata, including custom SVG `<desc>` content.
- **4D Class (ClassSVG):** Custom class demonstrating text-based hex color parsing and replacement across SVG/HTML/CSS files.
- **OPEN URL:** Launches external browsers (Safari/Edge/Firefox) to view generated or selected files.

## Best Practices Highlighted
1. Prefer SVG over raster images for UI elements/icons that must scale cleanly across varying DPI and resolution settings.
2. Be mindful of SVG's security exposure (scripts/CSS) specifically when rendering untrusted SVG content inside a web area.
3. Strip or control metadata on images served over HTTP to avoid leaking sensitive information such as location or camera details from raw photos.
4. For advanced color manipulation (including raster images or named-color conversion), consider established open-source libraries rather than building everything from scratch.

## Context / Positioning
Published for 4D v20.2, this note reflects the platform's ongoing accommodation of modern, high-DPI, theme-aware UI design and its long-standing web-area/HTML integration capabilities. It reinforces 4D's general strategy of embracing open, standard formats (SVG, HTML, CSS, JSON) over proprietary ones, complementing the broader project-mode/ORDA modernization direction seen in contemporaneous Tech Notes.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
