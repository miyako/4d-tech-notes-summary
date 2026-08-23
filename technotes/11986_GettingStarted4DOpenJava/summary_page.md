# Tech Note: Getting Started With 4D Open for Java

- **Asset ID:** 11986
- **Tech Note #:** 00-47
- **Published:** October 1, 2000
- **Product / Version:** 4D Open
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=11986
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_46-50_(OCT)/00-47_Getting_Started_Java.hqx

## Overview

Jamras Komoncharoensiri (4D, Inc. Technical Support) introduces 4D Open for Java — a 23-class, pure-Java package for connecting Java applets or standalone programs to a 4D Server — through a complete worked example: an `Employee` applet that connects, displays, searches, adds, deletes, and modifies records.

## Key Points

- 4D Open for Java is distributed as a single jar of 23 classes, runs on any JVM (Windows/Unix/Linux/Mac OS), and works in both Internet Explorer and Netscape Communicator, usable from JDK 1.2+, Visual J++, JBuilder, MRJ SDK 2.2, or CodeWarrior.
- Every 4D Open for Java program follows three steps: (1) create an `opDriverManager` and call `getConnection(ipAddress)` to obtain an `opConnection`; (2) call `connection.startProcess(workstation, user, password, processName)` to start a 4D Server process (up to six simultaneous processes per connection); (3) issue read/write requests as methods of the resulting `opProcess` object, then close with `connection.stopProcess(process)` and `connection.CloseConnection()`.
- The example `Employee` class extends `Applet` and implements `ActionListener, opConstants`; its constructor builds the main page and pop-up windows (New Entry, Search, Delete, Modify) up front, and a single `actionPerformed(ActionEvent event)` method dispatches all user actions by comparing the event source against each button.
- `doConnect()` hardcodes a server IP, obtains a connection via `opDriverManager`, starts a process against the `Employee.4DB` database, and calls `process.RecordsInTable(table)` to get the initial record count; `closeConnection()` calls `stopProcess`/`CloseConnection` when the user quits.
- `doPrint()` retrieves all records with `process.AllRecords(table)` into an `opDataArray[]`, tracked via `selection.mRecordsInSelection`, then renders them with helper methods `getResult` and `printDataArray`.
- Searching, adding, deleting, and modifying records each follow a two-action pattern: a first button opens a dedicated dialog window, and a second button (e.g. `searchButton2`) in that dialog executes the actual 4D Open for Java request and returns results to the main display.

## Featured Technology

- 4D Open for Java (opDriverManager, opConnection, opProcess classes)
- startProcess/stopProcess connection lifecycle
- opDataArray result handling
- Java Applet class connecting to a 4D Server
- actionPerformed event-driven UI for connect/search/add/delete/modify
- 4D Server multi-process connections (up to six per client)

## Historical Commentary

**Status:** Obsolete

This introductory note walks a Java developer through 4D Open for Java's three-step connection pattern (opDriverManager to get an opConnection, startProcess to open a 4D Server process, then opProcess request methods to read/write data) using a complete Employee applet example that implements connect, display-all, search, add, delete, and modify operations. It is a clear, ground-up tutorial for its era's Java-to-4D-Server integration path, but 4D Open (including 4D Open for Java) has been discontinued, and Java applets themselves are obsolete technology since browsers dropped NPAPI support; a Java client today would instead call 4D's REST/ORDA data server over HTTP, which needs none of this driver/connection/process machinery.

**References to newer/updated information:**
- 4D Open for Java has been discontinued along with the rest of the 4D Open product line
- Java applets are obsolete; browsers no longer support the NPAPI plugin mechanism required to run them
- 4D's REST/ORDA data server is the modern replacement for building external (including Java) clients that read/write 4D Server data
