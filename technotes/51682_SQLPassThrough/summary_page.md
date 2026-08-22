# Tech Note 08-41: 4D v11 SQL Pass-Through without ODBC

**Author:** Charles Vass, 4D Inc. Technical Services  
**Published:** November 25, 2008 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51682  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_40-41_(NOV)/08-41_SQL_Pass_Through.zip

## Proposition

4D v11 SQL Release 3 introduced SQL pass-through, a native, direct TCP/IP communication channel that allows 4D Professional applications to connect to 4D Servers (or other SQL data sources) without ODBC drivers or third-party plug-ins. This feature addresses a critical gap left by the discontinuation of the 4D Open plug-in, restoring full database-to-database communication capabilities with dramatically improved speed and flexibility over ODBC.

## Key Points

- **Configuration & Prerequisites:**
  - Only a 4D Server v11 SQL can accept direct SQL queries from other 4D applications.
  - Only 4D Professional product line applications can initiate direct connections to another 4D application.
  - Communication occurs via TCP/IP; SSL encryption is available if enabled on the target 4D Server's SQL Preferences.
  - Only one connection is authorized per process; additional simultaneous connections require separate processes.
  - Direct connections are only accepted by 4D Server if the SQL server is started.

- **SQL LOGIN/LOGOUT Renaming:**
  - All ODBC-prefixed commands (e.g., ODBC LOGIN, ODBC EXECUTE, ODBC EXPORT, ODBC IMPORT, ODBC GET LAST ERROR) have been renamed with SQL prefix (SQL LOGIN, SQL EXECUTE, SQL EXPORT, SQL IMPORT, SQL GET LAST ERROR).
  - Associated constants (e.g., ODBC All Records, ODBC Asynchronous, ODBC Connection Time Out) have been renamed to SQL equivalents.
  - Obsolete commands: USE EXTERNAL DATABASE and USE INTERNAL DATABASE are no longer maintained.

- **SQL LOGIN Syntax:**
  ```
  SQL LOGIN(sourceName{; userName; passWord{; *}})
  ```
  - `sourceName`: IP address/server name, DSN name, or "" (shows dialog).
  - `userName`: Login name (required for external connections).
  - `passWord`: Password (required for external connections).
  - Optional `*` parameter: If present, all SQL statements in the following Begin SQL/End SQL block are executed on the external database; if omitted, statements run on the internal database.

- **SQL LOGOUT:** Closes a previously opened connection; if omitted, all SQL statements in the following Begin SQL/End SQL block execute on the internal database.

- **Synchronous Data Exchange:**
  - All direct connections operate in synchronous mode, automatically eliminating synchronization and data integrity concerns.
  - Communication speed is significantly faster than ODBC.

- **Field-Level Change Tracking:**
  - The note includes a proof-of-concept for recording field-level modifications with ownership metadata and collision prevention.
  - Demonstrates pushing changes from a 4D Professional database to a 4D Server and pulling changes back.
  - Shows how to apply exchanged data to target tables with conflict resolution.

- **BLOB Storage Enhancements (Release 3):**
  - New picture variable and picture array BLOB storage capabilities.
  - Enables efficient handling of large binary data types across connections.

## Featured Technology

- SQL pass-through over TCP/IP
- Direct 4D Server to 4D Professional connections (no ODBC required)
- SQL LOGIN/LOGOUT command set
- Synchronous data exchange with automatic integrity guarantees
- Field-level change tracking with collision prevention
- BLOB storage in picture variables and arrays
- SSL-encrypted SQL connections
- Connection pooling per process

## Historical Context

Published November 2008 for 4D v11 SQL Release 3, this technical note marked a pivotal moment for 4D: the restoration of direct database-to-database communication capabilities (lost when 4D Open was discontinued) and the introduction of a faster, more flexible alternative to ODBC-based external data access. For developers upgrading from pre-SQL versions (v2004 and earlier), this feature made 4D v11 SQL adoption more attractive by providing a proven path for data exchange and system integration. The note's emphasis on synchronous communication and field-level change tracking reflects the real-world needs of multi-database environments and distributed data synchronization.

## Historical Commentary

**Status:** Superseded

SQL pass-through remains conceptually sound and is still technically available in modern 4D for backward compatibility. However, it has been largely superseded by more modern approaches to inter-application communication.

**Related Updates:**
- **ORDA (Object-Relational Data Model, 4D v2018+):** Provides a modern, object-centric abstraction for data access and cross-application communication, making raw SQL pass-through less necessary for most use cases.
- **Remote Objects and Web Services (4D v18+):** Modern 4D emphasizes REST APIs and remote object methods as the preferred mechanisms for database-to-application and application-to-application communication, with better security, versioning, and async support.
- **Security Evolution:** While SSL encryption for SQL connections was advanced for 2008, modern 4D uses TLS 1.2+ and certificate-based authentication, providing stronger guarantees than the SSL mechanism described here.
- **Data Synchronization:** Modern patterns (ORDA entities, JSON-based sync, event-driven architecture) have largely replaced the field-level change tracking approach described in this note's proof-of-concept, offering better scalability and conflict resolution.

Developers using 4D v11 SQL should understand this feature as a historical foundation; modern projects should prefer ORDA, Remote Objects, or REST-based integration patterns.
