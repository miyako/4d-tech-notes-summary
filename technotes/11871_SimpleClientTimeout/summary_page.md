# Tech Note: A simple client timeout technique

**Author:** Not specified
**Published:** February 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11871

## Overview
This Tech Note presents a simple method for automatically quitting a 4D Client that has been idle (no mouse clicks or key presses), useful for managing licenses and resources in 4D Server environments.

## Key Points
- Uses ON EVENT CALL to detect mouse clicks and key presses
- A background process periodically checks for user activity
- A Boolean variable tracks whether activity has occurred since the last check
- If no activity is detected between process runs, the client is automatically quit
- The startup method and ON EVENT CALL handler reset the activity flag

## Featured Technology
- ON EVENT CALL command (event interception)
- 4D Server/Client architecture
- Background process management
- QUIT 4D command

## Historical Context
**Status:** Superseded

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). The concept of automatically timing out idle clients remains important for license management and security. However, modern 4D Server provides built-in session timeout and client management capabilities, reducing the need for this kind of custom code. ON EVENT CALL is still available but less commonly used in modern 4D architectures that favor worker processes and web-based paradigms.
