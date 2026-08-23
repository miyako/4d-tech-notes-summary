# Tech Note: Understanding the 4D Password System

- **Asset ID:** 18204
- **Tech Note #:** 01-41
- **Published:** September 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon, Quality Assurance Manager, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=18204
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_41-45_(SEP)/01-41_Password_System.hqx

## Overview

Jean-Yves Fock-Hoon (Quality Assurance Manager, 4D, Inc.) gives a thorough tour of 4D's built-in, structure-file-embedded password system -- its dual Designer/Administrator user stores, group-based Access/Owner controls on objects, tables, and plug-ins, and how to layer custom password-expiration and account-lockout logic on top using the native user/group commands.

## Key Points

- Two independent password systems live in every structure file: the Designer's system (permanent, cannot be transferred to another structure file -- losing it means losing the database) and the Administrator's system (portable between structure files via Save Groups/Load Groups in the Password Editor's Passwords menu).
- Object-level security is granted per-form, per-method, per-menu-item, and per-plug-in via Access (who can load/use) and Owner (who can edit in Design mode) group pop-ups; the default is "All groups," and a Privilege error is raised if the current user isn't a member of the required group.
- Per-table record access (Load/Add/Modify/Delete) and table Owner are set individually from each table's Properties window -- there is no global switch to apply access rules to every table at once.
- Database Properties expose four additional group-based gates: 4D Open Access, Structure Access (entering Design mode), User Mode access, and a Default User setting; if no password is given to the Designer, the current user is always the Designer with an empty-string password and full implicit group membership.
- The User_and_Groups example database demonstrates EDIT ACCESS/CHANGE ACCESS commands plus GET USER LIST/GET USER PROPERTIES/Set user properties and GET GROUP LIST/GET GROUP PROPERTIES/Set group properties, including drag-and-drop group-membership editing and distinguishing Designer-created (negative) vs. Administrator-created (positive) user/group IDs.
- A custom Users table (User_ID/User_ChangePassword/User_DateRequiresChanged/User_OldPassword/User_Locked) layered on top implements forced password expiration, password-history checks, and account lockout, using CHANGE PASSWORD/Set user properties and the Validate password command -- capabilities the native 4D password system doesn't provide by itself.

## Featured Technology

- Designer's vs. Administrator's dual password systems
- GET USER LIST/GET USER PROPERTIES/Set user properties/GET GROUP LIST/GET GROUP PROPERTIES/Set group properties
- EDIT ACCESS and CHANGE ACCESS commands
- CHANGE PASSWORD and Validate password commands
- Per-object/per-table Access and Owner group assignment
- Save Groups/Load Groups Administrator system portability

## Historical Commentary

**Status:** Still Relevant

Jean-Yves Fock-Hoon explains 4D's built-in, structure-file-embedded password system in depth: its two parallel Designer's and Administrator's user/group stores, how Access/Owner group assignments gate forms, methods, menu items, plug-ins, and per-table record operations, and how to layer custom logic (forced password changes, expiration, account locking, an extra login screen) on top using commands like GET/Set user properties, Validate password, and CHANGE PASSWORD. The 4D language commands and password-system architecture described here (Designer/Administrator split, group-based object access, EDIT ACCESS/CHANGE ACCESS) remain fundamentally the same in current 4D versions, making this a still-accurate reference for the classic 4D privilege model, though modern projects increasingly pair or replace it with web-session/token-based authentication (e.g., for REST/ORDA endpoints) rather than relying solely on the desktop password system.

References to newer/updated information:
- The core 4D password/privilege commands and Designer/Administrator group model described here are still present and used the same way in current 4D versions
- Modern 4D web/REST/ORDA applications commonly add session- or token-based authentication layered on top of (or instead of) the classic desktop password system for web clients
