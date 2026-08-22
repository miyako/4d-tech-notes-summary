# Tech Note 18-06: 4D Mobile Generate PDF From HTML

**Author:** (not specified in available text)
**Published:** April 24, 2018 | **Product/Version:** 4D Mobile v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77989
**Download:** https://kb.4d.com/DLTN/TN/2018/18-06_4DMobilePDFfromHTML.zip

## Proposition
Demonstrates generating PDF documents from HTML content using Wakanda Enterprise's Print service and REST API within a 4D Mobile solution, covering server-side generation, client-side REST calls, browser download, and uploading the resulting PDF back into 4D.

*Note: the extracted text for this note consists of the sample database's Readme file (setup/run instructions) rather than the full narrative PDF; the summary below reflects what is documented in that Readme.*

## Key Points
- **Cross-stack dependency:** requires 4D v16 R5+, Wakanda Enterprise 2.4.0+, and a modern Safari/Chrome browser — 4D Mobile solutions ran on top of the separate Wakanda server platform.
- **Licensing requirements:** needs a 4D Mobile Server Expansion (or standalone fallback) plus a Wakanda Enterprise license (trial key provided with the demo).
- **Server-side PDF generation:** a backend `Generate_PDF.js` method uses the Wakanda Print service to render an HTML file (e.g., invoice.html) to PDF on the server.
- **REST API for PDF generation:** a `/print?report=...&output=...` REST endpoint exposes the same capability to remote/client callers, with options like `delay` and `copies`.
- **Client-side demo pages:** separate browser pages demonstrate downloading a generated PDF, submitting custom HTML for conversion, and uploading a generated PDF back into 4D.

## Featured Technology
- 4D Mobile
- Wakanda Enterprise / Wakanda Studio / Wakanda Server
- Wakanda Print service
- REST API
- 4D Web Server

## Best Practices Highlighted
(Not clearly documented in the available Readme-level text; the full technical note likely contained implementation guidance not captured in this extraction.)

## Context / Positioning
This note is squarely part of 4D's mid-2010s "4D Mobile" initiative, which paired classic 4D with the Wakanda JavaScript server platform to expose data and services (including this print/PDF service) to REST clients and eventually native mobile apps. It represents 4D's pre-ORDA, pre-Qodly approach to web/mobile-facing services, relying on a second product (Wakanda) rather than 4D's own built-in REST/web server capabilities.

## Historical Commentary
**Status:** Obsolete

Both 4D Mobile and the underlying Wakanda Enterprise platform have been fully discontinued by 4D; Wakanda Studio, the Wakanda Server, and its Print service no longer exist as supported products, so this Tech Note's exact implementation cannot be reproduced with current 4D software. 4D Mobile itself was superseded first by ORDA/REST-based responsive web development and later by tools like Qodly for building modern client applications against 4D data.

The general idea — generating PDF documents from HTML content via a server-side rendering service and exposing that as a REST endpoint — remains a valid and common pattern in web development broadly, but a 4D developer wanting this capability today would need to use an entirely different toolchain (e.g., a headless-browser-based PDF rendering service, a third-party library, or 4D's own evolving print/report commands) rather than anything shown in this note.
