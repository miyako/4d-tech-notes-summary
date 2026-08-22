# Tech Note 21-13: Building a 4D Application

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 29, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78754
**Download:** https://kb.4d.com/DLTN/TN/2021/21-13_BuildingApplication.pdf

## Proposition
Turning a 4D database into a distributable application involves more than clicking "Build" — the Application Builder and the underlying `Build Application` command expose many options for compiled structures, stand-alone apps, and client/server deployments. This note explains the full build surface and how to script it via the buildApp settings file.

## Key Points
- **Three build categories:** compiled structure (.4DC binary or .4DZ Project mode / component package), stand-alone single-user Application (.exe/.app), and Client/Server (separate Server + Client executables).
- **Licensing requirements** differ by build type: a Developer license is always needed; stand-alone builds additionally need a 4D Volume Desktop expansion license.
- **Data Linking Mode:** Application-name-based (portable across install locations) vs. Application-path-based (tied to install path).
- **Plugins & components trimming:** unused native components (e.g. 4D Progress, 4D SVG) can be excluded to shrink build size.
- **buildApp settings file:** generated on every build — named `buildApp.xml` before v19, renamed **`buildApp.4DSettings`** starting in v19 — and can be hand-edited or authored for use with the `Build Application` command for scripted builds.
- **Advanced XML keys** beyond the UI: Client/Server IP/port overrides, `ServerSelectionAllowed` dialog toggle, Windows `StartElevated` auto-update keys, and `ClientWinSingleInstance` for multiple client instances on one machine.
- **PackProject (new in v19):** controls whether a Project mode build's packed structure is read-only, relevant when the deployed app needs to create indexes or run SQL DDL after build.
- **Multi-platform deployment** requires separate build passes per OS and careful handling of automatic-update packages across platforms.

## Featured Technology
- Application Builder (Design > Build Application)
- `Build Application` command
- buildApp.xml / buildApp.4DSettings
- 4D Volume Desktop
- PackProject (Project mode)

## Best Practices Highlighted
1. Generate the buildApp file once via the Application Builder UI to get correct XML structure before hand-editing it for automation.
2. Uncheck unused plugins/components in the builder to reduce final build size.
3. Enable `ServerSelectionAllowed` for deployments where the server address isn't known at build time.
4. Use separate buildApp files for different build targets (e.g., one for compiled structure, one for client/server).

## Context / Positioning
Published at the moment Project mode was gaining traction (introduced ~v17-18), this note captures 4D's build tooling mid-transition: it documents both the legacy binary buildApp.xml naming and the new v19 buildApp.4DSettings naming, plus the brand-new PackProject setting specific to Project mode builds — a useful snapshot of the classic-to-Project-mode handoff in the build/deploy pipeline.

## Historical Commentary
**Status:** Still relevant

The Application Builder's overall structure (compiled structure / stand-alone / client-server tabs, licensing, plugin trimming) and the buildApp settings-file mechanism remain fundamentally how 4D applications are built and deployed today. Project mode has since become the default and near-universal project format, so the PackProject setting and .4DZ compiled structures described here as "new" are now the mainstream path, while the .4DC binary-mode structure option is increasingly a legacy fallback for older, unconverted databases. A developer building an app today would follow essentially the same builder workflow, just squarely within Project mode rather than treating it as one of two parallel options.
