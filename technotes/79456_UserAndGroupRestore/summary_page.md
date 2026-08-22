# Tech Note 24-08: Maintaining 4D Users and Groups in Project Mode

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** June 25, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79456
**Download:** https://kb.4d.com/DLTN/TN/2024/24-08_UserAndGroupRestore.zip

## Proposition
Because 4D's users-and-groups data lives inside the database structure, deploying an updated structure can inadvertently wipe out customer-created users, passwords, and group memberships. This note explains the project-mode users/groups model and provides an automated backup/restore pattern to prevent this loss.

## Key Points
- **Elevated accounts differ by mode:** Binary mode allows multiple Designer (Team Development) accounts; project mode allows only one Designer, since flat-file source is meant to be managed via Git rather than login-based protection.
- **Groups support nesting for license access:** A group like "4D Write Pro" can be added under "4D View Pro" so its members inherit both feature accesses without duplicate group assignment.
- **directory.json stores project-mode identity data:** Located in the Settings folder next to the Project directory (or, if present, next to the data file, which takes precedence), this single JSON file replaces binary mode's embedded structure storage.
- **Binary mode uses export/import commands:** USERS TO BLOB and BLOB TO USERS (or the Users and Groups window) let developers export/import credentials as an encrypted BLOB before/after structure updates.
- **backupCurrentUsers copies the active file on exit:** Guarded by Application type checks, it copies directory.json to `{Documents}/4DAppUsers/{Database name}/directory.json`, replacing any prior backup.
- **restoreCurrentUsers compares dates then content:** It checks modification date/time first; if dates match but times are ambiguous, it falls back to an MD5 digest (Generate digest) comparison to detect real content differences before restoring.
- **A restart is required to apply a restored file:** restoreCurrentUsers returns a Boolean indicating whether the active file was replaced, so the caller can conditionally trigger RESTART 4D.
- **Startup/shutdown hook placement depends on deployment mode:** Use On Exit/On Startup for standalone; On Server Shutdown/On Server Startup for client-server — never on remote clients.

## Featured Technology
- **directory.json** — project mode's flat-file store of users, groups, and permissions.
- **EDIT ACCESS 4D** — command opening the Toolbox Users and Groups window for manual edits.
- **USERS TO BLOB / BLOB TO USERS** — binary mode commands for exporting/importing users and groups data.
- **On Server Startup / On Server Shutdown (and On Startup/On Exit)** — database lifecycle methods used to trigger backup/restore.
- **Generate digest (MD5 digest)** — used to compare file contents when modification timestamps are ambiguous.

## Best Practices Highlighted
1. Never deploy an updated structure's default directory.json over an active deployment without first backing up the customer's current file.
2. Place backup/restore hooks in server-specific lifecycle methods (On Server Startup/Shutdown) for client-server deployments, and standalone hooks otherwise — never on remote clients.
3. Use MD5 digest comparison as a tiebreaker when file modification timestamps alone can't reliably indicate which version is authoritative.

## Context / Positioning
This note reflects 4D's ongoing effort to help developers adapt operational practices — previously built around binary-mode structure internals — to project mode's flat-file architecture, ensuring that modernization to project mode doesn't introduce new risks around losing deployed customer configuration data during routine structure updates.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
