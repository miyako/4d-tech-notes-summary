# Tech Note 11-08: Branding Web Apps: Customizing CSS primer

**Author:** Rudolf Psenicnik, Technical Services Team Member, 4D Inc.
**Published:** March 17, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76283
**Download:** https://kb.4d.com/DLTN/TN/2011/11-08_BrandingWebApps.pdf

## Proposition
This note is a primer for developers who want to brand a 4D Web 2.0 Pack web application — matching a company's colors, logo, or visual identity — without touching its underlying HTML markup or JavaScript logic. It breaks down the anatomy of a 4D web app (HTML, JavaScript, CSS) and the locations where CSS can live (inline, in the HEAD section, or in an external file), then walks through techniques for modifying existing styles and adding custom CSS files/overrides in each of those three locations. The emphasis throughout is on non-intrusive customization: changes that persist safely across future 4D Web 2.0 Pack updates rather than editing generated/shipped files directly.

## Key Points
- Breaks 4D web apps into three layers: HTML markup (semantics), JavaScript (logic), and CSS (style).
- Enumerates the three places CSS can be defined: inline, in the page HEAD section, and in external stylesheet files.
- Shows how to modify existing CSS styles safely for each of the three locations.
- Shows how to add custom/override CSS files without touching original app assets.
- Frames all techniques around being non-intrusive and update-safe.
- Positions CSS customization as the correct branding layer, leaving HTML/JS untouched.

## Featured Technology
- 4D Web 2.0 Pack web applications
- CSS customization (inline, HEAD section, external file)
- Non-intrusive branding overrides surviving web app updates

## Best Practices Highlighted
- Separate branding customizations into external/override CSS files rather than editing shipped markup
- Avoid touching HTML/JavaScript when only visual branding changes are needed, to reduce update-breakage risk

## Context / Positioning
Published for the 4D Web 2.0 Pack in 2011, at a time when 4D-generated web applications had a fairly fixed generated HTML/CSS structure, so developers needed guidance on safely re-skinning that output for client branding requirements.

## Historical Commentary
**Status:** Obsolete

This note is tied to the 4D Web 2.0 Pack, an older 4D web application technology; the general CSS-layering principle (external/override stylesheets, don't touch generated markup) is timeless and still good practice, but the specific product (Web 2.0 Pack) it targets has been superseded by 4D's modern web application and REST/ORDA-based approaches, and CSS customization today is more commonly done directly within custom HTML/CSS assets or Qodly Studio-based UI rather than overriding a fixed 4D-generated web app shell.
