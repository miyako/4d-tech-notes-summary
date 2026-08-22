# Tech Note 22-17: Intro to HTTPRequest: Asynchronous API Requests with Callbacks

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** September 26, 2022 | **Product/Version:** 4D v19 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79011
**Download:** https://kb.4d.com/DLTN/TN/2022/22-17_NewHTTPRequest.zip

## Proposition
4D v19 R6 introduces the 4D.HTTPRequest class store class, replacing the older HTTP Request/HTTP Get commands with an object-oriented, callback-driven, asynchronous-by-default API for outbound HTTP calls. This note explains the model and demonstrates it end-to-end against a public REST API.

## Key Points
- **4D.HTTPRequest.new($url; $requestOptions)** creates and sends a request; GET is the default method if none is specified in $requestOptions.
- **Requests are asynchronous by default**, removing the earlier need to dedicate a separate process to each HTTP Get call for non-blocking behavior; calling .wait() makes a request synchronous when needed.
- **Callback functions (onResponse, onError, onHeaders, onTerminate)** are defined on a request-options class and fire automatically as the request lifecycle progresses.
- **The returned HTTPRequest object centralizes state** (.response, .errors) instead of requiring separate output variables for headers/body/status as with the classic HTTP Get command.
- **onError replaces ON ERR CALL for network errors**, giving request-scoped error handling instead of global error-handler installation.
- **Callbacks can be chained** — the demo's onResponse for a data request triggers a further HTTPRequest for the artwork's image, building a multi-step async pipeline.
- **Demonstrated against the Art Institute of Chicago's public API**, building a searchable, image-populated list-box gallery entirely through chained async calls.

## Featured Technology
- 4D.HTTPRequest class (v19 R6+)
- onResponse / onError / onHeaders / onTerminate callbacks
- request.wait()
- Art Institute of Chicago public API demo

## Best Practices Highlighted
1. Prefer 4D.HTTPRequest over the legacy HTTP Request/HTTP Get commands for new code, since it removes the need for a dedicated process for asynchronous calls.
2. Reserve .wait() for cases where a single, final synchronous fetch is genuinely simpler than another async callback chain (as with the demo's large-image fetch before opening a modal).

## Context / Positioning
Published under 4D v19 R6 (September 2022), this note documents one of the more significant additions to 4D's networking API in that release cycle — part of 4D's ongoing modernization of its language toward class-store, object-oriented constructs (paralleling ORDA, ORDA-based REST, and other class-store additions of the same era).

## Historical Commentary
**Status:** current

4D.HTTPRequest remains the current, recommended way to perform outbound HTTP calls in 4D; the classic HTTP Request/HTTP Get commands still exist for backward compatibility but 4D's own documentation and sample code have continued to favor the class-based, async/callback approach introduced here. Nothing in later 4D releases has superseded this API — it is a genuine, durable upgrade, not a stopgap.
