# Tech Note 24-01: Generating Barcodes and QR Codes with 4D View Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 23, 2024 | **Product/Version:** 4D View Pro v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79366
**Download:** https://kb.4d.com/DLTN/TN/2024/24-01_VPBarAndQRCode.zip

## Proposition
Barcodes and QR codes are compact, scannable ways to encode data for inventory, ticketing, badges, and promotional use, and 4D View Pro exposes SpreadJS barcode formula functions that can render them — but using raw spreadsheet formulas with many positional parameters is cumbersome for application logic. This note packages that capability into a clean, class-based, one-line image generator that returns native 4D Pictures.

## Key Points
- **SpreadJS barcode functions:** 4D View Pro exposes formula functions like `BC_QRCODE`, `BC_EAN13`, `BC_CODE128`, `BC_PDF417`, `BC_DataMatrix`, etc., each accepting a value plus format-specific styling parameters (color, quiet zones, label font/position).
- **Thirteen-class hierarchy:** A `_VP_Barcode_Base` class holds properties/logic shared by all formats; `_VP_Barcode_Subbase` extends it for 1D-format label properties; eleven concrete classes (e.g., `VP_QRCode`, `VP_Barcode128`, `VP_Barcode_EAN13`) implement each specific format.
- **Hidden helper properties:** Prefixing internal object-notation items with an underscore hides them from the method editor's autocomplete, keeping the public class API clean.
- **Offscreen View Pro rendering:** `VP Run offscreen area` and the `On VP Ready` event let a View Pro document run without a visible form, so image generation needs no UI.
- **JavaScript extraction pipeline:** `WA Evaluate JavaScript`/`WA EXECUTE JAVASCRIPT FUNCTION` run against the (offscreen) View Pro area format the sheet and extract the rendered barcode image out of the spreadsheet cell.
- **One-line usage:** `cs.VP_QRCode.new("Hello World").generateImage()` returns a `Picture` variable directly, with optional attribute overrides done via simple property assignment before calling `generateImage()`.
- **Modularity and portability:** Because each format is its own class, only the needed classes need to be copied into a target database, and new SpreadJS barcode formats can be added following the same subclassing pattern.
- **Practical caveats:** Some formats have unvalidated value-length requirements (e.g., fixed digit counts) that will render as `#VALUE!` if violated, and very large generated images can exceed 4D text-size limits during base64 extraction, resulting in blank images.

## Featured Technology
- **4D View Pro / SpreadJS barcode functions:** Underlying spreadsheet formulas that actually render each encoded image format.
- **4D Classes:** Base/sub-base/concrete class hierarchy providing a modular, inheritance-based API.
- **Offscreen Web/View Pro Areas:** `VP Run offscreen area`, `On VP Ready` — run View Pro logic without a visible UI.
- **4D Web Area JavaScript commands:** `WA Evaluate JavaScript`, `WA EXECUTE JAVASCRIPT FUNCTION` — bridge to SpreadJS internals for formatting/extraction.
- **Picture data type:** Native 4D type used to hold and return the generated encoded image.

## Best Practices Highlighted
1. Use a base/sub-base class hierarchy to avoid duplicating shared properties (value, color, quiet zones, label styling) across many similar barcode formats.
2. Hide internal helper properties/functions with an underscore prefix so the public class surface stays simple for consumers.
3. Prefer offscreen View Pro areas for programmatic image generation so the feature doesn't require displaying a form to the user.
4. Validate format-specific input constraints (e.g., required digit counts) explicitly, since 4D View Pro will silently render `#VALUE!` rather than raise a catchable error.

## Context / Positioning
This note extends 4D's investment in 4D View Pro (its SpreadJS-based spreadsheet/reporting component) by exposing a specialized spreadsheet capability as a general-purpose, reusable native feature — reflecting a broader pattern in 4D Tech Notes of turning View Pro/SpreadJS internals into portable, object-oriented utility classes that any 4D application can adopt without extra licensing beyond View Pro itself.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
