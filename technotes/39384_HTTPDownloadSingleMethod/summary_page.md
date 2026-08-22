# Tech Note 05-31: HTTP Download with a Single Method

**Published:** September 23, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=39384
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_30-33_(SEP)/05-31_HTTP_Download.exe

## Overview
**Note:** this entry's content_source is `teaser_only` — the full PDF/example archive could not be recovered in this environment, so the following is based solely on the short on-page teaser text.

Per the teaser, this note responds to continued support requests for a simpler way to do HTTP downloads in 4D, despite earlier notes on the subject (TN 02-5, "HTTP Client with 4D," and TN 05-18, "cURL – HTTP Client"), by offering a single self-contained 4D method.

## Key Points (from teaser)
- Offers one 4D method that handles downloading an HTML page, posting data, receiving a picture, or downloading an entire file.
- Explicitly designed for minimal installation friction: no quitting 4D, no starting 4D Insider, and no need for multiple methods, a component, or an external application.
- Positioned as a deliberately simplified alternative to the more complex approaches in TN 02-5 and TN 05-18.
- No further detail on the method's exact parameters or internal implementation is available from the recovered teaser text.

## Featured Technology
- HTTP GET/POST download via a single 4D method
- 4D Internet Commands (implied, per predecessor notes)
- HTML page / file / picture download

## Historical Context
The full archive for this Tech Note could not be recovered (old-format download not accessible in this environment), so this summary is limited to the teaser's description. This kind of lightweight, copy-paste HTTP helper was a reasonable solution before 4D had native HTTP client support; 4D has since added built-in HTTP Client language commands/classes that handle GET/POST/file downloads directly, without needing a hand-written method or the 4D Internet Commands plug-in, superseding the specific technique while the underlying need (simple HTTP downloads from 4D) remains common.
