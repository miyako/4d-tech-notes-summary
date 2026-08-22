# Tech Note 08-35: Google Chart API and Web Area Integration

**Author:** Luis Pineiros (Technical Services Team Member, 4D Inc.)  
**Updated from:** Tech Note 08-04 by Christopher Visaya  
**Published:** October 1, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51186  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_35-39_(OCT)/08-35_Google_Web_Area.zip

## Overview

This is an updated version of Technical Note 08-04, adapted to leverage the new Web Area form object that arrived in 4D v11 SQL Release 2, eliminating the need for the deprecated 4D Live Window plug-in. The note demonstrates how 4D developers can construct and display interactive charts by dynamically building parameterized URLs for Google's Chart API and rendering them within a 4D Web Area, enabling real-time charting of database content without server-side rendering.

## Key Points

- **Google Chart API Basics:** Google's service accepts parameterized URLs, processes data and styling on Google's servers, and returns a rendered PNG chart image to the browser. This allows 4D developers to outsource charting to a robust third-party service without licensing additional software.

- **System Requirements:** 4D v11 SQL Release 2 or higher (mandatory for Web Area support). The note explicitly notes that the prior approach using 4D Live Window is no longer applicable.

- **Sample Database Structure:** Includes a single table containing time-series data (minutes spent on activities over seven days), used as example data for demonstrating chart parameter construction and rendering.

- **Five-Page Chart Configuration Form:**
  - Page 1 (Chart Title): Set title text, font size (point size), and RGB color using hex notation (RRGGBB format) via slider controls; spaces are converted to `+` signs automatically, and pipes (`|`) create line breaks.
  - Page 2 (Data Import): Select a table and numeric field to plot; data is encoded for Google Chart API's text encoding format.
  - Pages 3-4 (Chart Styling): Configure series colors, background fill (gradients with opacity), and grid line appearance using hex colors and sliders.
  - Page 5 (URL Display): Shows the complete parameterized Google Chart API URL for inspection and testing.

- **Google Chart API Parameters:**
  - `cht` = chart type (e.g., lc for line chart)
  - `chs` = chart size (e.g., 600x400 pixels)
  - `chd` = data encoding (text format with comma-separated values)
  - `chtt` = title text
  - `chts` = title styling (color and size)
  - `chco` = series colors (hexadecimal)
  - `chf` = background fills (solid or gradient with opacity)
  - `chxt` and `chxl` = axis labels

- **Live Chart Updates:** Every user interaction on the form pages (except Page 2, by design choice) immediately sends a new request to Google Chart API and refreshes the displayed chart, providing rapid visual feedback.

- **Hex Color Calculation:** The note includes code snippets showing how RGB sliders map to hexadecimal notation (FF = full intensity, 00 = no intensity) and how to combine red, green, and blue values into a single 6-character hex code.

## Featured Technology

- Google Chart API
- Web Area form object (new in 4D v11 SQL Release 2)
- Remote data visualization
- URL parameterization and encoding
- Real-time dynamic charting
- CSV/text data encoding for external APIs

## Historical Context

Positioned as an October 2008 update to an earlier 4D Live Window-based charting approach, this note reflects the transition from plugin-dependent charting to native form object support. At the time, leveraging Google's free Chart API was a practical way to provide rich charting capabilities to 4D web applications, avoiding the complexity of server-side image generation or proprietary charting libraries.

## Historical Commentary

**Status:** Obsolete

Google's legacy Chart API (which generated PNG images from parameterized URLs) has been deprecated in favor of Google Charts, a modern JavaScript library that requires a different integration pattern. Furthermore, 4D v11 SQL's Release 2 form object architecture has been superseded by ORDA and Project Mode (introduced in 4D v17, 2018), and Web Area itself now serves as a container for modern web frameworks and REST APIs rather than simple image URLs. Contemporary charting in 4D is accomplished via Qodly's native chart components, modern JavaScript libraries (Chart.js, D3.js, Webix), or Vue.js integration, none of which require the parameterized URL approach documented here.
