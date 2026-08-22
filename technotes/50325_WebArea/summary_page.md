# Tech Note 08-25: Web Area in 4D v11 SQL

**Author:** Luis Pineiros, Technical Services Team Member, 4D Inc.
**Published:** July 2, 2008 | **Product/Version:** 4D SQL v11.2 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_25-29_(JUL)/08-25_Web_Area.zip

## Overview
With the release of 4D v11 SQL Release 2, the Web Area form object provides native, plug-in-free web browser integration into desktop forms. Web Area replaces the 4D Live Window plug-in, addressing deployment friction by eliminating the need for separate plug-in installation and licensing. By leveraging the host OS's rendering engine (WebKit on Mac, Internet Explorer's ActiveX controls on Windows), Web Area offers tight platform integration and automatic security sandbox enforcement.

## Key Points
- **No plug-in required:** Unlike 4D Live Window, Web Area is built into 4D v11 SQL Release 2 and later, eliminating installation/distribution hassles.
- **Native rendering engines:** Mac OS X uses Apple's WebKit (same engine as Safari), ensuring consistent rendering. Windows uses the ActiveX Web Control (Internet Explorer's rendering engine).
- **Automatic URL and progress variables:** Each Web Area auto-generates a URL variable (e.g., myWebArea_url, String type) for setting/reading the current URL, and a Progression variable (e.g., myWebArea_progress, Longint 0–100) for loading percentage.
- **Standard navigation actions:** Four built-in actions (Open Back URL, Open Next URL, Refresh Current URL, Stop Loading URL) can be assigned to buttons/menu items; they automatically disable when inapplicable (e.g., back button grayed out at the start of history).
- **URL lifecycle events:** Seven form events allow fine-grained control: On Begin URL Loading (fires at the start), On URL Resource Loading (for each resource, updates progress), On End URL Loading (all resources loaded), On URL Loading Error (with error information), On URL Filtering (for intercepting/blocking URLs), On Open External Link (handling links outside the area), and On Window Opening Denied (handling blocked popups).
- **Mac OS X protocol requirement:** URLs must include the protocol (http://www.example.com); bare hostnames (www.example.com) fail silently.
- **Compositing mode on Mac:** The form window containing a Web Area must run in compositing mode (Open Form type 4096), limiting some form features but enabling graphics-intensive content.
- **Rich content support:** Web Areas render HTML (static and dynamic), images, PDF, Flash, and JavaScript.
- **Multiple Web Areas:** A single form can contain multiple Web Areas, useful for tabbed/split layouts.
- **Menu and drag-drop integration:** Edit menu commands and context menu automatically work within Web Areas. Drag-and-drop of URLs and files is supported.
- **20+ Web Area–specific commands:** WA OPEN URL, WA GET CURRENT URL, WA GET LAST URL ERROR, WA GET LAST FILTERED URL, and others provide programmatic manipulation beyond the basic variable interface.

## Featured Technology
- Web Area form object (4D v11 SQL Release 2+)
- WebKit rendering engine (Mac OS X)
- Internet Explorer ActiveX Web Control (Windows)
- JavaScript execution in Web Areas
- URL navigation and history management
- Progress tracking during page loads
- Form events for URL lifecycle management

## Historical Context
Released in summer 2008, Web Area was a major usability improvement over the plug-in-based Live Window approach. At the time, web-embedded views within desktop applications were less common; Web Area positioned 4D as progressive in enabling seamless web/desktop integration. However, the broader industry trend since 2010 has been toward cloud-native, API-first architectures. Desktop applications using embedded web browsers became a niche use case, while web-first development (mobile apps, SPA frameworks) dominated. 4D itself eventually embraced this shift with Qodly (GA 2021) and REST APIs, shifting focus away from desktop-form-based development.

## Historical Commentary
**Status:** Still Relevant

Web Area remains a valid and functional feature in modern 4D versions (v11 through v20 and later), and it is genuinely useful for developers building desktop applications that need to embed dynamic web content (e.g., dashboards, reports, external integrations like Google Maps, YouTube embeds, custom HTML previews). However, new 4D development has increasingly moved toward REST API architectures and the Qodly low-code web platform, meaning Web Area is no longer a primary tool for greenfield projects. It is most relevant today for:
- **Desktop application developers** still building traditional 4D fat-client UIs who need to embed web content.
- **Legacy application maintainers** modernizing existing systems without a full rewrite.
- **Hybrid scenarios** where a 4D desktop application needs to display a web dashboard or third-party content.

For new web-first or mobile-first projects, developers should prioritize REST APIs and Qodly or external web frameworks (React, Vue, etc.). The conceptual value of Web Area—embedding browser views within a rich desktop environment—remains timeless, but its implementation and relevance have narrowed significantly since 2008.
