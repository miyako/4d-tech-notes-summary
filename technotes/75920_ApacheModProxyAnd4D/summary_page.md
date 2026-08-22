# Tech Note 09-38: Apache, Mod_Proxy, & 4D

**Author:** Timothy Penner, Technical Services Team Member, 4D Inc.
**Published:** October 15, 2009 | **Product/Version:** 4D 11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75920
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_38-40_(OCT)/09-38_mod_proxy.zip

## Proposition
This Tech Note shows how to use Apache HTTP Server's mod_proxy module as a reverse-proxy front end to 4D's built-in Web Server, so that organizations standardized on Apache can still serve dynamic content from a 4D application.

## Key Points
- mod_proxy is installed with Apache and supports HTTP, HTTP/1.1, FTP, AJP13, and CONNECT (SSL) proxying, split across sub-modules (mod_proxy_http, mod_proxy_ftp, etc.).
- No configuration changes are required on the 4D side — all configuration lives in Apache's global httpd.conf or per-directory .htaccess files, and Apache must be restarted after changes.
- Three directives are explained in detail: `ProxyRequests` (forward proxy toggle, should be Off for reverse proxy), `ProxyPass` (maps a local URL path to a remote server URL), and `ProxyPassReverse` (rewrites Location/Content-Location/URI headers in redirects so clients don't bypass the proxy).
- Four worked configuration examples are given: proxy a specific directory (e.g. `/4D/`) to 4D; proxy only SOAP requests (`/4DSOAP`); proxy both SOAP and a directory together; and proxy all requests to 4D (full reverse proxy at the site root).
- Typical port setup: Apache on port 80, 4D's Web Server on a non-standard port like 8080, with mod_proxy bridging the two.
- WSDL caveat: Apache's rewrite engine does not properly strip the internal port number from the 4DWSDL file, so developers must manually save the WSDL, edit the `soap:address` location attribute, and redistribute the corrected file to SOAP consumers.

## Featured Technology
- Apache HTTP Server mod_proxy module
- ProxyRequests, ProxyPass, ProxyPassReverse directives
- 4D's built-in Web Server
- 4D SOAP web services (4DSOAP / WSDL)

## Best Practices Highlighted
1. Keep `ProxyRequests Off` in a reverse-proxy setup to avoid running an open forward proxy (a security risk).
2. Order exclusion `ProxyPass` rules (using `!`) before the general catch-all rule.
3. Always pair `ProxyPass` with `ProxyPassReverse` so redirect headers from the backend are correctly rewritten to the public-facing URL.
4. Manually correct and republish the WSDL file's `soap:address` when serving SOAP through a reverse proxy.

## Context / Positioning
Published in the v11.4 era when 4D's web server and SOAP-based web services were the standard integration surface, this note addressed a recurring enterprise deployment request — letting IT departments keep Apache as their public-facing server while 4D handled the application logic behind it.

## Historical Commentary
**Status:** Partially Superseded

The general Apache/mod_proxy reverse-proxy technique described here is still valid and commonly used today to front application servers, including 4D's web server, so this part of the note has aged well. The SOAP-specific guidance is the dated portion: 4D's web-service story has shifted decisively toward REST combined with ORDA for data access, making raw SOAP/WSDL proxy considerations far less relevant to a modern 4D deployment.

Developers setting this up today would likely still use mod_proxy or an equivalent (e.g., nginx) for the reverse-proxy piece, but would rarely need the WSDL-patching workaround since REST + ORDA (4D v16 R5+, 2017) has largely replaced SOAP as the primary 4D web-service integration approach.
