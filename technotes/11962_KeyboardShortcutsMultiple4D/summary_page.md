# Tech Note: Keyboard Shortcuts for Multiple Instances of 4D (TN 00-46)

**Author:** Not specified in source document
**Published:** October 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11962
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2000/windows/tn_2000_46-50_(oct)/00-46_keyboard_shortcuts.exe

## Overview
This Tech Note covers a technique for creating shortcuts that launch 4D or 4D Server directly against a specific data file, including running multiple instances at once.

## Key Points
- Its practical value is twofold: it speeds up the everyday workflow of reopening the same database repeatedly during development, and it enables running several separate instances of 4D on the same machine simultaneously, each pointed at a different database — useful for side-by-side testing, comparing versions, or simulating multiple users locally.
- Because only the teaser text and a note that the linked example is an old Windows self-extracting .exe survive in this archive (the Mac/Windows download links are no longer functional), the exact shortcut-construction steps for each platform are not preserved here.
- The technology involved is essentially OS-level file/shortcut mechanics of the classic Mac OS 9 and Windows 9x/2000/NT era rather than 4D language code — creating an alias or shortcut with an embedded reference to a specific data file, so double-clicking it launches the correct 4D executable pre-targeted at that file.
- This kind of trick was especially valuable to 4D Server administrators and developers juggling several client/test databases, since 4D at the time did not offer a rich built-in "recent databases" or command-line launch experience comparable to what exists in current releases.
- The note is a small, utilitarian workflow tip rather than a feature deep-dive, reflecting the kind of practical day-to-day guidance the 4D Technical Notes series regularly published alongside more substantial technique articles.

## Featured Technology
- 4D/4D Server launch shortcuts
- Multiple simultaneous 4D instances
- Open-database dialog bypass

## Historical Context
This short note describes creating OS-level shortcuts (Mac/Windows) to launch 4D or 4D Server directly against a chosen structure/data file, bypassing the Open-database dialog and enabling multiple simultaneous 4D instances on one machine — a practical developer/QA convenience of the classic Design-Mode era. The technique is OS-shortcut plumbing rather than 4D language code, so its mechanics (creating Mac aliases or Windows shortcuts with command-line style targeting) are dated to classic Mac OS/Windows 9x/2000 conventions, though running multiple 4D instances against different databases for testing remains a relevant workflow need today, now typically achieved differently (command-line launch parameters, recent-databases lists, or separate user accounts). Related updates since: Modern 4D includes command-line launch options and a persistent recent-databases list that reduce the need for hand-built OS shortcuts; Running multiple simultaneous 4D/4D Server instances for testing is still a common workflow, but is now usually handled via documented command-line arguments rather than custom shortcut tricks. The full Tech Note PDF/text could not be recovered for this archive entry because the linked archive was an old Windows self-extracting .exe installer that could not be extracted without a Windows environment; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
