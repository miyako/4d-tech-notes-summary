# Tech Note 02-26: Multi-level Clipboard in 4D

- **Asset ID:** 23243
- **Tech Note #:** 02-26
- **Published:** June 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Cha Yang
- **Page URL:** https://kb.4d.com/assetid=23243
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_25-27_(JUN)/02-26_Multi_level_Clipboard.hqx

## Overview

Cha Yang (4D Technical Support Engineer) implements "4D Clipboard," a five-slot private clipboard system built entirely with 4D's clipboard commands and a simulated Ctrl+C/Ctrl+V technique via POST KEY, letting a user copy multiple text/picture items and paste any one back individually.

## Key Points

- Reviews the OS clipboard model: the public desk scrap, private scraps, standard formats ("TEXT", "PICT"), optional formats ("snd", "movv", "styl"), and custom 4-character private formats, and explains how applications typically write multiple format instances of the same data (e.g. "SPSH"/"SYLK"/"TEXT") so other apps can pick their preferred type.
- Documents 4D's clipboard command set: `APPEND TO CLIPBOARD`, `CLEAR CLIPBOARD`, `GET CLIPBOARD`, `GET PICTURE FROM CLIPBOARD`, `Get text from clipboard`, `SET PICTURE TO CLIPBOARD`, `SET TEXT TO CLIPBOARD`, and `Test clipboard`, noting the 32,000-character limit on `SET/Get TEXT TO/FROM CLIPBOARD` (a 4D text-variable limitation, not a desk-scrap one) versus `APPEND TO CLIPBOARD`/`GET CLIPBOARD`'s blob-based, unlimited, arbitrary-4-character-type approach.
- 4D Clipboard stores five interprocess blob variables (`<>clipboard_1`...`<>clipboard_5`), each internally tagged with a 4-byte `"TEXT"` or `"PICT"` marker to identify the payload type on retrieval.
- Copying is triggered by Ctrl+6 or a palette button: `CLEAR CLIPBOARD` then `POST KEY(67;Command key mask)` simulates a native Ctrl+C; a separate `SaveToBlob` process (needed because `POST KEY` only fires after the calling method returns) waits via `DELAY PROCESS`, tests the type with `Test clipboard`, and retrieves the payload with `GET PICTURE FROM CLIPBOARD` or `GET CLIPBOARD` into a tagged blob.
- Pasting via `PasteFromClipboard_1`...`_5` reads the 4-byte type tag from the chosen slot's blob, restores the payload to the public clipboard with `SET TEXT TO CLIPBOARD` or `SET PICTURE TO CLIPBOARD`, then simulates Ctrl+V via `POST KEY(86;Command key mask)`.
- Keyboard shortcuts Ctrl+1 through Ctrl+5 paste from each of the five clipboard slots directly; the palette also shows a "T" or "P" indicator per slot and lets the user clear individual slots or all slots at once.

## Featured Technology

- APPEND TO CLIPBOARD / GET CLIPBOARD (private data-type clipboard slots)
- SET TEXT TO CLIPBOARD / Get text from clipboard
- SET PICTURE TO CLIPBOARD / GET PICTURE FROM CLIPBOARD
- Test clipboard
- POST KEY (simulating Ctrl+C / Ctrl+V)
- Interprocess BLOB variables as multi-slot clipboard storage
- VARIABLE TO BLOB / BLOB TO VARIABLE / BLOB to text

## Historical Commentary

**Status:** Still relevant

This note builds a five-slot private clipboard palette ("4D Clipboard") on top of the OS desk scrap, using 4D's clipboard commands (APPEND TO CLIPBOARD, GET CLIPBOARD, Test clipboard, SET/GET PICTURE TO/FROM CLIPBOARD) plus a clever trick of posting a simulated Ctrl+C/Ctrl+V (via POST KEY) in a separate process to let 4D capture whatever object the user has selected without knowing its type in advance. This is a legitimate and still largely valid explanation of the classic Mac/Windows desk-scrap model and 4D's clipboard API, both of which are largely unchanged today; multi-slot clipboard managers are now a mainstream OS-level or utility-level feature (macOS/Windows clipboard history, various clipboard manager apps) rather than something applications typically build themselves, so the specific need for an in-app multi-level clipboard is now less common, though the underlying 4D commands demonstrated remain fully usable.

References to newer/updated information:
- 4D's clipboard commands (APPEND TO CLIPBOARD, GET CLIPBOARD, Test clipboard, SET/GET TEXT|PICTURE TO/FROM CLIPBOARD) remain part of the current 4D language largely unchanged
- Modern operating systems (Windows 10+/macOS) now offer built-in or third-party multi-item clipboard history, reducing the need for applications to implement their own private multi-slot clipboard as this note does
