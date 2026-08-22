# Tech Note 17-14: Using a Custom Component to Patch Deployed Data Files

**Author:** Cam Adams, Justin Carr, and David Adams
**Published:** July 27, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77822
**Download:** https://kb.4d.com/DLTN/TN/2017/17-14_PatchDeployedDataFile.zip

## Proposition
This third-party Tech Note describes a strategy for safely patching deployed customer data using purpose-built 4D components, covering real-world constraints, host/component data interaction, and use of embedded SQL for patch logic.

## Key Points
- **Real-world scenarios:** covers diagnosing unclear bugs, fixing data beyond 4D Backup's recovery, and patching bugs in code or the OS interaction layer.
- **Deployment constraints:** addresses limited off-site data access, avoiding client-specific code pollution, urgency, and avoiding server restarts.
- **Component-based patching:** design, deploy, and run a dedicated component to execute the patch against live data.
- **Automation and idempotency:** covers automating the patch process and avoiding running the same patch twice.
- **Host vs. component data:** explains how patch components interact with data in the host database versus packaged component data.
- **Custom constants tip:** recommends using custom constants to simplify host/component data interaction.
- **SQL usage tradeoffs:** discusses "using more SQL" vs. "using less SQL" approaches for implementing patch logic.

## Featured Technology
- 4D Components
- Embedded 4D SQL
- Custom constants
- External data files

## Best Practices Highlighted
1. Package emergency data-repair logic as a versioned, deployable component rather than ad hoc code.
2. Guard patch components against being run more than once.
3. Separate host-database logic from component-packaged logic and constants for clarity.

## Context / Positioning
Published in 2017 for classic 4D v16, this third-party contributed note reflects deployment realities of the pre-Project-Mode era, where components were binary/classic-mode artifacts and embedded SQL was a common way to manipulate data programmatically.

## Historical Commentary
**Status:** Partially superseded

The operational pattern — a controlled, versioned patch mechanism for deployed customer data — remains valuable and conceptually sound for any long-lived deployed application, 4D or otherwise. However, the concrete implementation details (classic 4D components, heavy use of embedded SQL) reflect pre-Project-Mode, pre-ORDA tooling; a modern equivalent would likely be built as a class-based module under Project Mode using ORDA for data access, though SQL remains available as a legacy option.
