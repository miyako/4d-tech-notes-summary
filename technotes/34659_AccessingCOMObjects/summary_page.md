# Tech Note 04-44: Accessing COM Objects within 4D

**Author:** Not specified in source
**Published:** November 5, 2004 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=34659
**Download:** https://kb.4d.com/ftp:ftp.4d.com/ACI_TECHNICAL_NOTES/2004/Windows/TN_2004_41-45_(SEP)/04-44_Accessing_COM_Objects.exe

## Overview
This note explains how the new LAUNCH EXTERNAL PROCESS command in 4D 2004 makes it possible to access Windows COM objects from within a 4D application, aided by a code-generating CreateObject macro from the 4D Macro Pack.

## Key Points (from available teaser)
- LAUNCH EXTERNAL PROCESS is the new 4D 2004 command that enables COM object access.
- The CreateObject macro (4D Macro Pack) generates the 4D script needed to access a COM object.
- The macro includes an object browser for exploring a COM object's properties before coding against it.
- The note demonstrates this macro's implementation to show how COM objects can be leveraged in a 4D application.

## Featured Technology
- LAUNCH EXTERNAL PROCESS command
- Windows Component Object Model (COM)
- CreateObject macro / 4D Macro Pack
- COM object browser tooling

## Historical Context
**Note:** Only the on-page teaser paragraph was recoverable for this Tech Note; the full PDF and example database were not accessible (old archive format not retrievable in this environment), so the specific COM targets and code walkthrough cannot be detailed here. COM is a Windows-only legacy automation technology that has been largely superseded industry-wide by .NET, web services, and REST/JSON APIs, making this Windows-specific integration technique of historical interest rather than a currently recommended approach for cross-platform 4D development.
