# Tech Note: Installation of 4D Server as a Service on Windows 2000 Server

- **Asset ID:** 11995
- **Tech Note #:** 00-56
- **Published:** December 2000
- **Product / Version:** 4D Server not specified
- **Platform:** Windows
- **Author:** Steve Hartman
- **Page URL:** https://kb.4d.com/assetid=11995
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_56-60_(DEC)/00-56_4D_Server_As_Win2K_Service.hqx

## Overview

Steve Hartman of 4D Technical Support documents how to register 4D Server as a native Windows 2000 service via the 'Register as Service' File menu command, and walks through configuring it in the Windows Services MMC console's General, Log On, Recovery, and Dependencies tabs.

## Key Points

- Before registering, the 4D Server application must reside in a folder path containing no spaces or special characters; the database is launched normally under the Local System profile, then Register as Service is chosen from the File menu.
- Once registered, 4D Server is managed like any Windows service through the Services MMC console (Start > Programs > Administrative Tools > Services), including Start/Stop/Pause/Resume and Windows 2000's convenient one-click Restart option.
- The Log On tab controls which account the service runs as (typically Local System); the 'Allow service to interact with desktop' checkbox must be enabled for the 4D Server administration window to remain visible and usable.
- The Recovery tab configures separate failure responses (Take No Action, Run a File, Restart the Service, Reboot the Computer) for the first, second, and subsequent service failures, plus how many days must pass before the failure count resets.
- The Dependencies tab reveals that the 4D Server service depends on the Windows Print Spooler service, meaning a default printer must be installed on the machine or the service will not start.
- Contrasts Windows 2000's Restart option (stop-then-start in one click) with Windows NT 4, which required administrators to manually stop a service, wait, and then start it again.

## Featured Technology

- Register as Service (4D Server File menu command)
- Windows 2000 Services MMC snap-in
- Service Log On / Recovery / Dependencies configuration
- Local System account service execution

## Historical Commentary

**Status:** Still Relevant

Written by Steve Hartman of 4D Technical Support, this note documents the mechanics of registering 4D Server as a native Windows 2000 service via the File menu's 'Register as Service' command, so it launches automatically at boot rather than requiring an interactive login, and walks through the Windows Services MMC console's General, Log On, Recovery, and Dependencies tabs as they apply to 4D Server. The specific Windows 2000-era MMC screenshots and terminology are dated, but the fundamental technique — registering 4D Server as a Windows service for unattended, boot-time startup — remains a standard and still-supported deployment practice for 4D Server on Windows today, largely unchanged in principle across subsequent Windows Server versions.

**References to newer/updated information:**
- 4D Server on Windows still supports registering itself as a Windows service for unattended startup, with the same core Register as Service mechanism described here
- The Windows Services management console (services.msc) has evolved cosmetically since Windows 2000 but the General/Log On/Recovery/Dependencies configuration model described in this note remains fundamentally the same
