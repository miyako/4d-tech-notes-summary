# Tech Note 04-32: Client Self-Upgradable

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** August 12, 2004 | **Product/Version:** 4D vn/a | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=33569
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_31-35_(JUL)/04-32_ClientSelfUpgradable.exe

## Overview
This Tech Note describes a feature introduced in 4D 2004 that lets developers build stand-alone Client and Server versions of a final application, much like the traditional double-clickable Final Applications produced with 4D Engine, except split into separate Client/Server executables. These built executables are self-contained and can run independently of the 4D application itself, meaning end users do not need a copy of 4D installed to use the Client or Server pieces. The note's title, 'Client Self-Upgradable,' signals that a key focus is on how such client executables can be upgraded (presumably in place, without requiring end users to manually reinstall) as the underlying database structure or code evolves. This reflects a period when 4D was formalizing its merged/stand-alone deployment story for Client/Server applications, giving ISVs and in-house developers a way to distribute polished, self-updating client software to end users without exposing the 4D development environment. As a short feature-introduction note, it is aimed at developers packaging and distributing 4D Client/Server applications to non-technical end users.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- An explanation of 4D 2004's ability to build stand-alone, self-contained Client and Server final application executables that can run independently of 4D.

## Featured Technology
- 4D Client/Server merged executables
- 4D Engine final applications
- Application self-upgrade mechanism

## Historical Context
**Status:** superseded

This note documents an early-2000s mechanism for producing self-contained, upgradable 4D Client/Server executables via 4D Engine-based merging, aimed at simplifying end-user deployment and updates. 4D's application deployment and update tooling has evolved substantially since 2004 (including later Merged/stand-alone application builders and update mechanisms bundled with subsequent 4D and 4D Server releases), so while the underlying goal — distributing a self-contained, upgradable client app — remains a common requirement, the specific mechanism described here is no longer the current approach.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
