---
sidebar_label: 'File'
hide_title: 'true'
---

## Robot Task Activities - File

The File activities write, read, copy, move, delete, archive and wait for files.

![The File category in the activity list, from Write File to Empty Recycle Bin](../../../../../../../static/img/RPA/Robot%20Tasks/File/File.png)

The activities run in the desktop session of the Robot Task, as the user logged on to that session, so that user needs permission on every path used. Variables are resolved in every path and text field.

Several activities write their outcome to a _Result_ property, in the Properties pane under **Output**. The value is an RPA variable that exists while the Robot Task runs, used in later activities as `{RPA(VariableName)}`.

---

### Write File

Creates the file, writes the text to it, and closes it.

![The Write File activity, with the File path and Text fields](../../../../../../../static/img/RPA/Robot%20Tasks/File/Write.png)

- _File path_: the full path of the file
- _Text_: the text written to the file

:::warning

If the file already exists, it is replaced without warning.

:::

---

### Append File

Opens the file, adds the text to its end, and closes it. If the file does not exist, it is created.

- _File path_: the full path of the file
- _Text_: the text added to the file

No line break is added. To put each entry on its own line, end the text with a line break.

Use Append File rather than Write File when you log progress inside a loop, so that each iteration adds to the log instead of replacing it.

---

### Delete File

Deletes the file. A file that does not exist is not an error.

- _File path_: the full path of the file

:::warning

The file is deleted permanently. It is not moved to the Recycle Bin and cannot be restored.

:::

---

### Copy File

Copies a file to a new file. The copy fails if the destination file already exists.

![The Copy File activity, with the Source file path and Destination file path fields](../../../../../../../static/img/RPA/Robot%20Tasks/File/Copy.png)

- _Source file path_: the full path of the file to copy
- _Destination file path_: the full path of the new file

---

### Move File

Moves a file to a new location, optionally with a new name. The move fails if the destination file already exists.

- _Source file path_: the full path of the file to move
- _Destination file path_: the full path, including the file name, to move it to

---

### File Exists

Checks whether a file exists and writes the result to the _Result_ variable: "True" if the file exists, and "False" if it does not or the path is a folder.

![The File Exists activity, with the File path field](../../../../../../../static/img/RPA/Robot%20Tasks/File/Exists.png)

- _File path_: the full path of the file to check
- _Result_: in the Properties pane, the name of the variable the result is written to

Read the result in a later activity with `{RPA(VariableName)}`.

---

### Download File

Downloads a file from a URL.

![The Download File activity, with the Url address and File path fields](../../../../../../../static/img/RPA/Robot%20Tasks/File/Download.png)

- _Url address_: the URL to download from
- _File path_: the full path to save the file to; an existing file is replaced

---

### Read File

Reads the whole content of a text file and writes it to the _Result_ variable.

- _File path_: the full path of the file
- _Result_: in the Properties pane, the name of the variable the content is written to

Read the content in a later activity with `{RPA(VariableName)}`.

---

### Open File

Opens the file with the application registered for its file type, the same as double-clicking it in File Explorer.

- _File path_: the full path of the file

---

### Rename File

Gives a file a new name in the same folder.

- _File path_: the full path of the file
- _New name_: the new file name

---

### Touch File

Creates the file if it does not exist, and sets its last access time to the current time. The last write time is not changed.

- _File path_: the full path of the file

---

### Get Files

Finds the files that match a file filter and runs the _Body_ once for each one, with the full file name. It works like a For Each loop over the matched files.

![The Get Files activity, with the File path variable name field, the File filter button and the Body](../../../../../../../static/img/RPA/Robot%20Tasks/File/Get.png)

- _File path variable name_: the name of the variable the full file name is written to on each iteration
- _File filter_: opens the file filter window, used to choose which files match; see [File filter](../../../../job-tasks-file-filter)
- _Body_: the activities that run for each matched file

Use `{RPA(FileName)}` in the child activities to get the current file name, with the variable name you set in place of `FileName`.

![A Get Files activity whose Body contains an Open File activity that uses the file name variable](../../../../../../../static/img/RPA/Robot%20Tasks/File/Get%20Settings.png)

For example, a _Get Files_ activity whose _Body_ contains an _Open File_ activity with the _File path_ `{RPA(FileName)}` opens every matched file in turn.

---

### Archive - Compress

Creates a compressed archive of the files that match a file filter.

![The Archive - Compress activity, with the File filter button and the Compressed file path field](../../../../../../../static/img/RPA/Robot%20Tasks/File/Archive%20C.png)

- _File filter_: opens the file filter window, used to choose the files to compress; see [File filter](../../../../job-tasks-file-filter)
- _Compressed file path_: the path of the archive file to create

The archive is always written in 7z format, whatever the file extension.

:::warning

An existing file at _Compressed file path_ is replaced without warning.

:::

---

### Archive - Extract

Extracts all files from an archive.

![The Archive - Extract activity, with the Source file path and Destination folder path fields](../../../../../../../static/img/RPA/Robot%20Tasks/File/Archive%20E.png)

- _Source file path_: the archive file to extract
- _Destination folder path_: the folder the files are extracted to

:::warning

Files that already exist in _Destination folder path_ are replaced without warning.

:::

---

### Wait For File

Waits for a file to exist and writes the result to the _Result_ variable: "True" if the file appears before the time runs out, and "False" if it does not.

![The Wait For File activity, with the File path and Wait for file fields and the Throw exception check box](../../../../../../../static/img/RPA/Robot%20Tasks/File/Wait.png)

- _File path_: the full path of the file to wait for
- _Wait for file_: how long to wait, in milliseconds, "10000" by default
- _Throw exception_: when checked, which is the default, the activity fails if the file does not appear in time
- _Result_: in the Properties pane, the name of the variable the result is written to

:::warning

With _Throw exception_ cleared, a file that never appears is only written to the output, and the sequence continues. Unless a later activity tests the _Result_ variable, the Task reports success.

:::

---

### Create Shortcut

Creates a shortcut (`.lnk`) file. If the destination name does not end in `.lnk`, the extension is added.

- _Source file path_: the file the shortcut points to
- _Destination file path_: the path of the shortcut file

The Properties pane has further shortcut settings under **Additional**, such as the arguments, working directory, icon location and window style.

---

### Empty Recycle Bin

Empties the Recycle Bin, without asking for confirmation.

:::warning

This permanently deletes everything in the Recycle Bin on every drive, for the user the Robot Task runs as. Deleted files cannot be restored afterward. If emptying fails, the activity does not report it.

:::

---

### Tips

- Use _Wait For File_ rather than a fixed [Wait](other) activity when another system produces the file. It continues as soon as the file appears, instead of always waiting the full time
- Leave _Throw exception_ cleared on Wait For File and test the _Result_ variable with an [If (simple)](conditions) activity when a missing file is a case you want to handle rather than an error
- _Copy File_ and _Move File_ do not overwrite. If the destination may already exist, use _Delete File_ first, or check with _File Exists_ and branch on the result
- Use _Append File_ for progress logs inside a loop. _Write File_ replaces the file, so each iteration would discard the earlier entries
- Combine _File Exists_ with an [If (simple)](conditions) activity to make a Task safe to run again, for example by skipping records whose output file has already been produced
