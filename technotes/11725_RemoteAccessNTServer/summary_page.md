# Tech Note 96-50: Installing & Configuring Mac & PC Remote Access to a Windows NT-based 4D Server

**Author:** David Hartje
**Published:** November 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Win
**Page:** https://kb.4d.com/assetid=11725
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_45-50_(NOV)/96-50_Windows_Remote.exe

## Overview
This Technical Note illustrates one way to set up dial-up remote access — using freeware components — so that Mac and Windows 4D Client machines can connect over a modem to a 4D Server running on Windows NT, via Microsoft's Remote Access Service (RAS).

## Key Points
- **Server setup:** Windows NT machine with a network card bound to IPX/SPX (frame type 802.3, matched network-wide) and TCP/IP (fixed IP on the shared subnet), plus Windows NT Remote Access Service installed and configured to allow both protocols for dial-in.
- **Authentication:** Recommends starting with "allow any authentication, clear text included" due to Mac client compatibility, tightening security only after connections are verified.
- **Access control:** Remote Access Admin grants dial-in privileges per user; RAS itself need not be domain-joined.
- **Windows 95 client setup:** Install the Dial-Up Adapter (TCP/IP + IPX/SPX), select Server Type "PPP, Windows95, Windows NT 3.5, Internet," and create a Dial-Up Networking connection to reach the RAS server before launching 4D Client.
- **Macintosh client setup:** TCP/IP-only (no IPX/SPX dial-up on Mac); use FreePPP for a direct PPP connection without connect scripts, then launch 4D Client after connecting.
- **Server visibility caveat:** Any 4D Server instance not running directly on the Remote Access Server machine won't appear in the connection Browser — its address must be hard-coded on the client.
- Framed explicitly as one illustrative solution, not the only viable approach.

## Featured Technology
- Windows NT Remote Access Service (RAS)
- 4D Server / 4D Client
- TCP/IP and IPX/SPX dial-up networking
- PPP (FreePPP for Macintosh)
- Windows 95 Dial-Up Networking

## Historical Context
**Status:** Obsolete

This note documents a specific 1996 dial-up (modem/RAS) remote-access solution for reaching a Windows NT-based 4D Server. Dial-up modem networking and Windows NT 3.51's Remote Access Service have been obsolete for decades, first replaced by broadband VPN connections and now largely superseded by cloud/internet-native application access. The freeware utilities referenced (FreePPP, Windows 95 Dial-Up Adapter) are all long discontinued. The underlying need for secure remote database access remains very much alive today, but it is now addressed through VPNs, direct TCP/IP-over-internet connections, or ORDA/REST-based access rather than dial-up RAS.
