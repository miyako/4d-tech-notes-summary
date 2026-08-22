# Tech Note: Maintaining User Modifiable Choice Lists

**Author:** Not specified
**Published:** September 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11775
**Download:** Not available (no working download link archived — teaser only)

## Overview
This note addresses the dilemma that "User Modifiable" choice lists — which let end users tailor their own data-entry choice lists — are stored in the database structure and therefore get overwritten with default lists whenever a new structure is deployed, wiping out user customizations. It presents a generic, reusable code scheme to save and restore those customizations across structure updates.

## Key Points
- Choice lists are easy to implement (create a list, assign to a field/variable) and structures commonly contain 20-30 or more of them.
- Leaving choice lists "User Modifiable" lets end users tailor lists to changing needs, but risks losing those customizations when a new structure is deployed, since lists live in the structure.
- Proposed solution: save the choice lists with the data (not just the structure), and rebuild modifiable lists automatically on first launch of a newly deployed structure.
- The note provides generic, modular, copy-paste-ready code intended to give a working choice-list-saving system "within minutes."
- Acknowledges some developers may need a more complex solution and positions the note as a base to build on.
- References an accompanying example database, "SaveListsDemo," presumably containing the full implementation.

## Featured Technology
- 4D Choice lists and the "User Modifiable" list property
- SaveListsDemo example database
- Generic/modular save-and-restore code pattern

## Historical Context
Published September 1997, this note tackles a structure-vs-data separation problem inherent to 4D's classic binary structure file model of that era, where choice lists (like forms and other structure elements) lived inside the structure and were replaced wholesale on every deployment. The archive of the full technical content (specific method code, SaveListsDemo internals) could not be recovered (no working download link exists for the original page). The general problem this note solves — preserving user customizations across application updates — remains a valid, generally relevant software design concern, though modern 4D development (especially post-Project Mode, 2018, with structure elements as text/JSON files) and increasing use of collection/ORDA-driven dynamic lists offer different mechanisms than this note's classic choice-list approach.
