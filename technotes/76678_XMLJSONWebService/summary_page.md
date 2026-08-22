# Tech Note 12-19: Build a Web Service Iteratively (XML-JSON)

**Author:** Not specified
**Published:** November 2, 2012 | **Product/Version:** 4D v13.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76678
**Download:** https://kb.4d.com/DLTN/TN/2012/12-19_XML_JSON_WebServices.zip

## Proposition
This Tech Note (available here only as a short teaser summary) describes an iterative approach to building a data-publishing web service in 4D, and introduces two techniques for generating dynamic documents: model-based generation using 4D Tags, and XML templates driving the EXPORT DATA command.

## Key Points
- Describes building a web service for publishing data iteratively, i.e., incrementally adding capability.
- Introduces generating dynamic documents from models using 4D Tags.
- Introduces an alternative technique using XML templates in conjunction with the EXPORT DATA command.
- Positions XML and JSON as the two data-interchange formats of interest for the resulting web service.

## Featured Technology
- 4D Tags
- XML templates
- EXPORT DATA command
- Dynamic document/data publishing

## Best Practices Highlighted
1. Build data-publishing services incrementally, validating each step before adding further capability.

## Context/Positioning
Published in late 2012 for 4D v13.1, in the same period 4D was exploring REST/JSON directions for web services, reflecting an interim, template/tag-driven approach to dynamic document and data generation before native JSON tooling matured.

## Historical Commentary
**Status:** Partially Superseded

Only a short teaser is available for this note, but based on its stated approach — 4D Tags and XML-template-driven EXPORT DATA for generating dynamic XML/JSON documents — this reflects pre-native-JSON tooling. 4D has since added first-class JSON parsing/generation commands and an ORDA-based REST layer, making hand-built 4D Tags/XML-template document generation largely unnecessary for new data-publishing services.
