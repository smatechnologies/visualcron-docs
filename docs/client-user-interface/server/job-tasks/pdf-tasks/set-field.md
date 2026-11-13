---
sidebar_label: 'Task PDF - Set Field'
hide_title: 'true'
---

## Task PDF - Set Field

The PDF - Set field(s) Task sets the values of form fields in PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Set field(s): Main settings tab

![Main settings tab of the Set field(s) Task, with the Field values grid, the Get field names button, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Set%20Fields.png)

- _Name_ and _Value_ (_Field values ..._ grid): the name of each field to set, and its value

  Click _Get field names_ to load the field names of the files that the File filter matches. A name is not matched with wildcards. Variables are supported in both columns. To delete a field, select its row and press Delete.

  The value depends on the field type:

  - Check box: "1" or `true` checks it, "0" or `false` clears it
  - List box, combo box or radio button: the text of an item, or its index
  - Text field: the text; text longer than the field's maximum length is cut to that length
  - Image field: the path of an image file
  - Barcode field: the barcode value

  Push button and signature fields are not set.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  Only the fields on those pages are set.

:::warning

A field name that is not in the document, a read-only field, or a value that does not fit the field type is skipped, and the Task reports success.

:::

### File filter tab

The ***File filter*** tab selects the PDF files to change; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Set field(s) Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Set%20Fields%20Destination.png)

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

The Task output contains "Success" for each file it saves. For a file without fields, the output is "The document has no fields" and the file is not saved.
