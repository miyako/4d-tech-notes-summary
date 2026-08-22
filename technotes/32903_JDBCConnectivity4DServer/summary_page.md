# Tech Note 04-23: JDBC Connectivity for 4D Server

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** June 10, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32903
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_21-25_(MAY)/04-23_JDBC_Connectivity.exe

## Overview
This Tech Note documents the latest JDBC (Java Database Connectivity) driver for 4D Server, which enables Java programmers to access and manipulate data hosted in 4D Server, and more broadly lets any JDBC-aware application integrate with 4D Server as a data source. It describes the driver as a multi-platform API usable in any environment running a Java Virtual Machine, working by converting standard JDBC calls into 4D Server's own network protocol so that connections and queries can be processed by the server transparently to the calling Java code. The note demonstrates concretely how to use this JDBC driver from a Java program, walking through establishing a connection to 4D Server and issuing queries against the 4D database from Java. This reflects 4D's broader mid-2000s interoperability strategy of exposing 4D Server as a standards-compliant database backend reachable from non-4D environments (alongside ODBC connectivity), extending 4D's reach into heterogeneous, Java-centric enterprise environments that might not otherwise consider 4D as a viable data store. It is aimed at developers who need to integrate an existing or new Java application with a 4D Server-hosted database.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- A guide to using the JDBC driver for 4D Server, a multi-platform Java API that translates JDBC calls into 4D Server's network protocol so Java programs can query and manipulate 4D data.

## Featured Technology
- JDBC driver for 4D Server
- Java Database Connectivity
- 4D Server network protocol

## Historical Context
**Status:** still relevant

The general need for external (Java-based) applications to connect to and query a 4D Server database via JDBC remains valid today, and 4D has continued to offer and update a JDBC driver for 4D Server across subsequent versions, so this note's core proposition is still conceptually relevant. However, the specific driver version and Java integration details demonstrated in this 2004 note are dated, and any modern integration would use a current release of 4D's JDBC driver rather than the one described here.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
