# Tech Note 09-01: Collapsible Lists with Web Area

## Proposition
Show how to combine the 4D Web Area, 4D HTML TAGS, and JavaScript/CSS to build interactive collapsible lists that a native 4D hierarchical list cannot achieve.

## Key Points
- Web Area (new in 4D v11 SQL Release 2) embeds a native browser (WebKit on Mac, ActiveX on Windows) directly in a 4D form.
- Forms hosting a Web Area must use "compositing mode" windows (e.g., via Open form window).
- An HTML template file with embedded 4D TAGS is processed with PROCESS HTML TAGS, producing an output HTML file shown via WA OPEN URL.
- 4D TAGS (#4DSCRIPT, #4DLOOP, #4DVAR) dynamically pull database values (Appointments grouped by Category) into the HTML template.
- A short JavaScript function toggles div visibility to create the expand/collapse behavior, styled with CSS.

## Featured Technology
- 4D Web Area (WebKit / ActiveX)
- 4D HTML TAGS and PROCESS HTML TAGS
- WA OPEN URL
- BLOB TO DOCUMENT / DOCUMENT TO BLOB
- HTML, CSS, JavaScript

## Best Practices Highlighted
- Use compositing-mode windows for reliable Web Area rendering.
- Separate the HTML template (with 4D TAGS) from the generated output file to keep content dynamic.
- Keep JavaScript interactivity minimal and purpose-built rather than over-engineered.

## Context/Positioning
Published shortly after 4D v11 SQL Release 2 introduced Web Area as a built-in browser control (replacing the older 4D Live Window plug-in), 4D wanted to showcase how developers could go beyond native form controls using familiar web technologies.

## Historical Commentary
This is a clever but heavyweight period workaround: generating static HTML via 4D TAGS templating to get UI richness unavailable in classic 4D forms. The underlying Web Area itself was later re-based on Chromium (replacing the WebKit/ActiveX engines named here), and modern 4D forms (v17+) offer CSS-stylable objects and object/collection-based list boxes that natively provide much of what this technique worked around. The specific 4D TAGS + PROCESS HTML TAGS templating pattern is largely obsolete, superseded by direct JavaScript bridge commands (WA EXECUTE JAVASCRIPT, WA EVALUATE JAVASCRIPT) for two-way interop without regenerating static HTML files.
