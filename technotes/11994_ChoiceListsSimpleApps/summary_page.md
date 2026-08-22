# Tech Note: Simple Applications for Choice Lists

## Overview
- **Technical Note 00-55**
- **Author:** Unknown / not specified
- **Published:** November 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note surveys the everyday usefulness of 4D choice lists — presenting a set of values for data entry, populating drop-down lists, and naming the tabs of form tab-panel objects — while calling out their central structural weakness: choice lists are stored inside the database's structure file rather than its data file. Because of that, if a developer allows end-users to edit or extend a choice list at runtime, those edits are destroyed the moment the developer ships a new structure file, since the update simply overwrites the old structure (and its embedded lists) wholesale. The note's core proposition is a technique for keeping user-editable list values in the data file instead, so administrators can safely update the structure without clobbering end-user customizations. It focuses specifically on non-hierarchical choice lists (flat lists, as opposed to hierarchical/nested ones) and discusses a few applications built around this pattern. As with many notes of this era, the featured technology is a core 4D Design Mode data-modeling concept rather than a specific plug-in or API. Because the download archive with the full example database could not be recovered from this era's self-extracting Windows installer format, this summary is drawn only from the teaser abstract on the original kb.4d.com page.

## Featured Technology
- 4D Choice Lists
- Data file storage
- Form tab objects

## Historical Context
This note addresses a real structural limitation of classic 4D Design Mode: choice lists live in the binary structure file, so any end-user edits to a list are silently wiped out the next time a developer redeploys a structure update. Project Mode (introduced in 4D v17, 2018), which stores structure elements as individual text files under source control, changes this picture considerably by making structure elements easier to manage and merge, though the specific data-file storage workaround this note proposes remains a reasonable technique for classic/Design Mode databases still in production.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- 4D Project Mode (v17+) stores structure definitions as text files rather than one opaque binary structure file, changing how developers manage and version choice-list-like structure data
- Databases still running in classic Design Mode retain the exact storage behavior this note describes

