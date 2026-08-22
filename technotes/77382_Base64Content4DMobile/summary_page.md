# Tech Note 15-18: Transmit Base64-Encoded Content in 4D Mobile Method

**Author:** Xiang Liu, Technical Services Engineer, 4D Inc.
**Published:** September 28, 2015 | **Product/Version:** 4D Mobile v15 (demos built on 4D v14 R5 + Wakanda Enterprise 10) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77382
**Download:** https://kb.4d.com/DLTN/TN/2015/15-18_EncodedContent4DMobileR1.zip

## Proposition
Since the 4D Mobile API is fully RESTful and all payloads are JSON text, binary content (images, PDFs) returned or sent through a 4D method must be encoded as text. This note demonstrates using Base64 encoding to move binary data reliably between 4D, the Wakanda server, and web/mobile clients.

## Key Points
- **Why encoding is needed:** JSON/REST is text-only, so binary blobs can't pass through 4D Mobile method calls unmodified.
- **Base64 explained:** a widely supported binary-to-text scheme (originating in MIME email) using a 64-character printable ASCII alphabet, chosen for cross-platform and cross-language compatibility.
- **4D-side commands:** `BASE64 ENCODE` and `BASE64 DECODE` operate on BLOBs to convert to/from Base64 text.
- **Browser/Wakanda-side equivalents:** `btoa()`/`atob()` in the browser; Wakanda server-side JavaScript handling for decoding into datastore or file.
- **Server-to-client flow:** a 4D method Base64-encodes an image; the client either renders it directly in HTML or writes it to a downloadable file.
- **Client-to-server flow:** an uploaded image is Base64-encoded client-side (or by Wakanda), sent to a 4D method, and decoded back to a picture/blob.
- **Stack-specific:** all demos require Wakanda Enterprise 10 alongside 4D v14 R5, tying the technique to the specific 4D Mobile + Wakanda REST bridge architecture of the time.

## Featured Technology
- `BASE64 ENCODE` / `BASE64 DECODE` (4D)
- `btoa()` / `atob()` (browser JavaScript)
- Wakanda server-side JavaScript
- 4D Mobile RESTful method API

## Best Practices Highlighted
1. Always encode binary payloads to text (Base64) before returning them from a REST-style 4D Mobile method.
2. Use built-in encode/decode primitives on both ends (4D and JavaScript) rather than custom encoding schemes.
3. Separate static content delivery (image fields/files, transmitted automatically) from dynamic content delivery (generated on the fly, requiring manual encoding).

## Context / Positioning
This note is squarely part of the original 4D Mobile era (2015-2016): native mobile apps built with a Wakanda JavaScript front-end/server talking to a 4D back-end over a RESTful JSON API — architecturally distinct from, and predating, ORDA and the modern 4D REST server. It reflects "classic" 4D at v14/v15, well before Project Mode (2018) or 4D's later mobile/web strategy shift.

## Historical Commentary
**Status:** Obsolete

The specific technology this note is built on — 4D Mobile with a Wakanda server and JavaScript client — no longer exists; both native 4D Mobile apps and the standalone Wakanda product have been fully discontinued by 4D in favor of ORDA-based REST APIs and newer web/mobile tooling like Qodly. The general principle of Base64-encoding binary data for JSON/REST transport remains entirely valid and is still exactly how binary payloads are handled in modern ORDA REST responses, so the underlying idea survives even though the specific commands, stack, and workflow shown here are historical.
