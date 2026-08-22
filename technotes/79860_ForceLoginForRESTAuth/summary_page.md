# Tech Note 25-10: Force Login for REST Authentication in 4d

**Author:** Abir HSAINI, Technical Services Engineer, 4D Inc.
**Published:** October 31, 2025 | **Product/Version:** 4D Server v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79860
**Download:** https://kb.4d.com/TN/2025/25-10_ForceLoginforRESTAuth.zip

## Proposition
REST services expose application logic and data broadly (web, mobile, third-party clients), which
makes security paramount. Force Login, the default REST authentication mode for new 4D projects
since v20 R6, secures endpoints by denying all access until a session explicitly authenticates and
is granted privileges — replacing the deprecated "On REST Authentication" legacy method with a
more robust, fine-grained, deny-by-default model.

## Key Points
- **Deny-all default.** New projects auto-generate `roles.json` with `forceLogin: true` and a
  `"none"` default privilege that blocks the entire REST API until explicitly opened up.
- **Explicit migration required for existing projects.** Editing `roles.json` by hand is not
  enough; developers must click "Activate REST authentication through ds.authentify() function"
  in Settings → Web → Web Features, which removes legacy group permissions and deactivates the old
  method.
- **Guest sessions are free and limited.** The first REST request auto-creates a privilege-less,
  license-free guest session that can only issue descriptive requests (`/rest/$catalog`,
  `/rest/$catalog/authentify`, `/rest/$getWebForm`) — enough to discover dataclasses/fields and
  reach a login form before consuming a license.
- **`authentify()` is the single authentication gate.** An exposed `Function authentify(...)`
  datastore class function validates credentials and calls `Session.setPrivileges(...)`; only a
  successful call both grants privileges and consumes a license, cleanly separating
  authentication from license usage.
- **Three implementation patterns.** Open access (`Session.setPrivileges("Administrator")` with no
  credential check — explicitly flagged as insecure), mapping a legacy 4D read/write user group,
  or a fully custom credential-validation/user-management system.
- **Fine-grained roles.json permissions.** Access is defined per resource (datastore, dataclass,
  attribute, data-model function, singleton function) and per action (create, read, update, drop,
  execute, promote), checked on every request regardless of access path.
- **Programmatic privilege checks.** `ds.hasPrivilege()` and `ds.getPrivileges()` let custom
  datastore functions gate admin-only operations beyond what declarative `roles.json` rules alone
  express.
- **Qodly visual configuration.** A "Roles and Privileges" page in Qodly offers a more intuitive
  interface for editing the same `roles.json` structure.

## Featured Technology
- **`roles.json`** — declarative privilege/permission/resource configuration file in
  `Project/Sources`.
- **`ds.authentify()` / `Session.setPrivileges()`** — credential validation and privilege
  assignment entry point.
- **`ds.hasPrivilege()` / `ds.getPrivileges()`** — programmatic privilege inspection in custom
  datastore class functions.
- **Guest web sessions** — license-free, privilege-less sessions for descriptive-only REST access.
- **Qodly "Roles and Privileges" UI** — visual editor for `roles.json`.

## Best Practices Highlighted
1. *Default to `"none"` and grant explicitly* — keep all access locked by default and open only
   the specific resources/actions authorized sessions need.
2. *Never implement open-access `authentify()` in production* — the "Administrator with no
   credential check" pattern is shown only as a legacy-equivalence example, explicitly flagged as
   insecure.
3. *Use the migration button, not manual JSON edits* — hand-editing `roles.json` alone does not
   complete the conversion from legacy REST authentication.

## Context / Positioning
Published under 4D Server v20 R (late 2025), this note formalizes the secure-by-default posture
4D adopted starting at v20 R6, continuing the platform's move away from legacy, implicit REST
authentication toward explicit, ORDA-integrated, role-based access control — consistent with
broader industry expectations for API security and complementing 4D's other 2025–2026 notes on
session management and multi-layer web security.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
