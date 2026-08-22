# Tech Note 03-43: Complex Input Types with Web Services

**Author:** Not specified in source document
**Published:** September 30, 2003 | **Product/Version:** 4D v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=29817
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_40-43_(SEP)/03-43_ComplexInputTypesInWS.exe

## Overview
The first of a two-part Tech Note explaining how to properly construct complex, structured SOAP input parameters when calling Web Services that require them from 4D 2003.

## Key Points
- Part I of a two-part Tech Note on generating complex (structured) SOAP input parameters.
- Addresses a common pain point for developers used to only simple scalar Web Service parameters.

## Featured Technology
- SOAP
- Web Services (4D 2003)
- Complex XML input parameters

## Historical Context
Published shortly after 4D 2003 introduced SOAP/Web Services client support, addressing a natural next-level challenge beyond the basic introductory notes; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

SOAP's complex-type XML input construction, the specific focus of this note, has been broadly superseded by simpler JSON-object-based request bodies in modern REST APIs, which 4D now supports natively, making this note's specific technique largely of historical interest even though the underlying challenge — mapping structured data to an external service's expected wire format — remains a perennial integration concern.
