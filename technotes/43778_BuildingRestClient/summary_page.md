# Tech Note 06-30: Building a REST Client

**Author:** Yvan Ayaay, Technical Support Engineer, 4D Inc.
**Published:** July 28, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43778
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_27-30_(JUL)/06-30_REST_Client.zip

## Overview
This note explains what REST (Representational State Transfer) is, contrasts it with SOAP, and walks through building a REST client in 4D 2004 that queries the Yahoo Web Search service, since 4D's Web Services Wizard of that era could only discover and call SOAP web services, not REST ones.

## Key Points
- REST is described as an architectural style (not a standard) for distributed computing, derived from Roy Fielding's analysis of the web's architecture.
- Client requests target resources (identified by URLs); each response is a "resource representation" that changes the client's state — hence "state transfer."
- REST is contrasted with SOAP: REST emphasizes resources/nouns (e.g. "city") while SOAP emphasizes operations/verbs (e.g. "getCity").
- Key REST characteristics covered: client-server separation, statelessness, universally identified resources via URLs, and HTTP verbs (GET, POST) for actions.
- 4D's Web Services Wizard could not discover or call REST services automatically, so this note shows manual HTTP GET + XML parsing in 4D language instead.
- The worked example builds a REST client that queries the Yahoo Web Search API and processes its XML response inside 4D.

## Featured Technology
- REST (Representational State Transfer) architecture
- HTTP GET requests issued from 4D 2004
- Manual XML response parsing in 4D language
- Yahoo Web Search (classic REST API, now retired)

## Historical Context
Published in 2006, this note captures the era when RESTful web APIs were an emerging alternative to SOAP and 4D had no native REST or JSON support — everything had to be constructed manually with HTTP and XML commands. This predates 4D v11's 2007 SQL engine, Project Mode, and ORDA by many years, and long predates 4D's own later native REST server/API framework.

## Historical Commentary
**Status:** Superseded

The REST architectural concepts explained here (stateless, resource-oriented, HTTP-verb-based interactions) are foundational and still entirely valid descriptions of REST today. However, the concrete implementation technique — manually issuing HTTP GET requests and hand-parsing XML in 4D — has been superseded by 4D's later native REST/JSON support and its own REST server framework, and the Yahoo Web Search REST endpoint used in the worked example is no longer operational.
