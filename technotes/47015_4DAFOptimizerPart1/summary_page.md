# Tech Note 07-28: 4DAF Optimizer – Part 1

**Author:** Tom Fitch, Technical Support Engineer, 4D Inc.
**Published:** July 18, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47015
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_26-29_(JUL)/07-28_4DAF_Optimizer.zip

## Overview
This note introduces the 4DAF Optimizer, a companion tool for developers using 4D Ajax Framework (4DAF) objects in custom HTML pages, which strips unnecessary JavaScript files from the 'js' folder and rebuilds a leaner `framework.js` bundle to reduce page load time.

## Key Points
- **Step 1 – Select features:** choose which 4DAF objects/features the app needs from a checklist grouped as Core (always required), Client (the full default front end, all-or-nothing), Objects (Calendar, Data Grid, Data Tree, DDW, Data/Image Matrix), and Features (Hierarchical List, Sidebar, Taskbar); clicking "Generate" builds a trimmed `js` folder plus a rebuilt `framework.js`.
- **Step 2 – Deploy:** copy the new `js` folder into the app's `\dax\js` path (relative to the Default HTML Root), overwriting existing contents.
- Worked examples using bundled demo apps: 4D Jukebox (Data Grid only), Vacation Tracker (Data Tree + Calendar), Contacts (Data/Image Matrix).
- Each demo's homepage HTML must be updated to load `dax/js/framework.js` instead of the original `dax/js/compile.js`.
- The note flags that Templates and Localization support were planned for a future Optimizer version, not yet available at this release.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- 4DAF Optimizer utility
- JavaScript asset bundling (`framework.js`)

## Historical Context
Published July 2007 during active 4D Web 2.0 Pack development, ahead of 4D v11's native SQL engine later that year, and roughly a decade before Project Mode and ORDA arrived.

## Historical Commentary
**Status:** Obsolete

The 4DAF Optimizer and the 4DAF/4D Web 2.0 Pack asset architecture it manages have been fully discontinued, so this specific tool and workflow have no modern counterpart in current 4D. However, the underlying problem it solved — shipping only the JavaScript a page actually needs to minimize load time — is exactly what modern JS bundlers (webpack, Rollup, esbuild, Vite) with tree-shaking now solve automatically, making this note an interesting historical precursor to today's standard front-end tooling.
