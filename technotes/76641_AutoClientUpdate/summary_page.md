# Tech Note 12-16: Automatic Client Update - Updated for 2012

**Author:** Josh Fletcher, Technical Account Manager, 4D Inc.
**Published:** September 4, 2012 | **Product/Version:** 4D Server v12.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76641
**Download:** https://kb.4d.com/DLTN/TN/2012/12-16_AutoClientUpdate.pdf

## Proposition
This Tech Note revisits 4D's automatic client update feature for merged client/server applications, explaining how structure changes are automatically distributed to all connected clients, and — importantly — how developers can extend this mechanism to also update external resources or handle a new 4D version release, a capability added since 4D 2004 that previously required manual or fully custom code.

## Key Points
- Explains that 4D automatically distributes structure changes (new methods, forms, etc.) to all clients as fundamental client/server behavior.
- Notes that prior to 4D 2004, additional update needs (new 4D version, external resources) required manual work or custom code.
- Describes the feature 4D 2004 introduced to let developers handle these additional update scenarios.
- Covers configuring/customizing the automatic update process for the 2012-era 4D Server (v12.4).
- Discusses benefits of automatic updates for keeping merged client/server deployments consistent.

## Featured Technology
- 4D Client/Server architecture
- Automatic client update feature
- Structure/method/form distribution
- Custom update hooks for external resources

## Best Practices Highlighted
1. Rely on 4D's built-in automatic client update mechanism rather than manual client redistribution for structure changes.
2. Hook into the update process to also refresh external resources or the 4D runtime version when needed.

## Context/Positioning
Published for 4D Server v12.4 to keep developers current on client-update mechanics as 4D periodically enhanced this feature across major versions, a recurring topic given how central update reliability is to client/server deployments.

## Historical Commentary
**Status:** Partially Superseded

Automatic client updating for merged 4D client/server applications remains a core, actively used feature in current 4D versions, so the underlying concept in this note is still relevant. However, the specific mechanics described reflect the pre-Project-Mode, binary-structure-distribution era (structure/method/form changes as monolithic compiled artifacts); with Project Mode's text-based .4DProject structure (v17+) and modern deployment/build pipelines, how structure changes are packaged and distributed to clients has changed significantly from the 2012-era description here.
