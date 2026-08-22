# Tech Note 17-19: Running a REST Server from 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** November 2, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77879
**Download:** https://kb.4d.com/DLTN/TN/2017/17-19_4DRESTServer.zip

## Proposition
This Tech Note explains REST architecture fundamentals and shows how to hand-build a REST server on top of 4D's built-in Web Server, handling GET/POST parameters, JSON responses, error handling, and authentication manually.

## Key Points
- **REST fundamentals:** stateless, client-server, cacheable HTTP-based protocol for CRUD-style operations.
- **Serving REST from 4D:** implemented directly on 4D's Web Server rather than a dedicated REST product.
- **Manual request handling:** developer code parses incoming HTTP requests and formats JSON responses by hand.
- **GET/POST parameter handling:** dedicated example methods show extracting parameters from both request types.
- **Error handling:** a section dedicated to gracefully returning error information to REST clients.
- **Authentication:** demonstrates access control for protecting specific REST methods.
- **Sample database:** includes a basic REST method plus GET/POST parameter examples and an access-control demo.

## Featured Technology
- 4D Web Server
- HTTP GET/POST request parameters
- JSON response formatting
- Custom web access control / authentication

## Best Practices Highlighted
1. Keep REST responses in a consistent JSON format for client predictability.
2. Separate parameter-parsing logic from business logic for GET vs POST methods.
3. Implement explicit access control checks before executing protected REST methods.

## Context / Positioning
Published in late 2017 for 4D v16, this note predates 4D's own native ORDA-based REST server (introduced around v16 R6/v17) and Project Mode. At the time, exposing 4D data over REST required hand-rolled web-server hooks rather than automatic dataclass-to-REST exposure.

## Historical Commentary
**Status:** Partially superseded

REST as a concept and the general benefits described remain entirely accurate, but the specific implementation technique — manually parsing HTTP parameters and building JSON responses inside 4D web server methods — has been largely superseded by 4D's native, built-in REST server that automatically exposes ORDA dataclasses, entities, and methods as REST endpoints with standard query operators. A developer today would typically reach for 4D's built-in REST server rather than replicate this note's manual routing approach, though the conceptual REST primer remains a fine introduction.
