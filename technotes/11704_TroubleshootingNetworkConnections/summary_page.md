# Tech Note 96-51: Troubleshooting Network Connections

**Author:** Tony Cerrato and Thomas D'Urso
**Published:** October 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11704
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_49-51_(OCT)/96-51_Network_Connections.exe

## Overview
This Tech Note is a symptom-specific troubleshooting companion for diagnosing 4D Client/Server connection failures over ADSP (AppleTalk), IPX/SPX (Novell), and TCP/IP, covering common misconfigurations, known software defects, and diagnostic tools of the mid-1990s networking era.

## Key Points
- **ADSP issues:** PCI Power Macintosh clients require Open Transport (not Classic AppleTalk); Windows clients need MacLAN Connect with matching version compatibility; router/zone misconfiguration can hide the server from clients.
- **IPX issues:** "Frame Type" mismatches between client and server are the most common cause of an invisible server.
- **TCP/IP issues:** subnet mask mismatches and missing/misconfigured default routers are common causes of cross-subnet connection failure; recommends using Ping first to isolate the problem from 4D itself.
- **The "-10002" error:** explained as 4D Client's own connection timeout expiring while waiting on a server response, adjustable via the TCP.OPT file.
- **Known defect flagged:** a Windows 95 TCP/IP stack memory leak, with a Microsoft-provided fix.
- **General methodology:** isolate whether an issue is 4D-specific or a broader network/OS problem, and check for recent environmental changes before assuming a software bug.

## Featured Technology
- AppleTalk / ADSP (MacLAN Connect, Open Transport)
- IPX/SPX (Novell NetWare)
- TCP/IP (subnet, router, Ping diagnostics)
- 4D Server client/server connection layer

## Historical Context
As a companion to TN 96-28, this note shares the same fundamental datedness: AppleTalk/ADSP and IPX/SPX have both been fully discontinued for decades, and the TCP/IP troubleshooting details reflect a manually-configured, pre-DHCP networking world plus a Windows 95-specific software defect with no relevance to modern systems. The core diagnostic instinct of using Ping to isolate connectivity problems before assuming an application bug remains sound practice today, but essentially none of the protocol- or OS-specific details in this note apply to current 4D deployments.
