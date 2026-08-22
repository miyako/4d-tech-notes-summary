# Tech Note 08-39: MD5 Algorithm Implemented in 4D v11 SQL

**Author:** Atanas Atanassov, 4D Inc. Technical Services  
**Published:** November 12, 2008 | **Product/Version:** 4D v11, v11.2+ | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51554  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_35-39_(OCT)/08-39_MD5_in_4D.zip

## Overview

This technical note demonstrates how to implement the MD5 cryptographic hash algorithm within 4D v11 SQL (Release 2 and above) by embedding JavaScript code in a Web Area form object. MD5 is a cryptographic hash function that produces a fixed-size 128-bit "message digest" or fingerprint from input of arbitrary length. Though MD5 is fast and was widely used in 2008, it is primarily useful for non-security checksums and file integrity verification (collision vulnerabilities were discovered in 2004, rendering it cryptographically weak for security-critical applications). The note illustrates both the mathematical theory behind MD5 and two practical implementation patterns: an on-screen Web Area UI for interactive hashing, and an offscreen Web Area serving as a JavaScript execution engine for returning hash results to 4D forms.

## Key Points

- **MD5 Algorithm Overview:**
  - Input: Text of arbitrary length.
  - Output: 128-bit fixed-size hash (typically displayed as a 32-character hex string).
  - Properties: Fast to compute, infeasible to reverse, two different inputs rarely produce the same hash.
  - Designed by Ron Rivest in 1991 to replace the earlier MD4 algorithm.
  - Primary use case in 2008: file integrity verification, checksum generation; not recommended for cryptographic security (collision vulnerabilities known).

- **MD5 Mathematical Process (4 Rounds):**
  - **Step 1 – Padding:** Extend input to 448 bits mod 512 (64 bits short of 512-bit multiple).
  - **Step 2 – Length Appending:** Append original message length as last 64 bits (result: multiple of 512 bits).
  - **Step 3 – State Variables & Auxiliary Functions:** Four 32-bit state variables (A, B, C, D) initialized to fixed values. Four auxiliary functions F, G, H, I compute intermediate transformations.
  - **Step 4 – Message Digest:** After processing all 512-bit blocks through 64 iterations (4 rounds × 16 operations), output the four state variables as the 128-bit hash.

- **Web Area for JavaScript Execution (4D v11.2+):**
  - Before v11, injecting JavaScript required third-party plug-ins or the 4D Live Window plug-in.
  - 4D v11.2+ introduces the Web Area form object, providing a native browser-like shell for JavaScript execution.
  - Two key commands:
    - `WA OPEN URL(WebAreaName; url)` — Load an HTML file (with embedded JavaScript).
    - `WA EXECUTE JAVASCRIPT FUNCTION(WebAreaName; functionName; result; param1; ...)` — Execute a JavaScript function and retrieve the result into a 4D variable.

- **On-Screen Example:**
  - HTML page (test1.html) includes an input field, an "MD5" button, and an output field.
  - JavaScript function `myWrapper(a)` takes the input, calls the `md5(a)` function, and displays the result.
  - The HTML page loads php.js (containing the MD5 implementation) via `<script>` tag.
  - Users enter text, click "MD5", and see the hash instantly in the output field.

- **Offscreen Example:**
  - The Web Area form object is created but not visible (offscreen area).
  - 4D method calls `MD5_Execute1_Demo(inputText)`, which:
    1. Constructs a file URL to test.html and opens it in the Web Area via `WA OPEN URL`.
    2. Delays briefly to ensure JavaScript loads.
    3. Calls `WA EXECUTE JAVASCRIPT FUNCTION(WebArea_Demo; "md5"; $result; inputText)` to execute the md5 function with the input and capture the result.
    4. Returns `$result` to the caller.
  - Input comes from a 4D form field; output is displayed immediately in another form field.

- **Requirements:**
  - 4D v11 SQL Release 2 and above (Web Area object).
  - The sample includes an "Extras" folder with HTML and JavaScript files (.html, .js) located next to the database structure file.
  - UTF-8 encoding for character set (MD5 algorithm optimized for UTF-8; php.js includes utf8_encode function).
  - 32-bit machine optimization (MD5 bit-shift operations are efficient on 32-bit processors).

- **Generalizing the Pattern:**
  - The technique is not limited to MD5; any JavaScript algorithm can be embedded.
  - Developers can leverage open-source JavaScript libraries for cryptography, data processing, encoding, etc.
  - No third-party plug-ins required; no additional licensing or configuration needed beyond 4D itself.

## Featured Technology

- MD5 cryptographic hash algorithm
- 4D Web Area form object
- WA OPEN URL command for loading HTML/JavaScript files
- WA EXECUTE JAVASCRIPT FUNCTION command for invoking JavaScript functions from 4D
- JavaScript algorithm implementation (translated from PHP)
- File URLs and 4D folder path utilities
- UTF-8 encoding for internationalization
- Offscreen Web Area pattern for invisible JavaScript execution

## Historical Context

Published November 2008 for 4D v11 SQL Release 2+, this note demonstrates the power and flexibility of the newly introduced Web Area object. At the time, Web Area was a game-changer: it allowed 4D developers to tap into the vast ecosystem of JavaScript libraries and execute client-side algorithms without waiting for 4D to build native commands. The note emphasizes the generality of the pattern: developers could integrate any JavaScript code, opening doors to creative solutions. The specific choice of MD5 as the example is interesting: by 2008, MD5's cryptographic weaknesses were already known, yet it remained widely used for checksums and file integrity (and remained useful for that purpose). The note's practical examples (both on-screen and offscreen) show the versatility of Web Area.

## Historical Commentary

**Status:** Superseded

The MD5 hashing algorithm itself remains useful for non-security checksums and backward compatibility, but is no longer recommended for any cryptographic purposes. The technique of implementing cryptography in JavaScript within a Web Area is now an anti-pattern in modern 4D.

**Related Updates:**
- **Native Digest Commands (4D v13+):** 4D introduced the `GENERATE DIGEST` command, providing native support for MD5, SHA-256, SHA-512, and other hash algorithms without needing JavaScript or Web Area workarounds.
- **Modern Web Standards (4D v17+):** Project Mode and modern 4D shifted away from Web Area-based JavaScript execution toward native Web Components and standard web APIs (e.g., SubtleCrypto for cryptography).
- **SHA-256 and Modern Algorithms:** MD5 is cryptographically broken (collision attacks are practical); modern applications use SHA-256, SHA-512, or BLAKE2. If native hashing is needed in 4D, use `GENERATE DIGEST` with SHA-256.
- **Web Area Evolution:** Modern 4D's Web Area supports modern web technologies but is no longer used as a workaround for executing arbitrary JavaScript algorithms; native commands are preferred.
- **Third-Party Libraries:** Modern 4D integrates with package managers and extension libraries (npm packages via 4D Web Server, external components) rather than embedding JavaScript in Web Areas.

Developers today should use `GENERATE DIGEST` for hash generation and modern cryptography libraries/APIs rather than reimplementing algorithms in JavaScript. This note is valuable historically for understanding how 4D developers extended the platform in the pre-ORDA, pre-Project Mode era.
