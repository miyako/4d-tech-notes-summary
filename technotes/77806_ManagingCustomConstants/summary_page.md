# Tech Note 17-12: Managing Custom Constants with Code

**Author:** Cannon Smith and David Adams
**Published:** June 30, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77806
**Download:** https://kb.4d.com/DLTN/TN/2017/17-12_CustomConstants.zip

## Proposition
This third-party Tech Note provides code-based routines for defining and managing 4D custom constants directly in source code, addressing practical adoption barriers that have historically discouraged developers from using constants despite their benefits.

## Key Points
- **Benefits of constants:** improved readability, reduced typo risk in strings, less reliance on static interprocess variables, and better compiler error detection.
- **Background on 4D constants:** explains what constants are and the kinds 4D supports.
- **Code-managed alternative:** provides routines to define/manage constants directly in source code instead of relying solely on external editors like 4D Pop.
- **Naming/labeling guidance:** practical conventions for constant names.
- **Reload requirement:** modified constants require reopening the database to take effect.
- **Client/server considerations:** notes complications specific to client/server development.
- **Phantom compiler errors & duplicate names:** practical troubleshooting guidance for common constant-related pitfalls.

## Featured Technology
- Custom constants (XML-backed)
- 4D Pop component (referenced)
- 4D compiler behavior around constants
- Client/server development considerations

## Best Practices Highlighted
1. Prefer named constants over magic numbers/strings for readability and typo protection.
2. Reduce use of static interprocess variables in favor of constants when reworking code for preemptive/thread-safe processes.
3. Watch for duplicate constant names and phantom compiler errors when managing constants at scale.

## Context / Positioning
Published in mid-2017 for classic 4D v16, this third-party note reflects the pre-Project-Mode era where custom constants lived in external XML files managed by tools like 4D Pop, well before 4D's text-based project structure changed how such assets are stored and versioned.

## Historical Commentary
**Status:** Still relevant

The case for using custom constants — readability, typo safety, reduced reliance on static variables, compiler error detection — remains valid guidance in current 4D development. The specific tooling (external XML files, 4D Pop) is dated relative to Project Mode's text-based conventions, but the underlying practice of defining and using named constants is still directly applicable, sometimes now complemented by class-based constant organization.
