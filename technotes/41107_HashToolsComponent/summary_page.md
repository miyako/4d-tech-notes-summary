# Tech Note 05-43: The HashTools Component

**Author:** David Adams
**Published:** December 22, 2005 | **Product/Version:** 4D (2004 era) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41107
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-43_Hash_Tools_Component.zip

## Overview
This note documents the public and protected API of the HashTools component — a packaged, reusable 4D component implementing nine hashing algorithms and hash-optimized search routines for text, BLOBs, pictures, and documents, underpinning the techniques in several related technical notes.

## Key Points
- Explains why the code is packaged as a 4D component: reduced complexity (≈10 public methods vs. 50+ internal ones), simplified updates across related databases, and centralized, efficient parameter validation via protected "gateway" methods.
- Designed to run compiled, supporting strict "all variables typed" compilation.
- Core hashing routines: `HashTools_HashText`, `HashTools_HashBlob`, `HashTools_HashPicture`, `HashTools_HashDocument` (the latter streaming documents in 32,000-character chunks to limit memory use).
- `HashTools_FindByHash` performs an indexed search on a stored hash field before confirming exact matches on the real value — usable on alpha, text, BLOB, and picture fields.
- Full error-management API (`HashTools_GetLastErrorLocation`, `HashTools_GetLastErrorCode`, `HashTools_GetErrorText`) with a documented table of 14 internal error codes.
- Cross-references TN 05-44 (search optimization/benchmarks), TN 05-41 (case-sensitive operations), and TN 05-42 (efficient scanning).

## Featured Technology
- HashTools component (4D component architecture)
- Hashing text, BLOBs, pictures, and documents
- HashTools_FindByHash indexed search routine
- Component-based gateway/error-management pattern

## Historical Context
4D's component packaging mechanism for reusable code is a durable, still-supported concept, and the gateway/protected-method validation pattern remains solid practice today. This specific HashTools component, however, was a bespoke sample rather than an official 4D product, and modern 4D applications needing hashing or checksums would typically use native language commands or external libraries rather than seek out this particular legacy component — making it primarily of historical/illustrative interest now.
