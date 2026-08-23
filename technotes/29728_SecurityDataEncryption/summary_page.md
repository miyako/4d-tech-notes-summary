# Tech Note: Security via data encryption

- **Asset ID:** 29728
- **Tech Note #:** 03-28
- **Published:** June 26, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=29728
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_26-30_(JUN)/03-28_Security_Data_Encrypt.hqx

## Overview

Frank Chang (4D Inc. Technical Support) opens a three-part series on data encryption by explaining the history and mathematics of public-key cryptography and walking through a from-scratch RSA-style implementation built entirely in 4D methods and the 4D Real data type, demonstrated with an included 'Encryption Demo 1' key-generation/encryption/decryption sample database.

## Key Points

- Surveys the history of encryption from Caesar ciphers and Old Testament transposition schemes through WWII's Enigma machine to modern public-key (asymmetric) cryptography, motivating why symmetric single-key schemes are vulnerable when the key itself must be transmitted.
- Explains RSA key generation mathematically: choose primes p and q, compute n=pq and f=(p-1)(q-1), select public exponent e with GCD(e,f)=1, and derive private exponent d such that d=(1+nm)/e; the public key is (e,n) and the private key is (d,n).
- The `Generate_Public_Key` project method iterates a candidate value and repeatedly calls a `GCD` method until it finds one whose greatest common divisor with (p-1)(q-1) equals 1, returning that as the public exponent.
- The `Generate_Private_Key` method iterates to solve for the private exponent d from the formula d=(1+nm)/e, using 4D's `C_REAL` arithmetic throughout since the intermediate values can exceed integer ranges.
- The `Encrypt` method converts each character to its ASCII numeric value and applies C = X^E mod N (implemented via 4D's `Mod` function) to produce the encrypted character stream, described using the included 'Encryption Demo 1' database's Key Generation, Encryption, and Decryption tabs.
- Explicitly scoped as part 1 of 3: later parts (not included in this text) were to cover 4D Client/4D Open connection encryption and Web Services/SSL-based encryption.

## Featured Technology

- RSA public-key encryption
- Modulus/GCD-based key generation
- ASCII character-value encryption
- 4D Real-number arithmetic for cryptography
- Encryption Demo 1 sample database

## Historical Commentary

**Status:** Superseded

Explaining and implementing RSA from first principles in 4D methods was a genuinely useful educational exercise in 2003, when 4D developers had few built-in cryptography options and needed to understand the underlying math to secure their own protocols. Data encryption itself remains as critical a concern today as ever, but this specific from-scratch, real-number-arithmetic RSA implementation is now clearly superseded: modern 4D provides built-in, standards-based encryption commands (e.g. Generate encryption keypair, Encrypt data/Decrypt data, and X.509-based key management) plus native TLS/SSL support for transport security, all of which are far more secure and performant than a hand-rolled demo intended for teaching rather than production use.

**References to newer/updated information:**
- Current 4D versions provide built-in cryptography commands (e.g. Generate encryption keypair, Encrypt data, Decrypt data) rather than requiring a from-scratch RSA implementation
- Native TLS/SSL support in 4D's HTTP/network layers now handles transport-level encryption that this note's manual approach did not address
