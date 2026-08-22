# Tech Note 15-24: Deploying 4D Server 64-bit for Mac

**Author:** Timothy A. Penner, Technical Services Engineer, 4D Inc.
**Published:** December 7, 2015 | **Product/Version:** 4D v15.1 | **Platform:** Mac OS X
**Page:** https://kb.4d.com/assetid=77426
**Download:** https://kb.4d.com/DLTN/TN/2015/15-24_Deploy4DServer64bitforMac.pdf

## Proposition
This note is a deployment guide for the newly production-certified 4D Server 64-bit on Mac OS X (v15.1), covering minimum OS requirements, 64-bit compilation/compatibility, the new ServerNet network layer, migrating merged clients, and encrypted client-server connections.

## Key Points
- **Certification milestone:** 4D Server 64-bit for Mac moved from preview (v14 R3–v15.0) to certified/production status at v15.1.
- **Minimum OS X version and architecture requirements** are specified for a supported 64-bit deployment.
- **64-bit code compilation and compatibility:** addresses how compiled code behaves when moving to the 64-bit product, including process stack size differences.
- **Unsupported features list:** documents functionality not yet available in the 64-bit product at the time.
- **New ServerNet network layer:** introduced alongside 64-bit Server, with guidance on activating/deactivating the legacy layer for compatibility.
- **Migrating merged 4D clients** to work correctly against the new 64-bit/ServerNet architecture.
- **Encrypted client-server connections** and client request logging are covered for security and diagnostics.

## Featured Technology
- 4D Server 64-bit (Mac OS X)
- ServerNet network layer
- Encrypted client-server connections
- 4D merged client architecture

## Best Practices Highlighted
1. Verify feature compatibility against the "unsupported features" list before migrating a production 32-bit deployment to 64-bit.
2. Test merged client behavior explicitly when moving to the new ServerNet layer rather than assuming drop-in compatibility.

## Context / Positioning
This Tech Note was published in 2015, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Obsolete

This note documents a one-time, long-completed platform transition: 4D Server has been 64-bit-only for many years now, and ServerNet has been the standard (not new) network layer since shortly after this note was published, so the specific migration guidance, unsupported-features caveats, and legacy-network-layer toggling described here no longer apply to any current 4D deployment.
