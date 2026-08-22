# Tech Note 10-22: Hash Examples in 4D

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** July 16, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76130
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_21-24_(JUL)/10-22_Hash_Examples.zip

## Proposition
Timothy Aaron Penner's Tech Note introduces hash functions as a foundational security and data-integrity tool for 4D developers.

## Key Points
- Explains hash functions and the importance of salting, especially for password storage
- Covers three common use cases: password hashing, file integrity, and file fingerprinting/dedup
- Sample database includes a File Browser, File Hasher, Find Duplicate Files tool, and Password Hasher
- Demonstrates converting HFS paths to POSIX paths for cross-platform file handling
- Uses MD5-style checksums as the primary hashing example for file integrity

## Featured Technology
- hash functions
- salt
- password hashing
- MD5 file integrity checksums
- duplicate file detection

## Best Practices Highlighted
- Always salt passwords before hashing rather than storing raw hash values
- Use file hashes/checksums to verify integrity and detect duplicates rather than relying on filenames alone

## Context/Positioning
Published to give 4D developers a practical, from-scratch introduction to hashing for security (passwords) and data management (file integrity/dedup) use cases common in business applications of the era.

## Historical Commentary
**Status:** Still Relevant

The fundamentals covered here — using hash functions with salt for password storage, and hashes for file integrity/fingerprinting/duplicate detection — are timeless cryptographic and data-integrity concepts that remain best practice today. 4D has since added stronger, more modern built-in hashing/digest commands (and encouraged use of bcrypt-style adaptive hashing over plain MD5 for passwords), so while the concepts are current, the specific example commands and MD5-centric examples in this note are dated compared to today's recommended algorithms.
