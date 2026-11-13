---
sidebar_label: 'Task PDF - Concatenate'
hide_title: 'true'
---

## Task PDF - Concatenate

The PDF - Concatenate Task merges the PDF files that one or more File filters select into one PDF file.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### PDF files tab

![PDF files tab of the Concatenate Task, with the Add, Edit, Clone, Delete and Order toolbar and the Order, Source folder and File mask columns](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Concatenate%20PDF%20files.png)

The ***PDF files*** tab lists the File filters that select the files to merge; see [File Filter](../../job-tasks-file-filter). Click _Add_ to add a filter, and use _Edit_, _Clone_, _Delete_ and _Order_ to manage the list. The files are added in the order of the list, and the first file found is the start of the merged document. If a filter has a Credential, the Task uses it while it reads that filter's files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Concatenate Task, with the Destination Credential, Destination folder, File name and Overwrite options settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Concatenate%20Destination.png)

- _Destination Credential_: the Credential used to write the merged file, for a destination that needs authentication; see [Global - Credentials](../../global-credentials)
- _Destination folder_: the folder for the merged file; click the folder button to browse
- _Use same folder as first file_: saves the merged file in the folder of the first file found, instead of _Destination folder_
- _File name_: the name of the merged file
- _Use same file name as first file_: gives the merged file the name of the first file found, instead of _File name_

  With both _Use same_ options checked, the merged file has the path of the first source file, so _Overwrite options_ decide whether that file is replaced.

- _Overwrite options_: what happens when a file with the merged file's name already exists
  - "Overwrite - always if existing" (the default): replaces the file
  - "Do not overwrite if existing": keeps the file and does not save the merged file
  - "Overwrite - if destination size is": saves the merged file only when the size choice next to it is "Same"; with any other size choice, nothing is saved
  - "Append if destination is smaller - otherwise overwrite": replaces the file; nothing is appended
  - "Append if destination is smaller - otherwise skip": keeps the file and does not save the merged file
  - "Overwrite - if newer" and "Append if destination is smaller - otherwise overwrite if newer": compare the existing file with itself, not with the source files

:::warning

Apart from "Overwrite - always if existing" and "Do not overwrite if existing", the overwrite options check only the existing destination file, never the merged document. When no file is saved, including with "Do not overwrite if existing" when the destination file exists, the Task output is empty, and the Task reports success. Use "Do not overwrite if existing", or "Overwrite - always if existing" when the merged file must replace the existing one; see the next warning.

:::

:::warning

With "Overwrite - always if existing" or "Append if destination is smaller - otherwise overwrite", the Task deletes the existing file before it saves the merged file. When no file matches the filters, or the save fails, the existing file is deleted, nothing replaces it, and the Task fails.

:::

### Output and errors

The Task output lists the path of the merged file. When no file matches the filters, the Task fails; see the warning above about the existing destination file.
