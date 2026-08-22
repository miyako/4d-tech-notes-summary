# Tech Note 10-27: Comparing Client Deployment Options in 4D

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** September 2, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76170
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_24-28_(AUG)/10-27_Client_Deployment.pdf

## Proposition
Josh Fletcher's Tech Note tackles a foundational 4D Client/Server architecture decision: whether to deploy the standard 4D software package and connect in Remote mode, or to build and deploy a Merged client application.

## Key Points
- Defines Client Cache, Merged client, Automatic Client Update, Deployment/Upgrade client terminology
- 4D Remote advantages: arbitrary server access, server failover, interpreted mode, simplified development
- 4D Remote disadvantages: no automatic client update, less customization
- Merged client advantages: automatic client update, customization
- Merged client disadvantages: development overhead, deployment complexity, weaker server failover
- Scoped explicitly to 4D v11 SQL and v12 — older versions may differ

## Featured Technology
- 4D Remote client
- Merged client
- Automatic Client Update
- Deployment/Upgrade client concepts
- 4DLINK

## Best Practices Highlighted
- Choose 4D Remote for simplified development and arbitrary server access; choose Merged for tighter control over update/customization
- Re-evaluate the deployment model as project requirements around updates and customization evolve

## Context/Positioning
Published to help 4D VARs and consultants make an informed architecture decision at a time when both Remote and Merged deployment were mainstream, pre-cloud/pre-web-client options.

## Historical Commentary
**Status:** Still Relevant

This note's comparison of 4D Remote versus Merged client deployment models describes an architectural choice that is still fundamentally offered by 4D today, so the core tradeoffs discussed (arbitrary server access vs. customization/automatic update) remain broadly still relevant for on-premise Client/Server deployments. However, 4D's deployment landscape has broadened considerably since 2010 with cloud hosting options and web/Qodly-based clients that sidestep this classic Remote-vs-Merged decision entirely for many new projects.
