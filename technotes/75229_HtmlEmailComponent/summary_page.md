# Tech Note 09-12: HTML Email Component

**Author:** Thomas Maul, 4D Germany
**Published:** March 25, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75229
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_09-12_(MAR)/09-12_EMail_Component.zip

## Proposition
Provides a reusable component that displays, WYSIWYG-edits (via an embedded TinyMCE JavaScript editor inside a 4D Web Area), and sends HTML-formatted email from within a 4D database.

## Key Points
- **Display with privacy control:** hides remotely-linked images by default (a spam-tracking mitigation) with a command to reveal them on user request.
- **Enclosure handling:** `EMail_GetEnclosureList` retrieves expanded attachment files from a temporary folder for saving to disk.
- **WYSIWYG editing via TinyMCE:** embeds the TinyMCE 3.2.1 JavaScript editor inside a Web Area; requires careful event sequencing (`On Load`, `On Resize`, `On Timer`, `On End URL Loading`) because JS cannot run before the page fully loads.
- **Sending mail:** `EMail_Send` embeds local images as attachments and relays through an SMTP server (with optional auth) via 4D Internet Commands.
- **Extensive customization:** upgrade TinyMCE independently, add UI languages, edit the bridging HTML template, and localize component text via XLIFF.
- **Unicode Wrapper component:** lets the library be called (via pointers instead of direct text params) from 4D host applications still running in non-Unicode mode.
- **Licensing:** TinyMCE is LGPL; the component ships its license and source to remain compliant.

## Featured Technology
- 4D Web Area displaying/editing HTML email via embedded WebKit (Mac) / MS IE (Windows)
- TinyMCE 3.2.1 JavaScript rich-text editor embedded via WA EXECUTE JAVASCRIPT FUNCTION
- SMTP sending via 4D Internet Commands (EMail_Send)
- XLIFF-based component localization; Unicode wrapper component for non-Unicode hosts

## Best Practices Highlighted
1. Don't call JavaScript before the Web Area page has finished loading; use `On End URL Loading`/`On Load` events instead of assuming immediate readiness.
2. Route all editor-feature calls through the HTML template's JavaScript functions rather than calling TinyMCE features directly, so the editor framework can be swapped later.
3. Respect and redistribute the TinyMCE LGPL license terms (include source and license text) when embedding third-party JS libraries.
4. Provide a Unicode-compatibility wrapper so a component can serve both Unicode and non-Unicode host databases without rewriting calling code.

## Context / Positioning
Written by 4D Germany as a practical, end-to-end component for HTML email functionality — a common but nontrivial feature request — bundling both a ready-to-use component and a sample database.

## Historical Commentary
**Status:** Partially Superseded

The note's core technique — driving an embedded JavaScript rich-text editor inside a 4D Web Area and sending via SMTP — is conceptually still sound, but its implementation is tied to the era's Web Area engine (WebKit on Mac, MS Internet Explorer on Windows) and a decade-old TinyMCE 3.x build.

4D's Web Area component has since moved to a modern, unified Chromium-based rendering engine, making the platform-specific IE/WebKit caveats obsolete, and 4D is now fully Unicode-native, eliminating the need for the described Unicode Wrapper component. A developer wanting this functionality today would use current Web Area APIs with an actively maintained editor library rather than this specific implementation.
