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

**Convert > Destination sub tab, converting to PDF from TXT**

When *To PDF->From* is set to TXT, three extra group boxes appear on the Destination tab: Page margins, Font details, and Page orientation and Line fit.

![](pathname:///img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert%20Destination%20TXT.png)

**Page margins**

Left, Right, Top, and Bottom margin around the page content, in points. Leave a field blank (or enter a value that can't be parsed as a number) and VisualCron falls back to 50pt on that side. This group also appears when converting to PDF from IMAGE.

**Font details**

* _Font_ - the installed system font used to render the text. Leave blank to use Courier New.
* _Font size_ - point size for the text. Leave blank to use 12pt.
* _Font style_ - Regular, Bold, Italic, or Bold Italic.

**Page orientation and Line fit**

* _Orientation_ - Auto, Portrait, or Landscape. Auto uses Landscape when the text content is wider than it is tall, otherwise Portrait.
* _Line Fit_ - when checked, scales the text horizontally so it fits within the page margins.

**Convert > Destination sub tab, Output paper size**

An **Output paper size** group lets you fix the page dimensions of the converted PDF instead of relying on the auto-derived size.

* Converting to PDF: available for every *To PDF->From* format except SVG.
* Converting from PDF: available when *From PDF->To* is set to DOC, PPT, or XPS.

**Paper size**

Default (auto), A3, A4, A5, Letter, Legal, Tabloid, or Custom. Default (auto) reproduces the size VisualCron would have produced before this option existed.

**Width / Height / Unit**

Shown only when *Paper size* is set to Custom. Enter the page width and height and choose the unit (mm, in, or pt). Both values must be greater than 0 and, once converted to points, no larger than 14400pt (the maximum page dimension VisualCron supports) - VisualCron blocks the task if either is out of range.
