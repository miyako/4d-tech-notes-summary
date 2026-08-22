# Tech Note 08-30: 4D v11 SQL Database Access Files (4DLINK)

**Author:** Timothy Penner (Technical Services Team Member, 4D Inc.)  
**Published:** August 20, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=50815  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_28-31_(AUG)/08-30_4D_Link.zip

## Overview

This Technical Note introduces 4DLINK, a new XML-based database access file format in 4D v11 SQL that supersedes the deprecated Path Documents (.PTH) files and combines the capabilities of the command-line interface (CLI). 4DLINK files provide a user-friendly, maintainable way to automate and simplify database launching, connection to 4D Server, and automatic login—eliminating the need for users to manually navigate the Open Database dialog or remember complex server addresses and credentials.

## Key Points

**What Are 4DLINK Files**
- XML-based text files with `.4DLINK` extension
- Contain parameters for automating database access (launch, connect, login)
- Can specify either local database paths or remote 4D Server connections
- Small file size and human-editable (though 4D provides tools to create them)
- Support both single-user and server-based deployments

**Advantages Over Previous Methods**
- **vs. Path Documents (.PTH):** Path Documents stored 4D Server connection info only; 4DLINK also handles local databases and includes automatic login, encryption, and opening mode control
- **vs. Command-Line Interface (CLI):** CLI remains supported but is less user-friendly; 4DLINK provides cleaner abstraction and better integration with OS file management

**Usage Methods (Three Ways to Launch)**
1. **Double-click or drag-and-drop** onto 4D application icon
2. **Selection in 4D Open dialog** (browse and select .4DLINK file)
3. **Open Recent Databases submenu** (if file stored in local preferences folder, it appears in File > Open Recent Databases)

**File Locations (System Preferences)**
- **Windows:** `%APPDATA%\4D\Favorites v11\` (or equivalent local user data directory)
- **Mac OS:** `Users/UserName/Library/Preferences/4D/Favorites v11/`
- Files in these directories automatically appear in the Open Recent Databases submenu

**Basic Structure**
A 4DLINK file consists of two XML lines:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<database_shortcut structure_file="file:///C:/my.4DB" data_file="file:///C:/my.4DD"/>
```

**Attributes for All 4DLINK Files**

| Attribute | Description | Accepted Values | Default |
|-----------|-------------|-----------------|---------|
| `is_remote` | Identifies as remote (4D Server) or local database | `true`, `false` | `false` |
| `user_name` | Login username | text | `""` |
| `password` | Login password (plaintext) | text | `""` |
| `md5_password` | Encrypted password (MD5) | text | `""` |
| `structure_opening_mode` | Database compilation mode | `0` (normal), `1` (interpreted), `2` (compiled) | `0` |

**Attributes for Remote 4DLINK Files (is_remote=true)**

| Attribute | Description | Accepted Values | Default |
|-----------|-------------|-----------------|---------|
| `server_database_name` | 4D Server database name (without extension) | text | `""` |
| `server_path` | 4D Server IP address or DNS name | text (IP or hostname) | `""` |
| `open_login_dialog` | Force login dialog to appear | `true`, `false` | `false` |

**Attributes for Local 4DLINK Files (is_remote=false)**

| Attribute | Description | Format |
|-----------|-------------|--------|
| `structure_file` | Path to .4DB file | `file:///C:/path/to/file.4DB` (Windows) or `file:///Users/path/to/file.4DB` (Mac) |
| `data_file` | Path to .4DD file | `file:///C:/path/to/file.4DD` (or corresponding Mac path) |

**Security Considerations**
- Passwords can be stored in plaintext (`password` attribute) or MD5-encrypted (`md5_password` attribute)
- Encrypted passwords are more secure for shared or public-facing database shortcuts
- 4D provides tools to generate MD5-hashed passwords

**Portability**
- **Remote 4DLINK files** (is_remote=true) can be copied to different machines without modification; they reference the server by IP/DNS name
- **Local 4DLINK files** may require path updates when moved to different machines; file:/// URLs are absolute and may break if database location changes

**Sample Use Cases**
1. **Enterprise Deployment:** Create 4DLINK files pointing to production 4D Server; distribute to users; users simply double-click to connect with automatic login
2. **Multi-User Access:** Store 4DLINK in Open Recent Databases folder; users access database from File > Open Recent instead of memorizing server addresses
3. **Local Development:** Create 4DLINK shortcuts to different local databases during development; developers quickly switch between versions
4. **Automated Launch:** 4DLINK can be used in scripts or batch operations to programmatically launch 4D with specific database parameters

**DTD and Extensibility**
The note includes a complete DTD (database_link.dtd) found in the 4D application's `\Resources\DTD\` subfolder. Developers can reference the DTD to construct custom 4DLINK files with XML editors, enabling integration with custom deployment tools and scripts.

## Featured Technology

- 4DLINK XML format
- Database access automation
- XML Document Type Definition (DTD)
- MD5 password encryption
- Local and remote database parameters
- Automatic login and connection
- Database opening modes (normal/interpreted/compiled)

## Historical Context

Published in August 2008, this note reflects 4D's evolution toward more automation-friendly database deployment. The 4DLINK format represented a significant improvement over the CLI and Path Documents, providing a standard, extensible, XML-based mechanism for database access that could be easily integrated into deployment scripts, system management tools, and user-friendly shortcuts.

## Historical Commentary

**Status:** Obsolete

While 4DLINK files continue to exist in modern 4D versions and can technically still be used for launching local or remote databases, their practical importance has diminished substantially. Modern 4D deployments favor containerization (Docker), cloud hosting platforms, REST API-based remote access, and web-based interfaces over local database shortcuts. Project Mode (introduced v17, 2018) and modern development workflows emphasize version control and continuous integration over manual file-based launching. For contemporary 4D deployments, REST APIs provide a more flexible, scalable approach to database access than 4DLINK shortcuts. The 4DLINK format remains available for backward compatibility and niche scenarios (e.g., launching legacy local 4D databases), but it is no longer a recommended or primary deployment mechanism for new applications.
