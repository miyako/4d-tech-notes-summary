# Tech Note 17-08: 4D Load Launcher

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** May 15, 2017 | **Product/Version:** 4D Server v16 | **Platform:** Windows only
**Page:** https://kb.4d.com/assetid=77778
**Download:** https://kb.4d.com/DLTN/TN/2017/17-08_LoadLauncher.zip

## Proposition
This Tech Note introduces the Load Launcher, a Windows-only tool written in 4D that launches multiple isolated 4D Client instances from a single controlling UI, enabling local load testing of 4D client-server applications without cloud infrastructure.

## Key Points
- **Local load generation:** an alternative to cloud-based load testing, running multiple 4D Client instances on one machine.
- **LAUNCH EXTERNAL PROCESS:** the underlying 4D command used to spawn multiple concurrent 4D Client processes.
- **Client resource isolation:** each launched instance uses an isolated client resource folder, allowing concurrent connections to the same 4D Server.
- **Hidden UI option:** suppresses individual client windows to reduce desktop clutter when running many instances.
- **Version management:** supports adding multiple 4D versions to test against.
- **PID quick menu:** tracks and manages running client instances by process ID.

## Featured Technology
- LAUNCH EXTERNAL PROCESS command
- 4D Client isolated resource folders
- Windows-only process management tooling

## Best Practices Highlighted
1. Use isolated client resource folders when running multiple 4D Client instances concurrently.
2. Hide client UI windows when running large numbers of load-testing instances to reduce clutter.
3. Track running instances by PID for reliable management during extended load tests.

## Context / Positioning
Published in 2017 for 4D Server v16, this is a Windows-only DevOps/QA utility from the classic Design Mode era, reflecting a period when local, self-built load-testing tools were a practical necessity for many 4D shops without access to cloud load-testing infrastructure.

## Historical Commentary
**Status:** Partially superseded

The LAUNCH EXTERNAL PROCESS and client resource isolation mechanisms this tool relies on remain valid in current 4D, so the technique still works for quick local load generation. However, more rigorous or large-scale performance testing today more commonly uses dedicated load-testing platforms or cloud/multi-machine setups rather than a single-machine multi-instance launcher, making this note's specific tool a dated but still-functional niche utility.
