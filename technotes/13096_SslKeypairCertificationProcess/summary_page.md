# Tech Note 01-14: The SSL Keypair Certification Process

**Author:** Not specified in source document
**Published:** March 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13096
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_11-15_(MAR)/01-14_SSL_Keypair_Cert_Proc.exe

## Overview
An overview of SSL technology and the process of generating and certifying key pairs for securing a 4D (and WebSTAR) web site. This Tech Note introduces SSL (Secure Sockets Layer), the Internet protocol of the era used to secure communications between a web server and HTTP clients such as browsers, enabling a 4D-served site to safely accept credit card numbers or handle sensitive data like medical or HR records.

## Key Points
- It explains that both 4D and its companion web server product WebSTAR relied on the RSA algorithm, one of five algorithms qualified under the US federal Advanced Encryption Standard evaluation process, widely used at the time for authentication and encryption.
- The bulk of the note covers the practical mechanics: the basics of SSL technology, how 4D and WebSTAR each generate key pairs, and the steps required to install SSL support for both products.
- Its featured technology is therefore SSL/RSA cryptography as integrated into the 4D + WebSTAR web-serving stack of 2001, aimed at developers and administrators needing to stand up a secure, credit-card-capable 4D web site during the early e-commerce boom.

## Featured Technology
- SSL / RSA encryption
- 4D Web Server SSL support
- WebSTAR SSL integration
- Key pair generation & certification

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note explains SSL fundamentals and walks through generating and certifying RSA key pairs for securing a 4D web site, in an era when 4D's web server was closely paired with WebSTAR for production HTTPS deployments. The specific WebSTAR-based SSL setup, key-pair generation workflow, and RSA-centric framing described are entirely obsolete: modern TLS certificate issuance (e.g., via standard Certificate Authorities or automated services like Let's Encrypt) and 4D's own built-in SSL/TLS configuration have completely replaced this workflow, though the underlying concept — securing a web server with a certificate to protect sensitive data in transit — remains as important as ever.

**Related updates since:**
- 4D's web server now has its own built-in SSL/TLS certificate configuration, removing the need for a separate WebSTAR pairing to serve HTTPS
- Modern certificate issuance/renewal (Let's Encrypt, standard CAs, ACME automation) has fully replaced the manual RSA key-pair certification process described in this note
- TLS has superseded SSL industry-wide as the standard secure transport protocol

