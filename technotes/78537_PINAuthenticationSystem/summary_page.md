# Tech Note 20-15: Setting Up a PIN Authentication System

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** September 1, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78537
**Download:** https://kb.4d.com/DLTN/TN/2020/20-15_PinAuthentication.zip

## Proposition
Not every application needs (or wants) alphanumeric password entry — a numeric-keypad PIN interface can offer a faster, more modern-feeling authentication experience. This Tech Note walks through implementing a complete PIN authentication system in 4D: keypad UI, validation, success/failure handling, and PIN registration/change, backed by a `user` table storing securely hashed PIN codes.

## Key Points
- **Keypad UI components**: status message area, digit-count visual indicator (shaded shapes), numeric buttons, backspace button.
- **Hashed storage**: PINs are never stored in plain text — `Generate password hash`/`Verify password hash` handle hashing and comparison.
- **Validation flow**: looks up the current authenticated user in `ds.user`, compares the entered PIN hash, and returns "Success"/"Try Again."
- **Success handling**: displays a success message and calls `ACCEPT` to grant application access.
- **Failure handling**: clears the visual indicator, shows an error, and shakes the form for feedback.
- **First-run registration**: detects a missing `user` record for the current user and prompts double-entry PIN confirmation before saving.
- **Change-PIN flow**: reuses the same `setup_pin` method, which updates an existing record instead of creating a new one.
- **Current user integration**: uses 4D's `Current user` command, with `GET USER LIST` to resolve the numeric user ID for storage.

## Featured Technology
- Numeric keypad form UI pattern
- Generate password hash / Verify password hash
- ds.user (ORDA) table for PIN storage
- Current user / GET USER LIST commands

## Best Practices Highlighted
1. Always hash PINs before storing them — never keep them as plain text in the table.
2. Require double-entry confirmation when registering or changing a PIN to avoid lockouts from typos.
3. Provide clear visual and status feedback (shake animation, indicator clearing) on failed authentication attempts.

## Context / Positioning
Published as 4D continued to broaden its security/authentication Tech Note lineup (alongside data encryption and, later, two-factor/TOTP notes), this demonstrates that 4D applications can implement custom, application-level authentication schemes layered on top of — or independent from — 4D's native password system, useful for touch-friendly kiosk-style or point-of-sale-style applications where a numeric PIN is more practical than a full password.

## Historical Commentary
**Status:** Still relevant

This is an application-level pattern built on stable, still-current 4D commands (`Generate password hash`, `Verify password hash`, `Current user`), none of which have been deprecated or replaced, so the technique remains directly usable today. 4D has since published further authentication-related Tech Notes (e.g., covering two-factor/TOTP authentication) showing the platform's security tooling story has grown since 2020, but this PIN-based approach is not superseded by anything — it simply represents one of several valid authentication UX patterns a developer can choose from depending on the application's needs.
