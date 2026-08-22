# Tech Note 14-12: Validation of Client Build Version

**Author:** Tai BUI, Technical Services Engineer, 4D Inc.
**Published:** July 24, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77112
**Download:** https://kb.4d.com/DLTN/TN/2014/14-12_ValidationOfClientBuilds.pdf

## Proposition
This note explains 4D's versioning hierarchy — major release version, update release (e.g. v14.1, v14.2), and finer-grained build number — and notes that while 4D prevents connections between mismatched major/update versions, it does not strongly enforce matching build numbers within the same version, which can lead to subtle bugs when a 4D Remote client and 4D Server are running different builds; it then provides a technique to detect and preemptively quit on such mismatches before any application code runs.

## Key Points
- **Three-tier version hierarchy:** major release (v12/v13/v14), update release (e.g. v14.1, v14.2), and build number, each carrying progressively smaller (but still real) behavioral differences.
- **Major version changes are significant:** can include new features, deprecations, and structural changes (e.g. the note cites the v14 journaling system change and addition of C Objects).
- **Build-level mismatches are not strongly blocked** by 4D's connection mechanism the way version mismatches are, creating a gap where a client can connect to a server on a different build of the same version.
- **Risk:** mismatched builds can behave inconsistently even though 4D allows the connection, since bug fixes/behavior can differ between builds of the same version.
- **Proposed technique:** compare client and server build numbers at connection time and preemptively quit the client before any application logic executes if they don't match.
- **Preemptive quit rationale:** stopping before code runs avoids partially-executed operations against a potentially incompatible client build.

## Featured Technology
- 4D version/build numbering scheme
- 4D Server/Client connection mismatch handling
- Build-number validation and preemptive client quit technique

## Best Practices Highlighted
1. Validate client/server build numbers at connection time rather than assuming version matching is sufficient.
2. Quit the client preemptively, before running any business logic, if a build mismatch is detected.
3. Track build numbers deliberately when deploying updates across a fleet of 4D Remote clients.

## Context / Positioning
Published July 2014 for 4D v14.0, addressing 4D Server/4D Remote Client deployment hygiene in the classic Design Mode era, well before ORDA/REST-based clients (where 'client version' means something quite different) became common alongside traditional 4D Client/Server topologies.

## Historical Commentary
**Status:** Still Relevant

This note's operational advice remains sound for any deployment still using classic 4D Client/Server (4D Remote): 4D's version-matching enforcement still operates at the version level rather than the granular build level, so the mismatch risk and the preemptive-validation technique described are still applicable today.

Its relevance has narrowed somewhat as more solutions shift toward REST/ORDA-based web and mobile clients, where this specific 4D-Remote-build-matching concern doesn't apply in the same way — but for shops still running traditional multi-user 4D Client/Server deployments, this remains a practical, still-current piece of operational guidance.
