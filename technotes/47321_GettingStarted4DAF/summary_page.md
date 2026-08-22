# Tech Note 07-33: Getting Started with the 4D Ajax Framework

**Author:** Larry Sharpe, 4D Developer, InfoService
**Published:** August 22, 2007 | **Product/Version:** 4D Web 2.0 Pack (4DAF ~1.1) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47321
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_30-34_(AUG)/07-33_Getting_Started_w_4DAF.pdf

## Overview
A beginner's orientation to the 4D Ajax Framework (4DAF), part of the 4D Web 2.0 Pack, explaining what the 4DAF is, why to use it, the available documentation, and how to configure it via the Control Panel or Admin Client.

## Key Points
- The 4DAF is a 4D Component plus HTML/CSS/JavaScript/image assets, split into "4DAF Libraries" (low-level) and the ready-made "4DAF Client" front end.
- Frames the Web 1.0 → Web 2.0 shift as full-page reloads vs. partial-page updates, positioning the 4DAF as a fast on-ramp to Ajax-style development.
- Surveys the documentation ecosystem: Installation Guide, Admin Reference, Developer Guide, the Daxipedia wiki, and community Tech Notes/Tips.
- Details the 4DAF Control Panel's five tabs: About, General Prefs, Access Control (View/Sheet configuration, DDW buttons, Parent Record settings), Query Manager, and DDW Manager.
- Lists the eight back-end Project Method categories developers can hook into: Preferences, Authentication/Sessions, Data Modifications, Developer Created Selections (DCS), DDWs, Callbacks, Queries, and Lists.
- Notes that building fully custom HTML/JavaScript pages with 4DAF objects is possible and refers to a companion note (07-21, 4DAF Custom Data Grid) for that topic.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- 4DAF Control Panel and Admin Client
- Developer Defined Windows (DDW)
- Daxipedia documentation wiki

## Historical Context
Published August 2007, during the active but short-lived development of the subscription-based 4D Web 2.0 Pack, just before 4D v11 shipped native SQL support later that year. Predates Project Mode (v17) and ORDA by roughly a decade.

## Historical Commentary
**Status:** Obsolete

The 4DAF, 4D Web 2.0 Pack, and the Daxipedia wiki it repeatedly points to have all been discontinued, so the concrete installation steps, Control Panel tabs, and Project Method hooks described no longer apply to any current 4D product. The higher-level Web 1.0-to-Web 2.0 narrative remains an accurate historical description of that era's shift, but this note has no direct practical use for developers today, who would instead use 4D's built-in Web Server with REST/ORDA and modern JS frameworks.
