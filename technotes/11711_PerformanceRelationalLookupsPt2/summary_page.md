# Tech Note 96-32: Breaking the Rules to Improve Performance, Part 2—Using 4D's Built-In Relational Lookups

**Author:** Walt Nelson
**Published:** July 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11711
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_31-32_(JUL)/96-32_Performance_2.exe

## Overview
Part 2 of a two-part series, this Tech Note argues that developers should favor 4D's built-in many-to-one relational lookup mechanism over hand-written custom lookups whenever raw speed matters — especially for databases accessed over a WAN or dial-up connection — and shows a technique to overcome the built-in lookup's usability limitations without sacrificing its performance advantage.

## Key Points
- **Why developers avoid the built-in lookup:** synthetic primary keys aren't user-searchable by name; only two fields can display in the lookup list; the list isn't sorted; there's no UI control over the lookup window; and new-record primary key values can't be edited by the user.
- **Why to use it anyway:** it is at least twice as fast (sometimes several hundred percent faster) than custom routines, requires little or no code, and is easier to maintain.
- **The workaround technique:**
  1. Create a `[Lookups]` file with alpha "relational connector" fields to avoid double-relations.
  2. Add a concatenated `Wildcard_Choice` field to each "One" file combining several source fields.
  3. Pad concatenated values to fixed widths (via a `StringPadSpaces`-style routine) so they display as aligned columns.
  4. Place the lookup field on the target input layout with **Automatic Relate one** and **Auto wildcard support** enabled.
  5. Use **4D Customizer Plus** to set the Structure Font to a monospaced font (Monaco/Courier) so padded columns line up visually.
- **Example database:** "Performance Rules" demonstrates Company, Contact, and Product lookups implemented this way.

## Featured Technology
- 4D's built-in relational lookup mechanism (Automatic Relate one, wildcard support)
- 4D relations between files
- 4D Customizer Plus (Structure Font customization)

## Historical Context
The motivating scenario — dial-up modem and WAN latency making custom lookup performance unacceptable — is entirely obsolete given modern broadband, LAN, and cloud connectivity. The specific UI and workaround (a dedicated Lookups file, manual field padding, and a monospaced Structure Font set via 4D Customizer Plus) reflect 4D's pre-V6, pre-ORDA procedural data-access model. The general principle — favor a platform's optimized built-in mechanism over custom code when performance is critical — remains conceptually valid, but 4D's data access layer has since been substantially modernized with ORDA (2018), which supersedes this era's relation/lookup approach for most new development.
