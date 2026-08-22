# Tech Note 17-13: A Look into Tailoring the 4D Write Pro Interface

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 27, 2017 | **Product/Version:** 4D Write Pro v16 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77820
**Download:** https://kb.4d.com/DLTN/TN/2017/17-13_Tailoring4DWritePro.zip

## Proposition
This Tech Note explains why 4D Write Pro replaced the 32-bit 4D Write plug-in for 64-bit compatibility, surveys its default UI (controls and contextual menu), and demonstrates several ways to tailor its interface — control bars, contextual menus, and menu bars — to an application's needs.

## Key Points
- **64-bit transition:** 4D Write Pro replaces the old 32-bit 4D Write plug-in, which cannot run in 64-bit builds.
- **Native form object:** 4D Write Pro is integrated as a form object (since v15R3), not a separate plug-in tool.
- **Not a drop-in replacement:** 4D Write Pro is architecturally distinct from classic 4D Write, requiring a real migration effort.
- **Default UI review:** documents default user interface controls and default contextual menu behavior.
- **New standard actions:** shows adding new functions and tracking text selection state on the 4D Write Pro object.
- **Tailoring mechanisms:** customizing control bars, the 4D Write Pro Interface Component, contextual menus, and menu bars.
- **Sample database:** hands-on example built for v16R4 demonstrating the tailoring techniques.

## Featured Technology
- 4D Write Pro
- Control bars and menu bars
- Contextual menu customization
- 4D Write Pro Interface Component

## Best Practices Highlighted
1. Review 4D Write Pro's default UI and contextual menu before assuming they fit your end users' needs.
2. Use standard actions and selection tracking to build custom UI behaviors around the 4D Write Pro object.
3. Plan a deliberate migration path when transitioning from classic 4D Write to 4D Write Pro rather than expecting a drop-in swap.

## Context / Positioning
Published in mid-2017 for 4D Write Pro v16R4, this note captures 4D Write Pro in its early rollout period shortly after its v15R3 introduction, during 4D's broader move toward 64-bit compatibility, and well before Project Mode or ORDA existed.

## Historical Commentary
**Status:** Still relevant

4D Write Pro has fully superseded classic 4D Write, and the UI customization mechanisms described here — control bars, contextual menus, menu bars, and the Interface Component — remain part of current 4D Write Pro. The note is an early snapshot, though, so a present-day 4D Write Pro implementation would likely also draw on many additional features (advanced styling, page setup via JSON, mail merge, etc.) added in later versions that go beyond what this note covers.
