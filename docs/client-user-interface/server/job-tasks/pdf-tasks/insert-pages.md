---
sidebar_label: 'Task PDF - Insert Pages'
hide_title: 'true'
---

## Task PDF - Insert Pages

The PDF - Insert page(s) Task inserts a blank page, or pages taken from another PDF file, into PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Insert page(s): Main settings tab

![Main settings tab of the Insert page(s) Task, with the Password for file(s), Page range, Extract page(s) from file and Password for extract file groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Insert%20pages%20settings.png)

- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with the pages of the extract file to insert, separated by commas, for example `2-4` or `1,3,5-6`. Used only with _Extract page(s) from file_

  An entry that is not a page number or a valid range is ignored.
- _Extract page(s) from file_: the full path of the PDF file to take pages from; click the folder button to browse

  Leave it empty to insert one blank page instead.

- _Password for extract file_: the password that opens the extract file, if it is protected

:::warning

With an extract file, the Task always takes the page numbers from the _Pages_ box, even when _All pages_ is selected. With the box empty, no page is inserted, and the Task reports success. Select _Pages_ and enter the pages to insert, for example `1-5`.

:::

### File filter tab

The ***File filter*** tab selects the PDF files to insert pages into; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Insert page(s) Task, with the Insert at box, the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Insert%20pages%20destination.png)

- _Insert at ..._: the page number at which to insert

  The first inserted page gets this number, and the existing pages from this position on follow the inserted ones. A number larger than the page count is treated as the page count. With an extract file, the pages are inserted before the last existing page at the most; they cannot be added after it. Without an extract file, one blank page is inserted, and a number equal to or larger than the page count adds it at the end. When the box is empty, "0" or not a number, the Task inserts one blank page at the start, even when an extract file is set.

- _Same file_ (_Save to.._ group): saves the changed file over the source file
- _Same folder but use file mask_: saves the changed file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the changed file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, _Same folder but use file mask_ saves every result in the File filter folder, not in the subfolder the source file came from.

### Output and errors

The Task output contains "Success" for each file it saves.
