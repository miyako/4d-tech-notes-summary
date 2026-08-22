# Tech Note 09-27: IIS and ISAPI REWRITE

**Author:** Timothy Penner, Technical Services Team Member, 4D Inc.
**Published:** July 9, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75833
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_27-30_(JUL)/09-27_ISAPI_Rewrite.zip

## Proposition
This note shows how to use Microsoft IIS as a front-end reverse proxy to 4D's built-in Web Server, using the 3rd-party Helicon ISAPI_Rewrite filter, so that IT departments who insist on IIS can still serve a 4D application's dynamic and static content.

## Key Points
- **ISAPI_Rewrite** is a 3rd-party ISAPI filter from Helicon Tech, functioning like Apache's mod_rewrite but built specifically for IIS, using regex-based rules.
- Installed only on the IIS machine; **no configuration is required on the 4D side** beyond running the 4D Web Server on a reachable port.
- Configuration is split between a **global `httpd.conf`** and **per-site `.htaccess`-style files**.
- Key directives covered: `RewriteEngine`, `RewriteBase`, `RewriteProxy`, plus flags `H` (preserve Host header), `A` (add auth headers), and `CR` (pass credentials).
- **Example configurations** provided for: proxying a specific directory, proxying only SOAP requests, proxying SOAP + a directory, and proxying all requests to 4D.
- Special attention is given to keeping a **4D-hosted WSDL file's URLs correct** when accessed through the proxy.

## Featured Technology
- Microsoft IIS (Internet Information Services)
- ISAPI (Internet Server Application Programming Interface)
- Helicon Tech ISAPI_Rewrite filter (3rd-party reverse proxy/URL rewriter)
- 4D Web Server (as reverse-proxy target)
- SOAP request routing via reverse proxy

## Best Practices Highlighted
1. Run 4D's Web Server on a non-standard port and let IIS/ISAPI_Rewrite own port 80, rather than trying to run both servers on the same port.
2. Preserve the Host header (`H` flag) when proxying, so 4D-generated links and WSDL URLs resolve correctly behind the proxy.
3. Scope rewrite rules narrowly (specific directories or SOAP-only paths) rather than blindly proxying everything, to limit exposure.

## Context / Positioning
Published to solve a recurring real-world deployment friction point — corporate IT teams refusing to deploy on 4D's own web server — this note gave developers a documented, supported path to keep IIS in the picture while still using 4D's web capabilities, including its SOAP-based web services.

## Historical Commentary
**Status:** Partially Superseded

This note explained how to front 4D's built-in web server with Microsoft IIS using the 3rd-party Helicon ISAPI_Rewrite filter, mainly to satisfy corporate IT departments that insisted on IIS. The general need — fronting 4D's web server with a standard reverse proxy for corporate compliance, SSL termination, or URL rewriting — is still valid and unremarkable today.

However, the specific tool has been overtaken by more modern, actively maintained reverse-proxy options (IIS's own free URL Rewrite Module, nginx, or a cloud/CDN-based proxy), and the SOAP-specific routing examples reflect a web-services approach 4D has since moved beyond in favor of REST and ORDA.
