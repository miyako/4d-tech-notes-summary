# Tech Note 10-07: 2048 bit SSL Keys and the NEW Cipher List in 4D v11 SQL Release 6

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** March 8, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76046
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_11-14_(APR)/10-07_SSLKeys_CipherList.zip

## Proposition
This note explains SSL and RSA public-key cryptography theory, how to generate 2048-bit SSL key pairs and certificate requests in 4D, and how to configure and activate 4D v11.6's SSL cipher list for the Web Server, SQL Server, and Client-Server connections.

## Key Points
- Explains **public/private key cryptography** fundamentals and how 4D uses the **RSA algorithm** (a US Federal AES-qualified algorithm).
- **GENERATE ENCRYPTION KEYPAIR** creates a key pair; **GENERATE CERTIFICATE REQUEST** produces a certificate signing request.
- Documents 4D's **cipher list format**, available cipher strings, and notable suites: SSLv2, SSLv3, a stronger SSLv3 list, and the default v12 cipher list.
- Provides commands/UI for **setting, getting, and resetting** the current cipher list.
- Example database demonstrates the full workflow: adjusting the cipher list, generating a key pair, submitting a certificate request (self-signed or via a CA), and activating SSL.
- Covers activating SSL separately for the **Web Server, SQL Server, and Client-Server connections**, including secured-mode client settings.

## Featured Technology
- GENERATE ENCRYPTION KEYPAIR command
- GENERATE CERTIFICATE REQUEST command
- 4D SSL cipher list configuration (SSLv2/SSLv3 cipher suites)
- SSL for Web Server, SQL Server, and Client-Server connections

## Best Practices Highlighted
1. Use a properly signed certificate (fully qualified CA) rather than a self-signed certificate for production, public-facing deployments.
2. Configure the cipher list deliberately rather than relying on defaults, understanding the strength tradeoffs of each suite.
3. Activate SSL separately and appropriately for each connection type (Web, SQL, Client-Server) based on which channels carry sensitive data.

## Context / Positioning
Published as 4D v11 SQL Release 6 refreshed its SSL cipher support, this note served as the reference for developers deploying SSL-secured 4D solutions at the time.

## Historical Commentary
**Status:** Obsolete

This note explains SSL/RSA key theory, how to generate 2048-bit key pairs and certificate requests in 4D, and how to configure 4D v11.6's cipher list, including specific SSLv2 and SSLv3 cipher suites. The RSA/public-key cryptography concepts remain valid.

However, the specific protocol guidance is now obsolete: SSLv2 and SSLv3 are both deprecated/broken (SSLv3 broken by POODLE in 2014) and have been removed from modern browsers and TLS libraries, so the cipher lists and configuration examples described here no longer represent secure or even connectable configurations. Any 4D system still relying on this note's specific cipher settings needs to be upgraded to TLS 1.2/1.3 with a modern cipher suite.
