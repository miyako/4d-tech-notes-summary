# Tech Note: JDBC Connectivity for 4D Server

- **Asset ID:** 32903
- **Tech Note #:** 04-23
- **Published:** June 10, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Yvan Ayaay, Technical Support, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=32903
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_21-25_(MAY)/04-23_JDBC_Connectivity.hqx

## Overview

Yvan Ayaay demonstrates connecting to 4D Server via the 4D JDBC driver in two contexts: writing a Java program that loads the driver, connects, and issues SQL queries/updates directly, and configuring a generic JDBC-compliant application (iSQL-Viewer) to query and edit 4D data with no custom code at all.

## Key Points

- The 4D JDBC driver ships as `jdbc4d.jar`; Java code loads it with `Class.forName("com.fourd.jdbc.DriverImpl")` and connects with `DriverManager.getConnection(url, username, password)` using a URL of the form `jdbc:4d:<ip address>`.
- A full `Connect4D` Java class wraps driver loading and connection with proper `SQLException`/`ClassNotFoundException` handling, and the 4D Server process viewer visibly shows the resulting JDBC connection once established.
- Reading data uses `Statement`/`ResultSet` with `getString`/`getInt`/`getBytes` etc.; the note provides a full type-mapping table between 4D types (Alpha, Text, Real, Integer, Long Integer, Date, Time, Boolean, BLOB) and their Java equivalents (String, Double, Short, Integer, java.sql.Date/Time, Boolean, byte[]).
- Writing data uses `Statement.executeUpdate` with INSERT/UPDATE/DELETE; the note documents the specific SQL grammar the 4D JDBC driver supports at the time, including SELECT with `LEFT JOIN`, `WHERE`, and `ORDER BY`.
- Part II connects the open-source iSQL-Viewer tool to 4D Server purely via configuration: adding the driver JAR to iSQL-Viewer's classpath, then defining a connection with the driver class name, JDBC URL, and credentials in its Connection Manager.
- Once connected, iSQL-Viewer's SQL editor can query, insert, update, and delete 4D Server records, and export results to HTML, XML, or delimited ASCII formats -- illustrating the driver's value for interoperating with any generic JDBC client, not just custom Java code.

## Featured Technology

- 4D JDBC driver (jdbc4d.jar, com.fourd.jdbc.DriverImpl)
- Java Class.forName / DriverManager.getConnection
- JDBC URL format jdbc:4d:<ip address>
- SQL SELECT/INSERT/UPDATE/DELETE support over JDBC
- iSQL-Viewer JDBC client configuration
- 4D-to-Java data type mapping

## Historical Commentary

**Status:** Partially superseded

This note walks through connecting to 4D Server from a Java program (and from the generic iSQL-Viewer JDBC client tool) using 4D's own JDBC driver, covering driver loading, connection strings, and the subset of SQL SELECT/INSERT/UPDATE/DELETE syntax the 2004-era 4D JDBC driver supported. 4D has continued to ship and update a JDBC driver for 4D Server across later versions, so the core proposition -- letting external Java applications query 4D data via SQL -- remains valid today, though the specific driver class names, supported SQL grammar, and the iSQL-Viewer tool shown are dated. Since this note, 4D's SQL engine has also matured substantially (native SQL support), and ORDA-based REST APIs (2017+) now offer a modern, HTTP/JSON alternative to JDBC for external application integration.

**References to newer/updated information:**
- 4D has continued to maintain and update its JDBC driver for 4D Server across later 4D versions, with an expanded SQL command set beyond the 2004-era subset shown here
- 4D's ORDA-based REST APIs (introduced 2017+) now provide an additional, HTTP/JSON-based alternative to JDBC/ODBC for external application integration with 4D data
- The specific tool used for the demo, iSQL-Viewer, is no longer a commonly used SQL client; developers today typically use modern SQL clients or drivers
