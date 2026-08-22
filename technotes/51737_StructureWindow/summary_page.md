# Tech Note 08-42: The Structure Window

**Author:** Silvio Belini, 4D Inc. Technical Services  
**Published:** December 2, 2008 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51737  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_42-44_(DEC)/08-42_Structure_Window.pdf

## Overview

The Structure Window is the central visual interface for database schema design in 4D v11 SQL. It provides a graphical representation of all database objects—tables, fields, and relations—and a comprehensive toolbar for creating, modifying, and organizing these elements. The window serves as a single hub for database architects and developers to design, visualize, and manage data structures, with support for visual organization features such as coloring, folder grouping, and advanced sorting.

## Key Points

- **Core objects:** Tables (up to 32,767 per database), Fields (up to 32,767 per table), Relations (many-to-one / one-to-many), Indexes.
- **Toolbar functions:**
  - **Add button:** Create tables, fields, indexes, relations via popup menu or right-click context menu.
  - **Tools button:** Resize tables to fit content (Optimal Size), align multiple tables left/top, sort fields by Alphabetic/Type/Indexed/Related/Visibility/Creation order, or custom drag-and-drop reordering (Alt key).
  - **Color button:** Apply visual color coding to tables, fields, and relations to enhance organization.
  - **Index button:** Opens the Index List window for creation, editing, deletion, and rebuilding of indexes.
  - **Zoom:** Increase/decrease view magnification; Add button is disabled at ≤50% zoom.
  - **Folders button:** Display and organize tables by folder (folders are created and populated via the Explorer window).
  - **Display button:** Toggle visibility of all, invisible tables, invisible fields, unrelated fields, non-indexed fields, and relation lines.
  - **Search field:** Find tables and fields by name (Contains or Starts with) or by table number, with refine options.
- **Information bar:** Context-sensitive display at bottom showing table/field/relation details as you hover (table name/number/trigger events for tables; field name/number/type/null/unique properties for fields; relation direction and names for relations).
- **Inspector palette:** Floating panel for detailed object property editing:
  - **Structure window properties:** Background color and image.
  - **Table properties:** Name, comments, visibility, field order, deletion behavior, SQL compatibility, trigger events/methods.
  - **Field properties:** Name, comments, help tips, type, indexing, data entry controls, SQL compatibility.
  - **Relation properties:** Many-to-One and One-to-Many options, deletion control, color, SQL information.
- **Relation creation:** Click and drag from one field to another to create a relation; order of selection determines direction.

## Featured Technology

- Structure Window visual interface
- Database schema design and visualization
- Table, field, and relation management
- Index creation and management via Index List window
- Inspector palette for property editing
- Folder-based structure organization
- Color-coded visual organization
- Advanced field sorting (alphabetic, type-based, by index status, by relation status)
- Search and filtering tools

## Historical Context

Published December 2008 for 4D v11.3, this comprehensive guide documents the Structure Window as it had evolved to become the single authoritative visual interface for database design. The toolset reflects 4D v11's sophistication: the Folders feature, color coding, and advanced sorting options provided developers with rich organizational tools. The note emphasizes that the Structure Window was not merely a display; it was a full-featured design environment where every aspect of the schema could be manipulated.

## Historical Commentary

**Status:** Still Relevant

The Structure Window concept—a central visual interface for managing tables, fields, relations, and indexes—remains fundamental to 4D database design today. However, the specific UI (with classic Mac/Windows-era palettes and toolbars) has been significantly modernized. 

**Related Updates:**
- **Project Mode (4D v17, 2018):** Introduced file-based, collaborative development with JSON-backed structure storage. Structure editing moved into a redesigned visual editor that works alongside the project file system rather than a monolithic .4DB binary.
- **Modern Design Center (4D v18+):** Provides a contemporary UI with improved drag-and-drop, real-time validation, integrated code/data/design editing, and modern visual feedback (vs. the older palette-and-toolbar model).
- **Core concepts persistence:** The fundamental operations—creating tables/fields/relations, managing indexes, organizing by folders/colors, searching—remain essential and have been preserved with modern UX improvements.
- **Accessibility improvements:** Modern 4D's structure editor is more responsive and offers better keyboard shortcuts and touch-friendly interactions compared to this 2008-era description.

Developers upgrading from 4D v11 will recognize the conceptual model but will encounter a very different visual and operational experience in modern Project Mode.
