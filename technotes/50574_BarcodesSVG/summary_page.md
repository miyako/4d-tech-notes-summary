# Tech Note 08-27: Printing Barcodes using 4D v11 SQL and SVG

**Author:** Thomas Maul, General Manager, 4D Germany
**Published:** July 30, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_25-29_(JUL)/08-27_Barcodes.zip

## Proposition
This Technical Note updates the barcode-generation technique documented in TN 05-08 (4D v9 era) to take advantage of SVG (Scalable Vector Graphics) support newly available in 4D v11 SQL. The SVG-based approach yields faster barcode rendering and superior print quality compared to the older 4D Chart method.

## Key Points
- **SVG replaces 4D Chart:** The shift from 4D Chart to SVG for barcode encoding represents a performance and quality leap; barcodes render faster and print with higher fidelity.
- **Component distribution model:** The solution is packaged as a compiled component (Barcode.4dbase) installable into the 4D Components folder, allowing database-agnostic reuse without exposing source code.
- **Broad barcode format support:** The component encodes 12 barcode formats, including the ubiquitous 1D standards (Code 128, EAN-8/13, UPC-A/E) and supplemental codes used in retail and logistics.
- **Code 128 'g' bug fix:** The component fixes a rendering bug where the lowercase letter 'g' was incorrectly encoded in Code 128 barcodes, a common issue when encoding part numbers or product codes with mixed case.
- **Compatibility Mode vs. Unicode Mode:** By default, the component compiles in Compatibility Mode for broad compatibility; developers targeting Unicode-enabled 4D v11 SQL databases must recompile the source with Unicode Mode enabled.
- **Source and compiled versions provided:** The download includes both a source Matrix Database (for modification/study) and a pre-compiled component (for drop-in deployment).

## Featured Technology
- SVG (Scalable Vector Graphics) standard
- 4D v11 SQL barcode generation API
- 4D Components architecture
- Barcode encoding standards: Code 128, EAN, UPC, Industrial 2 of 5
- Compiled vs. interpreted database modes

## Historical Context
Published in summer 2008 as 4D v11 SQL was establishing itself as the successor to v9, this update reflects the maturation of 4D's graphics capabilities. SVG was a natural choice for barcode encoding—clean, scalable, and natively supported. The component model was 4D's primary mechanism for distributing reusable libraries before the Package Manager arrived (v18, 2018). Barcode generation itself, while remaining a perennial requirement in business software, has since been increasingly outsourced to external services or JavaScript libraries, reducing the pressure for server-side 4D barcode solutions.

## Historical Commentary
**Status:** Historical Interest Only

The technical approach—SVG-based barcode generation packaged as a 4D component—is sound and remains functional in 4D v11 SQL databases if one still has them. However, the broader ecosystem has shifted: modern 4D development favors 4D View Pro (v18+) for graphics work, and barcode generation itself is increasingly handled by external APIs (e.g., Barcode.js, zxing, or cloud services like Cloudinary) or delegated to client-side JavaScript libraries. The specific formats (Code 128, EAN-13, UPC-A) are timeless standards, but their implementation within a legacy 4D server component is no longer a recommended pattern. A developer today seeking barcode functionality would either integrate an external library or use a modern web-based barcode generator rather than maintain server-side 4D code for this purpose.
