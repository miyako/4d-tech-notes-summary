# Tech Note: Communicating With 4D

- **Asset ID:** 11957
- **Tech Note #:** 00-52
- **Published:** November 1, 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=11957
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_51-55_(NOV)/00-52_Communicating_With_4D.hqx

## Overview

Jamras Komoncharoensiri (4D, Inc.) builds "4D Communicator," a multi-user chat room and internal-mail sample application, to demonstrate a custom password system, interface tricks for scrolling text displays, and reliable multicast messaging between connected 4D clients using EXECUTE ON CLIENT.

## Key Points

- A custom password system stores login credentials and presence in a `[Member]` table (Username, Password, Firstname, Lastname, Status, Room, InBoxStatus) rather than 4D's built-in structure-based password system, letting the app track which chat room each signed-in user currently occupies.
- Leaving a room (`Enter_Room` method) checks `isFull` on the target room, then locks and updates the member's own `[Member]Room` field via `READ WRITE`/`QUERY`/`SAVE RECORD`/`UNLOAD RECORD`; other clients' `Participants_List` is refreshed by `On Timer`-driven calls to `Initialize_Participants_List` and `Get_Name_InRoom`.
- Interface tricks make a plain text variable act like a scrolling chat log: trim `Msg_Displayer` once it exceeds 30,000 characters (`Delete string`), use `HIGHLIGHT TEXT` on the last character to force auto-scroll, and use `POST KEY(9; Current process)` (Tab) to return focus to the message composer while re-highlighting its end via an `On Getting Focus` object method, to avoid the Tab selecting and overwriting existing composer text.
- A Boolean `InBoxStatus` field on `[Member]` drives a two-frame mailbox picture button, checked and flipped on an `On Timer` event to visually notify a user of new eMessages.
- The core multicasting mechanism: `Multicast_Message` queries all `[Member]` records in the sender's current room and calls `EXECUTE ON CLIENT([Member]Username; "Set_G_Message"; $Message)` for each, pushing text onto a shared inter-process variable `<>G_Message` on every recipient's machine.
- Reliability is enforced with a shared Boolean flag `<>G_Flag`: `Set_G_Message` busy-waits in a `While (<>G_Flag=True) ... DELAY PROCESS(Current process; 2) ... End while` loop before overwriting `<>G_Message`, ensuring an older undisplayed message is never clobbered by a newer one (the note explicitly warns that omitting `DELAY PROCESS` inside such a loop would starve other processes).
- The finished app's end-user features include internal-only eMessage (multi-recipient "To:" selector, Inbox with Prev/Next/Delete), a ten-room chat lobby with live room switching, and a "Find Member" locator reporting whether a named user is signed in, in a room, or not a member at all.

## Featured Technology

- EXECUTE ON CLIENT for pushing method calls to other connected clients
- Custom multi-user password/login system stored in a Member table
- HIGHLIGHT TEXT / POST KEY for auto-scrolling text-area chat displays
- Shared inter-process variables (<>G_Message, <>G_Flag) for message handoff
- On Timer polling to refresh chat room participant lists
- DELAY PROCESS busy-wait guard against concurrent message overwrite

## Historical Commentary

**Status:** Partially superseded

This note builds a real-time, multi-user chat and internal-mail application ("4D Communicator") on 4D Server, using EXECUTE ON CLIENT to multicast messages to selected connected clients, On Timer polling to refresh chat room participant lists and mailbox flags, and manually-coded interface tricks (HIGHLIGHT TEXT plus POST KEY of Tab) to make a plain text variable scroll like a chat log. EXECUTE ON CLIENT remains a core 4D Server command and this is a legitimate historical example of client-to-client messaging in 4D, but the polling-based (On Timer) update model and manual busy-wait synchronization via a shared <>G_Flag variable are dated compared to newer 4D mechanisms; modern 4D applications needing this kind of push notification more commonly rely on the more robust CALL WORKER/worker-based inter-process communication introduced in later 4D versions.

**References to newer/updated information:**
- EXECUTE ON CLIENT remains part of the current 4D language for invoking a method on a specific connected client
- 4D's later CALL WORKER / worker process model provides a more robust, less ad hoc mechanism for inter-process and inter-client messaging than the shared-variable, DELAY PROCESS busy-wait pattern shown in this note
- On Timer polling for UI refresh (e.g. chat participant lists) remains a workable but comparatively coarse technique next to modern event-driven update patterns
