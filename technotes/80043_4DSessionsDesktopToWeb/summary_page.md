# Tech Note 26-06: 4D Sessions: From Desktop to Web in a Single Shared Session

**Author:** Al Mahdi Bakkali, Technical Support Engineer, 4D Inc.
**Published:** June 29, 2026 | **Product/Version:** 4D v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=80043
**Download:** https://kb.4d.com/TN/2026/26-06_4DSessions.zip

## Proposition
Session management is critical infrastructure for multi-channel applications where a desktop
user, a web interface, and a mobile device must cooperate on the same task. Before 4D 21 R3, the
`Session` command returned `Null` on remote clients, forcing developers to build dedicated
server-side relay methods just to surface session data to client code. This note shows how
extending `Session` to remote clients — plus `createOTP()`, `storage`, and privilege functions —
eliminates that redundant architecture.

## Key Points
- **Direct client-side session metadata.** `Session.info` (available from 4D 21 R3 on remote
  clients) exposes `type`, `userName`, `machineName`, `IPAddress`, `ID`, and `creationDateTime`
  directly in form methods, e.g. on a form's `On Load` event, with zero server round-trips.
- **Desktop-originated OTP session sharing.** `Session.createOTP(10)` (extended to desktop
  sessions in 4D 21) generates a short-lived, single-use token appended to a URL as `$4DSID`,
  which the 4D server uses to bind a new HTTP connection to the token's originating session; the
  token is invalidated after first use, and the server subsequently switches to a cookie.
- **Multi-device pairing via QR code.** A second OTP, generated at a `/pair` HTTP route
  (`Session.createOTP(5)`), is encoded into a QR-code URL so a mobile device can scan and join the
  same session, resulting in three distinct clients (desktop, browser, mobile) sharing one session.
- **Session.storage for cross-device real-time state.** A shared object scoped to the session
  lifetime; writes from any participant (e.g. a challenge-response value) are immediately visible
  to all others on their next read, underpinning the demo's identity-challenge mechanism.
- **Privileges as guarded, verifiable state.** Since 4D 21, `Session.setPrivileges()` and
  `Session.clearPrivileges()` return a Boolean success indicator (previously void), letting
  security-sensitive code confirm a privilege change actually took effect before proceeding, and
  `Session.hasPrivilege()` gates protected class functions like a file-upload handler.
- **Server-only privilege operations.** `setPrivileges()`/`clearPrivileges()` remain callable only
  from server-side execution contexts; calling them from a remote client raises an error.
- **"Execute on Server" as a common failure point.** If the method generating the OTP/storage
  isn't marked "Execute on Server", HTTP handlers see `Null` storage, since the initialization ran
  client-side instead.

## Featured Technology
- **`Session.info`** — client-accessible read-only session metadata object.
- **`Session.createOTP()`** — single-use, short-lived token for session-sharing URLs
  (`$4DSID` query parameter).
- **`Session.storage`** — session-scoped shared object for real-time cross-device state.
- **`Session.setPrivileges()` / `clearPrivileges()` / `hasPrivilege()`** — privilege management
  with Boolean success return (4D 21+).
- **4D Web Server / HTTP handlers** — `/init`, `/pair`, `/scan`, `/reply` routes implementing the
  OTP admission flow.
- **QR code generation** (external API) — encodes the mobile-pairing OTP URL for scanning.
- **SHA-256 integrity hashing** — verifies uploaded evidence images haven't been altered post-submission.

## Best Practices Highlighted
1. *Never cache or reuse an OTP* — always generate a fresh token immediately before presenting it,
   since tokens are single-use and time-limited.
2. *Use HTTPS in production* — an OTP transmitted in a URL query string over plain HTTP can be
   intercepted and used to hijack the session.
3. *Always clear privileges at terminal state* — failing to call `clearPrivileges()` when a case
   closes leaves elevated privileges active into the next case, letting a new subject bypass
   verification.

## Context / Positioning
Published under 4D v20 R (2026), this note documents session-layer capabilities rolled out across
4D 21 and 21 R3, reflecting 4D's continued investment in web/mobile-native multi-channel
architectures (OTP-based session sharing, real-time shared state) that reduce reliance on custom
server-relay code — part of the same broader modernization trend (alongside ORDA and AI Kit) of
making native 4D primitives directly usable from client-side and web contexts.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
