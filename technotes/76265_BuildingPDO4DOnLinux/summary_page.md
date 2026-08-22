# Tech Note 11-04: Building PDO_4D on Linux

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** February 24, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76265
**Download:** https://kb.4d.com/DLTN/TN/2011/11-04_Building_PDO_4D_on_Linux/11-04_Building_PDO_4D_on_Linux.zip

## Proposition
This note documents how to build and compile the PDO_4D module — a PHP Data Objects (PDO) driver for 4D — on a Linux operating system, using Debian 5 for the demonstration. It covers preparing the Linux developer environment, the actual build process, and verifying that the compiled module is available to PHP. A pre-built Linux virtual machine appliance with PDO_4D already configured is included, along with instructions for importing it into VirtualBox, finding its IP address, and modifying the included CRUD sample PHP files. The note targets developers who want PHP applications running on Linux to access 4D databases via the standard PDO abstraction layer rather than a 4D-specific driver.

## Key Points
- Explains PDO_4D as a PDO (PHP Data Objects) driver enabling PHP code to talk to 4D SQL Server using standard PDO syntax.
- Walks through preparing a Linux (Debian 5) build environment and the actual compilation process.
- Shows how to verify the PDO_4D module is correctly available/loaded in PHP.
- Includes a ready-made Linux VM appliance with PDO_4D pre-built, importable into VirtualBox.
- Provides instructions for finding the VM's IP address and modifying included CRUD example PHP files.
- Provides guidance for viewing/running the PDO_4D CRUD examples end to end.

## Featured Technology
- PDO_4D PHP Data Objects driver for 4D SQL
- 4D SQL Server accessed from PHP on Linux
- Included pre-built Debian 5 virtual machine appliance

## Best Practices Highlighted
- Use a provided VM appliance to shortcut environment setup when validating a build process
- Verify module availability after compilation before building application logic on top of it

## Context / Positioning
Published in 2011 to support developers running PHP web applications on Linux who wanted standards-based (PDO) connectivity to 4D SQL Server rather than platform-specific drivers, reflecting the era's push toward broader interoperability for 4D.

## Historical Commentary
**Status:** Deprecated

PDO_4D and manually compiling PHP database drivers on Linux is a niche, dated integration technique; 4D's modern interoperability story is built around REST APIs (via ORDA) that any language, including PHP, can call using plain HTTP/JSON without needing a compiled native driver. For new PHP-to-4D integrations, REST is far simpler and more portable than building and maintaining a PDO_4D module.
