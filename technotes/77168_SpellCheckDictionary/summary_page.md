# Tech Note 14-16: Working With the Spell Check System and Dictionary in 4Dv14

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** November 3, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77168
**Download:** https://kb.4d.com/DLTN/TN/2014/14-16_SpellCheck_V14.zip

## Proposition
This note documents 4D v14's move from the Cordial dictionary to the open-source Hunspell engine for spell checking, explaining the practical differences developers and users will notice, how passive (as-you-type underlining) and active (explicit check) spell check work, native Mac OS X spell-check behavior, where the main/custom/user dictionary files live, and how to add words programmatically.

## Key Points
- **Cordial → Hunspell switch in v14:** motivated by a larger dictionary, fixes for prior Cordial issues, and native compatibility with Mac OS X.
- **Passive spell check:** as-you-type underlining of misspelled words in text areas/fields.
- **Active spell check:** an explicit, on-demand check the user or developer triggers.
- **Mac OS X-specific behavior:** additional native OS spell-check features available on that platform.
- **Three dictionary tiers:** Main Dictionary (built-in Hunspell word list), Custom Dictionary, and User Dictionary, each with distinct file locations and purposes.
- **Modifying the dictionary list programmatically**, with example code for adding/managing custom words.
- **File naming/location changes from v13**, important for developers who shipped custom dictionaries with earlier-version apps.

## Featured Technology
- Hunspell dictionary engine
- 4D passive/active spell check
- Custom and user dictionary files
- Mac OS X native spell check integration

## Context / Positioning
Published November 2014 for 4D v14.0, this documents an internal engine swap during the classic Design Mode era. Spell checking is a UI-layer feature largely orthogonal to the later ORDA/Project Mode transition, so this note has aged more gracefully than data-layer-focused notes from the same period.

## Historical Commentary
**Status:** Still Relevant

Hunspell remains 4D's spell-check dictionary engine well beyond v14, so the architectural information here (why the switch happened, the three-tier dictionary model) is still broadly accurate; developers troubleshooting spell-check/dictionary issues in reasonably modern 4D apps can still find this note useful.

The main risk of staleness is in exact file paths/naming conventions, which may have shifted slightly in newer 4D releases — readers should verify current dictionary file locations against up-to-date 4D documentation rather than assuming the v14-era paths are unchanged.
