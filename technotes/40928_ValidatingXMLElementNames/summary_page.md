# Tech Note 05-40: Validating XML Element Names

**Author:** David Adams
**Published:** December 13, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=40928
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-40_Validating_XML_Names.zip

## Overview
This note documents the XML specification's naming rules for elements/attributes and provides a 4D method to validate custom-generated XML names against those rules, aimed at developers producing their own XML from 4th Dimension.

## Key Points
- XML names are case-sensitive (unlike 4D's own naming), unlike 4D's own naming rules.
- Legal first characters: ideograms, letters, hyphen, and period.
- Legal body characters: ideograms, letters, digits, hyphen, period, colon (namespaces only), and underscore.
- No whitespace of any kind is permitted in an XML name.
- Names beginning with any case variant of "xml" are reserved for current/future XML standards.
- No defined length limit on XML names.
- Provides a simplified practical checklist: case-sensitive; start with a letter; use only letters/digits/period/underscore; avoid other punctuation.
- Cross-references TN 05-41 for the case-sensitive comparison techniques needed to actually enforce these rules in 4D code.

## Featured Technology
- XML element/attribute naming rules (W3C specification)
- Custom XML generation from 4th Dimension
- Name validation methods

## Historical Context
The XML naming rules themselves are an unchanging W3C specification and remain fully accurate today. What has changed is that 4D's own XML tooling (built-in DOM-based XML generation/parsing commands) has since absorbed much of this validation automatically, making a hand-rolled validation method less commonly necessary for typical custom-XML-production tasks — though the reference information here remains a correct and useful explanation of the underlying rules.
