# Tech Note: 4D Web Serving Using Perl CGIs

- **Asset ID:** 12147
- **Tech Note #:** 01-07
- **Published:** February 28, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jon Baltazar
- **Page URL:** https://kb.4d.com/assetid=12147
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_06-10_(FEB)/01-07_Web_Serving_Perl_CGI.hqx

## Overview

Jon Baltazar of 4D, Inc. Technical Support demonstrates 4D v6.7's new ability to call external CGI programs — specifically five Perl scripts (a hit counter, a script-call counter, a hello-world demo, a question/answer board, and a site redirector) — from a Non-Contextual 4D web server, covering installation, the platform-specific CGI types supported, and how HTML tags invoke them.

## Key Points

- Requires Non-Contextual web-serving mode (developer-authored HTML, no auto-generated pages by 4D) with Database Properties set to Publish Database at Startup, Start without Context, and a Default HTML Root ('/') and Home Page.
- All CGI scripts must be placed in a cgi-bin folder located alongside the 4D structure file; scripts are invoked via a URL, an HTML action, or an embedded HTML tag containing /cgi-bin/ followed by the script name and any search string.
- Documents platform-specific CGI types: Windows supports .exe/nph-*.exe executables and ISAPI .dll extensions; Mac OS supports WebSTAR/MacHTTP .cgi/.acgi applications; Perl scripts (xxx.pl/xxx.cgi/nph-*) are cross-platform but require ActivePerl (Windows) or MacPerl (Mac OS) as an interpreter.
- Notes operational constraints: a CGI call never modifies 4D's own environment (selection, variables, etc.), CGI processing is capped at 30 seconds, and CGI's returning HTML in Contextual mode risk desynchronizing 4D's context.
- The sample database's img_counter.pl is invoked via an <img src> tag referencing a count.txt data file to implement a homepage hit counter; counter.pl reports how many times it has itself been executed.
- hello_world.pl demonstrates the minimal CGI call/response cycle; qa.pl implements a question/answer board backed by three text files (ans.txt, many.txt, quest.txt); redirect.pl presents a dropdown of sites and redirects the browser to the chosen URL.

## Featured Technology

- 4D Web Server Non-Contextual mode
- CGI invocation via cgi-bin folder
- Perl CGI scripts (ActivePerl / MacPerl)
- HTML tags calling external CGI executables
- Database Properties: Publish at Startup / Start without Context

## Historical Commentary

**Status:** Obsolete

Written by Jon Baltazar of 4D, Inc. Technical Support, this note explains how 4D v6.7's newly added CGI support let a Non-Contextual 4D web server delegate specific tasks (hit counters, guestbooks, redirects, Q&A pages) to external Perl scripts placed in a cgi-bin folder, invoked from hand-authored HTML pages. This entire 'shell out to an external CGI/Perl process' pattern for extending 4D's web server has been superseded first by native 4D web-serving commands and then decisively by 4D's move to REST APIs on ORDA and separate modern application/web servers, making CGI-based extension a historical curiosity rather than a technique developers reach for today.

**References to newer/updated information:**
- 4D's web serving model has moved away from CGI-based extension entirely, toward native 4D web server commands and, more recently, REST APIs built on ORDA
- Modern 4D web applications typically rely on JavaScript front-ends or components like Qodly rather than delegating tasks to external CGI executables
