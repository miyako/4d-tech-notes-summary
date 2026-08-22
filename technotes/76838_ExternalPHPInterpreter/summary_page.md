# Tech Note 13-08: Start and Stop External PHP Interpreter within 4D

**Author:** Aaron Smith, Technical Services Team Member, 4D Inc.
**Published:** June 17, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76838
**Download:** https://kb.4d.com/DLTN/TN/2013/13-08_StartStopExtPHPInterp.zip

## Proposition
This Tech Note documents how to start, stop, and check the status of an external PHP interpreter from within a 4D application, filling a gap since 4D natively manages only its internal PHP interpreter and provides no built-in commands for controlling an external one.

## Key Points
- Distinguishes 4D's internal PHP interpreter (used for EXECUTE PHP-family commands) from an externally installed PHP interpreter.
- Provides a component interface with features to start, check status of, and stop an external PHP process.
- Gives separate implementation code paths for Windows and OS X since process management differs by platform.
- Explains why a developer might prefer an external interpreter (different PHP version, extensions, or configuration than 4D's bundled one).
- Includes installation steps for the provided component.

## Featured Technology
- PHP interpreter (internal vs external)
- 4D PHP execution engine
- Shell/process commands (LAUNCH EXTERNAL PROCESS)
- Cross-platform (Windows/OS X) process control component

## Best Practices Highlighted
1. Check interpreter status before attempting to start/stop it to avoid orphaned or duplicate processes.
2. Wrap platform-specific process commands behind a single component interface for portability.

## Context/Positioning
Published for 4D v13.3 when PHP integration (via 4D's internal PHP interpreter) was a common way to extend 4D applications with PHP libraries, and developers needed finer control over interpreter lifecycle than 4D exposed natively.

## Historical Commentary
**Status:** Partially Superseded

4D's internal PHP execution model has evolved over subsequent versions, and this note's platform-specific external-process launch/kill technique is a workaround for a gap 4D has since narrowed with improved internal PHP support and more general external process commands. The underlying need — bridging 4D to external interpreters/processes — is now more often addressed via 4D's native REST/JSON capabilities or newer process-management commands rather than manually scripted OS-level process control.
