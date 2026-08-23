# Tech Note: Process HTML Tags and more!

- **Asset ID:** 35116
- **Tech Note #:** 04-49
- **Published:** December 9, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Julien Feasson
- **Page URL:** https://kb.4d.com/assetid=35116
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_49-50_(NOV)/04-49_Process_HTML_Tags.hqx

## Overview

Julien Feasson (Software Engineer, 4D Inc.) presents PROCESS HTML TAGS, new in 4D 2004, as a command that brings 4D's web-server tag language (4DVAR, 4DSCRIPT, 4DLOOP, etc.) to any text or blob outside the context of the Web server -- demonstrated through templated email generation, Word XML mail merge, and externally executed maintenance scripts.

## Key Points

- Documents the full 4D tag set usable by PROCESS HTML TAGS: `4DVAR`/`4DHTMLVAR` to insert expressions, `4DSCRIPT` to call a 4D method with a string parameter, `4DINCLUDE` to nest templates, and `4DIF`/`4DELSE`/`4DENDIF` plus `4DLOOP`/`4DENDLOOP` for conditional and iterative logic within the template text.
- Explains that `PROCESS HTML TAGS(input; output)` takes text or blob parameters and processes the tags without requiring the 4D Web server to even be started, and that tag behavior can differ outside a Web process (e.g. `4DINCLUDE`'s default folder becomes the structure file's folder).
- Example #1 shows generating a personalized email from a template with conditional phone fields (`<!--#4DIF [PEOPLE]HomePhone#""-->`), processed with two lines: `PROCESS HTML TAGS([EmailTemplates]Subject;processedSubject)` and the equivalent for the Body.
- Example #2 demonstrates mail merge into Microsoft Word 2003's newly-opened XML file format by embedding 4D tags directly inside a saved Word XML template, letting `PROCESS HTML TAGS` populate fields like OfficePhone conditionally before the file is opened in Word.
- Example #3 covers running external "4D Scripts" -- text files or documents embedding 4D tags including `4DSCRIPT` calls and `4DLOOP`/`4DIF` logic -- to perform maintenance/config updates against a running compiled server without shutting it down or recompiling, since the script is just processed text.
- Covers security safeguards: `4DSCRIPT` only calls methods with the "Available through 4DACTION, 4DMETHOD and 4DSCRIPT" flag enabled and consults `On Web Authentication`, but warns that arbitrary 4D commands (e.g. `<!--#4DIF (QUIT 4D=0)--><!--#4DENDIF-->`) can be embedded, and recommends `ENCRYPT BLOB`/`DECRYPT BLOB` plus `DOCUMENT TO BLOB` to protect and verify externally stored scripts before executing them.

## Featured Technology

- PROCESS HTML TAGS command
- 4D HTML/template tags (4DVAR, 4DHTMLVAR, 4DSCRIPT, 4DINCLUDE, 4DIF/4DELSE/4DENDIF, 4DLOOP/4DENDLOOP)
- Template-driven email generation and Microsoft Word XML mail-merge
- External 4D script execution via text-file templates
- ENCRYPT BLOB / DECRYPT BLOB for securing external scripts

## Historical Commentary

**Status:** Partially superseded

Julien Feasson, a 4D Software Engineer, champions PROCESS HTML TAGS -- new in 4D 2004 -- as what he calls the most powerful command in the language, because it lets the classic 4D web-server tag language (4DVAR, 4DSCRIPT, 4DIF, 4DLOOP, etc.) be applied to any text, not just pages served by the Web server, enabling templated email generation, Word XML mail merge, and even executing external 4D scripts against a compiled server without recompiling. This 4D-tag templating approach was the primary way to do dynamic templating/scripting in the mid-2000s; it has since been substantially superseded for general text/document generation by 4D's native JSON, string-formatting, and modern web/ORDA capabilities, though PROCESS HTML TAGS and the underlying 4D tag language remain part of 4D today and are still used, particularly in legacy 4D web applications.

**References to newer/updated information:**
- PROCESS HTML TAGS and the 4D tag language (4DVAR, 4DSCRIPT, etc.) still exist in current 4D versions and remain usable for legacy templating needs
- Modern 4D development favors native JSON, string manipulation commands, and the QodlyApp/ORDA ecosystem over 4D-tag-based templates for new development
- The described technique of running external, unsigned/plaintext scripts against a production server is now generally discouraged in favor of more secure deployment and update mechanisms
