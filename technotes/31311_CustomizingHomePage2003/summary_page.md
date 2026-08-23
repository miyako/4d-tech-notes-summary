# Tech Note: Customizing the Home Page Automatically Created by 4th Dimension 2003

- **Asset ID:** 31311
- **Tech Note #:** 04-06
- **Published:** February 12, 2004
- **Product / Version:** 4th Dimension 2003
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=31311
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_05-09_(FEB)/04-06_Customizing_Home.hqx

## Overview

David Adams explains how 4th Dimension 2003's Web server auto-generates a default welcome page when no home page/Web folder is present, where that HTML actually lives (an "Html" resource with ID 1 inside 4D itself), and how a vertical-market developer can override it — including linked stylesheets and images — by placing custom resources into just the structure file.

## Key Points

- Starting in 4D 2003, if the default Web folder and home page are missing when the Web server starts, 4D auto-creates them from an "Html" resource with ID 1, viewable in a resource editor like Resorcerer.
- Because 4D searches for a resource in the most recently opened document (the structure file) before falling back to 4D itself, saving a custom "Html" resource with ID 1 into the structure overrides the built-in page without modifying 4D — this works identically across client/standalone/server.
- Sample code writes the override using `TEXT TO BLOB` + `SET RESOURCE("Html";1;$html_blob)`, and reads it back with `GET RESOURCE` + `BLOB to text`.
- Linked assets can be served from resources too: a `WebGetStyles` 4DACTION method reads CSS text via `Get text resource(16000)` and returns it with `SEND HTML TEXT`; a `WebGetPictureResource` method loads an image via `GET PICTURE RESOURCE`, converts PICT to GIF with `PICTURE TO GIF`, and returns it with `SEND HTML BLOB` (each method must have "Available through 4DACTION" enabled).
- Resource ID ranges are noted (-32,767 to 32,767; below 15,000 reserved by OS/4D; 15,000-32,767 for plug-ins/custom code), and PICTURE TO BLOB/JPEG is mentioned as an alternative to GIF if QuickTime is installed.
- Development guidance: it's fastest to edit `index.html` directly while iterating, but the final HTML must be pushed back into the structure's Html resource before distribution; testing means copying the structure to an empty folder and letting 4D regenerate the page.
- Notes on 4D Server/Client resource synchronization: 4D Client copies resources locally when it detects structure changes (triggered by an "Update resource" counter), and resource edits made under 4D Client don't automatically propagate back to the server structure.
- Lists resource-editing tools and further reading: ResEdit (Mac Classic only), Resorcerer (commercial, OS X), Orchard Software's free open-source Windows editor, ResFool ($20 shareware for OS X), and books/articles on 4D and resources.

## Featured Technology

- 4th Dimension 2003 auto-generated Web server home page
- Html-type resource (ID 1) overriding via structure file
- TEXT TO BLOB / SET RESOURCE / GET RESOURCE / BLOB to text commands
- SET TEXT RESOURCE / Get text resource for CSS storage
- GET PICTURE RESOURCE / PICTURE TO GIF and 4DACTION callback methods
- Resource editors: ResEdit, Resorcerer, Orchard Software, ResFool

## Historical Commentary

**Status:** Obsolete

This note explains how to override 4th Dimension 2003's auto-generated Web server welcome page (shown when no home page/Web folder exists) by placing custom HTML, CSS, and images into 'Html', 'TEXT', and 'PICT' resources of the structure file, so a vertical-market developer can ship a branded home page from just a structure file. The technique is tied to classic Mac-style resource forks and 4D's older resource commands (SET RESOURCE, GET PICTURE RESOURCE, 4DACTION callbacks) and 4D's early web server architecture, all of which have been substantially superseded; modern 4D web deployments serve static or dynamically-generated pages directly from the project's Web Folder rather than relying on resource-fork tricks or the classic 4DACTION mechanism, making this note historical-interest-only today.

References to newer/updated information:
- 4D's built-in web server and Web Folder handling have been substantially rearchitected since 4D 2003, and resource-fork-based storage (Html/TEXT/PICT resources) is no longer the standard mechanism for serving default or customized content
- Modern 4D projects typically ship a real Web Folder with static HTML/CSS/JS/image files (or dynamically generated pages via 4D Web methods/REST), rather than relying on 4D auto-generating a welcome page from an internal resource
- 4DACTION-based method callbacks described here have been largely superseded by 4D's newer Web Server and REST-based request handling model
