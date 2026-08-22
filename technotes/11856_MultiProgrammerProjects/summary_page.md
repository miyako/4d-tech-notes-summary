# Tech Note: Multiple Programmer Projects Using 4D

**Author:** Not specified
**Published:** November 1, 1999 | **Product/Version:** 4D Server v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11856

## Overview
This Tech Note discusses best practices and strategies for multiple programmers simultaneously developing within a 4D database, addressing the lack of built-in version control and standards enforcement in 4D Server.

## Key Points
- General hints and tips for multi-programmer development
- Cross-platform development efficiency tips
- Naming conventions and standards for team projects
- Multi-developer productivity improvements
- Programmer communication strategies
- Techniques for avoiding object locking issues in Design Mode
- Schemes for code refinement by other programmers
- Self-documentation practices

## Featured Technology
- 4D Server (simultaneous multi-developer access)
- Design Mode object locking
- Cross-platform development (Mac & Windows)
- Team development practices

## Historical Context
**Status:** Superseded

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). This note reflects the pre-version-control era of 4D development, where binary structure files (.4DB/.4DC) made external version control impractical and Design Mode object locking was the only concurrency mechanism. Modern 4D's Project Mode (introduced in v17, 2018) stores all code as text files, enabling standard Git-based version control, branching, merging, and CI/CD pipelines. While the specific advice about object locking is obsolete, the principles of naming conventions, team communication, and self-documenting code remain universally relevant.
