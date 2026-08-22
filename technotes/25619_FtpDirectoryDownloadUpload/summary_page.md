# Tech Note 03-2: FTP directory Download and Upload

**Author:** Jamras Komoncharoensiri, Technical Support Engineer
**Published:** January 31, 2003 | **Product/Version:** 4D Internet Commands v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25619
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_01-05_(JAN)/03-02_ftp_download_upload.exe

## Overview
TN 03-2 shows how to build a recursive FTP directory download/upload routine on top of the 4D Internet Commands plug-in, which in 2003 only natively supported single-file transfers, by enumerating the remote tree into arrays and replaying it locally (or vice versa for uploads).

## Key Points
- 4D Internet Commands (as of 2003) could transfer individual files over FTP but not whole directories.
- Strategy: enumerate target FTP path, choose a local destination, recursively list all remote sub-directories and files into arrays, recreate the directory structure locally, then download every file.
- Walks through a concrete example directory tree to illustrate how the directory/file path arrays are built.
- Upload direction follows the mirror-image process of the download strategy.

## Featured Technology
- 4D Internet Commands
- FTP
- Recursive directory traversal

## Historical Context
4D Internet Commands (4D Internet Commands, aka 4D IC) was 4D's classic plug-in for TCP/IP, FTP, SMTP/POP/IMAP and other Internet protocol access in the pre-built-in-networking-command era of the 4D language.

## Historical Commentary
**Status:** Superseded

The 4D Internet Commands plug-in and its FTP command set have long since been folded into 4D's core language as built-in FTP/SFTP commands with richer directory-handling support, so the specific workaround engineered in this note is no longer necessary for FTP directory transfers in current 4D versions. The general recursive-enumeration technique for mirroring a remote tree, however, remains a conceptually valid pattern for any tree-copy problem.
