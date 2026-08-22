# Tech Note 23-01: JSON Web Tokens in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 23, 2023 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79100
**Download:** https://kb.4d.com/DLTN/TN/2023/23-01_JWT.zip

## Proposition
JSON Web Tokens are a widely adopted standard for securely transferring identity/authentication data between systems, especially online APIs. This note shows that JWTs can be generated and verified entirely in native 4D code, without third-party libraries, useful both for consuming external JWT-based APIs and securing 4D's own REST server.

## Key Points
- **Three-part structure:** header (algorithm + token type), payload (the actual claims/data), and a verify signature — joined by periods into the final token string.
- **Header contents:** at minimum `alg` (e.g., HS256, RS256) and `typ: "JWT"`, describing how the signature was produced.
- **Payload flexibility:** an arbitrary JSON object of claims agreed upon between the two communicating parties (e.g., identity fields, expiration).
- **Signature generation:** Base64URL-encode the header and payload, concatenate with a period, then hash with the algorithm from the header, optionally salted with a shared secret key.
- **4D object-based construction:** header/payload are built as native 4D objects (`New object(...)`) then encoded via `BASE64 ENCODE(JSON Stringify(...); ...; *)` for URL-safe output.
- **Four signature algorithm families implemented:** HS (HMAC), ES (ECDSA), RS (RSASSA-PKCS1), and PS (RSASSA-PSS), combined with SHA-256/SHA-512 hashing, dispatched by parsing the two-letter prefix of the header's `alg` value.
- **CryptoKey class for non-HMAC signing:** a dedicated `jwtHashSign` method leverages 4D's built-in CryptoKey class to perform RSA/ECDSA-based hashing, while `jwtHashHMAC` handles the HMAC case directly.
- **Verification workflow:** split the token on `.`, Base64-decode and JSON-parse header/payload, recompute the signature with the shared secret, and compare it to the received signature.

## Featured Technology
- **JSON Web Token (JWT) structure** — the header.payload.signature standard this note implements natively in 4D.
- **BASE64 ENCODE / BASE64 DECODE** — encodes/decodes the header and payload in URL-safe Base64 form.
- **4D CryptoKey class** — provides RSA/ECDSA cryptographic operations used for non-HMAC signature algorithms.
- **HMAC/RSA/ECDSA signing** — the four algorithm families (HS/ES/RS/PS) implemented across two hashing strengths (SHA-256/512).

## Best Practices Highlighted
1. Always apply a shared secret key when generating/verifying signatures, since an unsigned or secret-less JWT is trivially forgeable.
2. Match the exact hashing/signing algorithm indicated in the token's own header (`alg`) when verifying, rather than assuming a fixed algorithm.
3. Cross-validate custom JWT implementations against a trusted external tool like jwt.io during development to confirm standard compliance.

## Context / Positioning
Published as 4D's REST server and web-facing features matured, this note equips 4D developers to implement industry-standard token-based authentication natively — whether integrating with third-party JWT-secured APIs or hardening 4D's own REST endpoints — without pulling in external cryptography libraries.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
