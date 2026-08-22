# Tech Note 10-34: Replication via HTTP

**Author:** Rudi Psenicnik, Technical Services Team Member, 4D Inc.
**Published:** December 6, 2010 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76224
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_34-36_(DEC)/10-34_Replication_With_HTTP.pdf

## Proposition
Written by Rudi Psenicnik, this Tech Note explains how 4D v12's new REPLICATION and SYNCHRONIZATION SQL commands can mirror data between a local 4D database and virtually any remote platform — from mobile devices to desktop servers — using HTTP requests and JSON notation as the transport.

## Key Points
- REPLICATION/SYNCHRONIZATION are new 4D v12 SQL commands for automatic 4D-to-4D data mirroring
- HTTP-based replication is a manual alternative for syncing 4D data with non-4D platforms
- Developers must write their own remote client/server; 4D provides no ready-made HTTP replication server
- Uses JSON as the universal, cross-platform data interchange format
- Designed for low-level record mirroring, not for enforcing business logic or validation

## Featured Technology
- REPLICATION/SYNCHRONIZATION SQL commands
- HTTP web requests
- JSON notation
- custom remote database bridge

## Best Practices Highlighted
- Use HTTP replication only when you truly need to sync with a non-4D remote system
- Understand it mirrors data, not business logic — validation must be handled separately

## Context/Positioning
Published as smartphones (Android, iPhone) proliferated, this note helped 4D developers bridge desktop 4D databases with the era's emerging mobile/web platforms before 4D had its own REST/ORDA layer.

## Historical Commentary
**Status:** Partially Superseded

This note documents a hand-rolled HTTP+JSON replication bridge built on 4D v12's REPLICATION/SYNCHRONIZATION SQL commands, requiring developers to write their own remote client or server logic from scratch. Since then 4D has invested heavily in built-in, standards-based REST APIs (powered by ORDA) for exchanging data with any platform, which cover much of what this custom bridge aimed to solve with far less bespoke code. The general architecture (HTTP + JSON as a universal sync bridge) remains sound, but the specific low-level SQL replication commands and DIY protocol shown are now a legacy approach.
