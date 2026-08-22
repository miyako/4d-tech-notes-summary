# Tech Note: Powerful Uses of the On Keystroke Form Event

**Author:** Not specified in source document
**Published:** June 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11764
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note introduces and demonstrates the On Keystroke form event, a new 4D v6 Form Event that lets developers react to individual user keystrokes inside enterable form objects, replacing the far more laborious On Event Call-based technique required in 4D v3.

## Key Points

- On Keystroke is one of 4D v6's new Form Events for capturing user interaction with form objects.
- Achieving similar keystroke-reaction behavior in 4D v3 required On Event Call and considerably more manual coding.
- Covers how 4D handles enterable objects and user actions, and how to correctly maintain an enterable object's value while intercepting keystrokes.
- Provides step-by-step implementation guidance.
- Ships with an example database containing interactive demos and ready-to-use example code.

## Featured Technology

- 4D V6 Form Events
- On Keystroke event
- Enterable form objects
- On Event Call (contrasted V3 predecessor technique)

## Historical Context

Written just after 4D v6's introduction of the Events model (replacing the older "Phases" terminology used in earlier versions), this note reflects an era when reacting to fine-grained user input like keystrokes required dedicated new language support — a capability now taken for granted in modern form/object event handling, which has since been extended well beyond this initial V6 implementation.

## Historical Commentary
**Status:** Superseded

This note documents the newly introduced On Keystroke form event in 4D v6 (part of the broader V6 Form Events system), contrasted against the much more cumbersome On Event Call-based V3 technique it replaced; the specific V6 Events terminology and API described here were themselves superseded when 4D later expanded and renamed aspects of the event model, though reacting to individual keystrokes in enterable fields remains a standard, still-relevant capability in current 4D.
