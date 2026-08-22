# Tech Note 12-15: Multiple Web Servers on a Single OS

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** August 8, 2012 | **Product/Version:** 4D v12.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76631
**Download:** https://kb.4d.com/DLTN/TN/2012/12-15_MultiWebserversOnSingleOS.zip

## Proposition
This Tech Note describes how to run multiple 4D Web Servers on a single machine by assigning multiple static IP addresses to one network card and configuring each 4D database to listen on a specific IP.

## Key Points
- 4D's Web Server requires exclusive access to an IP address, so multiple servers on one OS need multiple IPs (DHCP cannot be used — static IPs are required).
- Step-by-step instructions for adding additional static IP addresses on Windows (Network Connections / TCP/IP Advanced settings) and Mac OS X (Network preferences "Duplicate Service").
- Two approaches for the database to learn which IP to use: DNS/FQDN lookups (including editing the local hosts file) or hard-coded/external specific IP addresses.
- Sample project methods (SET_SPECIFIC_IP_OR_HOST, SET_WEB_LISTEN_IP, GET_IP_FROM_EXTERNAL_FILE) show parsing an IP string, converting octets to a Long Integer, and calling WEB SET OPTION to bind the listen address.
- Supports reading the target IP from an external ListenIP.txt file next to the structure, useful for per-deployment configuration without recompiling.

## Featured Technology
- 4D Web Server administration (WEB SET OPTION, WEB START SERVER, WEB STOP SERVER)
- 4D Internet Commands plugin (NET_Resolve)
- OS-level static IP configuration (Windows & Mac OS X)
- Regex matching (Match regex) for IP address validation

## Best Practices Highlighted
1. Use static IPs rather than DHCP for machines hosting multiple 4D Web Servers.
2. Externalize the listen IP configuration (via a text file) to simplify per-deployment changes without code edits.
3. Restart the Web Server cleanly (stop, reconfigure, start) after changing the listen IP.

## Context/Positioning
Published for 4D v12.4 in 2012 when 4D's built-in Web Server was a primary deployment option for many customers, this note filled a documentation gap around hosting several 4D web applications side by side on one server.

## Historical Commentary
This is fundamentally an OS networking tutorial paired with a stable 4D Web Server command (WEB SET OPTION), so the approach still functions today, though the screenshots reflect long-superseded OS versions and the underlying deployment pattern (multiple IPs on one OS) has been largely overtaken by containerized or reverse-proxy-based hosting architectures. The core 4D commands referenced remain part of the current classic language and are unaffected by ORDA or Project mode changes.

**Status:** Still relevant
