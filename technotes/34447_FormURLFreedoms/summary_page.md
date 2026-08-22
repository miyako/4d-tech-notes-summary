# Tech Note 04-42: 4th Dimension 2004 Allows New Freedoms in Form URLs

**Author:** David Adams
**Published:** October 21, 2004 | **Product/Version:** 4th Dimension v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=34447
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_41-45_(SEP)/04-42_Change_Get_Web_Form.pdf

## Overview
This note explains a significant 4D 2004 Web Server change: developers gained full freedom to use any URL for form submissions, whereas previously URLs had to start with the special keywords 4DACTION, 4DCGI, or 4DMETHOD for POST form data to be retrievable at all.

## Key Points
- In prior 4D versions, POST form data was stripped from `On Web Authentication`'s $2, `On Web Connection`'s $2, and `GET WEB FORM VARIABLES` arrays unless the URL began with 4DACTION, 4DCGI, or 4DMETHOD — with no workaround.
- Each special keyword triggers a distinct processing chain: 4DACTION runs `Compiler_Web`, `On Web Authentication`, then the named method; 4DCGI runs `Compiler_Web`, `On Web Authentication`, then `On Web Connection`; 4DMETHOD runs `On Web Authentication`, `On Web Connection`, then the named method in contextual mode.
- Custom/unknown URLs already followed the same processing sequence as 4DCGI requests in both 4D 2003 and 2004 — what's new in 2004 is that POST data is now actually populated for such requests.
- Developers can now use arbitrary URLs (e.g. `/cgi-bin/process_form.php`, `/forms/search/`) for policy, security, aesthetic, commercial, or usability reasons while still retrieving submitted form values.
- The recommended pattern is to call `GET WEB FORM VARIABLES` once in `On Web Authentication` and store results in process arrays for reuse throughout the request.

## Featured Technology
- 4th Dimension built-in Web Server
- GET WEB FORM VARIABLES command
- On Web Authentication / On Web Connection database methods
- 4DACTION / 4DCGI / 4DMETHOD special URL keywords

## Historical Context
Published as 4D 2004 loosened a longstanding Web Server URL naming restriction, this note reflects a period when 4D developers were expected to work directly with raw HTTP form submissions and custom database methods rather than a higher-level web framework. The specific commands (GET WEB FORM VARIABLES, On Web Authentication, On Web Connection) remain supported in current 4D for classic web publishing, so the technique still works, but 4D's web development focus has since moved decisively toward REST APIs built on ORDA (2018+) paired with modern client-side frameworks, making this kind of raw URL/form handling a legacy pattern for new development.
