# Tech Note 17-15: Managing web content for multiple languages

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** August 31, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77834
**Download:** https://kb.4d.com/DLTN/TN/2017/17-15_ManageMultiWebLang.zip

## Proposition
This Tech Note demonstrates a cookie-based approach to serving multilingual web content from a single URL through a 4D Web Server, using the On Web Connection method to detect a visitor's language preference and route to the correct localized page.

## Key Points
- **Problem framing:** a single 4D web server URL should transparently serve content matching the visitor's language preference.
- **Page organization:** web pages are organized into per-language folders/structures.
- **Cookie-based persistence:** a language cookie is set once chosen and checked on subsequent requests.
- **Accept-Language fallback:** the browser's Accept-Language header is read when no cookie yet exists.
- **Central routing:** all logic is unified inside the On Web Connection method.
- **Demo database:** shows menu-based language switching, cookie setting, and persistence across browser sessions.

## Featured Technology
- 4D Web Server
- HTTP cookies
- On Web Connection method
- Accept-Language HTTP header

## Best Practices Highlighted
1. Use cookies to persist a visitor's language choice across page requests.
2. Fall back to the Accept-Language header when no explicit preference cookie exists.
3. Organize localized content by language folder for maintainability.

## Context / Positioning
Published in 2017 for classic 4D v16, this note reflects a period when 4D web applications were commonly built as server-rendered pages managed through On Web Connection, prior to the rise of SPA frontends and client-side i18n libraries now common in modern 4D-backed web apps.

## Historical Commentary
**Status:** Still relevant

The cookie- and header-based localization technique described here remains technically valid and the On Web Connection mechanism still exists in current 4D. That said, the broader industry trend (and much modern 4D web development) has shifted toward client-side frontend frameworks with their own i18n libraries, making server-side cookie routing one option among several rather than the default approach it may have been in 2017.
