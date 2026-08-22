# Tech Note 20-07: Implementing a Remote Datastore

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 22, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78452
**Download:** https://kb.4d.com/DLTN/TN/2020/20-07_RemoteDatastore.zip

## Proposition
4D v18 introduced remote datastores: a 4D application can expose its ORDA datastore as a REST server so another 4D application can connect to and manipulate it natively, as an alternative to SQL server-based cross-database access. This note covers server-side exposure/security setup and client-side connection.

## Key Points
- **Expose as REST server**: a Database Settings toggle (Web section, REST resource tab) requiring a 4D Developer Professional or 4D Server license, disabled by default.
- **Read/Write privilege setting**: default `<Anyone>` access via 4D users/groups; takes effect immediately without restarting the web server or database.
- **`On REST Authentication method`**: custom authentication hook with parameters username, password, a hashed-password boolean, and requesting IP address; must return `$0:=True` to accept, and takes priority over the simpler group-based setting.
- **Per-table/field exposure control**: "Expose as REST resource" toggle in the Structure Inspector lets developers hide specific tables or fields from the remote datastore.
- **`Open datastore`**: client-side command connecting via a configuration object (`hostname`, `user`, `password`, `idleTimeout`, `tls`, `type:"4D Server"`) that returns a fully functional ORDA datastore object.
- **Proper method removal**: deleting an `On REST Authentication` method's contents is not the same as deleting the method itself via the Explorer window — an emptied method still exists and defaults `$0` to False, blocking all connections.

## Featured Technology
- ORDA (remote datastore, `Open datastore`)
- 4D REST server exposure settings
- `On REST Authentication` method

## Best Practices Highlighted
1. Use `On REST Authentication` for custom access control (e.g., IP restriction) instead of relying solely on default group-based privileges.
2. Explicitly delete unwanted database methods via the Explorer rather than emptying their contents, to avoid unintended access denial.
3. Restrict exposed tables/fields at the Inspector level to minimize the remote datastore's attack surface.

## Context / Positioning
This note documents one of ORDA's most significant v18 extensions — turning ORDA from an in-app data-access layer into a full inter-application integration mechanism. It reflects 4D's broader strategy of making REST/ORDA the unifying technology for both internal data access and external/cross-app connectivity, displacing older cross-database techniques.

## Historical Commentary
**Status:** Still relevant

Remote datastores remain a current, actively used 4D feature: `Open datastore`, the REST exposure settings, and `On REST Authentication` are all still part of the modern 4D language and Database Settings with no deprecation. This is the standard, modern way to let 4D applications talk to each other's data (and to build client/server or microservice-style 4D architectures), effectively superseding older techniques like connecting to another database's SQL server for cross-database queries. Developers building 4D-to-4D or 4D-to-external integrations today should still follow this pattern; only cosmetic UI details (dialog locations) may have shifted slightly across 4D versions.
