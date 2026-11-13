---
sidebar_label: 'Task PDF - Replace Text'
hide_title: 'true'
---

## Task PDF - Replace Text

The PDF - Replace text Task finds a text or a regular expression in PDF files and replaces each match with another text.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Replace text: Main settings tab

![Main settings tab of the Replace text Task, with the Find and Replace boxes, the Is regular expression check box, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Replace%20text%20settings.png)

- _Find_ (_Replace ..._ group): the text to find, without quotation marks; required

  Variables are supported.

- _Is regular expression_: treats _Find_ as a regular expression
- _Replace_: the text that replaces each match

  Variables are supported.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  A page number larger than the page count raises an error.

### File filter tab

The ***File filter*** tab selects the PDF files to change; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Replace text Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Replace%20text%20destination.png)

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

The Task output contains "Success" for each file it saves. The file is saved even when nothing matches.
