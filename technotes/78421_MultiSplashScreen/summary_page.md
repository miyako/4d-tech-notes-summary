# Tech Note 20-03: Multi-Splash Screen

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** February 26, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78421
**Download:** https://kb.4d.com/DLTN/TN/2020/20-03_MultiSplashScreen.zip

## Proposition
4D's built-in splash screen support shows a single static image at startup. This note provides a sample database that randomly selects from multiple developer-chosen images (including animated GIFs) each time the application launches, giving apps visual variety without per-release rework.

## Key Points
- **Picture Library sourcing**: candidate splash images are uploaded into the database's built-in Picture Library.
- **Splash Image Chooser Form**: a checklist UI (backed by `PICTURE LIBRARY LIST`) lets developers mark which library pictures are eligible splash images.
- **JSON persistence**: selections are saved to `splash.json` in a `Splash` folder via `JSON Stringify`/`Document to text`, and reloaded via `JSON Parse` so prior choices persist across sessions.
- **Library sync handling**: the chooser form reconciles saved settings against the live Picture Library, correctly surfacing newly added pictures, removing deleted ones, and updating renamed ones.
- **Dual splash forms**: a variable-object form (`splash_screen`) handles static images while a Web Area-based form (`Gif_splash`) properly renders animated GIFs, selected based on picture type.
- **`On Startup` integration**: the database startup method reads `splash.json`, randomly selects an eligible image, resizes it for consistent sizing, and displays the appropriate splash form.

## Featured Technology
- 4D Picture Library (`PICTURE LIBRARY LIST`)
- JSON persistence (`JSON Stringify`, `JSON Parse`)
- Web Area (for animated GIF rendering)
- `On Startup` database method

## Best Practices Highlighted
1. Reconcile saved JSON settings against the live Picture Library on each form open to gracefully handle added/removed/renamed pictures.
2. Use a Web Area rather than a static variable object specifically when the source image is an animated GIF.
3. Resize splash images at startup to keep the splash window a consistent size regardless of source image dimensions.

## Context / Positioning
This note is a creative, developer-experience-focused utility rather than a core platform feature announcement — it shows how far a small amount of custom code atop stable, long-standing 4D APIs (Picture Library, JSON, classic forms) can go toward polishing an application's first impression, a recurring theme in 4D's tech note series aimed at practical application-craft tips.

## Historical Commentary
**Status:** Still relevant

Every API used here — the Picture Library commands, JSON serialization, `On Startup`, classic forms, and Web Areas — remains fully current in 4D with no deprecation. 4D has not added a native multi-splash-screen feature since, so this DIY pattern is still the way to achieve randomized/varied splash screens today. It is unaffected by the Design Mode → Project Mode transition or ORDA's rise, since it deals purely with UI/startup behavior rather than data access.
