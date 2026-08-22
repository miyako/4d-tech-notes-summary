# Tech Note 10-35: Localization in 4D v12

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** December 17, 2010 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76233
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_34-36_(DEC)/10-35_Localization_in_4D_v12.zip

## Proposition
This Tech Note by Jesse Pina addresses how to make a 4D application multilingual, a capability that became significantly easier with 4D v12 and 4D v11 SQL.

## Key Points
- XLIFF is presented as the preferred resource format over 'old style' 4D resources
- SET DATABASE LOCALIZATION (new in 4D v12) lets developers programmatically control the active language
- An alternative technique using an Interprocess variable is also demonstrated for finer control
- Includes a full worked deployment example showing how to ship a localized database
- Distinguishes localization (full cultural/format adaptation) from simple text translation

## Featured Technology
- XLIFF resources
- SET DATABASE LOCALIZATION command
- Interprocess variables
- resource-based string localization
- runtime language switching

## Best Practices Highlighted
- Centralize all user-facing strings in resource files rather than hard-coding text
- Use SET DATABASE LOCALIZATION for the cleanest runtime language switch
- Test deployment of localized resources before shipping to confirm correct language loads

## Context/Positioning
Published as 4D v12 shipped, this note showcased new localization tooling meant to help ISVs sell 4D-built software into non-English-speaking markets.

## Historical Commentary
**Status:** Still Relevant

Localization via XLIFF resource files and the SET DATABASE LOCALIZATION command remains part of 4D's classic language and is still functional today, since 4D has kept strong backward compatibility for resource-based string translation. Contemporary 4D projects increasingly favor Project mode's plain-text file organization for resources, and web-facing front-ends often rely on standard web i18n libraries rather than 4D resource files, but the underlying technique documented here is still valid and used.
