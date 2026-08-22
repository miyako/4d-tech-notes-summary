# Tech Note 08-22: Web Serving the 4D Ajax Framework on 4D Client

**Author:** Jason Zajdel | **Published:** June 12, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=50104  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_21-24_(JUN)/08-22_4DAF_on_4D Client.pdf

## Proposition
Deploy the 4D Ajax Framework web server on a client machine rather than the database server, enabling remote web-based data access while keeping the main 4D Server database secure behind a firewall.

## Key Points
- **Architecture advantage:** Web processing on client machine frees the database server to focus solely on database operations; only port 19813 (4D client/server communication) needs to be opened in the firewall.
- **Security advantage:** The main 4D database and 4D Server remain inside the firewall; only the client machine running 4DAF is exposed to the internet.
- **Component installation:** For 4D v11 SQL 11.2, copy the "4DAF v11.2 Unicode.4dbase" component into a "Components" folder next to the structure file; for 4D 2004, use 4D Insider's Install/Update menu.
- **Support folder migration:** In 4D v11 SQL 11.2, the Support folder has moved from inside the component's Extras to the Resources folder next to the database structure (upgrades only).
- **Plugins folder:** Copy the 4D Pack plug-in to a Plugins folder next to the structure.
- **Database methods:** Add DAX_Dev_Initialize, DAX_Dev_Shutdown, and DAX_Dev_OnWebConn to the appropriate database methods; create a Compiler_Web method with DAX_Dev_CompilerWeb.
- **Web preferences:** Enable "Publish database at Startup" and use TCP port 8080 (or configure as needed); set Starting Mode to "Non-contextual Mode".
- **WebFolder location:** For 4D v11 SQL, use Get 4D folder(HTML Root Folder) to discover the auto-generated WebFolder path (typically Windows: C:\Users\user_name\AppData\Local\4D\...\WebFolder\ or Mac: Macintosh HD:Users:user_name:Library:Caches:4D:...:WebFolder:); for 4D 2004, WebFolders are in the same directory as the 4D Client application by default.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- 4D Client/Server network architecture
- 4D Pack plug-in
- Web server publishing from non-server application
- WebFolder and Resources folder deployment
- Mac OS X and Windows platform-specific paths

## Context / Positioning
Published mid-2008 for 4D v11 SQL Release 2, this note reflects an era when 4D web publishing required the Web 2.0 Pack subscription and manual deployment of components onto client machines. The client-as-publisher pattern was a legitimate distributed architecture strategy before Project Mode consolidated web serving into the server itself.

## Historical Commentary
**Status:** Obsolete

This deployment pattern is no longer applicable or recommended. The 4D Ajax Framework and 4D Web 2.0 Pack have been discontinued, superseded by 4D's modern web component architecture and Qodly. Additionally, modern 4D Server (v16+) includes built-in web publishing capabilities without requiring a separate client machine to act as a publisher. The security and load-balancing benefits this note describes are now achieved through standard server-side scaling and containerization rather than distributed client-based publishing.
