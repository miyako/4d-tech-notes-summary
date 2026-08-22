# Tech Note 09-46: QuickTime and YouTube movies in Web Area

**Author:** Joe Resuello, Technical Marketing Engineer, 4D Inc.
**Published:** December 11, 2009 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75969
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_46-48_(DEC)/09-46_WebAreaVideos.zip

## Proposition
This note demonstrates controlling embedded QuickTime and YouTube videos from a 4D Web Area using each platform's public JavaScript API in combination with 4D's Web Area JavaScript injection functions, extending an earlier series of Web Area technical notes.

## Key Points
- Builds on prior Web Area notes covering **mashups**, **extending the Web Area as a form**, and **JavaScript injection**.
- **QuickTime section**: gets a reference to an embedded movie via its public JavaScript API and wires up Play, Pause, and Volume controls on the 4D form; some browsers (e.g., IE) may show harmless load errors.
- **YouTube section**: explains the Flash-based **SWFObject** embed, how to obtain a reference to the video, and wires up equivalent Play/Pause/Volume controls.
- Running the **YouTube demo requires 4D to be running as a web server** with an appropriate license; otherwise a 404-type error appears.
- Demo dialog uses a tab control to switch between the QuickTime and YouTube pages.

## Featured Technology
- 4D Web Area JavaScript injection functions
- QuickTime JavaScript API
- YouTube SWFObject / Flash-embedded JavaScript API

## Best Practices Highlighted
1. Verify 4D's web-server license is active before testing Web-Area demos that depend on serving local pages.
2. Anticipate and tolerate benign browser warnings (e.g., IE's QuickTime page errors) rather than treating them as fatal bugs.
3. Reuse each platform's own public JavaScript API rather than attempting to control embedded media through unsupported means.

## Context / Positioning
Published as a refinement of 4D's Web Area JavaScript-injection technique series, applying it to the specific and popular use case of controlling embedded video playback from native 4D form controls.

## Historical Commentary
**Status:** Obsolete

This note shows how to control embedded QuickTime and Flash-based YouTube videos from a 4D Web Area using each platform's public JavaScript API and 4D's Web Area JavaScript injection functions.

Both the QuickTime plugin and Flash/SWFObject-based YouTube embeds it relies on have since been discontinued (QuickTime plugin support removed from browsers years ago; YouTube itself moved entirely away from Flash to HTML5 video around 2015, and Adobe Flash was fully retired in 2020-2021), making the specific embedding techniques in this note non-functional today. The general pattern of injecting JavaScript into a 4D Web Area to control an embedded web page remains valid and is still used, but must now target modern HTML5 video APIs (e.g., the YouTube IFrame Player API) instead.
