# Tech Note 03-50: Securely Synchronizing databases with dissimilar structures via SOAP

**Author:** Not specified in source document
**Published:** November 30, 2003 | **Product/Version:** 4D v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=30594
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_48-51_(NOV)/03-50_Synchronizing_SOAP.exe

## Overview
A Tech Note describing a SOAP-based technique for securely synchronizing data between two 4D databases even when their table/field structures differ or change over time.

## Key Points
- Uses SOAP (new in 4D 2003) as the transport for synchronizing data between two dissimilar/changing database structures.
- Aims for structure-agnostic synchronization, without either side needing prior knowledge of the other's schema.
- Includes an optional fully secure (encrypted) transfer mode.

## Featured Technology
- SOAP
- 4D 2003 Web Services
- Data synchronization
- Encryption/security

## Historical Context
Reflects 4D 2003's newly introduced SOAP/Web Services capability being applied to the long-standing practical problem of multi-database synchronization; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

SOAP as the specific synchronization transport described here has since been broadly superseded by REST/JSON-based sync approaches and, for many 4D-to-4D scenarios, by ORDA-based remote datastore access, so the concrete mechanism is dated. The underlying goals — structure-agnostic, secure data synchronization between databases — remain core, still-relevant concerns for distributed 4D applications today.
