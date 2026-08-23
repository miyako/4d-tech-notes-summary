# Tech Note: The OPEN WEB URL Command

- **Asset ID:** 13097
- **Tech Note #:** 01-15
- **Published:** March 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hussey
- **Page URL:** https://kb.4d.com/assetid=13097
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_11-15_(MAR)/01-15_OPEN_WEB_URL.hqx

## Overview

Steve Hussey (CEO, Alto Stratus LLC) provides a compact reference for 4D's `OPEN WEB URL` command, which passes a URL string to the user's default application for that URL's protocol type — a web browser for http(s), a mail client for mailto:, or an FTP client for ftp:. The note demonstrates each use case with concrete syntax examples and covers a special case for opening local HTML files as a simple help system.

## Key Points

- Web sites can be opened with a full URL (`OPEN WEB URL("http://www.jumpstart-4d.com")`) or a partial one many browsers accept (`OPEN WEB URL("www.jumpstart-4d.com")`); the URL string can be stored in a variable or field and is not validated by 4D itself.
- E-mail composition uses `mailto:` links, e.g. `OPEN WEB URL("mailto:shush@harborside.com")`, extendable with `?subject=` and `?body=` query parameters to pre-fill a new message.
- Since 4D's own carriage return/line feed characters (ASCII 13/10) can't be embedded directly in the mailto body, the note shows using the percent-encoded equivalents `%0D` (Mac OS) and `%0D%0A` (Windows) to insert line breaks in the message body.
- FTP sites are opened the same way, e.g. `OPEN WEB URL("ftp.4d.com")`, launching the user's default FTP client.
- Local HTML files can be opened with a `file:///` URL (e.g. `"file:///MyDrive/myfolder/file.html"`), where the triple slash separates the protocol from a root-level path using the standard Unix `/` delimiter regardless of the underlying OS.
- The author suggests this local-file technique as a simple way to build a context-sensitive help system: buttons throughout a 4D application can open specific HTML pages stored alongside the application, letting users navigate help using their familiar web browser interface.

## Featured Technology

- OPEN WEB URL command
- mailto: links with subject/body query parameters
- ftp:// URL launching
- file:/// local HTML file opening
- URL percent-encoding for carriage return/line feed (%0D/%0A)
- Default-application URL dispatch (browser/mail client/FTP client)

## Historical Commentary

**Status:** Still relevant

Steve Hussey's note is a straightforward reference for 4D's OPEN WEB URL command, covering how to launch the user's default browser for http(s) sites, compose pre-filled e-mails via mailto: links (including percent-encoded line breaks in the body), connect to FTP sites, and open local HTML files as a lightweight context-sensitive help system. OPEN WEB URL remains part of the current 4D language and this technique still works exactly as described, though for building help systems specifically, many developers today would reach for 4D's built-in Help/Info features or a modern web-based help viewer rather than raw local file:/// links.

**References to newer/updated information:**
- OPEN WEB URL is unchanged and remains a standard 4D command for launching URLs in the user's default applications
- Modern 4D applications building in-app help more often use dedicated documentation viewers or web-based help systems rather than local file:/// HTML pages, though the underlying technique described here still functions
