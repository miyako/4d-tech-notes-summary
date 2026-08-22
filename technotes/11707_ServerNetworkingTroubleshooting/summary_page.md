# Tech Note 96-28: 4D Server: Networking and Troubleshooting

**Author:** Jim Staples, Jr.
**Published:** June 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11707
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_27-30_(JUN)/96-28_Server_Troubleshoot.exe

## Overview
This Tech Note is a networking primer and troubleshooting guide for connecting 4D Client and 4D Server, covering the three protocols supported at the time (ADSP/AppleTalk, TCP/IP, IPX/SPX), 4D's "ACI Network Component" translation layer, and step-by-step troubleshooting practices.

## Key Points
- **Three supported protocols:** ADSP (AppleTalk, native to Mac OS), TCP/IP (Internet standard), and IPX/SPX (Novell NetWare's protocol) — with a table showing which OS includes which natively and where third-party add-ons (MacLAN Connect, NetWare Client) are required.
- **ACI Network Components:** protocol-specific translator layers, pre-installed on Mac and delivered as DLLs on Windows (`4DNCADSP.DLL`, `4DNCTCP.DLL`, `4DNCSPX.DLL`), sitting between 4D and the OS networking stack.
- **4D Remote:** ACI's proprietary dial-up protocol enabling remote 4D Server access without AppleTalk Remote Access (Mac-only at time of writing).
- **Troubleshooting methodology:** (1) check what recently changed in the environment, (2) confirm network configuration is intact, (3) re-install software as a last resort (re-applying Customizer Plus settings afterward).
- **Protocol-specific tips:** Open Transport requirements on PCI Macs (ADSP), matching Frame Types (IPX), and subnet/router/gateway diagnosis with Ping (TCP/IP).
- **The "-10002" error:** 4D Client timing out waiting for a server response, adjustable via the TCP.OPT time-out setting.
- **Known issues flagged:** a Windows 95 TCP memory leak (with a Microsoft patch), and corrupted `.opt` files causing 4D Client to freeze on launch.

## Featured Technology
- AppleTalk (ADSP)
- TCP/IP
- IPX/SPX (Novell)
- ACI Network Components (4D's protocol translation layer)
- 4D Remote (proprietary dial-up access)

## Historical Context
Two of the three protocols covered here — AppleTalk/ADSP and IPX/SPX — were discontinued by Apple and Novell respectively years ago and have no presence in any modern network. TCP/IP, the only protocol still in use today, is now built directly into every operating system's network stack rather than requiring a separate driver/component installation as described here. 4D Remote, the proprietary dial-up protocol highlighted in this note, is not part of the modern 4D product line — remote access to 4D Server today happens over standard TCP/IP, typically via VPN or the Internet. The general three-step troubleshooting methodology (check recent changes, verify configuration, reinstall) remains a reasonable practice today, even though the specific protocol details are obsolete.
