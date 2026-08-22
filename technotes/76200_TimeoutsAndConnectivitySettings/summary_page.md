# Tech Note 10-31: Mastering 4D Timeouts & Connectivity Settings

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** November 1, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76200
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_31-35_(NOV)/10-31_Mastering_4D_Timeouts_and_Connectivity.pdf

## Proposition
Timothy Aaron Penner's extensive Tech Note serves as a master reference for 4D Client/Server network configuration.

## Key Points
- Explains Idle Connections Timeout (Parameter 54) in depth, including when and how to change it
- Covers TCP_NODELAY and other parameters that affect client-server responsiveness
- Documents Automatic Client Reconnect and Register Clients at Startup tradeoffs, warning against combining certain settings
- Provides router/firewall-specific configuration notes for common hardware of the era
- Includes a diagnostic methodology for isolating network vs. router vs. internet connectivity issues
- Ends with a recommended 'safest settings' baseline

## Featured Technology
- 4D Server/Remote mode timeouts
- Idle Connections Timeout (Database Parameter 54)
- TCP_NODELAY (Database Parameter 33)
- Automatic Client Reconnect
- Register Clients at Startup
- Encrypt Client-Server Connections
- router/firewall configuration

## Best Practices Highlighted
- Do not combine 'Use Automatic Client Reconnect' and 'Idle Connections Timeout' simultaneously
- There is no universal suggested value for Idle Connections Timeout — tune per network
- Use Encrypt Client-Server Connections where security requirements warrant the overhead

## Context/Positioning
Published to help 4D VARs and IT administrators diagnose the era's common client-server disconnect complaints across the wide variety of consumer/business routers and firewalls then in use.

## Historical Commentary
**Status:** Still Relevant

This note's deep dive into 4D Client/Server timeout parameters, router/firewall quirks, and connectivity settings addresses network administration fundamentals that remain broadly relevant today, since TCP/IP timeout and firewall behavior hasn't fundamentally changed. Some of the specific router models discussed (Cisco, Sonicwall, older DD-WRT/Tomato firmware) are dated, and 4D has since added newer connectivity features (e.g., improved encryption defaults, cloud-oriented deployment), but the core troubleshooting methodology is still a solid reference.
