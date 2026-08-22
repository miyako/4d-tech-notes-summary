# Tech Note: Understanding the 4D Data File

## Overview
- **Technical Note 00-49**
- **Author:** Unknown / not specified
- **Published:** October 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note gives 4D developers a conceptual overview of the two core files that make up any 4D application: the structure file, which holds the database's schema, forms, and methods, and the data file, which holds the actual records. Its proposition is that understanding what's inside the data file specifically — including how it can be divided into multiple data segments — helps developers manage deployed applications more effectively, spot early signs of data integrity problems, and recover more successfully when something does go wrong (for example, after a crash or disk issue). This kind of foundational architectural knowledge was especially valuable for the era's 4D administrators, who often had to manage backup/restore and file-size constraints without the tooling safety nets available today. The featured technology is 4D's core data file format and segment structure rather than any language command or plug-in. Because only the teaser abstract for this note survives (its original download was an old Windows self-extracting installer that could not be extracted in this environment), the technical depth of the actual data-segment explanation could not be recovered here.

## Featured Technology
- 4D data file (.4DD)
- 4D structure file
- Data segments

## Historical Context
This note explains the classic two-file architecture of a 4D database (structure file plus data file) and the internal segment structure of the data file, information that was practically important in 2000 given the smaller disk/file-size limits and single-segment-at-a-time addressing constraints of that era. The basic structure-file/data-file split is still how classic (Design Mode) 4D databases work today, but concerns about multi-segment data files stemming from older operating-system file-size limitations are largely moot on modern systems, and 4D's newer Project Mode changes how the structure side of this picture is stored and versioned.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- Modern operating systems and file systems have eliminated most of the practical file-size constraints that historically motivated splitting 4D data files into multiple segments
- 4D Project Mode (v17+) changes how the structure side of a database is stored (as text files) even though the core structure-file/data-file conceptual split for data still applies to classic databases

