# Tech Note 10-12: PDO_4D Driver

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** April 16, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76084
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_11-14_(APR)/10-12_PDO_4D.zip

## Proposition
This note documents PDO_4D, an open-source project sponsored by 4D that produces a PHP Data Objects (PDO) driver enabling Apache, IIS, and other third-party web servers to access a 4D database's SQL Server through standard PHP code, allowing 4D and PHP development responsibilities to be cleanly separated.

## Key Points
- **PDO** is a PHP extension providing a consistent, database-agnostic interface; a specific driver (like PDO_4D) is required per backend.
- **PDO_4D** was created as an open-source project sponsored by 4D, made possible by the SQL Engine introduced in 4D v11 SQL.
- PDO_4D lets PHP code run both **raw SQL statements** and **4D methods** against a 4D SQL Server.
- Enables **coding compartmentalization**: a 4D expert can focus on backend database logic while a PHP expert builds the frontend.
- The note walks through a full **Apache + PHP + PDO_4D** setup for developers new to third-party web server stacks.
- A complete **CRUD example** (Create, Read, Update, Delete) demonstrates end-to-end usage.

## Featured Technology
- PDO_4D open-source PHP Data Objects driver
- 4D v11/v12 SQL Engine/SQL Server
- PHP PDO abstraction layer
- Apache / IIS web server integration

## Context / Positioning
Published as 4D's SQL engine and SQL Server were maturing, this note showcased an early third-party integration path meant to widen 4D's reach into the broader PHP web development ecosystem.

## Historical Commentary
**Status:** Partially Superseded

This note documents PDO_4D, an open-source PDO driver 4D sponsored so that PHP running on Apache or IIS could access a 4D database's SQL Server directly, decoupling PHP front-end development from 4D back-end coding.

This was a notable integration path when 4D's SQL engine was still new, but the surrounding architecture has since been superseded: modern 4D applications typically expose data through native REST/ORDA APIs rather than requiring a third-party web server and a separate PDO driver bridge, and the PDO_4D open-source project itself has seen little to no maintenance in the years since. It remains a historical curiosity rather than a recommended integration technique today.
