# Tech Note: 4D Web Serving Revisited

**Author:** Not specified
**Published:** April 1, 1998 | **Product/Version:** 4D Client v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11793

## Overview
This Tech Note provides a supplementary explanation of 4D's built-in web serving capabilities in v6, bridging the gap between the Language Reference Manual's Web Services chapter and practical implementation. It aims to clarify the main concepts for developers learning to serve dynamic web content from their 4D databases.

## Key Points
- **Supplements the manual:** Not a complete explanation, but an alternative take on key web serving concepts from the V6 Language Reference.
- **4D Client vs. web browser:** Describes fundamental differences between how a 4D Client connects to a database and how a web browser interacts with 4D's web server.
- **Behavioral approximation:** Explains how 4D replicates native 4D Client behavior within the limitations of a web browser.
- **Code samples included:** Provides example code and a framework for implementing web access from 4D.
- **Prerequisites:** Readers should first read the Web Services chapter of the Language Reference and understand basic web server/HTML concepts.

## Featured Technology
- 4D v6 built-in Web Server
- HTML generation and dynamic web content from 4D
- Web browser vs. 4D Client architectural comparison
- Web application framework patterns in 4D

## Historical Context
**Status:** Obsolete

4D's built-in web server was a headline feature of the v6 era, positioning the platform as a combined database and web application server during the late-1990s internet boom. The specific web serving model described here — based on contextual connections, form-to-HTML translation, and the On Web Connection database method — has been overhauled multiple times since. Modern 4D uses a REST server with ORDA-based data model access, and web application development has shifted to frameworks like Qodly. The conceptual lesson — serving dynamic data-driven content directly from a 4D database — remains the platform's identity, even though every technical detail in this note is outdated.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
