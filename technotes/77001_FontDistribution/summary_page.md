# Tech Note 14-04: Automating a Font Distribution and Installation for an Application

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** March 14, 2014 | **Product/Version:** 4D v13.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77001
**Download:** https://kb.4d.com/DLTN/TN/2014/14-04_FontDistribution.zip

## Proposition
This note shows how to distribute custom fonts to client workstations via a database's Resources folder and automatically install them at startup, so an application's custom look and feel renders consistently across Mac and Windows without manual IT intervention.

## Key Points
- Custom fonts placed in a database's "Resources" folder are automatically copied down to each 4D Client's local Resources folder in Client/Server deployments.
- Style sheets group font attributes so the correct custom font is consistently applied across forms and platforms.
- On Mac, installing a font is a simple `COPY DOCUMENT` into the user- or system-level Fonts folder.
- On Windows, font installation additionally requires registry registration; the note generates a VBScript at runtime (using the Shell Application's "Install" verb) and runs it with `LAUNCH EXTERNAL PROCESS`.
- An "On Startup" method compares fonts bundled in Resources against the machine's installed fonts and triggers installation only when needed, then prompts for a required restart.
- A demo form visually reports font installation status and disables further install attempts once fonts are present.

## Featured Technology
- Database "Resources" folder for cross-platform asset distribution
- Style sheets for consistent multi-platform font display
- VBScript-generated Windows font installer via `LAUNCH EXTERNAL PROCESS`
- `COPY DOCUMENT` for direct Mac font installation

## Best Practices Highlighted
1. Use the Resources folder (not ad-hoc file copies) to leverage 4D's built-in Client/Server asset sync.
2. Pair custom fonts with style sheets rather than hardcoding font properties per object.
3. Check whether a font is already installed before reinstalling and forcing an unnecessary restart.

## Context/Positioning
Published for 4D v13.4, this note addressed a recurring, practical deployment concern for teams shipping applications with custom branding/typography across mixed Mac/Windows client fleets.

## Historical Commentary
**Status:** Still relevant

Distributing custom fonts via a database's Resources folder — automatically synced to 4D clients in Client/Server — and gating font-dependent forms with style sheets remains a valid technique, since both mechanisms are still supported by 4D today. The Windows installation approach is the most dated element: generating a VBScript that invokes the shell's "Install" verb via `LAUNCH EXTERNAL PROCESS` is a fragile 2014-era automation pattern that a modern implementation would more likely replace with PowerShell or a more direct API call, though it may still function on current Windows versions. The underlying problem and Resources-folder-based strategy remain sound.
