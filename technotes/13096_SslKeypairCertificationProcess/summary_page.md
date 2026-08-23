# Tech Note: The SSL Keypair Certification Process

- **Asset ID:** 13096
- **Tech Note #:** 01-14
- **Published:** March 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hartman and Elaine Smith
- **Page URL:** https://kb.4d.com/assetid=13096
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_11-15_(MAR)/01-14_SSL_Keypair_Cert_Proc.hqx

## Overview

Steve Hartman and Elaine Smith (4D, Inc. Technical Support) explain the theory and practice of SSL security for a 4D web site, covering public-key cryptography and digital signature fundamentals before showing exactly how to generate an RSA keypair, request a certificate, and install it for use with WebSTAR Server Suite to serve HTTPS traffic.

## Key Points

- Uses an extended Alice/Bob/Ted/Carol narrative to explain public-key authentication: Bob signs a message digest with his private key so Alice can verify his identity with his public key, and a trusted third party (Ted) vouching for Bob's key establishes a "web of trust"; an impersonator (Carol) fails because she lacks Bob's private key.
- A certificate binds a public key to an identity (issuer name, subject, public key, timestamps) and is itself signed by a certificate authority's private key, letting anyone verify it against that authority's known public key.
- `GENERATE ENCRYPTION KEYPAIR` produces an RSA private/public key pair as BLOBs, defaulting to 512-bit keys (a "good compromise" at the time) with an optional 1024-bit size, noting that only 512/1024 bits are accepted for SSL certificate requests and many browsers reject longer keys.
- Keys can be saved to disk via `BLOB TO DOCUMENT` in PEM-style text with `-----BEGIN RSA PRIVATE KEY-----`/`-----END RSA PRIVATE KEY-----` (and public key equivalents) headers/footers.
- `GENERATE CERTIFICATE REQUEST` (secured protocol version 6.7) builds a text-format certificate signing request from the generated keypair, suitable for submission to certificate authorities like Verisign or Thawte, using the same RSA principle that underlies the `ENCRYPT BLOB`/`DECRYPT BLOB` commands' second syntax.
- The example database's "Certificate request" form collects Common Name, Country, City, State/Province, Company, and Unit fields; the note walks through generating the keypair and request via the Create Keypair / Generate Certificate buttons, then step-by-step instructions for installing the private key and returned certificate into the appropriate WebSTAR Server Suite virtual host folder.

## Featured Technology

- GENERATE ENCRYPTION KEYPAIR command (RSA key generation)
- GENERATE CERTIFICATE REQUEST command
- ENCRYPT BLOB / DECRYPT BLOB
- SSL/TLS public-key cryptography and digital signatures
- 4D Web Server secured (HTTPS) mode
- WebSTAR Server Suite SSL certificate installation

## Historical Commentary

**Status:** Partially superseded

Steve Hartman and Elaine Smith's note is a two-part explainer: a from-first-principles introduction to public-key cryptography, digital signatures, and certificate authorities (illustrated with the classic Alice/Bob/Ted/Carol trust scenario), followed by concrete steps for generating an RSA keypair and certificate request with 4D's GENERATE ENCRYPTION KEYPAIR and GENERATE CERTIFICATE REQUEST commands and installing the resulting certificate into WebSTAR Server Suite for SSL-secured web serving. The cryptography theory remains entirely valid and still a good primer, but the specific mechanics -- 512-bit default key sizes (now considered far too weak), 4D's tight pairing with WebSTAR as the web server, and the RSA-only keypair commands -- are dated; modern 4D web serving uses far larger key sizes, integrates with standard TLS/certificate tooling, and no longer depends on WebSTAR.

**References to newer/updated information:**
- 4D's default and minimum recommended RSA key sizes have grown well beyond the 512/1024-bit options presented here, in line with modern TLS security requirements
- 4D's built-in web server no longer depends on WebSTAR Server Suite for SSL; modern 4D versions manage HTTPS certificates directly, typically via standard PEM certificate/key files rather than the manual GENERATE CERTIFICATE REQUEST workflow shown here
