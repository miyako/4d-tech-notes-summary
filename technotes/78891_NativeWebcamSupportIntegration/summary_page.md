# Tech Note 22-06: Native Webcam Support and Integration

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** March 17, 2022 | **Product/Version:** 4D v19 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78891
**Download:** https://kb.4d.com/DLTN/TN/2022/22-06_WebCamIntegration.zip

## Proposition
With 4D's Web Area rendering engine upgraded to support HTML5 webcam APIs natively, this note replaces an older third-party-framework-based camera integration with a simpler, native approach and packages it as a reusable Photo Booth component.

## Key Points
- **Prerequisite**: 'Use embedded Web rendering engine' must be checked on the Web Area object; native camera support requires 4D v19R3+.
- **Core HTML5 APIs**: the `<video>` element plus JavaScript's `navigator.mediaDevices.getUserMedia()` handle the live stream, no third-party plugin needed.
- **Bidirectional control from 4D**: WA EXECUTE JAVASCRIPT FUNCTION lets 4D code trigger JS functions (flip video, switch camera, capture snapshot).
- **Multi-camera support**: `enumerateDevices()` lists all video sources, results are passed back to 4D via `$4d.loadVideoSources(...)`.
- **Snapshot capture**: an HTML5 canvas draws the current video frame and returns a base64 PNG, converted server-side to a 4D picture object with BASE64 DECODE / BLOB TO PICTURE.
- **snapShot component**: exposes `openPhotoBooth({mode; crop})` supporting single/multiple photo modes and optional automatic cropping, ready for drop-in reuse.

## Featured Technology
- Web Area (embedded rendering engine)
- HTML5 <video> / getUserMedia
- WA EXECUTE JAVASCRIPT FUNCTION
- HTML5 canvas snapshot capture
- snapShot / Photo Booth component

## Best Practices Highlighted
1. Always check 'Use embedded Web rendering engine' before relying on native HTML5 camera APIs in a Web Area.
2. Package reusable camera UI as a self-contained component (single exposed method) rather than duplicating HTML/JS per project.
3. Handle multiple video sources explicitly since users increasingly have more than one camera (built-in + external webcam).

## Context / Positioning
This note reflects 4D's strategy of continuously modernizing its embedded Web Area engine so that native browser capabilities (HTML5 media APIs) become directly usable inside 4D applications, reducing developers' reliance on external frameworks and keeping 4D competitive with contemporary web/mobile app expectations.

## Historical Commentary
**Status:** Still Relevant

This approach remains current: the embedded Web Area rendering engine and HTML5 getUserMedia/canvas APIs are still the standard way to do camera capture in 4D, and no native 4D command has since replaced this JS-based approach. It is a clean improvement over the 2015-era technique it explicitly supersedes. Developers building similar features today would still follow essentially this same pattern, possibly adjusting for browser API changes (e.g., stricter permissions/HTTPS requirements) that have evolved industry-wide since 2022.
