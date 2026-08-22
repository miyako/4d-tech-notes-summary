# Tech Note 12-20: REST Web Services with 4D (Part 1)

**Author:** Christophe Keromen
**Published:** November 28, 2012 | **Product/Version:** 4D v13.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76694
**Download:** https://kb.4d.com/DLTN/TN/2012/12-20_REST_WebService_w_4D1.pdf

## Proposition
This first installment of a series introduces building REST-style web services in 4D, framing the growing demand for multi-device, API-driven data access and social-network-style connectivity, and describing how to implement a REST-based data service in 4D exposing Create/Retrieve/Update/Delete (CRUD) operations over HTTP.

## Key Points
- Motivates REST web services via the rise of multi-screen access and standardized HTTP-based APIs.
- Contrasts REST with other web service approaches (implicitly SOAP) available to 4D developers at the time.
- Frames CRUD (Create-Retrieve-Update-Delete) as the core operation set a data-oriented REST service should expose.
- Sets up the implementation approach continued in a later Part 2 of the series.

## Featured Technology
- REST architecture (CRUD over HTTP)
- 4D Web Server (classic)
- HTTP request handling in 4D
- Data service design

## Best Practices Highlighted
1. Design web services around standard HTTP verbs/CRUD semantics for interoperability.
2. Favor REST/JSON over heavier SOAP/XML web services for broader client compatibility (mobile, JS, etc.).

## Context/Positioning
Published in late 2012 for 4D v13.2, when 4D was manually implementing REST-style services on top of its classic Web Server ahead of any built-in REST/ORDA data-access layer, anticipating the industry's shift away from SOAP.

## Historical Commentary
**Status:** Partially Superseded

This note's central instinct — that REST/CRUD over HTTP was the right direction for 4D web services — was fully validated by 4D's own product direction, but the specific hand-built implementation approach shown here (manually parsing HTTP requests against the classic 4D Web Server) has been superseded by 4D's built-in, ORDA-based REST server introduced years later, which auto-generates a full CRUD/query REST API from the data model with no custom routing code required.
