# Tech Note 14-17: Web Area Callbacks in v14

**Author:** Timothy Aaron PENNER, Technical Services Engineer, 4D Inc.
**Published:** November 13, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77177
**Download:** https://kb.4d.com/DLTN/TN/2014/14-17_WebAreaCallbacks.zip

## Proposition
This note covers the JavaScript-to-4D callback bridge introduced in 4D v14: previously a Web Area could only be driven from 4D code, but v14 (with the WebKit rendering engine enabled) exposes a `$4d` object to page JavaScript that can invoke 4D methods and receive results back through developer-defined callback functions, illustrated with a jQuery accordion menu example.

## Key Points
- **Prior limitation:** before v14, 4D-to-WebArea communication (`WA EXECUTE JAVASCRIPT FUNCTION`, `WA EVALUATE JAVASCRIPT`) was one-directional; calling 4D from JavaScript required awkward workarounds like URL filtering.
- **New in v14:** a direct `$4d` JavaScript object lets page-side JS call 4D methods and get results, but only when the WebKit rendering engine is enabled — it must be explicitly turned on via the Property List.
- **Multiple callback styles supported** for specifying how a JavaScript function is invoked to receive the 4D method's response.
- **Worked example:** a jQuery accordion menu driven by 4D data via the callback mechanism.
- **Deployment considerations:** guidance on when (and when not) to enable the Web Inspector in production, since it also exposes access to 4D methods.
- **Stack size warning:** explicitly cautions against undersizing the process stack when using this feature, to avoid runtime issues.

## Featured Technology
- 4D Web Area (WebKit engine)
- $4d JavaScript object
- WA EXECUTE JAVASCRIPT FUNCTION / WA EVALUATE JAVASCRIPT
- JavaScript-to-4D callback mechanism

## Best Practices Highlighted
1. Explicitly enable the WebKit engine and the JS-to-4D bridge in the Property List; it is off by default for security.
2. Avoid exposing the Web Inspector in deployed applications unless deliberately intended.
3. Size the process stack generously when using JavaScript callbacks into 4D.

## Context / Positioning
Published November 2014 for 4D v14.0, describing a then-new HTML/JS embedding feature in the classic Design Mode era. Web Areas backed by WebKit were 4D's primary way to mix rich web content into desktop forms before headless/offscreen web areas and broader REST/ORDA-based web architectures became common.

## Historical Commentary
**Status:** Still Relevant

The $4d callback bridge described here has remained a supported, still-relevant part of 4D's Web Area feature set in subsequent versions, so this note's core content is not obsolete — developers embedding HTML/JS widgets in a 4D form still rely on essentially this mechanism.

What has changed is the broader landscape around it: 4D later added offscreen web areas for headless use cases, and many teams now build the 'rich UI' portion as an external web/mobile client talking to 4D via REST/ORDA rather than embedding it in a form — so this technique is best seen as one still-valid option among several, not the default architecture it once was.
