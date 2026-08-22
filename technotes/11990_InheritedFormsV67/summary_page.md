# Tech Note: Inherited Forms in 4D v6.7

## Overview
- **Technical Note 00-60**
- **Author:** Unknown / not specified
- **Published:** December 1, 2000
- **Product/Version:** 4D v6.7
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note addresses a practical wrinkle introduced by 4D v6.7's new inherited forms feature, which let a developer define a single form (with standard buttons and layout) in one table and reuse it as the list or input form for other tables as well. While this promotes consistency and reduces duplicated form design work, it raises an immediate question: since the same form method now runs in the context of different tables depending on which one it was invoked from, how does the 4D code inside that shared form know which table's selection of records it should currently be acting on? The note's proposition is a simple, reusable pattern for detecting the current table context from within an inherited form's method, so that generic button code (for example, a 'duplicate record' or 'delete selection' button) can correctly operate on whichever table's data is actually being displayed. This is a foundational 4D Design Mode form-architecture technique rather than a plug-in or external API feature. Because only the teaser abstract is available for this note (the original download was an old Windows self-extracting installer that could not be extracted in this environment), this summary reflects only the general proposition described on the historical kb.4d.com page rather than the specific code shown in the full note.

## Featured Technology
- Inherited forms
- 4D form architecture
- Table()/Self() context detection

## Historical Context
Inherited forms — one form defined once and reused across multiple tables for consistent buttons/layout — was a genuinely useful v6.7-era feature, but it created a real problem: form code couldn't automatically tell which table it was currently running against. This note's technique for detecting the calling table from within a shared form's method is squarely a workaround for classic Design Mode form architecture; modern 4D form and object-method architecture provides cleaner, more built-in ways to write table-agnostic form code, though the underlying goal of reusable, standardized forms remains entirely valid today.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- 4D's form architecture and object/form method model have evolved substantially since v6.7, offering more structured ways to write reusable, table-agnostic form logic
- The core idea of standardizing buttons and layout across multiple tables via shared forms remains a common and valid practice in current 4D development

