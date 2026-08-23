# Tech Note: Advanced Method Editor Macros

- **Asset ID:** 35423
- **Tech Note #:** 05-01
- **Published:** January 6, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jonathan Le
- **Page URL:** https://kb.4d.com/assetid=35423
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_01-04_(JAN)/05-01_AdvMethodEdtiorMacros.hqx

## Overview

Jonathan Le (Technical Support, 4D, Inc.) explains 4D 2004's expanded Method Editor Macro language, centered on the new `method` tag that lets a macro call any project method in the current database -- transforming macros from static code-snippet tools into interactive, code-generating and code-manipulating utilities.

## Key Points

- Recaps pre-2004 macros as simple, predefined code-snippet generators (e.g. the built-in "If" macro producing `If( )` / `End If`), stored as XML files in the system-level "Active 4D" folder (with a default `Macros.xml` plus an optional `Macros` subfolder for additional files).
- Documents the macro tagging language in detail: `<macros>`/`<macro name="...">` wrappers, `<text>` bodies, and inline tags `<caret/>` (cursor placement), `<selection/>` (inserts highlighted text), `<user_os/>`, `<date format="...">`, `<time format="...">`, `<method_name/>`, and the new `<method>...</method>` tag for invoking a project method.
- Walks through an "IfWrap" macro example that extends the stock "If" macro by adding `<selection/>` so a highlighted line of code gets wrapped in `If(<caret/>) ... End If`.
- Documents the special process variables available to a method called via the macro tag -- inputs `_textSel`/`_blobSel`/`_selLen`/`_textMethod`/`_blobMethod`/`_methodLen` and outputs `_textReplace`/`_blobReplace`/`_action` (0=none, 1=insert text, 2=insert blob, 3=replace method with text, 4=replace method with blob) -- illustrated with a "ReverseIt" macro that reverses highlighted text.
- Presents a "Variable Wizard" example showing a macro-called project method that opens a dialog form (`Open form window`, `DIALOG`), collects variable types/names into arrays, and generates 4D compiler declarations (`VARIABLE_TYPE($variableName)`) inserted into the method editor via `_blobReplace` and `_action:=2`.
- Advises spawning new processes for macros that display forms (since the macro call executes in a process similar to the Custom Menus/User Environment process, which stays locked while the macro runs) and using blobs instead of 32,000-character-limited text variables for larger code manipulation.
- References the bundled Macro Pack component's ready-made macros for auto-documentation, assigning named parameters, organizing declarations, and generating SOAP declarations.

## Featured Technology

- 4D Method Editor Macros (XML macro files, Active 4D folder)
- <method> macro tag (calling project methods from a macro)
- Macro tagging language (<macro>, <text>, <caret/>, <selection/>, <user_os/>, <date/>, <time/>, <method_name/>)
- Special macro process variables (_textSel, _blobSel, _textReplace, _blobReplace, _action)
- Macro Pack component (auto-documentation, parameter assignment, SOAP declarations)

## Historical Commentary

**Status:** Superseded

Jonathan Le documents the biggest upgrade to 4D's Method Editor macro language since its 2003 introduction: the new <method> tag, which lets a macro call any project method in the calling database, turning macros from static code-snippet generators into interactive, code-executing tools (illustrated with a string-reversal macro and a dialog-driven "Variable Wizard" that generates compiler declarations). This XML-tag-based macro system was specific to the classic Design Mode method editor and Macro Pack component; it has been superseded by the vastly more capable code editor, snippet, and extension/plugin architecture of modern 4D (v19+ code editor, Project Mode), though the core idea of code-generation macros driven by user-selected text persists in spirit in modern editor snippets.

**References to newer/updated information:**
- 4D's modern code editor (introduced with Project Mode/v19+) offers far richer code snippet, auto-completion, and refactoring tools than the classic XML macro system described here
- The Macro Pack component referenced in this note is a legacy artifact of the classic Design Mode era
- The core productivity goal -- reducing repetitive typing during method editing -- is now addressed by modern editor features rather than XML-tagged macro files
