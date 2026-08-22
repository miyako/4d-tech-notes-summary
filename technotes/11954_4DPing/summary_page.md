# Tech Note: 4D Ping (TN 00-43)

**Author:** Arnaud Lion, 4D S.A. Technical Support
**Published:** September 1, 2000 | **Product/Version:** 4D Internet Commands v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11954
**Download:** https://kb.4d.com/DLTN/TN/2000/Windows/TN_2000_41-45_%28SEP%29/00-43_4D_Ping.exe

## Overview
This Tech Note covers a sample utility database that implements a network "ping" tool using the 4D Internet Commands plug-in, for diagnosing network issues during application deployment.

## Key Points
- Technical Support, introduces a small utility program that lets a 4D application "ping" another computer on the network, built entirely using the 4D Internet Commands plug-in.
- Its stated purpose is squarely practical: helping developers and administrators isolate network-related problems while deploying multi-machine 4D applications, a common pain point whenever a 4D Server-based system spans several client machines and network segments.
- The sample database's interface is organized into four functional areas — Local Computer (entering the local IP address and subnet mask), Ping Settings (entering the target address, selecting the number of packets, and enabling continuous pinging), Packet Settings (configuring the content and size of test packets, and the interval between them), and Ping Report (a running log showing sequence numbers, tested addresses with DNS resolution, and ping duration measured in ticks for each successful test).
- The featured technology is the 4D Internet Commands plug-in's TCP/IP primitives, used here to implement classic ICMP-style ping/reachability testing entirely from within a 4D application rather than relying on OS-level command-line tools.
- Before using any 4D IC command, the code must first initialize the TCP layer, a step handled in the sample database's On Startup method, reflecting the explicit low-level network stack setup required by 4D's internet plug-in architecture at the time.
- This kind of tool was valuable for 4D Server administrators troubleshooting connectivity issues in the field, giving them a purpose-built, cross-platform (Mac/Windows) diagnostic utility built with the same toolkit they used for their production applications' own networking features, rather than needing separate OS utilities.

## Featured Technology
- 4D Internet Commands
- TCP/IP networking
- Network diagnostics (ping)
- 4D Server deployment troubleshooting

## Historical Context
This note presents a working "ping" utility built with the 4D Internet Commands plug-in, letting developers diagnose network connectivity issues while deploying 4D Server-based applications — a practical, still-relevant class of problem, though the specific plug-in (4D Internet Commands) it depends on was long ago folded into or replaced by native 4D language commands for TCP/IP and internet operations. The core diagnostic concept (testing reachability/latency to isolate network problems during deployment) remains fully relevant today, even though a modern equivalent would use current 4D networking commands rather than the classic 4D Internet Commands plug-in API described here. Related updates since: 4D Internet Commands has since been superseded by native 4D language commands and classes for TCP/IP, HTTP, and related network operations; Network diagnostic techniques like ping-based reachability testing remain a standard, relevant troubleshooting approach for deployed 4D Server applications today.
