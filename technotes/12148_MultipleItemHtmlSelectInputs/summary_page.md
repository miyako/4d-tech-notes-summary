# Tech Note: Handling Multiple Item HTML Select Inputs with 4D 6.5

- **Asset ID:** 12148
- **Tech Note #:** 01-08
- **Published:** February 28, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Eric Saltzen
- **Page URL:** https://kb.4d.com/assetid=12148
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_06-10_(FEB)/01-08_MultipleItem_Select.hqx

## Overview

Eric Saltzen of 4D, Inc. Technical Support supplies hand-written 4D parsing methods — ProcessMultipleItemSelect, DecodeURLText, and HexToDec — to correctly collect all values from an HTML MULTIPLE SELECT form input submitted via either GET (4DACTION) or POST (4DCGI/On Web Connection), a case 4D v6.5's built-in web form handling did not support.

## Key Points

- On Web Connection recognizes /4DCGI/Form01 POST submissions and calls ProcessMultipleItemSelect("GameSystems";$2;->atGameSystems) against the raw POST body in $2 to collect all selected values into an array.
- AcceptForm01 handles the equivalent GET-method submission from getform.html, calling ProcessMultipleItemSelect against the URL text in $1 for the Name, Experienced, and GameSystems fields.
- ProcessMultipleItemSelect walks the input text in a While loop, repeatedly using Position to locate the next "FieldName=" occurrence, extracting the value up to the next "&" or end of string, and appending it to the results array with INSERT ELEMENT — returning a normal single-entry array for ordinary (non-multiple) inputs.
- DecodeURLText converts POST-submitted, URL-encoded text back to plain text: it replaces "+" with spaces, then scans for "%XX" sequences and converts each to its corresponding character via Char(HexToDec(...)), finally normalizing the result with ISO to Mac.
- HexToDec manually converts up to 8 hexadecimal digits to a LONGINT by iterating characters from least- to most-significant and summing digit*16^position via a large Case of statement (rather than using a shortcut library function).
- The note ends with an explicit obsolescence notice: 4D v6.7's new GET WEB FORM VARIABLES command renders this whole technique 'trivial' by comparison, and the author recommends upgrading rather than adopting a 6.7 version of this workaround.

## Featured Technology

- On Web Connection / 4DCGI (POST) form handling
- 4DACTION (GET) form handling
- Custom ProcessMultipleItemSelect parsing method
- Custom DecodeURLText / HexToDec URL-decoding methods
- HTML MULTIPLE SELECT form inputs

## Historical Commentary

**Status:** Obsolete

Written by Eric Saltzen of 4D, Inc. Technical Support, this note supplies hand-written 4D methods (ProcessMultipleItemSelect, DecodeURLText, HexToDec) to parse HTML forms containing a MULTIPLE SELECT input, since 4D v6.5's built-in web form processing did not natively handle multiple values submitted under the same field name for either GET (4DACTION) or POST (4DCGI/On Web Connection) submissions. The note explicitly flags its own obsolescence in a closing note: 4D v6.7's new GET WEB FORM VARIABLES command made this hand-rolled parsing 'trivial,' and 4D's web stack has since moved even further, through GET WEB FORM VARIABLES-based processing to today's WEB SEND FILE/httpRequest and ORDA/REST-based web development, making this manual URL-decoding and multi-value parsing technique obsolete for current 4D web applications.

**References to newer/updated information:**
- 4D v6.7 introduced GET WEB FORM VARIABLES, which the author himself flagged as making this hand-rolled multiple-select parsing technique trivial by comparison
- Modern 4D web development has moved to WEB SEND FILE/httpRequest, REST APIs on ORDA, and browser-side JavaScript, superseding raw form-string parsing entirely
