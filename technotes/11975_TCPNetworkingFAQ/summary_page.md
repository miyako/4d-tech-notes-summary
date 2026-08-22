# Tech Note: TCP Networking FAQ

## Overview
- **Technical Note 00-35**
- **Author:** Thomas D'Urso
- **Published:** July 1, 2000
- **Product/Version:** Network Components v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is a wide-ranging FAQ compiled by 4D Technical Support to address the most common TCP networking questions raised by users of 4D Server and 4D Web Server. It is organized into five major sections: basic configuration issues (introducing TCP/IP terminology, minimum network requirements, and how to connect 4D Client to 4D Server over the Internet or by manually entering a server address), network components (explaining what these platform-level networking abstractions are and how they differ between Macintosh and Windows, plus compatibility considerations), port numbers (what they are, which ports various 4D applications use, running multiple 4D Servers on one machine, and how 4D Open port usage changed between pre-6.5 and 6.5 versions), diagnostic tools (ping, traceroute, and platform-specific TCP utilities), and a troubleshooting section addressing specific, commonly-seen error conditions such as 'You need at least one network component to run' or version-mismatch errors between client and server. The note explicitly excludes the 4D Internet Commands plug-in from its scope, focusing purely on the core client-server and web-server TCP layer. Its featured technology is 4D's network-components networking abstraction as it existed for 4D version 6 and 6.5 applications on both Macintosh and Windows.

## Featured Technology
- TCP/IP networking
- 4D network components (ADSP/TCP)
- 4D Server / 4D Web Server port configuration

## Historical Context
This FAQ covers TCP/IP basics, 4D's platform-specific 'network components' abstraction, port number usage, and troubleshooting steps for 4D Server and 4D Web Server connectivity circa v6/6.5. The general TCP/IP and port-number material remains conceptually accurate today, but the Mac-specific 'network components' abstraction described here was tied to classic Mac OS's pluggable networking stack (pre-dating Mac OS X's Unix-based, unified TCP/IP stack that arrived the following year), so that portion of the note is superseded, along with several of the 4D-version-specific port-number behaviors it documents.

## What's Changed Since
- Mac OS X's Unix-based networking stack unified TCP/IP handling and obsoleted the classic Mac OS 'network components' concept this note explains
- 4D's own network configuration and port-handling behavior has been refined across many releases since v6.5

