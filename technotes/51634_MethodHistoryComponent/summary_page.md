# Tech Note 08-40: Method History Component

**Author:** Thomas Maul, 4D Germany  
**Published:** November 20, 2008 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51634  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_40-41_(NOV)/08-40_Method_History.zip

## Overview

The Method History Component is a sophisticated, reusable tool for tracking and comparing method modifications in 4D v11 SQL Release 3. It demonstrates advanced 4D capabilities: macro events (auto-triggered on method save), SQL Pass-through (for flexible storage across databases), Web Area rendering (for visual diff display), and component-based packaging. Every method change is automatically recorded with timestamp and user attribution, enabling developers to browse, compare, and retrieve previous versions of any method.

## Key Points

- **Automatic Capture via Macros:**
  - The "method_save" macro is automatically triggered each time a method is saved in the Method Editor.
  - No action required from developers beyond installing and initializing the component.

- **Storage Flexibility:**
  - **Local storage:** Methods stored in the host database via a local Method_History table (simple, portable, lost if host data file is replaced).
  - **External 4D Server storage:** Via SQL pass-through TCP/IP (Release 3+, no ODBC configuration needed).
  - **ODBC source storage:** Via SQL pass-through ODBC (Release 2+, requires ODBC DSN configuration).
  - **Multi-project support:** Specify a project name to store multiple projects' method histories in the same data file.

- **MethodHistory_Init Method (Initialization Parameters):**
  - `Server name`: SQL_INTERNAL (constant) for host database, IP/server name for external 4D Server, or DSN name for ODBC.
  - `User`: Database username (required for external connections; defaults to "Designer" if using 4D's password system).
  - `Password`: Database password (required for external connections).
  - `Project`: Project/module name (defaults to structure name; useful for consistent naming across version changes).
  - `Designer`: Username to attribute changes to (auto-filled if 4D's password system is active; otherwise pass manually).
  - `AutoCreateTable`: Boolean (default true) to auto-create the Method_History table if needed.
  - Call without parameters to disable method history.

- **History Comparison:**
  - Open the Method_Compare macro from the macro menu while a method is open in the Method Editor.
  - A dialog displays all stored versions with save timestamps and usernames.
  - Select any two versions (using Command+click on Mac or Ctrl+click on Windows); they appear side-by-side.
  - Differences are color-coded: orange (modified), green (added), red (deleted).
  - Horizontal and vertical scrollbars allow navigation through large methods.
  - "Copy older to clipboard" button retrieves a previous version for paste/restore.

- **Technical Architecture:**
  - **Component:** Protects internal variables, prevents namespace collisions, auto-installs macros and web resources.
  - **Macros:** Triggered on method save; capture method name/content to a "jobs" array processed by a background loop.
  - **Web Area rendering:** Dynamically builds HTML/DOM tree for diff display; CSS styling customizable via included CSS file.
  - **JavaScript diff logic:** Uses jsdifflib/jsdiffview (open-source, Snowtide Informatics) to compute line-level differences.
  - **SQL Pass-through:** All record handling uses SQL statements only, enabling seamless internal/external database switching without code changes.

- **Unicode Support:**
  - Recommended to run in Unicode mode (mandatory for methods >32K in size).
  - In compatibility mode (disabled Unicode), text variables are limited to 32K, truncating large methods.

- **SQL Dialect Customization:**
  - Component tested with MS SQL Server 2008; other SQL dialects may require modifications to MethodHistory_Start method's SQL syntax.

- **Installation & Deployment:**
  - Drop component into the Components folder of the host database.
  - Call `EXECUTE METHOD("MethodHistory_init";*;SQL_INTERNAL)` (or variant with external server params) in the On Startup Method.
  - Uses EXECUTE METHOD so component can be removed without breaking compilation (method not invoked directly in compiled mode).
  - Component only activates in interpreted mode; safe to leave in place during deployment.

## Featured Technology

- 4D macro system (macro events, auto-triggered on method save)
- SQL Pass-through over TCP/IP and ODBC
- Web Area form object for dynamic HTML rendering
- JavaScript diff library integration (jsdifflib/jsdiffview)
- CSS styling for visual diff display
- Component architecture for encapsulation and reusability
- SQL-only data access pattern (no language-specific commands)
- External database connectivity for distributed storage

## Historical Context

Published November 2008 for 4D v11 SQL Release 3, this component exemplifies the capability-building mindset of 4D's early SQL era. The note showcases several cutting-edge (for 2008) 4D features: macros were a relatively new way to hook into IDE events, the Web Area was a powerful but unconventional choice for rendering complex UIs, and SQL pass-through enabled true database-independent storage. The component's architecture—leveraging open-source JavaScript libraries executed within a Web Area—demonstrates creative problem-solving in an era before rich native form objects and web component standards were common. The component was practical for development teams needing method version tracking without external source control systems (a luxury in 2008).

## Historical Commentary

**Status:** Obsolete

The Method History Component represents a valid and clever solution for 2008, but has been completely superseded by modern development practices and 4D's native tooling.

**Related Updates:**
- **Project Mode (4D v17, 2018):** Introduced git-based version control as the foundation for 4D projects. All source files (methods, forms, classes, etc.) are now stored as JSON/text files in a repository, enabling standard git history, branching, and diff tools.
- **Native IDE History:** Modern 4D's Method Editor includes built-in history/comparison features directly in the IDE, eliminating the need for external components.
- **Source Control Integration:** Modern 4D seamlessly integrates with git (via GitHub Desktop, GitKraken, command-line, etc.), providing professional-grade version tracking and collaboration.
- **Component Architecture Deprecation:** The pattern of using components for IDE-level tools (macros + Web Area rendering) is no longer used; native IDE extensions and language server plugins are the modern equivalent.
- **Web Area Rendering Superseded:** Modern form objects, web components, and native rendering APIs have eliminated the need for creative Web Area workarounds.

Developers working with modern 4D should never need to build or use a method history component; git and the IDE provide comprehensive version tracking out of the box. This note is valuable purely from a historical perspective, illustrating how 4D developers solved a real problem with the tools available at the time.
