# Tech Note: WebSTAR: Front End for 4D Business Kit

- **Asset ID:** 36185
- **Tech Note #:** 05-07
- **Published:** February 17, 2005
- **Product / Version:** 4D Business Kit 2.2.2
- **Platform:** Mac OS X
- **Author:** Steve Hartman
- **Page URL:** https://kb.4d.com/assetid=36185
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_05-11_(FEB)/05-07_WebSTAR_Front_End_4DBK.hqx

## Overview

Steve Hartman (Information Systems, 4D Inc.) explains how to configure 4D WebSTAR 5.3.3's Web ReWrite plug-in as a reverse-proxy front end for 4D Business Kit 2.2.2, so WebSTAR can serve as the public-facing web server while Business Kit runs as a secondary server on a different port or machine.

## Key Points

- Requires 4D WebSTAR 5.2.3 or later; the Web ReWrite module is configured via the 4D WebSTAR Admin Client (available on both Mac OS X and Windows).
- Business Kit ships a template Rewrite proxy rules.txt in its "Files to import"/"4D WebSTAR Rules" folder containing generic proxy rules referencing a placeholder server address (www.4dbkstore.com).
- Setup steps: edit the rules file, replacing every www.4dbkstore.com occurrence with your real Business Kit address (e.g. 127.0.0.1:8080), save it, then import it via the Admin Client's Web ReWrite Proxy rules page and click Save to apply.
- Default rules assume a store folder following the "XXXX_Site" naming convention and pages served with .htm/.html extensions; other setups require custom rules, for which the note points to the WebSTAR Technical Reference's Regular Expression Reference chapter.
- On the Business Kit side, enable 'Use 4D Business Kit as a secondary server for a 4D WebSTAR, Apache or MS IIS server' on the '4D WebSTAR/Apache' Preferences page, and supply the WebSTAR server's IP address and optional port (with a toggle for HTTPS handling).
- End result: HTML pages served by WebSTAR can link directly to Business Kit-served pages (e.g. /Test_Site/WebPagesUS/home.htm) and have them transparently proxied through to the Business Kit server.

## Featured Technology

- 4D WebSTAR Web ReWrite plug-in (reverse-proxy rules)
- 4D WebSTAR Admin Client
- 4D Business Kit secondary-server preference configuration
- Rewrite proxy rules.txt template file
- HTTP/HTTPS request forwarding to a secondary web server on a custom port

## Historical Commentary

**Status:** Obsolete

Steve Hartman documents how to place 4D WebSTAR (4D's own Mac OS X web server product of that era) in front of 4D Business Kit — 4D's e-commerce storefront product — using WebSTAR's Web ReWrite plug-in to reverse-proxy requests to Business Kit running on a different port, editing a supplied Rewrite proxy rules.txt template and importing it via the Admin Client. This is a narrowly scoped configuration guide tying together two discontinued 4D products (4D WebSTAR and 4D Business Kit), both long retired from 4D's current product lineup, making the note almost entirely of historical interest; the general reverse-proxy concept it demonstrates lives on today via mainstream web servers (Apache, Nginx, IIS) or reverse-proxy layers, none of which use this specific 4D WebSTAR configuration.

References to newer/updated information:

- Both 4D WebSTAR and 4D Business Kit have been discontinued and are no longer part of 4D's current product lineup
- Modern 4D web deployments typically use the built-in 4D Web Server behind a standard reverse proxy (Apache, Nginx, IIS, or a cloud load balancer) rather than 4D WebSTAR's Web ReWrite plug-in
