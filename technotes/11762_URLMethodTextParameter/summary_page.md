# Tech Note: The Text Parameter Passed to 4D Methods Called via URLs

**Author:** Not specified in source document
**Published:** May 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11762
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note documents an undocumented parameter behavior in 4D v6's early built-in web serving feature: methods bound to HTML links via the /4DMETHOD/ URL convention are always passed an implicit text parameter, which compiled databases must explicitly declare to avoid runtime errors.

## Key Points

- Methods can be bound to HTML objects using a /4DMETHOD/Name_of_your_method URL, per the Language Reference manual's Web Services documentation.
- 4D automatically sends an (undocumented) text parameter to any method invoked this way.
- The method must declare C_TEXT($1) even if unused, or runtime errors occur in compiled-mode web access.
- The parameter's value is whatever extra text was appended to the end of the invoking URL, usable as a simple HTML-to-4D data channel.

## Featured Technology

- 4D Web Services (early built-in web server feature)
- /4DMETHOD/ URL-to-method binding
- C_TEXT($1) compiled-mode parameter declaration

## Historical Context

Written in 1997 during 4D's earliest built-in web serving era (well before 4D's REST engine and ORDA), when binding HTML links directly to 4D methods via a fixed /4DMETHOD/ URL convention was itself a novel capability; the implicit-parameter quirk described here is specific to that early implementation and has no direct analog in the substantially different modern 4D web/REST architecture.

## Historical Commentary
**Status:** Superseded

This note documents an undocumented, easily-missed detail (an implicit $1 text parameter passed to any 4D method invoked via a /4DMETHOD/ URL, requiring explicit C_TEXT($1) declaration for compiled databases) tied to 4D's very first-generation built-in web serving feature; the specific mechanism has been long since superseded by 4D's modern, far more capable web server and REST/ORDA-based web request handling, though the general lesson about compiled-mode parameter declaration remains conceptually relevant.
