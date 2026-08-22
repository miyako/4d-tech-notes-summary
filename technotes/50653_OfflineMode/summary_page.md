# Tech Note 08-28: Exploring 4D Ajax Framework Offline Mode

**Author:** Thomas Fitch, Technical Services Team Member, 4D Inc.
**Published:** August 6, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=50653

## Overview
Before smartphones dominated work and connectivity was assumed always-on, Offline Mode in the 4D Ajax Framework offered a practical solution for mobile and remote users: the ability to work in a web-based Data Grid without an internet connection. This note explains how Offline Mode works, what technologies power it (HTML5 and Google Gears), how to configure it, and how to troubleshoot the inevitable compatibility headaches that arose from this dual-technology approach.

## Key Points
- **Two technology pathways:** HTML5 Web Applications 1.0 (supported by Firefox 3+ and Safari 3+) uses browser-native storage; Google Gears (a SQLite-based browser extension) provides fallback for browsers without HTML5 support (e.g., Internet Explorer 7).
- **Framework-level configuration:** Offline Mode must be explicitly enabled in the 4D Ajax Framework Control Panel for specific views; only then can users toggle offline mode in the web interface.
- **Field access requirement:** All fields in an offline-enabled view must have the input box checked in access control; views without full input access will fail silently when attempting to add records.
- **View-limited scope:** Only Data Grids are supported; other framework objects cannot be accessed offline.
- **Offline cache management:** Users can optionally purge the offline cache when going offline (clearing cached data) or retain it for continued work.
- **Sync on reconnect:** Upon reconnecting and switching back to online mode, cached records are automatically synchronized to the 4D server; however, session timeouts complicate this (timed-out users must log back in and re-sync manually).
- **Browser permission dialog:** Gears-dependent browsers (Internet Explorer, Firefox) show a security prompt allowing the user to grant Gears access to the website; denied access prevents offline mode activation.
- **Status indicator:** The online/offline button displays color-coded status (green = online, yellow = transitioning, red = offline).
- **API for custom pages:** Developers using custom HTML pages can access Offline Mode via JavaScript functions (`dax_goOffline()`, `dax_goOnline()`, `dax_purgeOfflineCache()`) and corresponding event handlers.

## Featured Technology
- HTML5 Web Applications 1.0 specification
- Google Gears browser extension (SQLite-based)
- 4D Ajax Framework Data Grid
- JavaScript APIs for offline mode control
- Firefox 3.x, Safari 3.x, Internet Explorer 7.x (with Gears), Opera

## Historical Context
Published in August 2008, this note captured a critical moment in web application history: mobile and remote work were rising, but browser vendors had not yet standardized on modern offline-first patterns. HTML5 was still in draft, and Google Gears was considered the interim solution. By 2011, Gears was abandoned, and the web gradually coalesced around modern standards (Service Workers, IndexedDB, Fetch API) that arrived in the mid-2010s. The conceptual need Offline Mode addressed—enabling work without connectivity and syncing on reconnect—remains relevant today, but every technology mentioned here is now obsolete.

## Historical Commentary
**Status:** Obsolete

Both HTML5 Web Applications (as specified in 2008) and Google Gears have been superseded by modern web standards. Gears was officially discontinued by Google in December 2011 with no migration path within 4D. The 4D Ajax Framework itself was retired, leaving no direct successor path for Offline Mode functionality. Modern offline-first web applications today rely on Service Workers (background scripts that cache network requests), IndexedDB (large-scale client-side storage), and Progressive Web App (PWA) standards—a fundamentally different architecture that emerged in the 2015–2020 timeframe. A developer seeking equivalent functionality today would build a PWA or use a backend-agnostic sync framework like Watermelon DB or RxDB, not expect it from a traditional server-side framework.
