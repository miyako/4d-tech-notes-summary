# Tech Note 22-04: 4D REST API: Connecting 4D with Angular

**Author:** Not specified in available source (see meta.json)
**Published:** February 25, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78873
**Download:** https://kb.4d.com/DLTN/TN/2022/22-04_RESTandAngular.zip

## Proposition
4D can act as a REST/ORDA backend for a modern Angular single-page application; this note demonstrates basic CRUD over HTTP and the configuration needed on both sides to connect them.

## Key Points
- **4D as REST backend**: the note positions 4D's REST API (ORDA-based) as the bridge to any modern JS frontend framework.
- **Angular frontend**: chosen as the example SPA framework to consume the REST API.
- **CRUD via HTTP**: basic Create/Read/Update/Delete operations demonstrated through standard HTTP requests.
- **Configuration guidance**: covers setup needed on both the 4D and Angular sides (per the abstract; specifics unavailable).
- **Content limitation**: full implementation details, code samples, and specific commands are not available — only the published KB abstract could be retrieved.

## Featured Technology
- 4D REST API
- Angular
- CRUD via HTTP requests

## Context / Positioning
This note fits squarely into 4D's ongoing positioning of ORDA/REST as the modern replacement for older SOAP-based 4D web services, and reflects the broader industry move toward decoupled SPA frontends talking to REST backends — a pattern 4D actively supports and continues to document.

## Historical Commentary
**Status:** Still Relevant

4D REST + ORDA remains the current, recommended way to connect 4D to modern JS frameworks like Angular; this pattern has not been superseded and is, if anything, more emphasized in 4D's product direction today (with newer tools like Qodly building further on similar API-driven architectures). Full technical detail unavailable — this summary is based on the published abstract/teaser only, as the original demo download could not be retrieved, so specific API calls or Angular code patterns cannot be independently verified.
