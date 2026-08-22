# Tech Note 09-11: 4D Pop: Developer Components

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** March 18, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75217
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_09-12_(MAR)/09-11_4D_Pop.zip

## Proposition
Introduces 4D Pop, an extensible Design-Mode palette of free developer productivity components enabled by 4D v11 SQL's simplified component architecture, and documents how to install, extend, and use each first-party component.

## Key Points
- **Extensible palette architecture:** compatible components declare themselves via a `4DPop.xml` descriptor (name, icon, shared methods for click/drop actions).
- **Bookmarks, Color Chart, Commands finder:** quick-access tools for URLs/files/email, drag-and-drop color code generation, and searchable 4D command lookup/insertion with documentation links.
- **Constants Editor & Image Buddy:** GUI tools for managing plugin-stored constants and Resources-folder images (with basic transforms).
- **Migration tools:** dedicated assistants for migrating Shortcuts, Constants (4DK# resources), and Macros when moving a database to 4D v11 SQL.
- **SqlSchemas & XLIFF editors:** GUIs for managing 4D v11 SQL schemas/table rights and for creating/editing XLIFF-based localization files.
- **Client/Server aware:** most components work from a 4D Client, though changes are pushed from server to clients rather than edited locally.
- **Deployment hygiene:** 4D Pop components are development-only and should be excluded from merged/deployed applications via the build dialog.
- **Open, community-extensible:** third-party developers contributed additional compatible components via the 4D Pop forum.

## Featured Technology
- 4D Pop palette window and its XML-based (4DPop.xml) tool-plugin architecture
- Design-mode developer productivity components: Bookmarks, Color Chart, Commands lookup, Constants Editor, Image Buddy, Rulers, SqlSchemas, XLIFF editor
- 4D v11 SQL component architecture enhancements enabling easy component installation
- Migration Assistants (Constants, Macros, Shortcuts) for pre-v11 SQL databases

## Best Practices Highlighted
1. Uncheck 4D Pop (and other dev-only) components in the build application dialog before shipping a merged application.
2. Use the Constants/Macros Migration Assistants when moving legacy databases to 4D v11 SQL rather than migrating resources by hand.
3. Store localizable strings in XLIFF files (the v11 SQL standard) rather than legacy STR# resources going forward.

## Context / Positioning
Published to showcase what the newly streamlined 4D v11 SQL component architecture made possible: a rich, community-driven ecosystem of Design-Mode developer tools distributed as ordinary components.

## Historical Commentary
**Status:** Obsolete

4D Pop's entire premise — a palette of add-on tools for the classic, binary Design-Mode IDE, working with rsrc-based constants and XLIFF localization files — is tied to an IDE architecture that no longer exists.

Project Mode (4D v17+, 2018) replaced Design Mode's binary structure/component/constants model with a text-based, version-controllable one, and the modern 4D IDE has since absorbed much of what 4D Pop's components offered (command search, quick navigation, etc.) as native features. The specific components and forum ecosystem this note describes are no longer applicable to current 4D development.
