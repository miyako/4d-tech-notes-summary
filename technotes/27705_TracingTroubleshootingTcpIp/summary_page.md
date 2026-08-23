# Tech Note: Tracing and Troubleshooting TCP/IP

- **Asset ID:** 27705
- **Tech Note #:** 03-21
- **Published:** May 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=27705
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_21-25_(MAY)/03-21_TraceTrbleshootTCPIP.hqx

## Overview

David Adams surveys the world of Unix/OS X network diagnostic tools for 4D developers whose problems -- in 4D Web systems, 4D Web Services, IIS/WebSTAR integrations, custom TCP/IP code, or 4D Server client connections -- lie in the network layer where the 4D Debugger provides no visibility. Since OS X is BSD-based, it gives access to decades of mature Unix networking tools, and the note is a practical guide to installing and using them.

## Key Points

- Frames the problem: application-level 4D debugging cannot diagnose network-layer issues (crashed DNS, misconfigured routers, bad cables), so dedicated tracing tools are essential before problems arise.
- Covers three ways to install additional OS X Terminal tools: pre-built package installers (e.g., via the OSXGNU project), Fink (needed for tools like Ethereal, which has no package), and compiling from source using the Apple Developer CD.
- Reviews built-in commands: `ping` (connectivity check, with sample successful/failed/unresolvable output), `nslookup` (DNS server/address discovery), `netstat` (active connections and interface configuration), `traceroute` (hop-by-hop route discovery, with `mtr` as an alternative), and `whois` (domain registration lookup, noting the `-h` flag for specifying a registrar server).
- Explains OS X's restriction of ports below 1024 to the root user, and recommends the built-in `ipfw` firewall to forward port 80 to a high port like 8080 (`sudo ipfw add 101 fwd 127.0.0.1,8080 tcp from any to any 80 in`) rather than running 4D's web server as root -- with the caveat that ipfw rules don't persist across restarts.
- Covers packet/stream capture tools in depth: `tcpdump` (low-level, filterable, built into OS X) versus `tcpflow` (stream-reassembling, better suited to tracing HTTP/SOAP/SMTP conversations), and the GUI analyzers EtherPeek (commercial) and Ethereal (free, but requiring Fink + X11 to run on OS X).
- Recommends tracing the local loopback interface (`lo0`) for debugging same-machine integrations, e.g. `sudo tcpflow -c -i lo0 port 80`, useful for combining 4D with another web server on one machine via FastCGI, 4DLINK, 4DCONNECT, or ISAPI.
- Suggests assigning multiple IP addresses to one machine (via Network Preferences) so different local services (Apache, WebSTAR, 4D) can each be traced independently, using Apache's `BindAddress` directive as an example.
- Notes that Web browsers are a poor substitute for real network tools, and recommends terminal browsers like Lynx/Links for tracing HTTP conversations without the noise of automatically-downloaded images.

## Featured Technology

- OS X Terminal-based network diagnostic tools (ping, traceroute, whois, nslookup, netstat)
- Packet/stream capture tools (tcpdump, tcpflow, Ethereal, EtherPeek)
- Local loopback interface (lo0) tracing for same-machine 4D/web-server integrations
- ipfw port forwarding for OS X's restricted sub-1024 ports
- Fink / package-installer based Unix tool installation on OS X

## Historical Commentary

**Status:** Obsolete

David Adams provides a broad, practical tour of Unix/OS X network debugging tools -- ping, nslookup, netstat, traceroute, whois, tcpdump, tcpflow, Ethereal, EtherPeek -- aimed at 4D developers whose systems (Web, Web Services, IIS/WebSTAR integrations, custom TCP/IP code) fail in ways the 4D Debugger cannot diagnose. The central thesis, that application-level debugging is not enough for network-layer problems and dedicated tools are required, remains completely true today. However, essentially every specific tool recommendation is dated: Ethereal has been renamed and succeeded by Wireshark, EtherPeek and Fink-based X11 installs are obsolete workflows, and the OS X-specific installation friction described (needing the Developer CD, Fink, X11) no longer applies on modern macOS, which ships or easily installs equivalents via Homebrew. The lo0 loopback-tracing and ipfw-port-forwarding techniques are also outdated (ipfw was removed from macOS in favor of pf), though the underlying concepts (loopback tracing, port forwarding for privileged ports) remain valid networking knowledge developers must reapply with current tools.

References to newer/updated information:
- Ethereal was renamed Wireshark in 2006 and remains the standard graphical packet analyzer; EtherPeek is discontinued
- Apple removed ipfw from macOS (10.10+) in favor of the pf packet filter, so the ipfw port-forwarding example shown here no longer works on modern macOS
- Modern macOS/Homebrew make installing tools like tcpflow, nmap, and Wireshark far simpler than the Fink/X11/Developer-CD process described in this note
- The core principle -- that network-layer problems require dedicated tracing tools rather than the 4D Debugger -- remains valid and is unchanged in current 4D development
