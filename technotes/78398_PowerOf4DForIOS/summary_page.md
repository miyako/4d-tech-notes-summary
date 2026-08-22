# Tech Note 20-02: The Power of 4D for iOS

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** January 29, 2020 | **Product/Version:** 4D for iOS v18 | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=78398
**Download:** https://kb.4d.com/DLTN/TN/2020/20-02_PowerOf4DforIOS.zip

## Proposition
4D for iOS let developers generate native Swift/Xcode iOS apps from a 4D database backend without writing Swift code. This note builds a sample CRUD app, "WorkPin" (a workplace bulletin board), end-to-end — backend structure, mobile project editor, CRUD actions, forms, and authentication.

## Key Points
- **Backend-first design**: a normalized 4D structure (Postings, Users tables, foreign-key relation) is designed before touching the mobile project editor, to minimize costly structural rework later.
- **Mobile Project Editor**: eight sections — General (identity/icon/theme), Structure (publish fields), Data, Actions (CRUD definitions), Labels & Icons, Main Menu, Forms, and Publishing.
- **Automatic theming**: 4D for iOS derives the app's color theme from the average tone of the uploaded app icon.
- **CRUD actions**: developers define Create/Read/Update/Delete operations bound to backend tables/fields through the Actions section rather than writing Swift networking code.
- **Toolchain version coupling**: the note documents a strict compatibility matrix tying specific 4D, Xcode, Swift, and macOS versions together (e.g., 4D v18 required Xcode 11.2/Swift 5.1/macOS 10.14).
- **Offline & sync support**: 4D for iOS apps could work offline with data synchronization back to the 4D backend when reconnected.

## Featured Technology
- 4D for iOS (native mobile project generator)
- Xcode / Swift project generation
- 4D Mobile simulator and data synchronization

## Best Practices Highlighted
1. Finalize backend structure (tables/fields/relations) before building the mobile project to avoid revising dependent actions/forms.
2. Use a high-resolution (1024×1024 px) app icon for the best automatic theme-color calculation.
3. Toggle 4D's "adjustment" option in the Structure section to auto-add sync-support fields/tables for better mobile loading performance.

## Context / Positioning
This note represents 4D's mobile strategy circa 2018-2020: 4D as a low-code generator of fully native Xcode/Swift iOS apps, aimed at existing 4D developers wanting mobile reach without learning Swift. It was one of several tech notes promoting 4D for iOS as a flagship differentiator during this period.

## Historical Commentary
**Status:** Obsolete

4D for iOS (and the broader "4D Mobile" native app generation product line) was discontinued by 4D; it is not part of current 4D versions, and the entire workflow described in this note — the Mobile Project editor, native Xcode/Swift generation, the built-in simulator — no longer exists to be followed today. 4D's modern mobile strategy instead centers on building responsive web front ends powered by ORDA/REST APIs, and, for low-code app building more broadly, its separate Qodly Studio platform. This tech note is now valuable only as a historical snapshot of an abandoned product direction, illustrating how tightly 4D for iOS was coupled to (and vulnerable to churn in) Apple's Xcode/Swift toolchain — a coupling that likely contributed to the difficulty of sustaining the product long-term.
