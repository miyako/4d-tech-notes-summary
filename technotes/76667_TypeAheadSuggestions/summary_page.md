# Tech Note 12-17: Type Ahead Suggestions

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** October 1, 2012 | **Product/Version:** 4D v13.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76667
**Download:** https://kb.4d.com/DLTN/TN/2012/12-17_TypeAheadSuggestions.zip

## Proposition
This Tech Note shows how to add Google-style type-ahead suggestions to any enterable text variable in a 4D form, delivered as a component with a simple entry point requiring only a single line of code attached to the variable's 'On After Keystroke' form event, with full component source included for further customization.

## Key Points
- Frames type-ahead suggestions as a familiar UX pattern from web search boxes, brought to native 4D forms.
- Implements the feature via the 'On After Keystroke' form event on the target variable.
- Packages the logic as a component with a minimal one-line integration API.
- Ships the component's full source code so developers can inspect, customize, or upgrade the behavior.

## Featured Technology
- On After Keystroke form event
- Type-ahead/autocomplete component
- Hierarchical list / pop-up suggestion UI
- Reusable single-line integration API

## Best Practices Highlighted
1. Package reusable UI behaviors as components with minimal integration surface (single call) for easy adoption.
2. Trigger suggestion lookups on keystroke events rather than polling, for responsiveness.

## Context/Positioning
Published for 4D v13.1 to bring a now-ubiquitous web UX convention (search-box autocomplete) into classic native 4D desktop forms.

## Historical Commentary
**Status:** Still Relevant

The On After Keystroke-driven type-ahead technique still works today in classic 4D forms and remains a reasonable approach for native desktop UI, since 4D has not removed this event or replaced it with a built-in autocomplete widget. That said, for web-facing 4D applications this kind of behavior is now more commonly implemented with modern JavaScript/CSS autocomplete libraries in an HTML-based front-end, and for object-driven data lists a developer might source suggestions from an ORDA entity selection query rather than a classic array/selection lookup.
