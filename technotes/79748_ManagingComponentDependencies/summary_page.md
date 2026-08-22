# Tech Note 25-06: Managing Component Dependencies: Challenges and Solutions

**Author:** Abir HSAINI, Technical Services Engineer, 4D Inc.
**Published:** June 30, 2025 | **Product/Version:** 4D v20 R8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79748
**Download:** https://kb.4d.com/DLTN/TN/2025/25-06_ManagingDependencies.zip

## Proposition
As 4D projects grow, managing external and built-in component dependencies becomes increasingly error-prone: version drift, broken updates, and interpreted/compiled incompatibilities can silently break applications. This note gives developers a structured way to declare, monitor, and troubleshoot dependencies so builds remain stable and reproducible across environments.

## Key Points
- **dependencies.json declares requirements:** Placed at `/Project/Sources/dependencies.json`, it lists local and GitHub-hosted components a project needs, ensuring 4D loads the correct ones on every open.
- **environment4d.json customizes paths:** An optional file (searched upward from the project root) that overrides where local components are found — useful for shared components across projects or keeping machine-specific paths out of source control.
- **Resolution order matters:** 4D checks the project's Components folder first, then environment4d.json paths, then dependencies.json paths, and finally falls back to built-in 4D components (e.g., 4D NetKit, 4D SVG).
- **Project Dependencies panel (Design menu):** A GUI alternative to hand-editing JSON, showing each dependency's origin tag and supporting add/update/remove actions without manual file edits.
- **GitHub dependency rules:** Latest, Up to Next Major/Minor Version, Exact Version (Tag), and Follow 4D Version control how updates are resolved; LTS tags use `x.y.p` and R-release tags use `xRy.p` naming conventions.
- **Interpreted vs. compiled components:** Interpreted components (.4dbase folders) only work in interpreted host projects; compiled components (.4DZ files) work in both modes and are required when the host runs compiled — the simpler flat .4DZ layout is less suited to macOS notarization.
- **Automatic background updates:** ~3 minutes after startup in developer mode, 4D silently checks for component updates and can auto-install them on restart if automatic updates are enabled, which can cause unexpected version changes.
- **Common failure modes documented:** Undetected updates (untagged GitHub releases), invalid archive structure (extra nested top-level folder), and "unable to find latest release" errors (usually a bad access token).

## Featured Technology
- **dependencies.json** — central manifest declaring local/GitHub component requirements.
- **environment4d.json** — override file for custom local component paths.
- **Project Dependencies panel** — Design → Project Dependencies GUI for dependency management.
- **GitHub Releases & Tags** — source of versioned component distribution with Semantic Versioning (major.minor.patch) and wildcard/range support (`1.*`, `>=1.2.3`, `^`, `~`).
- **GitHub Personal Access Tokens** — required for private repository component access.

## Best Practices Highlighted
1. Use relative paths in environment4d.json to keep projects portable and Git-friendly.
2. Follow 4D's LTS/R-release tag naming conventions precisely when using "Follow 4D Version" to ensure correct release matching.
3. Ensure GitHub release ZIP archives place the component directly at archive root, not nested in an extra folder.
4. Monitor and control automatic update checks to avoid unintended version changes in production deployments.

## Context / Positioning
Published as 4D's project-mode and component ecosystem matures, this note reflects the platform's push toward Git-friendly, flat-file project structures and modular, GitHub-distributed component reuse — part of a broader trend of aligning 4D development workflows with modern software engineering practices (version control, semantic versioning, CI-style dependency resolution).

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
