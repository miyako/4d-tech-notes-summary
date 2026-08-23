# Tech Note: 4D Macros in Version 2004

- **Asset ID:** 33006
- **Tech Note #:** 04-24
- **Published:** June 17, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Mac & Win
- **Author:** Jonathan Le, Technical Support, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=33006
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_21-25_(MAY)/04-24_4D_Macros_in_2004.hqx

## Overview

Jonathan Le documents two new Method Editor macro features in 4th Dimension 2004: storing macros across multiple XML files in a dedicated Macros folder, and a new `<method>` tag that lets a macro invoke an actual 4D project method rather than just insert static text, enabling dynamic, code-generating macros.

## Key Points

- Macros can now live in multiple XML files placed in a "Macros" folder next to the original Macros.xml in the active 4D directory, letting authors organize macros by relevance instead of maintaining one monolithic file.
- The `<macros>` tag is the top-level container; `<macro name="...">` describes an individual macro; single-value tags like `<selection/>`, `<caret/>`, `<user_4D/>`, `<user_os/>`, `<method_name/>`, `<time/>`, and `<clipboard/>` are self-closing and stand for dynamic values.
- The `<text>...</text>` tag holds the content inserted into the calling method; the new `<method>...</method>` tag executes a named 4D project method (optionally with parameters) the moment the macro runs.
- A `TestMacro` walkthrough shows generating a comment header with `<user_os/>`, `<time/>`, `<selection/>`, and `<caret/>`; a `FirstTable` example calls a project method that auto-generates field-assignment code (`[Table 1]Field 1:=` etc.) for the database's first table.
- A `TouchTable` example demonstrates calling a method with string parameters from within the macro to create a record, timestamp it, and open an output form -- illustrating that `<method>` calls behave just like a normal method invocation from a form, database, or project method.
- Table 3/4 in the note document the special `_textSel`, `_textMethod`, `_blobSel`, `_blobMethod`, `_selLen`, `_methodLen` input variables and `_textReplace`, `_blobReplace`, `_action` output variables that 4D manages for macro-driven text/BLOB substitution.
- Macros can be invoked via the new Macros toolbar item in the method editor, a right-click "Insert macro" context menu, or the auto-complete function.

## Featured Technology

- 4D Method Editor macros (Macros.xml)
- Multi-file macro storage in a Macros folder
- <method> tag for calling project methods from macros
- <text>, <selection>, <caret>, <user_4D>, <user_os>, <time>, <clipboard> macro tags
- _action / _blobReplace macro process variables
- Project method invocation with parameters from a macro

## Historical Commentary

**Status:** Superseded

This note documents 4D 2004's expanded Method Editor macro system, notably the new ability to store macros across multiple XML files in a Macros folder and the new `<method>` tag that lets a macro call a project method (for example, to auto-generate field-assignment code or create records) rather than just insert static text. The underlying macro mechanism and process-variable protocol (`_textReplace`, `_blobReplace`, `_action`) described here is specific to the classic, non-Project-Mode Method Editor and has been superseded by 4D's modern code editor and its own macro/snippet facilities introduced with Project Mode (2018 onward). The core productivity idea -- generating boilerplate/code via reusable macros -- remains valid and is still supported by current 4D tooling, just through different, more modern mechanisms.

**References to newer/updated information:**
- 4D's code editor and macro/snippet system were substantially modernized with Project Mode (introduced 2018), superseding the classic Method Editor's XML-based Macros.xml mechanism described here
- The specific `<method>`, `<text>`, and single-value tags, plus the `_textReplace`/`_blobReplace`/`_action` process variables, are tied to the legacy Method Editor and are not how current 4D code-generation features work
