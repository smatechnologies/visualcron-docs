---
sidebar_label: 'Task PDF - Convert'
hide_title: 'true'
---

## Task PDF - Convert

The PDF - Convert Task can convert between different file formats and the PDF format.
 
**Convert > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert.png)

**To PDF->From**

Currently this Task can convert ***to*** PDF from the following formats;
 
* XPS
* PCL
* SVG
* EPUB
* MHT
* HTML
* TeX
* TXT
* CGM
* XML
* IMAGE (various formats)
 
**From PDF->To**

Currently this Task can convert ***from*** PDF to the following formats;
 
* PDF (various formats)
* HTML
* DOC
* XLS
* PPT
* XPS
* XML
* TeX
* TXT
* SVG
* EPUB
* IMAGE (various formats)
 
**Password for file(s)**

If any of the specified PDF files contains a password it should be entered here
 
**Page range**

The pages that should be converted. Specify a range like 2-4 or specific pages 1,3,5-6.
 
**Convert > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter) to filter out the files that should be processed in this Task.
 
**Convert > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert%20Destination.png)

**Save to**

Selects where the converted file is written. Available options:

* _Save to same file_ - write to the same folder as the source, using the original name
* _Same folder with file mask_ - keep the original folder, but save under a different name (set the *File mask* below)
* _Different folder with file mask_ - save under a different name in a different folder (set both *Folder* and *File mask* below)

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the output file. Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
