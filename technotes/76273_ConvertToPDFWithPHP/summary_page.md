# Tech Note 11-06: Convert to PDF with 4D v12 and PHP

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** March 3, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76273
**Download:** https://kb.4d.com/DLTN/TN/2011/11-06_Convert_to_PDF.zip

## Proposition
This note addresses the historical difficulty of generating PDF documents identically on both Mac OS and Windows by leveraging 4D v12's newly embedded PHP interpreter together with the open-source fPDF library. It introduces fPDF (what it is and isn't, how it works, and its library functions), then shows how to call it dynamically from 4D via PHP wrapper methods. Two worked examples are provided: a list-and-detail report layout, and a two-page marketing brochure, both generated as real PDF files from 4D data. The note closes with a discussion of fPDF's limitations and possible next steps for further development.

## Key Points
- Frames cross-platform PDF generation as a longstanding pain point solved by embedding PHP in 4D v12.
- Introduces the fPDF library's capabilities and scope (what it is / is not).
- Shows how to execute dynamic PHP calls from 4D and wrap them for reuse.
- Worked Example 1: generating a list form and detail form as PDF documents.
- Worked Example 2: generating a two-page brochure as a PDF document.
- Discusses fPDF's limitations and suggests possible next steps for extending the approach.

## Featured Technology
- 4D v12 embedded PHP interpreter
- fPDF PHP PDF-generation library
- 4D-to-PHP wrapper methods for dynamic PDF document creation

## Best Practices Highlighted
- Wrap PHP library calls in reusable 4D methods to keep PDF-generation logic maintainable
- Evaluate library limitations up front (as this note does) before committing to a PDF-generation approach

## Context / Positioning
Published in 2011 right after 4D v12 added an embedded PHP interpreter, this note demonstrated a compelling practical use case — true cross-platform PDF generation — to drive adoption of the new PHP integration.

## Historical Commentary
**Status:** Partially Superseded

This PHP/fPDF bridge for PDF generation is now a legacy technique; 4D has since added native PDF generation and manipulation commands directly in the 4D language (including PDF creation from 4D Write Pro documents and dedicated PDF commands), removing the need for a PHP interpreter bridge for this specific task. The approach in this note still functions but is no longer the recommended path for cross-platform PDF generation in modern 4D applications.
