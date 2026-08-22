# Tech Note 17-06: Data encryption and decryption between 4D and PHP

**Author:** Nicolas Brachfogel, Senior Developer, 4D SAS
**Published:** March 27, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77755
**Download:** https://kb.4d.com/DLTN/TN/2017/17-06_EncryptionBtw4DAndPHP.zip

## Proposition
This tech note explains how to handle RSA-based data encryption and decryption between 4D and PHP scripts, covering three scenarios: pure 4D encryption/decryption, decrypting a 4D-encrypted file in PHP, and decrypting a PHP-encrypted file in 4D. It focuses on the practical compatibility issues that arise when crossing the language/library boundary.

## Key Points
- **Key generation:** GENERATE ENCRYPTION KEYPAIR creates a private/public RSA key pair (2048-bit in the example), saved as plain-text-encoded BLOBs.
- **Encrypt/decrypt in 4D:** TEXT TO BLOB + ENCRYPT BLOB (private key) to encrypt; DECRYPT BLOB (public key) + BLOB TO DOCUMENT to decrypt.
- **Calling PHP from 4D:** PHP EXECUTE runs a named PHP function and returns results or errors via PHP GET FULL RESPONSE.
- **Key format mismatch:** 4D generates PKCS#1 RSAPublicKey-format keys, while PHP/OpenSSL commonly expects SubjectPublicKeyInfo — the phpseclib library is used to convert between them.
- **4D's proprietary header:** 4D prepends a 3-byte header (4 bytes on big-endian systems) to every encrypted BLOB, which must be stripped for external decryption or added when decrypting externally-encrypted data in 4D.
- **Chunked decryption in PHP:** the PHP example decrypts the file chunk-by-chunk based on RSA key size, using openssl_public_decrypt.
- **Reverse flow:** 4D can decrypt data encrypted externally (e.g., via openssl_private_encrypt in PHP) as long as the correct header bytes are manually inserted first.

## Featured Technology
- GENERATE ENCRYPTION KEYPAIR
- ENCRYPT BLOB / DECRYPT BLOB
- PHP EXECUTE / PHP GET FULL RESPONSE
- phpseclib (open-source PHP RSA library)
- BLOB TO DOCUMENT / DOCUMENT TO BLOB

## Best Practices Highlighted
1. Generate and store the key pair once, reusing it for all subsequent encrypt/decrypt operations.
2. Convert the 4D public key to SubjectPublicKeyInfo format once, cache it, rather than re-converting on every call.
3. Always account for the 4D header bytes (3 on little-endian, 4 on big-endian) when moving encrypted data across the 4D/external boundary.

## Context / Positioning
Published in early 2017 against 4D v16, this note sits squarely in the "classic" 4D era — Design Mode binary databases, pre-ORDA, with SOAP/PHP-execute-style integration being typical ways to bridge 4D to other web technologies. Interoperability tech notes like this one were common because 4D's web/scripting integrations (PHP, SOAP) required careful attention to low-level format details that 4D's documentation didn't always spell out.

## Historical Commentary
**Status:** Still relevant

Unlike many of its era-mates covering 4D Mobile/Wakanda or classic-only UI hacks, this note concerns fundamental RSA cryptography interoperability that hasn't changed: ENCRYPT BLOB/DECRYPT BLOB and GENERATE ENCRYPTION KEYPAIR remain part of current 4D, and the PKCS#1-vs-SubjectPublicKeyInfo key format distinction along with 4D's header-byte quirk are still accurate today for anyone bridging 4D-encrypted data with an external system.

The specific PHP library referenced (phpseclib) is still actively maintained, and the general approach — convert key formats, strip/add the 4D header — remains the correct mental model. A developer picking this up in 2026 would find the crypto guidance directly usable, needing only to swap in whatever current PHP/OpenSSL idioms are preferred.
