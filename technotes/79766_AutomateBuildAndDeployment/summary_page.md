# Tech Note 25-07: Automating Build and Deployment processes with Build4D Component

**Author:** Soukaina BACHIKH, Customer Success Engineer, 4D Inc.
**Published:** July 24, 2025 | **Product/Version:** 4D v20 R | **Platform:** Win
**Page:** https://kb.4d.com/assetid=79766
**Download:** https://kb.4d.com/DLTN/TN/2025/25-07_AutomateBuildAndDeployment_R2.zip

## Proposition
Manually building, signing, and packaging 4D applications through the graphical interface does
not scale for teams that need fast, consistent, repeatable releases. This note introduces Build4D,
a 4D component that turns the build process into scripted, automatable code — the foundation for
integrating 4D projects into modern CI/CD pipelines like GitHub Actions.

## Key Points
- **Build4D as a scriptable build layer.** Available since 4D v19 R3 for project-based (v18+)
  applications, Build4D replaces manual build-menu operations with code, callable from a single
  command or triggered by CI.
- **Version-matched installation.** Build4D should match the installed 4D version; developers
  select the corresponding branch from the official `4D-depot/Build4D` GitHub repo and add it as
  an interpreted (`.4dbase`) or compiled component.
- **A class per build target.** `cs.Build4D.CompiledProject` (`.4dz` structures),
  `cs.Build4D.Component` (reusable `.4dbase` components), `cs.Build4D.Standalone`,
  `cs.Build4D.Server`, and `cs.Build4D.Client` all extend a common `_core` class and expose a
  `build()` method.
- **Settings-object configuration.** Each build is configured via parameters such as
  `projectFile`, `sourceAppFolder`, `destinationFolder`, `buildName`, `IPAddress` (linking a
  client build to its server), `versioning`, `appShortVersion`, and `iconPath`.
- **Headless execution via Tool4D.** 4D's `tool4d.exe`/`tool4d` CLI runs project methods or
  builds without the GUI (`--startup-method`, `--build`, `--compile`, `--check`), making it the
  bridge between Build4D scripts and CI runners.
- **GitHub Actions integration.** Workflows are YAML files under `.github/workflows/` defining
  triggers (push, pull_request, workflow_dispatch), jobs, and steps; the note walks through a
  minimal example workflow and a self-hosted Windows runner setup for actual 4D builds.
- **Split compile/build workflow pattern.** The demo separates a "Compile" workflow (auto-run on
  push, verifying compile success) from a "Build" workflow (manually triggered, producing the
  client/server app), with log capture used to detect and diagnose failures.

## Featured Technology
- **Build4D component** — scriptable build/packaging automation for 4D projects.
- **`cs.Build4D` class hierarchy** — `CompiledProject`, `Component`, `Standalone`, `Server`,
  `Client`, each wrapping a specific build target behind a shared `build()` method.
- **Tool4D** — 4D's headless CLI utility for running builds/methods without the graphical
  environment.
- **GitHub Actions** — CI/CD platform automating build/test/deploy via YAML-defined workflows.
- **Self-hosted runners** — Windows runners registered to GitHub Actions to execute actual 4D
  builds using local 4D/Tool4D installations.

## Best Practices Highlighted
1. *Match Build4D's version to the installed 4D version* to avoid compatibility issues and
   ensure full functionality.
2. *Separate compile-verification from build-and-package steps* in CI (as in the demo's two
   distinct workflows) so failures are isolated and easier to diagnose.
3. *Capture and inspect CI logs* for build failures (e.g. misconfiguration, missing files, logic
   errors) before reattempting a build.
4. *Use Tool4D's headless mode* for all CI-triggered operations to avoid dependency on a running
   GUI session.

## Context / Positioning
Published in mid-2025 for 4D v20 R, this note reflects 4D's continued push to align its
development platform with mainstream DevOps practices, following the maturation of project-based
(text-based, Git-friendly) 4D applications introduced in v18. By combining the Build4D component
with GitHub Actions and Tool4D, 4D provides a complete, reproducible path from source control to
packaged application, addressing the automation and CI/CD expectations increasingly common among
professional software teams.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
