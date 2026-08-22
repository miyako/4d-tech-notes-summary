# Tech Note 09-41: Using the Amazon Product Advertising API with 4D

**Author:** Keisuke Miyako, 4D Japan (per PDF; not attributed in this catalog entry)
**Published:** November 5, 2009 | **Product/Version:** 4D v11.4 SQL | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75942
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_41-45_(NOV)/09-41_AmazonProductAdvertisingAPI.zip

## Proposition
Uses Amazon's Product Advertising API as a worked example of calling a demanding, cryptographically-signed web service from 4D v11 SQL, working around the built-in SOAP client's limitations with REST, custom SOAP construction, and a purpose-built HMAC-SHA256 plugin.

## Key Points
- **Three limitations of built-in `CALL WEB SERVICE`**: it can't fully parse Amazon's complex SOAP responses, can't build multi-element SOAP headers Amazon requires, and 4D has no native HMAC-SHA256 command.
- **REST alternative**: build a query-string URL and hand it to `DOM Parse XML source` (with an `https` prefix if needed) to avoid SOAP header complexity entirely.
- **Custom SOAP alternative**: bypass `CALL WEB SERVICE` and construct/POST the SOAP envelope manually using 4D Internet Commands for full control over the HTTP request.
- **4D OpenSSL Plugin**: a custom C plugin dynamically loads the OpenSSL module already embedded inside the 4D application itself (via `GetProcAddress`/`CFBundleGetFunctionPointerForName`) to expose MD5/SHA1/SHA256/SHA384/SHA512 and HMAC variants — since Amazon mandated HMAC-SHA256 signing starting August 2009.
- **Alternative "Hash and Digest Component"**: performs the same hashing via `LAUNCH EXTERNAL PROCESS` calling VBScript (Windows) or ruby (Mac), for developers who want to avoid plugins.
- **4D AWS Library component**: a reusable, XSLT-driven component (`APPLY XSLT TRANSFORMATION`) that builds REST URLs or SOAP envelopes from a generic intermediate XML request, supporting both transports uniformly.
- **Sample applications**: a GUI test suite for exercising the AWS Library, and an "iTunes Artwork Manager" demo that fetches album art from Amazon and applies it to local iTunes tracks via AppleScript/VBA.

## Featured Technology
- Amazon Product Advertising API (SOAP and REST)
- HMAC-SHA256 request signing via a custom 4D OpenSSL Plugin
- DOM Parse XML source for REST calls
- 4D Internet Commands-based custom SOAP call (bypassing CALL WEB SERVICE)
- 4D AWS Library component with XSLT-based request generation (APPLY XSLT TRANSFORMATION)

## Best Practices Highlighted
1. Prefer REST over SOAP when a web service supports both and the built-in SOAP client cannot handle the required header/response complexity.
2. Isolate volatile request-construction logic (namespaces, endpoints, versions) behind small methods/XSL so the component can adapt as an API evolves.
3. Keep confidential account credentials out of distributed source code (compiled/protected methods) while still shipping an editable, credential-free source variant.

## Context / Positioning
Published as a showcase of advanced 4D web-services techniques, using a genuinely difficult real-world API (Amazon's, with its then-new mandatory cryptographic signing) to demonstrate workarounds for gaps in 4D v11 SQL's built-in SOAP client — techniques applicable to any complex, secured web service of the era.

## Historical Commentary
**Status:** Obsolete

The workaround techniques shown here — bypassing `CALL WEB SERVICE` for complex headers/responses, calling REST via `DOM Parse XML source`, and building a plugin to reach OpenSSL for HMAC-SHA256 — were genuinely clever engineering for 4D v11 SQL's limitations. But the concrete target, Amazon's 2009-era Product Advertising API (authenticated with just an AWS access key and HMAC-SHA256), no longer exists in that form.

Amazon has since retired that API generation multiple times over, and the current Product Advertising API 5.0 requires AWS Signature Version 4 plus an active, sales-qualifying Associates account — neither of which this note's signing scheme or sample code supports. As a result, none of the concrete Amazon-calling code here will function against Amazon's API today, even though the general SOAP/REST/cryptographic-signing techniques remain a useful reference. Additionally, 4D has since gained native REST request commands and built-in hashing commands, making the custom OpenSSL plugin largely unnecessary for new work.
