# Tech Note: Building Interactive Graphic Interfaces with 4D Draw, Part VI: Implementing an Interactive Map

## Overview
- **Technical Note 00-25**
- **Author:** Tim Tonooka, 4D, Inc. Technical Support
- **Published:** May 1, 2000
- **Product/Version:** 4D Draw v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the sixth entry in Tim Tonooka's long-running series on constructing interactive, vector-graphic interfaces using 4D Draw, and it recaps the prior five installments before diving into its own topic: implementing an interactive map. The series as a whole is built around a single example database, 'v65Trace,' which auto-traces bitmapped (BMP) images into 4D Draw vector graphics and then builds several interactive interfaces on top of that data — Part I covered vector-graphic creation and image-format validation groundwork, Part III built a pixel-inspection interface letting users click a displayed BMP picture to see per-pixel color information, Part IV built an interactive color-palette diagram with clickable, highlightable color swatches synced to picture clicks, and Part V added a 4D Chart-based 3-D graph of pixel color value distributions. This sixth part builds on all of that groundwork to implement a genuinely interactive map interface, applying the same object hit-testing, cursor-highlighting, and picture/vector-area coordination techniques developed across the series to a map-specific use case. The featured technology throughout is 4D Draw, one of the 4D Productivity Modules, used here to build rich, click-interactive vector graphic interfaces well before modern web-based mapping or charting libraries existed as an alternative within the 4D ecosystem.

## Featured Technology
- 4D Draw
- v65Trace example database
- BMP picture pixel-color analysis

## Historical Context
This is the sixth installment of a lengthy series on building interactive vector-graphic interfaces with 4D Draw, here applying the accumulated techniques from Parts I-V to implement an interactive map. 4D Draw, part of the 4D Productivity Modules alongside 4D Calc and 4D Write, was discontinued long ago; modern 4D applications requiring interactive graphics or mapping rely on entirely different tools (web-based mapping components, picture/area objects, or third-party plug-ins), so the specific 4D Draw techniques described are obsolete, though the underlying UI-interaction concepts (hit-testing clicks against graphic objects, highlighting selections) remain generally instructive.

## What's Changed Since
- 4D Draw and the broader 4D Productivity Modules suite (4D Calc, 4D Draw, 4D Write, superseded partly by 4D Write Pro) have been discontinued or replaced by modern equivalents
- Interactive mapping and graphic interfaces in current 4D applications are typically built with web technologies or modern 4D picture/form objects rather than 4D Draw vector areas

