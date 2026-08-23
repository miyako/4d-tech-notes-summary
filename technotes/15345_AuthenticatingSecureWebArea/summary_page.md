# Tech Note: Authenticating Access to a Secure Area within a Web Site

- **Asset ID:** 15345
- **Tech Note #:** 01-26
- **Published:** June 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar
- **Page URL:** https://kb.4d.com/assetid=15345
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_26-30_(JUN)/01-26_Web_Authentication.hqx

## Overview

Jonathan Baltazar (4D, Inc.) surveys three distinct techniques for securing pages of a website served by 4D, illustrated with the "Web Exam" example database (a student exam/login system), covering fully custom application-level logins, 4D's built-in Password System, and the flexible On Web Authentication database method.

## Key Points

- Custom login approach: the "Web Exam" login page (`cert.html`) posts username/password to a `/4DACTION/W_Cert` action, whose `W_cert` method runs `QUERY([Students];[Students]Name=User)` and routes the browser via `SEND HTML FILE` to the exam, a retry page, or a name-error page depending on whether exactly one matching, verified record is found.
- Built-in Password System approach: creating non-default users in the Password Editor and enabling "Use Passwords" + "Include 4D Passwords" in the Web Server II database properties makes 4D display its own login dialog automatically — but only if no `On Web Authentication` method exists, since its presence tells 4D the developer wants custom control.
- `On Web Authentication` receives six text parameters — `$1` URL, `$2` full HTTP header+body, `$3` client IP, `$4` server IP, `$5` username, `$6` password — and must return Boolean `$0` (True = accept connection, False = reject/prompt); the note shows viewing `$2`'s full contents by pasting into a text editor to inspect real request headers.
- Example `On Web Authentication` code validates users via `GET USER LIST`/`Find in array`/`Is user deleted` against 4D's own user list, falling back to a `QUERY([Students]; ...)` check against the Students table for non-4D users, with a `WithWildcard` helper method rejecting `@`-containing (wildcard) usernames/passwords as a security measure.
- Explains that disabling "Include 4D Passwords" while keeping "Use Passwords" means the developer must fully implement username/password verification themselves via table lookups.
- Closes with compatibility notes: 4D Link (WebSTAR) and `nph-cgi4d.exe` (Apache for Windows) support all three approaches, but `4DISAPI.dll` (IIS) only works with a fully custom password system since IIS doesn't forward the `$5`/`$6` username/password parameters to 4D.

## Featured Technology

- 4DACTION-based custom login (Web Exam example database)
- SEND HTML FILE for conditional page routing
- 4D built-in Password System (Use Passwords / Include 4D Passwords)
- On Web Authentication database method (6 parameters, Boolean $0)
- GET USER LIST / Is user deleted for 4D user validation
- 4D Link / nph-cgi4d.exe / 4DISAPI.dll web-server-gateway compatibility notes

## Historical Commentary

**Status:** Partially superseded

The high-level authentication strategies this note surveys — application-level login tables, 4D's built-in user/password system, and a custom authentication hook — remain conceptually sound approaches to securing web access today. However, the specific implementation details are tied to 4D's original built-in Web Server and its era-specific gateway options (4D Link/WebSTAR, nph-cgi4d.exe, 4DISAPI.dll), all of which have been superseded by 4D's modern, rewritten web server and by REST/ORDA-based authentication mechanisms (session tokens, standard HTTP auth schemes) that didn't exist in 2001, making the specific code and configuration steps here dated even though On Web Authentication itself is still supported.

**References to newer/updated information:**
- 4D's web server architecture was substantially rewritten in later 4D versions (moving away from the CGI-era 4D Link/nph-cgi4d.exe/4DISAPI.dll gateway model described here)
- Modern 4D web/REST authentication commonly uses session tokens and standard HTTP authentication schemes rather than the On Web Authentication six-parameter method shown, though On Web Authentication itself remains available in current 4D versions
- 4D's REST/ORDA APIs provide additional, more modern mechanisms for securing programmatic access to data that did not exist in 2001
