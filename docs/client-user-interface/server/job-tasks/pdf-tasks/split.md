---
sidebar_label: 'Task PDF - Split'
hide_title: 'true'
---

## Task PDF - Split

The PDF - Split Task splits PDF files into one file per page, into two halves, at a page, or into odd and even pages.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Split: Main settings tab

![Main settings tab of the Split Task, with the Split type list, the Page number and Page name format boxes, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Split.png)

- _Split type_ (_Split ..._ group): how the document is split; the examples are for a file named `report.pdf`
  - "Page" (the default): one file for each page, named by _Page name format_, for example `report - Page 1.pdf`
  - "Half": two files, split at about the middle of the document, for example `report 1-4.pdf` and `report 5-8.pdf`
  - "At": two files, split after the page in _Page number_, for example `report 1-2.pdf` and `report 3-6.pdf`
  - "EvenOdd": `report odd pages.pdf` and `report even pages.pdf`
- _Page number_: the last page of the first file; used with "At". The default is "2"
- _Page name format_: the text added to the file name for each page; used with "Page"

  `{#}` is replaced by the page number. The default is ` - Page {#}`. When the format has no `{#}`, the number is added at the end.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  Only those pages go into the new files. With "Half", the split is at the middle of the selected pages.

### File filter tab

The ***File filter*** tab selects the PDF files to split; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Split Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Split%20Destination.png)

The new file names are built from the destination path set here, with the split text added before the extension. The source file is not changed.

- _Same file_ (_Save to.._ group): saves the new files in the source file's folder, named after the source file
- _Same folder but use file mask_: saves the new files in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the new files in _Folder_, named by _File mask_; the folder is created if it does not exist
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the base name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

A file that already has a new name is replaced without a prompt.

:::

### Output and errors

The Task output contains "Success" for each file it splits.
