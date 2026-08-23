# Tech Note: Limiting Access When Using 4D Client Across the Internet

- **Asset ID:** 25617
- **Tech Note #:** 02-61
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Larry Sharpe
- **Page URL:** https://kb.4d.com/assetid=25617
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-61_Limiting_Access.hqx

## Overview

Larry Sharpe of Infoservice describes a real client engagement: a 4D Server in California being accessed by 4D Client users in Texas over the open Internet, where the client wanted assurance that only known staff — not a former employee or an intruder who obtained valid credentials — could connect. Because the legitimate users all had fixed IP addresses on their DSL lines, the solution logs every connection attempt and checks it against a table of known-good addresses using the IT_MyTCPAddr command from the 4D Internet Commands plug-in, implemented with two small tables: xLogins, which records date, time, IP address, 4D username, computer info, and login status for every attempt (viewable and clearable through a 4D List/AreaList window), and xValidIPs, which stores the allowlist of approved IP addresses and their owners (editable through its own add/modify/delete window). The check runs from the On Startup database method via a Login_CheckIP project method every time a client connects, logging the attempt and — in a commented-out block the developer must deliberately enable and configure with their own IP address as a safety valve — optionally calling Quit 4D to forcibly disconnect a client whose IP is not on the allowlist. The note candidly reports real-world results: DSL/Internet-based 4D Client access proved generally reliable, with an early performance problem traced to the Texas office's ISP being too many network hops from the Internet backbone, resolved by switching providers, and mentions catching a user who was falsely reporting their logged-in hours.

## Key Points

- Because the client's legitimate remote staff all connected from fixed DSL IP addresses, the solution logs every connection attempt and checks the caller's address using `IT_MyTCPAddr` from the 4D Internet Commands plug-in, run from the `Login_CheckIP` project method that is called from the `On Startup` database method on every client connection.
- An `xLogins` table records the date, time, IP address, 4D username, computer info, and login status of every connection attempt, and is displayed to an administrator through a form using a 4D List (AreaList) external area; double-clicking an entry shows the raw IP and its resolved host name, and a Delete option clears the log.
- An `xValidIPs` table stores the allowlist of approved IP addresses and associated user names, editable through its own add/modify/delete window driven by the `ValidIPs`/`ValidIPs_ALHandler` methods.
- The actual enforcement — quitting the database via `Quit 4D` for an unrecognized IP — is deliberately left commented out in `Login_CheckIP`, with an explicit warning to set a `$developerID` safety-valve variable to the developer's own IP first, to avoid accidentally locking out the developer themselves.
- Real-world field notes: DSL-based 4D Client access over the Internet worked well overall; an early performance/dropped-connection problem traced to the Texas office's ISP being too many network hops from the backbone was fixed by switching providers; and the logging incidentally caught a user misreporting the hours they were logged in.

## Featured Technology

- IT_MyTCPAddr command (4D Internet Commands plug-in)
- On Startup database method as a connection-time login hook
- xLogins connection-history/audit table
- xValidIPs static IP allowlist table
- 4D List/AreaList external area for displaying login history
- Optional Quit 4D-based hard connection rejection

## Historical Commentary

**Status:** Superseded

This is a pragmatic, field-tested security recipe for a real problem in the early 2000s: 4D Client's classic architecture had no built-in way to restrict which network locations could connect, so this note fills that gap with a lightweight logging-and-allowlist layer built from a couple of tables and the 4D Internet Commands plug-in. The specific reliance on static client-side IP addresses is a poor fit for most networks today (many client connections now come from dynamic IPs, NATed offices, or roaming/VPN users), and 4D itself has since added built-in, server-side connection security controls (including SSL/TLS enforcement and more granular network/access configuration) that provide more robust protection than a hand-rolled IP allowlist checked after the fact in On Startup.

References to newer/updated information:
- 4D Server has since added native network-level security controls (SSL/TLS, more granular connection settings) that provide more robust protection than a hand-rolled On Startup IP-check table
- Static-IP-based allowlisting is a poor fit for most modern network setups (dynamic IPs, NAT, VPN/roaming users), reducing the practical applicability of this note's specific technique today
