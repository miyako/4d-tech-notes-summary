# Tech Note 12-06: Music Player Integration

**Author:** Sonya Rackwitz, Technical Services Team Member, 4D Inc.
**Published:** March 28, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76546
**Download:** https://kb.4d.com/DLTN/TN/2012/12-06_MediaPlayer.zip

## Proposition
This Tech Note shows how to embed a QuickTime-based music player inside a 4D Web area and control playback (play/stop, progress, volume) via JavaScript called from 4D, packaged as a reusable component.

## Key Points
- Embeds a QuickTime player via the HTML <EMBED> tag inside a 4D Web area.
- Explains what QuickTime is and why it was chosen (broad audio/video file type support).
- Uses JavaScript to expose playback controls and calls those JavaScript functions from 4D code.
- Provides a component database packaging a full control bar (play/stop, progress/scrubbing, volume).
- Includes a separate host database demonstrating how simply the component's control bar integrates into another application.
- Points to further "See Also" resources for related integration techniques.

## Featured Technology
- 4D Web area
- QuickTime <EMBED> media playback
- JavaScript playback control functions
- 4D-to-JavaScript calling bridge
- 4D component database packaging

## Best Practices Highlighted
1. Package reusable media UI (control bar) as a component so it can be dropped into any host database.
2. Separate the JavaScript control logic from the 4D application logic, calling into JavaScript only for playback actions.
3. Provide a working demo/host database alongside the component to show real integration usage.

## Context/Positioning
Published in 2012 when embedding QuickTime via HTML was still a common way to add media playback to web content, this note showed 4D developers how to bring rich media controls into their applications using the Web area bridge available at the time.

## Historical Commentary
QuickTime plugin-based playback was discontinued by Apple and is no longer supported in modern browsers, making the specific <EMBED>-based technique in this note fully obsolete; any current implementation would need to use HTML5 audio/video elements instead. The broader pattern of embedding HTML/JS media UI in a 4D Web area and bridging control via JavaScript calls remains structurally sound, but 4D's own Web area JavaScript integration has also evolved considerably since this note was published.

**Status:** Obsolete
