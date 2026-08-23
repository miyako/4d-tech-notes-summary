# Tech Note: User Defined Forms

- **Asset ID:** 34735
- **Tech Note #:** 04-45
- **Published:** November 11, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Sati Hillyer
- **Page URL:** https://kb.4d.com/assetid=34735
- **Download:** https://kb.4d.com/ftp://@ftp.4d.com/ACI_TECHNICAL_NOTES/2004/MacOS/TN_2004_41-45_(SEP)/04-45_User_Def_Forms.hqx

## Overview

Sati Hillyer (4D Evangelist) introduces 4D 2004's User Defined Forms, which let an end user customize a form's layout at runtime -- even inside a compiled, merged application -- via a simplified Form Editor invoked with the new EDIT FORM command, with user customizations preserved separately from the developer's original "source" form in a dedicated User Structure File (.4DA).

## Key Points

- Explains the "Editable by User" form property in the Design environment, which unlocks end-user editing via EDIT FORM and locks the "source" form in Design mode (requiring a lock icon click to re-edit it), with property-level locking controlling exactly which graphic properties/actions users may alter.
- Shows the two usage models: calling `EDIT FORM([Table];"FormName";"";objectLibraryPath)` directly against the source form for one-off quick fixes (with the customized result auto-saved to the .4DA User Structure File), versus using `CREATE USER FORM([Table];"FormName";vNewName)` to stamp out many independently named duplicates of a template form (e.g. per-department forms), managed with `LIST USER FORMS` and `DELETE USER FORM`.
- Demonstrates a university vertical-market scenario where Accounting, Scholar, and Admission each get their own duplicated user form via `CREATE USER FORM`, then are independently customized via `EDIT FORM`, and finally displayed via `INPUT FORM([Students];"InputForm";vRequestedForm)`/`OUTPUT FORM` with the requested user form name.
- Covers Scenario 3's solution to the "source form changes obsolete existing user forms" problem: combining 4D's existing parent/child inherited form system with User Defined Forms, so the child (inheriting from the parent) is the "source" that spawns user forms, and developers make ongoing updates only to the parent, leaving in-flight user customizations intact.
- Notes an internal revision counter stored in the structure file: every save of a "source" form increments it, and 4D compares this against the counter in the .4DA file to decide whether existing user forms are still current or have become obsolete.
- Documents 4D 2004's new error codes for this feature (-9750 Form is not editable, -9751 Not enough privilege, -9753 Source form does not exist, -9754 EDIT FORM called from a DIALOG, -9755 Creating an unnamed user form, -9757 User form does not exist, -9758 User form already exists) and lists other commands compatible with user-defined forms (ADD RECORD, MODIFY RECORD, DISPLAY RECORD, MODIFY/DISPLAY/PRINT SELECTION, PRINT LABEL, PRINT RECORD, QUERY BY EXAMPLE, DIALOG).

## Featured Technology

- EDIT FORM command (runtime, simplified Form Editor for end users)
- CREATE USER FORM / LIST USER FORMS / DELETE USER FORM commands
- Editable by User form property and User Structure File (.4DA)
- Inherited (parent/child) forms combined with User Defined Forms
- INPUT FORM / OUTPUT FORM extended with a user-form parameter

## Historical Commentary

**Status:** Partially superseded

Sati Hillyer, a 4D Evangelist, presents 4D 2004's new User Defined Forms feature, which lets end users customize forms at runtime -- even in a compiled, merged application -- via EDIT FORM, CREATE USER FORM, LIST USER FORMS, and DELETE USER FORM, with per-user customizations stored in a separate .4DA User Structure File so the developer's original "source" form stays intact, and shows combining this with 4D's inherited (parent/child) form system so developers can push updates without wiping out user customizations. This runtime form-customization mechanism belongs to the classic Design Mode form architecture; while EDIT FORM and the User Defined Forms commands still exist in 4D, this style of binary form customization has been largely superseded in modern development by 4D's forms-as-JSON architecture in Project Mode and by more flexible client-side/ORDA-driven UI approaches, particularly for web and Qodly-based applications.

**References to newer/updated information:**
- 4D's Project Mode (introduced v17, 2018) stores forms as JSON/text files, which are easier to version, diff, and dynamically manipulate than the classic binary form + .4DA User Structure File model described here
- The EDIT FORM/CREATE USER FORM/LIST USER FORMS/DELETE USER FORM commands still exist in 4D for classic-mode form customization scenarios
- Modern 4D web and Qodly-based UIs offer alternative, more dynamic approaches to end-user interface customization beyond the classic form editor
