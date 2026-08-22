# Tech Note 96-24: Localizing the Textual Representation of Numbers in Various Languages Using STRtoArray

**Author:** Kent Wilbur
**Published:** May 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11695
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_22-26_(MAY)/96-24_Numbers_to_Text.exe

## Overview
This Tech Note presents an example database ("Numbers") demonstrating how to convert numeric values into their spelled-out textual representation — as currency, plain quantities, or calendar years — across four languages (English, French, German, Spanish), with support for mixing any of four currencies (US Dollar, French Franc, German Mark, Mexican Peso) with any display language.

## Key Points
- A "Try Me" runtime layout lets the user enter a number and select language, currency type, and display item interactively (e.g. displaying French Francs in German).
- **Hard-coded approach:** `BUILD CURR` and `BUILD LITERALS` procedures embed every currency name and number word (zero through billion, per language) directly as array literals in 4D code.
- **Resource-based approach:** `STR RSRC CURR` and `STR RSRC LITERA` instead load the same words at runtime from **STR# Macintosh resources** (numbered 15001-15004 and 16001-16004) via ACI_PACK's `STRtoArray` external.
- The resource-based procedures are dramatically shorter than the hard-coded ones, and their behavior can be changed by editing the STR# resources (with ResEdit or Resorcerer) **without recompiling any code** — a key maintenance/localization advantage highlighted by the note.
- Language-specific number-formation quirks are noted: English and French are structurally closest; German tends to concatenate numbers into one long compound word; Spanish is a hybrid, concatenating only some digit groups.
- The approach could be extended to any additional language, since the localization data is stored as external, editable resources rather than embedded logic.

## Featured Technology
- ACI_PACK's `STRtoArray` external
- `STR#` Macintosh resources (edited via ResEdit or Resorcerer)
- 4D arrays (contrasting hard-coded vs. resource-driven localization data)
- Multi-language currency/number-to-words conversion (English, French, German, Spanish)

## Historical Context
Published May 1996, this note reflects the practical localization techniques available to 4D developers of the era, who leaned on the classic Mac OS resource-fork model (STR# string list resources) as an externalized, easily-editable data store — a pattern common across classic Mac OS software long before dedicated internationalization (i18n) frameworks existed.

## Historical Commentary
**Status:** Obsolete

The specific tooling this note relies on — ACI_PACK, STR# Macintosh resources, and resource editors like ResEdit/Resorcerer — is entirely classic Mac OS-era and has no equivalent in current 4D or any modern operating system. The general software localization problem this note addresses (spelling out numbers/currency amounts correctly across multiple languages) remains real and relevant today, but it is now typically solved using dedicated internationalization (i18n) libraries or platform locale APIs rather than resource-fork-based string tables loaded via a custom external.

