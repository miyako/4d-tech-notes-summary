# Tech Note 06-02: Active Directory - Single Sign-on Using 4D 2004

**Author:** Thomas Maul, General Manager, 4D Germany
**Published:** January 11, 2006 | **Product/Version:** 4D 2004 | **Platform:** Windows only
**Page:** https://kb.4d.com/assetid=41346
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_01-04_(JAN)/06-02_Active_Directory.zip

## Overview
This Tech Note demonstrates how to integrate a 4D 2004 database with Microsoft Active Directory to achieve single sign-on (SSO) for Windows domain users, without requiring a dedicated plug-in. It targets Windows environments with a domain controller (Windows 2000/2003 Server or Small Business Server) and explicitly notes the technique cannot be used on Mac OS clients.

## Key Points
- Explains the business case for AD/SSO: centralized user/group management, avoiding repeated password prompts, and support for stronger authentication methods (smartcards, fingerprint scanners) inherited "for free" from Windows.
- Introduces a single reusable method, `AD_UserGroups`, that returns the current authenticated user name, domain name, domain DNS suffix, and the user's AD security group memberships.
- Implementation detail: the method dynamically generates a VBScript (.vbs) file using WSH/ADSI objects (`WScript.Network`, `WinNT://`, `LDAP://RootDSE`), executes it with `LAUNCH EXTERNAL PROCESS` and `cscript //Nologo`, then parses the captured stdout back into 4D as text or a text array.
- Shows two integration patterns: (1) checking AD group membership before showing (or skipping) a custom password dialog, and (2) fully delegating to 4D's built-in password system, automatically creating/updating 4D user records and group assignments to mirror Active Directory on each startup.
- Describes a security-conscious startup sequence using a low-privilege "Default User" account with no rights (used only to run `On Startup` before real login), a hidden admin account for provisioning, and encrypted BLOB storage of auto-generated random passwords.
- Notes benefits of 4D's native password system: `Current User` works even inside triggers, integrates with 4D Server/4D Backup logging, and supports `Locked Attributes` for record-locking diagnostics.

## Featured Technology
- 4D 2004 (Windows)
- Windows Active Directory / LDAP / ADSI
- VBScript generated and run via `LAUNCH EXTERNAL PROCESS`
- 4D's built-in password/group system (`CHANGE CURRENT USER`, `SET USER PROPERTIES`, `GET GROUP LIST`, `GET USER LIST`)
- BLOB encryption (`ENCRYPT BLOB` / `DECRYPT BLOB`) for stored credentials

## Historical Context
Published in January 2006, this note predates 4D's native SQL engine (introduced with 4D v11 in 2007), Project Mode (v17, 2018), and ORDA (2018+); at the time, Design Mode with a binary .4DB structure file was the only development mode. Shelling out to a hand-written VBScript via `LAUNCH EXTERNAL PROCESS` was a common, pragmatic way to reach Windows-only APIs (like ADSI/LDAP) that 4D itself did not expose natively — a workaround style largely superseded today by dedicated plug-ins, REST/OAuth-based identity integration, or built-in LDAP support in later 4D versions.

## Historical Commentary
**Status:** Obsolete

The specific mechanism — generating and executing a VBScript through `LAUNCH EXTERNAL PROCESS` to query Active Directory — is a dated, Windows-only workaround that modern 4D developers would replace with more robust LDAP/REST-based identity integration or a dedicated authentication component. The underlying goal (synchronizing AD group membership into an application's user/permission model for SSO) remains a valid and recurring integration pattern, but the note's concrete code and architecture reflect pre-SQL-engine, pre-Project-Mode 4D development conventions from 2006 and are not a recommended approach today.
