# Tech Note: Web Assistant for Dummies

- **Asset ID:** 11993
- **Tech Note #:** 00-54
- **Published:** November 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar
- **Page URL:** https://kb.4d.com/assetid=11993
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_51-55_(NOV)/00-54_Web_Assistant.hqx

## Overview

Jonathan Baltazar of 4D, Inc. Technical Support walks through installing and configuring 4D v6.7's no-code Web Assistant component, which lets developers publish selected database tables to the web with configurable per-user access, list/detail/search views, and HTML page customization — demonstrated end-to-end on the sample Music_Library database.

## Key Points

- Installing into an existing database requires 4D Insider's Components menu (Install/Update) plus manual edits to On Web Connection (add wbaOnWebConnect), On Web Authentication (call wbaOnWebAuthentication), and for 4D Server, On Server Startup/On Server Shutdown (wbaStartWeb/wbaQuitWeb); new databases can instead simply check 'Install 4D Web Assistant' at creation time.
- Required Database Properties settings: uncheck Publish Database at Startup, check Start without Context (Web Server I tab), and check Use Passwords (Web Server II tab).
- The wbaPalette floating palette exposes Start/Stop Web Service, Set Tables and Fields (User Access), HTML Editor, and Appearance Editor as the four core functions of the component.
- Set Tables and Fields configures, per user (including an automatic Guest user for anonymous browsers), which tables are visible and what access level applies via letter codes: 'r' read-only, 'a' add, 'm' modify, 'd' delete — plus separate List View (sort field/order, records per page), Detail View (field selection), and Search Fields configuration per table.
- The HTML Editor customizes headers/footers for the Home, Login, List View, Detail View, Search Screen, and Message pages using predefined tags such as <!--Message-->, <!--NavBar-->, <!--DatabaseName-->, <!--Another4Dsolution-->, <!--Login-->, <!--LoginPict-->, and <!--SearchPict-->, while still allowing standard hand-written HTML alongside them.
- A full walkthrough publishes the Music_Library sample database (Album, Artist, Tracks tables) with Guest given 'd' (full) access, custom sort order and field selection for List/Detail/Search views, and a customized Home page message and navigation bar, demonstrating the complete configuration flow.

## Featured Technology

- 4D Web Assistant component (4D Extensions folder)
- wbaPalette / wbaOnWebConnect / wbaOnWebAuthentication
- User Access table/field permission configuration (r/a/m/d)
- Web Assistant HTML Editor and Appearance Editor tags

## Historical Commentary

**Status:** Obsolete

Written by Jonathan Baltazar of 4D, Inc. Technical Support, this note introduces the 4D v6.7 Web Assistant, a no-code component that let developers publish selected tables and fields to the web with configurable per-user read/add/modify/delete access, customizable list/detail/search HTML pages, and appearance settings, all without writing 4D web-serving code by hand. The entire code-free, wizard-driven publishing model of the Web Assistant has been superseded by 4D's move to REST APIs on ORDA combined with modern JavaScript front-ends, and more recently by low-code tools like Qodly Studio, making the specific Web Assistant component and its wba*/HTML-tag mechanics obsolete for current web development, even though the underlying goal of quickly publishing table data to the web without hand-coding persists in these newer tools.

**References to newer/updated information:**
- The 4D Web Assistant component itself has been discontinued; 4D's web publishing strategy moved to REST APIs on ORDA combined with modern JavaScript front-ends
- 4D Qodly Studio now offers a modern low-code alternative for quickly building and publishing data-driven web interfaces without hand-writing web-serving code
