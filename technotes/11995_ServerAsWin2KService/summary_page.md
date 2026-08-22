# Tech Note: Installation of 4D Server as a Service on Windows 2000 Server

## Overview
- **Technical Note 00-56**
- **Author:** Unknown / not specified
- **Published:** December 1, 2000
- **Product/Version:** 4D Server v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note addresses a practical deployment need that emerged with the release of Windows 2000: running 4D Server as a registered Windows service rather than as a manually launched desktop application. Registering 4D Server this way means the database engine starts automatically whenever the Windows 2000 Server machine boots, removing the need for an administrator to log in and launch 4D Server by hand after every restart. The note walks through the specific steps required to register 4D Server as a service under Windows 2000 Server, and it also surveys some of the service configuration options exposed by the Windows 2000 Services control panel, such as startup type and recovery behavior. This reflects the broader trend of 4D shops in this era moving from desktop-hosted databases toward dedicated, always-on server deployments as e-commerce and intranet usage of 4D Server grew. The featured technology is squarely 4D Server integration with core Windows Server operating system service infrastructure, rather than any 4D-language feature. Because the download archive containing the full walkthrough and example configuration could not be recovered, this summary is based only on the teaser abstract available on the historical kb.4d.com page.

## Featured Technology
- 4D Server
- Windows 2000 Server
- Windows Services

## Historical Context
This note documents how to register 4D Server as a Windows 2000 Service so it auto-launches at boot, a real operational concern in the early Windows NT-family server era. Windows Server service registration mechanics and 4D Server's own startup model have since evolved considerably (4D Server ships with more modern, built-in service-mode installation options on current Windows Server releases), so the specific 2000-era steps described are no longer directly applicable, though the underlying goal of running 4D Server as an unattended background service remains standard practice today.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- 4D Server now offers built-in, documented options for running as a Windows service on modern Windows Server versions, without needing this manual registration workaround
- Windows Server's own service management tooling (services.msc, sc.exe, PowerShell) has changed substantially since Windows 2000

