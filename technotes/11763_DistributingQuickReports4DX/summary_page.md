# Tech Note: Distributing Quick Reports and Files on 4D Server

**Author:** Not specified in source document
**Published:** June 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11763
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note explains how to use the special Mac4DX and Win4DX folders on a 4D Server machine to automatically distribute saved Quick Reports and other supplementary files to 4D Client machines at logon, without needing a separate file server.

## Key Points

- Addresses frequent customer requests for an easy way to manage/distribute saved Quick Reports across 4D Client machines.
- Files placed in the Mac4DX (Mac clients) or Win4DX (Windows clients) folders on the server are automatically copied to the corresponding client at 4D Client startup/logon.
- No separate file server or manual per-machine copying is required.
- Presented as a direct answer to a recurring 4D Technical Support question.

## Featured Technology

- 4D Server / 4D Client architecture
- Mac4DX and Win4DX auto-distribution folders
- Quick Reports

## Historical Context

Reflects the self-contained client/server deployment conventions of 4D Server v6 in the mid-to-late 1990s, when distributing supplementary client-side files (like saved reports) without a dedicated network file server was a real practical concern for administrators; modern 4D Server deployment and update mechanisms have since evolved well beyond this simple auto-copy folder convention.

## Historical Commentary
**Status:** Superseded

This note documents a client/server file-distribution mechanism specific to 4D v6's Mac4DX/Win4DX client folder convention, used to auto-push saved Quick Reports and other files to 4D Client machines at logon; this exact folder-based distribution mechanism is tied to the classic 4D Client/Server architecture of that era and has been superseded by later, more integrated client update/deployment mechanisms in modern 4D Server.
