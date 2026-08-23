# Tech Note 02-11: Creating and Administering 4D Portal

- **Asset ID:** 23255
- **Tech Note #:** 02-11
- **Published:** March 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=23255
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_10-14_(MAR)/03-11_Portal_Administration.hqx

## Overview

Christian Cypert (4D & WebSTAR Plug-in Evangelist) walks through the 4D Portal Administration web interface — hosting a new Portal, configuring its services ("Portlets"), and administering Forums, Classified Ads, and Users — entirely through a browser UI accessed at `/portaladmin/`.

## Key Points

- Portal Administration is reached at "http://127.0.0.1/portaladmin/", where you can host a new Portal, edit an existing Portal, or delete one; new Portals require a Host Name (URL/IP) and an Administrator, initially only satisfiable by the built-in Super-Admin account until users exist.
- Portal-wide options include allowing self-signup ("Users can sign up"), a maximum Survey question count (default 10, up to 100), a date format (English Month/Day/Year vs. International Day/Month/Year), and a time format (AM/PM vs. 24 Hour).
- Services are exposed as checkbox-selectable "Portlets" (e.g., Favorites, Reminders); unchecking a Portlet removes that feature from the Portal entirely, letting operators tailor which services are offered.
- Forum administration lets you create Categories (e.g., "Cars") each containing multiple Forums (e.g., Ford, Chevrolet, Chrysler) entered one per line; per-category options include renaming the Category, adding a Forum with an optional Moderator, removing a Forum, changing a Moderator, and transferring all topics/posts from one Forum to another to consolidate forums without losing content.
- Classified Ads administration mirrors Forums: a Category (e.g., "4D Products") contains Subcategories (e.g., 4D Standalone, 4D Server, 4D Open), entered the same one-per-line way and editable by clicking the Category link.
- User administration has two parts: configuring which signup fields (First/Last Name, Email, Street, Phone Number) are collected and which are required, and a searchable/paginated (by first letter) list of current Portal users with the ability to delete selected users or create a new user via a Register form that highlights required fields in red.

## Featured Technology

- 4D Portal Administration site (/portaladmin/)
- Portal hosting and Host/Administrator setup
- 4D Portal Portlets (Forums, Classified Ads, Users, Favorites, Reminders)
- Forum category/moderator administration
- Topic/post transfer between forums
- User registration field requirements

## Historical Commentary

**Status:** Obsolete

This note is a step-by-step, screenshot-driven walkthrough of the 4D Portal Administration web application: hosting a new portal, configuring services/portlets, and administering Forums, Classified Ads, and Users through a browser UI. It reflects the early-2000s trend of 4D-built turnkey community/portal products bundled with the 4D platform. 4D Portal as a distinct product has long been discontinued, and the specific administrative workflow it documents (Portal Admin URLs, Portlet checkboxes, forum-to-forum topic transfer) has no direct modern equivalent in current 4D releases, making this note of historical interest only.

References to newer/updated information:
- 4D Portal has been discontinued; modern portal/community-style applications would be built with current web frameworks or 4D's own modern web/REST/Qodly capabilities
- No direct successor feature in current 4D replicates 4D Portal's built-in Forums/Classified Ads/Users portlets
