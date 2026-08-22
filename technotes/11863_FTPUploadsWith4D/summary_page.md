# Tech Note: FTP Uploads with 4D

**Author:** Not specified
**Published:** December 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11863

## Overview
This Tech Note demonstrates building an FTP client within a 4D application to connect to remote FTP servers and upload files, using 4D's FTP commands from the Internet Commands plug-in.

## Key Points
- Builds a complete FTP client within 4D for file uploads
- Cross-platform sample application (Mac & Windows)
- Supports connecting to FTP sites, creating directories, and uploading files
- Requires adaptation for specific FTP site credentials and configuration
- User needs FTP site access with upload/directory creation privileges

## Featured Technology
- 4D Internet Commands (FTP protocol support)
- FTP file upload and directory management
- Cross-platform networking

## Historical Context
**Status:** Obsolete

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). FTP was a primary file transfer protocol in 1999, but has since fallen out of favor due to security concerns (plaintext credentials). Modern alternatives include SFTP, HTTPS uploads, and cloud storage APIs. 4D Internet Commands have been largely superseded by built-in HTTP commands and the 4D.HTTPRequest class in modern 4D. The note documents a common late-1990s pattern of building internet protocol clients within database applications.
