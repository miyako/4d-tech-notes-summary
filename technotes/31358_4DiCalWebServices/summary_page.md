# Tech Note: 4D, iCal and Web Services

- **Asset ID:** 31358
- **Tech Note #:** 04-07
- **Published:** February 19, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac
- **Author:** Sati Hillyer, Technical Support Engineer, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=31358
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_05-09_(FEB)/04-07_iCal_Web_Services.hqx

## Overview

Sati Hillyer shows how to schedule precisely-timed 4D operations — beyond what 4D Server's built-in backup scheduler supports — by exposing a 4D method as a SOAP Web Service and having Apple's iCal 1.5.1 trigger an AppleScript (via a calendar alarm) that calls it, demonstrated through a scheduled bi-monthly backup and a scheduled weekly Quick Report print job.

## Key Points

- 4D 2003's Web Services feature lets any method be called remotely and is platform-independent, meaning the 4D database can run on Mac or Windows even though iCal itself is Mac-only.
- Scenario 1 (Scheduled backup): a method uses `BK Begin full backup`, `BK Start copy`, a polling loop on `BK Get state`, and `BK END BACKUP` to drive the 4D Backup plug-in, returning a SOAP text result (`SOAP DECLARATION(bkResult;Is Text;SOAP Output;"backup_result")`).
- Scenario 2 (Scheduled report): a Quick Report project (e.g. "Inventory_Report") is built with the Quick Report Wizard targeting the printer, then a method generates and prints it programmatically on each call.
- To expose a method as a Web Service, enable "Offered as a Web Service" (and optionally "Published in WSDL") in Method Properties, start the Web Server (or set it to start at Startup), and enable "Allow Web Services Requests" in preferences.
- The AppleScript uses the `call soap` command against a local SOAP endpoint (`http://127.0.0.1:8080/4DSOAP/`), setting `method_name`, `method_namespace_URI`, and `SOAP_action` properties, and displays a dialog with 4D's confirmation or an error message.
- An iCal event is created with the desired recurrence (e.g. 1st/15th of the month at 9pm, or every Monday at 8am) and its alarm set to "Open File," pointing at the compiled AppleScript, so the alarm firing launches the script, which calls 4D via SOAP to run the backup/report.
- References a related Tech Note (30140) covering 4D/iCal integration from a different angle.

## Featured Technology

- 4D 2003 SOAP Web Services (method published as Web Service/WSDL)
- Apple iCal 1.5.1 scheduled alarms (Open File action)
- AppleScript SOAP web service calls (call soap command)
- 4D Backup plug-in scripted via BK Begin full backup / BK Start copy / BK Get state
- 4D Quick Report generation and printing from a method
- 4D Web Server startup publishing and Allow Web Services Requests option

## Historical Commentary

**Status:** Obsolete

This note shows how to use Apple's iCal 1.5.1 as a poor-man's task scheduler for 4D, by having a calendar alarm launch an AppleScript that calls a 4D method exposed as a SOAP Web Service, illustrated with a scheduled database backup and a scheduled Quick Report print job. The specific mechanism is thoroughly obsolete: iCal was renamed/rearchitected into Apple's Calendar app long ago, its AppleScript-driven SOAP calling convention is gone, and 4D itself has moved from SOAP to REST/JSON web services. The underlying need — triggering 4D business logic (like backups or scheduled reports) on a precise recurring schedule — is now handled far more robustly by native 4D scheduling (On Server Startup / Execute on Server methods, 4D Server's own scheduler enhancements, or OS-level schedulers) rather than a calendar app and an AppleScript SOAP shim.

References to newer/updated information:
- Apple's iCal was renamed and re-architected into the Calendar app; the described AppleScript 'call soap' invocation and alarm-triggered script launching workflow described here no longer applies
- 4D's SOAP Web Services have been superseded by REST/JSON web services in modern 4D development
- Modern 4D applications typically use native scheduling (4D Server's scheduler, timed/periodic processes, or OS-level cron/Task Scheduler) rather than a calendar app's alarm system to trigger recurring tasks like backups or reports
