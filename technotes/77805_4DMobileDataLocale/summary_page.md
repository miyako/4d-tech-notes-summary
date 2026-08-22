# Tech Note 17-11: 4D Mobile Customize Data display using Locale

**Author:** Not specified in source document
**Published:** June 30, 2017 | **Product/Version:** 4D Mobile v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77805
**Download:** https://kb.4d.com/DLTN/TN/2017/17-11_4DMobileDataLocale.zip

## Proposition
This Tech Note (presented as a Read Me/setup guide) explains how to install a 4D Mobile demo requiring Wakanda Enterprise and Wakanda Studio, and how to customize locale-based date/time/number display formatting in the resulting Angular mobile app.

## Key Points
- **System requirements:** 4D v16+, Wakanda Enterprise 2.0.0+, supported OS/browser versions.
- **Licensing note:** Wakanda Enterprise requires a separate 4D Mobile license registered on the Wakanda side.
- **Installation steps:** open the demo .4dbase in 4D, start the 4D Web server, open the .waSolution file in Wakanda Studio, and run it.
- **Data model access:** the 4D Mobile data model is exposed under a RemoteModel folder in Wakanda Studio.
- **model.js customization:** server-side methods, calculated attributes, and events (including locale logic) live in model.js.
- **Angular app source:** the demo's HTML/TypeScript app files (app.component.html/.ts) contain the client-side locale customization code.
- **Further resources:** points to 4D Mobile, Angular, and Wakanda documentation.

## Featured Technology
- 4D Mobile
- Wakanda Enterprise / Wakanda Studio
- Angular (client framework)
- Locale-based date/time/number formatting

## Context / Positioning
Published in 2017 for 4D Mobile v16, this note is entirely dependent on the Wakanda Enterprise server product and Wakanda Studio tooling that accompanied 4D Mobile during that era, well before ORDA, Project Mode, or Qodly existed.

## Historical Commentary
**Status:** Obsolete

4D Mobile and the entire Wakanda platform (including Wakanda Enterprise and Wakanda Studio) have been discontinued by 4D, so the specific installation steps, licensing requirements, and model.js-based customization approach described in this note no longer apply to any currently supported 4D product. The general concept of locale-aware date/time/number formatting remains a valid requirement, but developers today would address it using current 4D/ORDA formatting commands or client-side JS framework i18n libraries rather than this note's Wakanda-specific instructions.
