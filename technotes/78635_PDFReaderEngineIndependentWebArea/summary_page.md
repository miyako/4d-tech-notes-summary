# Tech Note 21-02: 4D PDF Reader Using Engine-Independent Web Area

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** January 25, 2021 | **Product/Version:** 4D v18 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78635
**Download:** https://kb.4d.com/DLTN/TN/2021/21-02_PDFReader.zip

## Proposition
Traditionally, viewing PDFs inside a 4D Web Area required the host OS's web engine to have a PDF plugin installed and configured — an unreliable dependency across different workstations. This Tech Note demonstrates a self-contained alternative: convert each PDF page to a PNG with the open-source Xpdf `pdftopng` tool, then render the PNGs as paginated HTML inside a standard Web Area, with no external viewer dependency.

## Key Points
- **PNG rasterization via Xpdf**: `pdftopng`, invoked with `LAUNCH EXTERNAL PROCESS`, converts each PDF page into a numbered PNG file.
- **Environment setup**: `SET ENVIRONMENT VARIABLE("_4D_OPTION_CURRENT_DIRECTORY";...)` ensures the external process resolves relative paths correctly.
- **HTML templating**: An HTML template using 4D's `#4deval`/`#4dloop`/`#4dtext` tags is resolved per-document via `PROCESS 4D TAGS`, then written to disk with `TEXT TO DOCUMENT`.
- **Web Area rendering**: The generated HTML is loaded with `WA OPEN URL`, and page navigation is done by appending a `#pageNumber` anchor to the URL.
- **Thumbnail navigation**: A list box (Picture array data source) built from scaled-down PNGs (`READ PICTURE FILE`, `TRANSFORM PICTURE`) lets users jump to any page.
- **Per-session isolation & cleanup**: Each opened PDF gets a unique UUID-named PNG folder so multiple instances can run concurrently; `deleteViewedPDF` removes it on close to prevent disk bloat.
- **Read-only limitation**: Because the PDF becomes static images, interactive PDF features (links, form fields, signatures) are lost.
- **Ships as an installable component**: exposes `openPDFReader`, `loadPDFInWA`, and `deleteViewedPDF` for integration into any host application.

## Featured Technology
- LAUNCH EXTERNAL PROCESS / SET ENVIRONMENT VARIABLE
- Xpdf `pdftopng` (third-party open-source CLI)
- PROCESS 4D TAGS / Document to text / TEXT TO DOCUMENT
- WA OPEN URL (classic Web Area)
- READ PICTURE FILE, PICTURE PROPERTIES, TRANSFORM PICTURE, APPEND TO ARRAY
- 4D component build & distribution

## Best Practices Highlighted
1. Isolate generated assets per PDF instance in a uniquely named folder to support multiple concurrent viewers.
2. Always clean up temporary PNG folders on unload to avoid unbounded disk usage.
3. Package reusable UI features (like a PDF reader) as an installable 4D component with a small, well-documented public API.

## Context / Positioning
Published just before 4D's Web Area engine was modernized, this note reflects a period when 4D developers had to work around inconsistent, platform-dependent PDF rendering support in the underlying web engine. It exemplifies 4D's Tech Note style of providing pragmatic, dependency-free workarounds using existing 4D commands plus a lightweight open-source helper tool, packaged as a ready-to-use component — a common pattern for extending 4D's built-in capabilities during this period.

## Historical Commentary
**Status:** Partially superseded

This workaround was clever for its time but its underlying justification has significantly weakened: 4D's Web Area was subsequently rebuilt on a bundled Chromium engine (introduced across v19/v20-era releases), which reliably renders PDFs natively without any plugin dependency, making the "engine-independent" rasterize-to-PNG approach largely unnecessary for basic PDF display use cases today. The general techniques shown — shelling out to an external CLI tool via `LAUNCH EXTERNAL PROCESS`, templating HTML with `PROCESS 4D TAGS`, and packaging functionality as a component — remain valid and still commonly used patterns in 4D development, even if this specific PDF-viewing use case is now more simply solved by pointing a modern Web Area directly at the PDF file or by using `4D.File`/native OS handling. Developers today building a PDF viewer would typically first try a plain Web Area with a `file://` URL to the PDF before resorting to the rasterization approach described here.
