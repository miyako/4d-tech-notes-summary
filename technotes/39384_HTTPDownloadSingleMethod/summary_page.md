# Tech Note: HTTP Download with a Single Method

- **Asset ID:** 39384
- **Tech Note #:** 05-31
- **Published:** September 23, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thomas Maul
- **Page URL:** https://kb.4d.com/assetid=39384
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_30-33_(SEP)/05-31_HTTP_Download.hqx

## Overview

Thomas Maul (General Manager, 4D Germany) presents HTTP_Download, a single, self-contained 4D method that consolidates HTTP GET/POST downloading of HTML text, pictures, and arbitrary files into one copy-paste routine, explicitly aimed at developers who found the multi-method approaches of earlier HTTP Tech Notes too cumbersome for occasional use.

## Key Points

- Core call signature: `HTTP_Download(Job; Resultpointer; URL; {Referer; {Cookie; {Postdata; {Timer; {Redirect}}}}}) -> Header`, where Job is "text", "picture", or "blob" and Resultpointer must match that type.
- Automatically handles chunked response data, follows HTTP redirects (301/302/307) and preserves cookies across them, and can be told via the Redirect parameter to not auto-follow redirects for manual header handling.
- Supports HTTP POST by passing a Postdata parameter (x-www-form-urlencoded), and provides a built-in URL_Encoder helper job for encoding spaces and 8-bit/international characters (e.g. umlauts) into valid URL-safe strings.
- Includes Get_Cookie and File_name helper jobs (invoked via the same Job parameter mechanism) for extracting cookies from a response header and determining a downloaded file's original name.
- Defaults to a 30-second timeout (adjustable via the Timer parameter) and returns descriptive error strings (e.g. "URL required", "Wrong result type, blob expected", "Connection failed") rather than raw 4D error codes.
- Requires 4D 2004.1 or newer (uses pointers on local variables) and the 4D Internet Commands plug-in; positioned as a simpler alternative to TN 02-5 ("HTTP Client with 4D") and TN 05-18 (cURL).
- The author notes the finished method exceeds 500 lines, acknowledging the code-organization tradeoff made in favor of single-file portability across many small client projects.

## Featured Technology

- 4D Internet Commands plug-in
- HTTP GET/POST via a single method
- Cookie and redirect (301/302/307) handling
- URL percent-encoding helper (URL_Encoder)
- BLOB/text/picture result typing via pointer parameters
- 4D 2004.1 local-variable pointers

## Historical Commentary

**Status:** Superseded

This note offers a genuinely practical, single-method HTTP client built on the 4D Internet Commands plug-in, complete with cookie/redirect handling and helper routines that were non-trivial to implement correctly in 2005. It was a reasonable, portable solution before 4D shipped native HTTP client support, but 4D has since introduced built-in HTTP Client commands (and, in the ORDA/class-based era, HTTP request objects) directly in the core language, removing the need for the 4D Internet Commands plug-in and this hand-written wrapper for standard GET/POST/file-download scenarios.

**References to newer/updated information:**
- 4D introduced native HTTP Client commands (HTTP Request and related APIs, added in 4D v13 and later expanded) that handle GET/POST, cookies, and redirects without the 4D Internet Commands plug-in or a custom helper method
- The 4D Internet Commands plug-in this method depends on has been phased out in favor of these built-in commands in modern 4D development
