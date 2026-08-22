# Tech Note 13-13: Preparing External Databases for Components

**Author:** Milan Adamov, International Technical Support Team Member, 4D SAS.
**Published:** December 18, 2013 | **Product/Version:** 4D v13.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76932
**Download:** https://kb.4d.com/DLTN/TN/2013/13-13_PrepEXDBforComp.zip

## Proposition
This note shows how to give a 4D component its own private external database — built visually in the structure editor and converted to a portable SQL dump for runtime initialization — rather than cluttering a host database with component-specific tables, which is considered bad practice.

## Key Points
- 4D External Databases (since v11) give components a fully separate `.4DB`/`.4DD` data file of their own.
- Building/populating an external database purely via `CREATE DATABASE`/`USE DATABASE ... DATAFILE` SQL commands is tedious; the note's code library lets developers design the structure visually instead.
- `SQL EXPORT DATABASE` generates a SQL dump of the structure (and optionally data), which becomes the basis for a component's `MyComponent_Init` method.
- After the SQL dump is generated, the original tables are deleted from the working database before it is installed as a component.
- `MyComponent_Init`, run from a host's "On Startup" method, recreates the external structure/data file (e.g., a `ContactMaster` folder) the first time the component runs.
- Component form methods must call `USE DATABASE`/`CLOSE DATABASE`-style wrapper methods around SQL calls to target the external database rather than the host's internal engine.
- For Client/Server, `USE REMOTE DATABASE DATAFILE` lets all connected clients share one external database centrally hosted on the 4D Server, instead of each maintaining a local copy.

## Featured Technology
- 4D External Database (`.4DB`/`.4DD` data file, since 4D v11)
- SQL `CREATE DATABASE` / `USE DATABASE DATAFILE`
- `SQL EXPORT DATABASE` for structure/data dump and re-import
- `USE REMOTE DATABASE` for Client/Server-hosted component data

## Best Practices Highlighted
1. Never create host-database tables purely for a component's private/internal data — use an external database instead.
2. Design a component's private structure visually in 4D's structure editor, then generate SQL to automate its recreation, rather than hand-writing `CREATE DATABASE` SQL.
3. For Client/Server deployments, host the component's external database centrally on 4D Server with `USE REMOTE DATABASE` rather than letting each client keep its own local copy.

## Context/Positioning
Published for 4D v13.4, this note targeted 4D component authors wrestling with a genuine architectural constraint: keeping component-private data out of a host database's structure while still being able to design that data relationally.

## Historical Commentary
**Status:** Partially superseded

The core good-practice message — components should avoid polluting a host database with their own tables and should keep private data self-contained — remains sound design guidance. However, the concrete mechanism taught here (structure-editor-built external `.4DB`/`.4DD` databases, SQL `CREATE`/`USE DATABASE DATAFILE`, and manually generated SQL dumps for component initialization) is tied to the classic binary Design Mode structure file format that Project Mode (4D v17+, 2018) moved away from, and to the classic SQL-engine-centric data access model that ORDA later modernized. A component built today would more likely manage its private data through a Project Mode data model and an ORDA datastore rather than a hand-built external SQL database file.
