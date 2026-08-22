# Tech Note 10-33: Idle User Detective

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** November 24, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76221
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_31-35_(NOV)/10-33_Idle_User_Detective.zip

## Proposition
Charles Vass's Tech Note tackles a practical Client/Server administration problem: users who leave 4D running in Remote mode for long stretches without activity, tying up server licenses and resources.

## Key Points
- Combines internal (4D event loop) and external (OS-level) idle detection for reliability
- Displays a countdown warning dialog before forcing disconnection
- Implements platform-specific idle detection code for both Windows and Mac OS X
- Programmatically quits 4D Remote mode once the timeout is reached
- Aimed at reclaiming Client/Server license seats tied up by inactive users

## Featured Technology
- idle user monitoring
- countdown warning dialog
- programmatic client disconnect
- Remote mode (Client/Server)
- OS-level idle detection (Windows/Mac OS X)

## Best Practices Highlighted
- Warn users with a countdown before disconnecting them, rather than silently kicking them off
- Combine 4D-level and OS-level activity signals for more accurate idle detection

## Context/Positioning
Published to help 4D Client/Server shops manage license usage and server load caused by users leaving Remote sessions open and idle for long periods.

## Historical Commentary
**Status:** Still Relevant

This note demonstrates a classic-language technique for monitoring user inactivity and programmatically disconnecting idle Remote (Client) connections, using an internal 4D method loop plus OS-specific external calls for true system idle-time detection. The core approach (background process polling, countdown dialog, forced disconnect) still works unchanged in current 4D versions since it relies on stable, backward-compatible commands, so it remains a valid, still-relevant pattern for client/server deployments that need to reclaim idle licenses today.
