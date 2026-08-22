# Tech Note 96-05: Selecting the Proper Transport Layer on the Macintosh Version of 4D Server

**Author:** Christopher Chapman
**Published:** January 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=11688
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_01-05_(JAN)/96-05_Transport_Layer.exe

## Overview
For 4D Client running under Windows 3.1(1), Windows 95, or Windows NT 3.5.x to properly connect to and decode packets from a 4D Server running on a Macintosh, the database administrator must select the correct network transport layer on the Mac server machine. This note explains the difference between the two available options — EtherTalk and Ethernet — and why Ethernet is almost always the correct choice for mixed Mac/Windows environments.

## Key Points
- **EtherTalk** splits native TCP/IP or IPX/SPX packets (larger than AppleTalk's) into multiple AppleTalk-format packets; only machines with an AppleTalk stack can reassemble them, which most PC machines lacked at the time.
- **Ethernet** transport posts packets in their native TCP/IP or IPX/SPX format directly, compatible with virtually all PC clients, and faster since no AppleTalk encode/decode step is needed.
- A Mac server set to EtherTalk will be **invisible** to Windows 4D Clients unless those PCs have AppleTalk installed and use the ADSP network component.
- The transport layer must be switched to Ethernet in **both** the MacTCP and MacIPX control panels on the server machine.
- Switching to Ethernet has **no effect** on Macintosh-to-Macintosh client connections, including those using ADSP.
- The only scenario favoring EtherTalk over Ethernet is when part of the network must be routed through an AppleTalk-only router.

## Featured Technology
- AppleTalk / EtherTalk networking
- Ethernet transport (native TCP/IP or IPX/SPX packet format)
- MacTCP and MacIPX control panels
- Cross-platform 4D Server (Mac) ↔ 4D Client (Windows) networking

## Historical Context
Published in January 1996, this note reflects the practical cross-platform networking challenges of running 4D Server on classic Mac OS while serving a growing base of Windows 4D Clients, at a time when AppleTalk and TCP/IP/IPX coexisted as competing (and largely incompatible without translation) network transport options on the Mac.

## Historical Commentary
**Status:** Obsolete

This entire transport-layer selection concern is obsolete: AppleTalk networking was discontinued by Apple in the 2000s, and every modern operating system — and every current version of 4D Server/4D Client — communicates exclusively over standard TCP/IP. The MacTCP and MacIPX control panels referenced here are themselves artifacts of classic Mac OS with no equivalent in macOS or any current system, making this note of historical interest only.

