# Tech Note: Spell-check and Dictionary

- **Asset ID:** 36663
- **Tech Note #:** 05-12
- **Published:** March 24, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thang Nguyen
- **Page URL:** https://kb.4d.com/assetid=36663
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-12_Spell_Check_and_Dictionary.hqx

## Overview

Thang Nguyen (Quality Assurance, 4D Inc.) documents the spell-checking feature integrated into 4th Dimension 2004: how to turn it on for form fields/variables and 4D Write areas, how to switch dictionary language via SET DICTIONARY, how personal dictionaries are stored, and how to merge multiple personal dictionaries since 4D only supports one active at a time.

## Key Points

- Spell-check can be enabled declaratively (property list "Auto Spellcheck" option under the Entry theme; 4D Write "Checking as you type" preference) or programmatically via the SPELL CHECKING command in form events like On Losing Focus/On Validate.
- For 4D Write areas, WR SET AREA PROPERTY (Area; wr on the fly spellchecking; 0/1) turns spell-checking on or off programmatically.
- SET DICTIONARY(constant) switches the active dictionary; the note lists the four base longint constants — English (69632), German (131584), Spanish (196608), French (262144) — plus a long table of regional variant values (e.g. English UK/Irish/Australian/US/Canadian, German Austria/Switzerland, Spanish Latin American countries, French African/Canadian/Caribbean regions), noting these variants aren't yet fully supported by the checker.
- Default dictionaries are encrypted/read-only; on Windows they live in the 4D extension folder next to the app, on Mac OS X inside the app package's extension folder.
- User-added words go into a personal dictionary file named persoxxxxx.dic (xxxxx = dictionary reference number), created in the 4D Active folder (e.g. C:\Documents and Settings\All Users\Application Data\4D on Windows, or Library:Application Support:4D on Mac OS X) — locatable at runtime via Get 4D folder; 4D must be restarted after first use for the file to appear.
- The persoxxxxx.dic file is plain text (one word per line) and can be hand-edited, or extended via the spell-check's "Add" dialog, though words added that way stay in memory until 4D quits.
- Since only one personal dictionary can be active at a time, the note provides sample code using Open document/Append document plus RECEIVE PACKET/SEND PACKET to merge, e.g., a French personal dictionary's contents into the active English one.

## Featured Technology

- SPELL CHECKING command
- SET DICTIONARY command and language/variant constants
- WR SET AREA PROPERTY (wr on the fly spellchecking) for 4D Write areas
- Personal dictionary files (persoxxxxx.dic)
- Get 4D folder command for locating dictionary storage
- SEND PACKET / RECEIVE PACKET for merging dictionary files

## Historical Commentary

**Status:** Partially Superseded

Thang Nguyen documents 4D 2004's then-new integrated spell-checker: how to enable it declaratively via the property list or 4D Write preferences, or programmatically via SPELL CHECKING and WR SET AREA PROPERTY, how to switch between the four bundled language dictionaries with SET DICTIONARY, and how to merge personal .dic files by hand since 4D doesn't support multiple simultaneous personal dictionaries out of the box. The core spell-check commands and dictionary architecture described here are still part of 4D today with only incremental changes, making this note largely still relevant as a reference for classic form-based text/alpha field spell-checking, though 4D Write itself has since been superseded by 4D Write Pro for rich document editing.

References to newer/updated information:

- SPELL CHECKING and SET DICTIONARY remain part of the current 4D language with fundamentally the same behavior described here
- 4D Write Pro (2016+) is now 4D's primary rich document editor and has its own spell-check configuration, distinct from the classic 4D Write WR SET AREA PROPERTY approach shown in this note
