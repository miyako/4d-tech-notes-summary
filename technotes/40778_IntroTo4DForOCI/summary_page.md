# Tech Note 05-39: Introduction to 4D for OCI

**Author:** Yvan Ayaay, Technical Support Engineer, 4D Inc.
**Published:** December 5, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=40778
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_37-39_(NOV)/4D_For_OCI_2004.zip

## Overview
This note introduces the 4D for OCI plug-in, which allows 4D applications to act as native Oracle clients via the Oracle Call Interface (OCI), and walks through installing and configuring Oracle client connectivity on both Windows and Mac OS X.

## Key Points
- 4D for OCI supports Oracle 8i, 9i, and 10g databases and requires the Oracle Database Client software/libraries to be installed for the plug-in to function.
- **Windows:** install via the Oracle Universal Installer, then configure a `tnsnames.ora` network file (via Net Configuration Assistant or manually) specifying protocol, host address, and port.
- **Mac OS X 10.3.x:** a detailed terminal-based process using the Oracle 10g Instant Client — creating a root-owned `/Oracle` directory, copying `libclntsh.dylib` into `/usr/lib`, and creating a user `environment.plist` file to configure the runtime environment.
- Positioned as the foundation for the companion TN 05-45 on 4D for OCI error handling.

## Featured Technology
- 4D for OCI plug-in
- Oracle Call Interface (OCI)
- Oracle Instant Client / Oracle Database Client
- tnsnames.ora configuration

## Historical Context
The 4D for OCI plug-in has since been discontinued as a distinct product, with 4D's connectivity story moving toward its own SQL engine (v11 SQL, 2007) and ODBC-based database connections. The Mac OS X installation steps shown here (manual dylib placement, environment.plist configuration) reflect early-2000s macOS conventions that have since been superseded by later security and library-loading changes (e.g., System Integrity Protection), making the specific installation walkthrough obsolete.
