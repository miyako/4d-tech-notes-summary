# Tech Note 18-02: Elevated Privileges on macOS using sudo

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** January 18, 2018 | **Product/Version:** 4D v16 | **Platform:** Mac OS X
**Page:** https://kb.4d.com/assetid=77931
**Download:** https://kb.4d.com/DLTN/TN/2018/18-02_ElevatePrivileges.zip

## Proposition
Explains how to customize `/etc/sudoers` on macOS so a 4D application can run specific system commands (or all commands) with elevated privileges, without repeatedly prompting the admin for a password.

## Key Points
- **The problem:** some macOS commands (e.g., `purge`, `fdisk`) require elevated privileges to execute, which normally means an interactive password prompt each time.
- **/etc/sudoers as the solution:** editing this file lets specific accounts run designated commands (or all commands) via sudo without a password.
- **Two techniques compared:** allowing ALL commands (simpler, broader access) versus allowing only specifically named commands (more restrictive, safer).
- **Sample interface for editing sudoers:** the included demo app provides a UI for adding commands to `/etc/sudoers` directly.
- **Sample interface for testing:** a separate interface tests whether commands run successfully from within 4D.
- **Three tested outcomes:** command found and executed without error; command found but blocked/unauthorized; command not found at all — each with distinct feedback shown to the user.

## Featured Technology
- `/etc/sudoers` configuration
- `sudo` command
- 4D external/shell command invocation (e.g., LAUNCH EXTERNAL PROCESS-family commands)

## Best Practices Highlighted
1. Prefer allowing only specifically named commands in `/etc/sudoers` rather than blanket ALL-commands access, to minimize security exposure.
2. Test and clearly surface the three possible outcomes (success, unauthorized, command-not-found) to users/administrators rather than assuming success.
3. Document and audit any sudoers changes made to support unattended/automated 4D operations.

## Context / Positioning
This is an operations/system-integration note rather than a core 4D language feature note, addressing a recurring need for 4D applications on macOS (particularly server or kiosk-style deployments) to perform privileged maintenance tasks without manual password entry. It reflects macOS security norms circa 2017-2018 (macOS 16-era 4D, roughly macOS High Sierra timeframe).

## Historical Commentary
**Status:** Still relevant

Configuring `/etc/sudoers` for passwordless, scoped privilege elevation is a standard Unix/macOS technique that remains valid today and is unaffected by 4D's own Design-Mode-to-Project-Mode or ORDA evolution — this note's core guidance is essentially timeless system administration knowledge applied to a 4D use case.

What has shifted since 2018 is the broader macOS security landscape: Apple has continued tightening System Integrity Protection, app notarization, and Gatekeeper restrictions, which can limit what even a properly-elevated command is permitted to do on modern macOS versions. Developers applying this technique today should verify that their target privileged commands still function as expected under current macOS security policies, but the sudoers configuration approach itself remains sound.
