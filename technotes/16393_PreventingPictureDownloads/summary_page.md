# Tech Note: Preventing Web Users from Downloading Pictures

- **Asset ID:** 16393
- **Tech Note #:** 01-40
- **Published:** August 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Chiheb Nasr, 4D S.A.
- **Page URL:** https://kb.4d.com/assetid=16393
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_36-40_(AUG)/01-40_Preventing_Picture_Downloads.hqx

## Overview

Chiheb Nasr (4D S.A.) demonstrates a two-layer, explicitly imperfect scheme for discouraging (not truly preventing) users from downloading web-published images: JavaScript right-click interception on the browser side, plus a time-windowed 4DACTION image URL on the 4D side that rejects delayed/replayed requests.

## Key Points

- The note opens with an explicit disclaimer that no combination of these techniques can fully stop image copying -- drag-and-drop, browser cache inspection, and screenshots remain available to a determined user -- and points to digital watermarking as the only real way to protect and trace copyrighted images.
- A JavaScript disableclick function is attached to every image's onmousedown handler (via a loop over document.images, or document.onmousedown for IE's document.all model) and shows an alert("This picture cannot be downloaded...") instead of allowing the browser's native right-click Save Image menu; Mac users are told the equivalent gesture is Control-click.
- Images are served via a 4DACTION URL (e.g. /4daction/Web_Display/<timestamp>) embedded in the page's <img src="<!--4dvar Webphoto-->"> tag rather than as a static file reference, generated fresh with a Current time-based token each time On Web Connection serves demo.shtm.
- The Web_Display method extracts the embedded timestamp from $1, compares it to the current time, and sends the real picture (converted with PICTURE TO GIF and streamed via SEND HTML BLOB) only if the gap is under roughly 1-2 seconds; otherwise it sends error.html instead, defeating attempts to reuse or replay a copied image URL after the fact.
- This combination targets casual right-click saving and stale/replayed direct-URL access specifically, while acknowledging it does nothing against screenshotting or cache-based extraction of the still-displayed image.

## Featured Technology

- JavaScript onmousedown/right-click interception (disableclick handler)
- 4DACTION-served image delivery (SEND HTML BLOB of PICTURE TO GIF)
- Time-window URL replay protection (comparing Current time to an embedded timestamp)
- 4dvar tag for embedding a dynamic image-fetch URL in an <img> tag

## Historical Commentary

**Status:** Obsolete

Chiheb Nasr (4D S.A.) shows a two-layer scheme to discourage casual downloading of images served by 4D's web server: a browser-side JavaScript handler that blocks right-click/context-menu access to <img> elements, and a server-side 4D check that compares the current time to a timestamp embedded in the 4DACTION image-fetch URL, rejecting requests made too long after the page was generated (to defeat users who copy the raw image URL from View Source). The note is explicit up front that none of this actually prevents image copying (screenshots, cache inspection, drag-and-drop all still work), and today both halves of the technique are essentially obsolete: browsers have moved away from relying on right-click-blocking JavaScript as any kind of protection, and real image protection now relies on watermarking, DRM, or simply accepting that browser-rendered images can always be captured.

References to newer/updated information:
- Right-click/context-menu-blocking JavaScript is now a well-known, easily bypassed anti-pattern rather than a real protection technique
- Modern approaches to protecting web images rely on watermarking, licensing/DRM, or server-side access control rather than client-side click interception
