# Tech Note 00-42: 4D Mixed-Mode Web Serving Techniques: Crossing the bridge between Contextual and Non-contextual Modes

**Author:** Eric Saltzen, 4D, Inc. Technical Support
**Published:** September 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11998
**Download:** https://kb.4d.com/DLTN/TN/2000/Windows/TN_2000_41-45_%28SEP%29/00-42_Mixed-Mode_Web.exe

## Overview
This Tech Note, authored by Eric Saltzen of 4D's own Technical Support team, tackles a genuine architectural transition point introduced in 4D v6.5: the arrival of Non-Contextual Mode, a 'classical' stateless HTTP web-serving mode that let developers build sites with any graphical or text-based HTML editor and serve them directly, in contrast to 4D's original Contextual Mode, which maintained an interactive session for each connection.

## Key Points
- Because Non-Contextual Mode does not maintain session state, any site requiring persistent, multi-step interaction (a shopping cart, a multi-page form sequence) still needs explicit state tracking, and the note surveys the three standard techniques of the era — cookies (referencing an earlier note, TN 00-17), hidden fields on HTML forms, and URL-encoded context information — noting that the third technique is essentially what 4D's built-in Contextual Mode already does automatically.
- Rather than treating Contextual and Non-Contextual Mode as mutually exclusive choices, the note shows how a single site can mix static Non-Contextual pages with dynamic Contextual sessions, using a sample database, '4DMixedModeWeb,' that implements a class roster and bulletin board application exercising three different form-submission styles (pure Contextual, Contextual with pre-coded HTML, and pure Non-Contextual) alongside link-harvesting and file-upload examples.
- It also documents a newer 'New Context Referencing Mode,' which uses the HTML <BASE HREF> tag to carry Context and Subcontext IDs once per page rather than repeating them in every link, reducing page size while preserving 4D's ability to route each request to the correct web process and detect out-of-order navigation.
- The featured technology is therefore the full breadth of 4D v6.5's web-serving session-management options, presented by 4D's own support team as an authoritative guide to combining them effectively.

## Featured Technology
- 4D Web Server (Contextual & Non-Contextual Mode)
- Cookies / hidden form fields / URL encoding (session state tracking)
- New Context Referencing Mode (<BASE HREF>)
- 4DMixedModeWeb example database

## Historical Context
This summary is based on the full extracted text of the original Tech Note PDF, published September 2000 for 4D v6.5 (Mac & Win).

## Historical Commentary
**Status:** Obsolete

This substantial note, written by 4D's own technical support, explains how to blend 4D v6.5's new Non-Contextual Mode web serving (a 'classical' stateless HTTP server) with the existing Contextual Mode session model, covering all three era-standard state-tracking techniques (cookies, hidden form fields, URL-encoded context IDs) and a newer <BASE HREF>-based Context Referencing Mode to keep pages smaller. While cookies as a session-tracking mechanism remain an industry standard today, 4D's own Contextual/Non-Contextual Mode session architecture with Context/Subcontext IDs has been completely superseded by 4D's later move to REST APIs built on ORDA, making the note's specific mixed-mode techniques obsolete for current web development, even as it remains a well-documented artifact of a genuine architectural inflection point in 4D's web server history.

**Related updates since:**
- 4D's web serving architecture has moved decisively from Contextual/Non-Contextual Mode session management to REST APIs built on ORDA, superseding the entire mixed-mode Context/Subcontext ID system this note documents
- Cookie-based session tracking remains a standard web technique today, but modern implementations typically pair it with token-based authentication (JWT/OAuth) rather than 4D's proprietary Context ID mechanism
- The 4D sample databases referenced (WebExam, Auction, Snap-e, eBiz) are no longer part of 4D's current example library

