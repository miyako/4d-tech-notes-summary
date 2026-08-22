# Tech Note 19-11: 4D on GitHub

**Author:** Ayoub Khali, Technical Services Engineer, 4D Inc.
**Published:** June 21, 2019 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78277
**Download:** https://kb.4d.com/DLTN/TN/2019/19-11_4DonGitHub.zip

## Proposition
4D's new Project Mode converts a binary database into per-element text files, finally making real Git-based version control practical for 4D team development. This note explains Project Mode's structure and provides a complete Git/GitHub primer tailored to 4D developers.

## Key Points
- **4D Project Mode (new in v17R5):** converts a `.4DB` binary database into a `Project` folder with every form/method/menu/structure element as a text file, via File > Export > Structure to project…
- **One-way conversion:** the `.4DB` file is untouched; re-converting later replaces the project folder, but there's no path back from project to binary.
- **Project folder layout:** `BuildSettings`, `DerivedData`, `Sources`, and `Trash` subfolders plus a `.4DProject` file.
- **Git fundamentals covered:** distributed vs. centralized VCS, working directory/staging area/local repository, remote repositories, and branching (feature branches merging into master).
- **Full installation walkthrough:** GitHub account creation, Git installation on Windows/macOS, credential helper setup, and creating a first remote repository.
- **Three hands-on demos:** interacting with a remote repo (including `git reset --hard`), resolving a real merge conflict, and using branches with stashing.

## Featured Technology
- 4D Project Mode (text-based `.json`, `.4dm`, `.4DCatalog` files)
- Git, GitHub, Git Bash
- Git branching, merging, stashing, conflict resolution

## Best Practices Highlighted
1. Convert to Project Mode before attempting to adopt Git-based team workflows — binary structure files are not diff/merge-friendly.
2. Configure `git config --global user.name/email` and a credential helper immediately after installation.
3. Use feature branches rather than committing directly to master for team development.

## Context / Positioning
Published right as 4D's Project Mode was newly introduced (v17R5), this note reflects a pivotal moment in 4D's evolution toward modern, text-based, diff-friendly source control — a foundational shift that would go on to become the default development mode in subsequent 4D versions, positioning 4D to interoperate with the broader software engineering ecosystem (Git, GitHub, CI/CD).

## Historical Commentary
**Status:** Still relevant

This note captures 4D Project Mode at its introduction; Project Mode has since become the default, standard 4D development format starting with v18, with classic binary (.4DB) "Design Mode" now considered legacy/deprecated for new projects. The Git/GitHub concepts and workflow guidance remain accurate today, though some UI screenshots (GitHub's signup flow, specific installer download links) are visually dated. A developer starting fresh today would use Project Mode as the default (not an optional conversion) and would find current 4D documentation with more mature Git-integration tooling, but the fundamentals taught here are still sound.
