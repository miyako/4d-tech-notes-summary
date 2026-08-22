# Tech Note 14-05: Auto Update Feature 4D v14

**Author:** Julian Weidenbacher, Technical Services Team Member, 4D Inc.
**Published:** March 21, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77005
**Download:** https://kb.4d.com/DLTN/TN/2014/14-05_AutoUpdateV14.zip

## Proposition
4D v14 introduces a built-in mechanism for fully automated updates of merged server/standalone applications, letting developers make the entire download-extract-backup-restart cycle transparent to the end user via new commands like `SET UPDATE FOLDER` and `RESTART 4D`.

## Key Points
- Developer side: build, compress, and host the update (the example uses an FTP server, but any distribution channel works).
- Customer side: download, extract, prepare, run the update, and restart — all now automatable, whereas previously it required manual, error-prone steps.
- Critical setup rules: never include "update" in the application's name; keep the data file outside the database folder; store backups/downloads in the user's temp folder to avoid access-rights issues.
- Extraction can use platform-native tools (`LAUNCH EXTERNAL PROCESS` with 7-zip on Windows, native `open` on Mac) or 4D's PHP execution bridge.
- Before replacing the application folder, back up logs, the external preferences file (available since 4D v13), and any web folder content, then restore them into the updated build.
- `SET UPDATE FOLDER` points 4D at the new build (works with 4D Server or 4D Volume Desktop merged apps); `RESTART 4D` terminates the app and hands off to the updater, which performs the swap.
- Startup code detects update success/failure via a marker file (e.g., `Version.txt`), and `Get last update log path` retrieves the updater's log for troubleshooting.

## Featured Technology
- `SET UPDATE FOLDER`, `RESTART 4D`, `Get last update log path` (4D v14)
- 4D Internet Commands `FTP_` routines / `HTTP Get` for update distribution
- `LAUNCH EXTERNAL PROCESS` with 7-zip (Windows) / native tools (Mac) for extraction

## Best Practices Highlighted
1. Keep the data file outside the application/database folder so it survives an update untouched.
2. Back up logs, preferences, and web content before the update replaces the application folder.
3. Detect and log update success/failure at startup so support staff can diagnose failed updates.

## Context/Positioning
Published as 4D v14 shipped, this note showcased a major deployment-quality-of-life feature aimed at reducing support burden and end-user friction for teams distributing merged 4D applications.

## Historical Commentary
**Status:** Still relevant

The built-in update architecture this note documents — `SET UPDATE FOLDER` plus `RESTART 4D` and the accompanying updater tool and logging — remains part of 4D today and is still the standard way to auto-update merged/standalone and client/server 4D applications. The peripheral details are what have aged: distributing updates via FTP and unpacking them by shelling out to 7-zip via `LAUNCH EXTERNAL PROCESS` reflect 2014-era practice, whereas a modern implementation would more likely fetch updates over HTTPS/REST. The core update-folder/restart workflow itself, however, is unchanged.
