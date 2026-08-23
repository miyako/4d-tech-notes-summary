# Tech Note: Working with 4D Dialogs within a Plug-in

- **Asset ID:** 23238
- **Tech Note #:** 02-21
- **Published:** May 15, 2002
- **Product / Version:** 4D Open 6.8
- **Platform:** Mac & Win
- **Author:** Christian Cypert, 4D & WebSTAR Plug-in Evangelist
- **Page URL:** https://kb.4d.com/assetid=23238
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_20-24_(MAY)/02-21_Dialogs_in_a_Plug-in.hqx

## Overview

Christian Cypert demonstrates how to embed a 4D-designed dialog resource inside a compiled 4D plug-in, using a database login/security screen as the running example. The technique lets a plug-in reuse a dialog built visually in 4D (rather than constructing the UI from scratch in C/C++) and drive it through the classic 4D Plug-in API's modal dialog loop.

## Key Points

- The 4D-side dialog is built with two 40-character string variables, `vs40_Username` and `vs40_Password`, plus "Log-In" and "Quit" buttons; the Quit button's method simply calls `QUIT 4D`.
- Pressing Command-9 (Mac) / Ctrl-9 (Windows) in the Structure window saves the table's dialogs to a resource file on disk; the note recommends creating an empty table in an isolated database just to hold the plug-in's dialog, to avoid bloated resource files.
- In the Plug-in Wizard, a new command `sc_openSecurity` is created taking two `PA_Pointer` parameters (`PassField`, `UserField`) pointing to the database's password and username fields, with the "use 4D Dialog file" option checked and the saved resource file attached.
- The C implementation validates the pointers with `PA_GetPointerKind`/`ePK_PointerToField`, resolves table/field numbers via `PA_GetPointerTableField`, then opens the dialog with `PA_NewDialog` + `PA_OpenDialog("sc_SecurityForm", 1)`.
- A `do...while` loop calls `PA_ModalDialog(dialog, lastVarName)` to detect the Log-In click, reads the entered strings with `PA_Dial4DGetString`, and runs a query using `PA_OpenQuery` / `PA_QueryString` (`eQO_NoOperator` / `eQO_LogicalAND`, `eQC_IsEqual`) / `PA_CloseQuery`.
- `PA_RecordsInSelection` result drives the outcome: 0 records triggers "No Username or Password found", exactly 1 record sets `okOrCancel` to dismiss the dialog and grant access, and more than 1 record alerts the user to contact the System Administrator (since usernames should be unique).
- The dialog is finally closed with `PA_CloseDialog`, and the compiled plug-in is placed in the `4DX` folder for use by the host database.

## Featured Technology

- 4D Plug-in API (PA_ commands)
- 4D Dialog resource embedded in a plug-in
- PA_NewDialog / PA_OpenDialog / PA_ModalDialog / PA_CloseDialog
- PA_Dial4DGetString
- PA_OpenQuery / PA_QueryString / PA_CloseQuery
- PA_GetPointerParameter / PA_GetPointerTableField

## Historical Commentary

**Status:** Superseded

This note walks through building a compiled C/C++ plug-in that embeds a 4D Dialog resource (a login screen) and drives it with the classic Plug-in API's modal-dialog loop and query commands to validate a username/password pair. The classic 4D plug-in API (PA_* calls) and 4D Dialog resource mechanism it relies on have been superseded by 4D's modern component and plug-in architecture, so the specific implementation shown is dated. The underlying idea -- a password-gated dialog controlling database access -- is still common, but a modern 4D application would implement it directly in 4D code (with On Load/On Clicked form events and native QUERY) rather than via a bespoke compiled plug-in.

References to newer/updated information:
- 4D's classic Plug-in API (PA_* functions, 4D Dialog resources) has been superseded by 4D's modern plug-in/component architecture and the modern 4D language, making compiled-plug-in dialogs like this one unnecessary for most use cases
- A password-gated login dialog is now typically built directly in 4D form code rather than as a separate C/C++ plug-in
