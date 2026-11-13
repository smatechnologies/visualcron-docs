---
sidebar_label: 'Folder'
hide_title: 'true'
---

## Robot Task Activities - Folder

The Folder activities create, copy, move, empty, delete, list and wait for folders.

![The Folder category in the activity list, from Copy Folder to Wait For Folder](../../../../../../../static/img/RPA/Robot%20Tasks/Folder/Folder.png)

The activities run in the desktop session of the Robot Task, as the user logged on to that session, so that user needs permission on every path used, including permission to delete for _Delete Folder_ and _Empty Folder_. Variables are resolved in every path field.

Several activities write their outcome to a _Result_ property, in the Properties pane under **Output**. The value is an RPA variable that exists while the Robot Task runs, used in later activities as `{RPA(VariableName)}`.

---

### Copy Folder

Copies the contents of a folder, with all its subfolders and files, into a destination folder. Create the destination folder first if the source has no subfolders; otherwise the copy fails.

- _Source folder_: the full path of the folder to copy
- _Destination folder_: the full path of the folder the contents are copied into

:::warning

Files that already exist in the destination are replaced without warning.

:::

---

### Create Folder

Creates a folder, including any missing parent folders. A folder that already exists is not an error.

- _Folder path_: the full path of the folder

---

### Delete Folder

Deletes a folder.

- _Folder path_: the full path of the folder
- _Recursive_: checked by default, which deletes the folder with all its subfolders and files; when cleared, the activity fails if the folder is not empty

:::warning

Deleted files and folders are not moved to the Recycle Bin and cannot be restored. Because _Recursive_ is checked by default, a new Delete Folder removes everything below the folder.

:::

---

### Empty Folder

Deletes all files and subfolders in a folder, and leaves the folder itself in place.

- _Folder path_: the full path of the folder

:::warning

Deleted files and subfolders are not moved to the Recycle Bin and cannot be restored.

:::

---

### Folder Exists

Checks whether a folder exists and writes the result to the _Result_ variable: "True" if the folder exists, and "False" if it does not.

- _Folder path_: the full path of the folder to check
- _Result_: in the Properties pane, the name of the variable the result is written to

#### Example: branching on whether a folder exists

Setting _Result_ to `Exists` makes the outcome available as `{RPA(Exists)}`.

To check whether the folder `C:\Testing\RPA\FolderExists` is present, then delete it if it is and create it if it is not:

1. Add a _Folder Exists_ activity with _Folder path_ set to `C:\Testing\RPA\FolderExists` and _Result_ set to `Exists`.
2. Add an [If (simple)](conditions) activity after it, with _Left operand_ `{RPA(Exists)}`, _Operator_ "Equal", _Right operand_ "True" and _Type_ "String".
3. In the _Then_ body, add a _Delete Folder_ activity with the same folder path and _Recursive_ checked.
4. In the _Else_ body, add a _Create Folder_ activity with the same folder path.

The result is written as the text "True" or "False", so a "String" comparison with "True" works.

---

### Move Folder

Moves a folder and its contents to a new location. The move fails if the destination folder already exists.

- _Source folder_: the full path of the folder to move
- _Destination folder_: the full path the folder is moved to

---

### Open Folder

Opens a folder in File Explorer.

- _Folder path_: the full path of the folder

---

### Rename Folder

Gives a folder a new name in the same parent folder.

- _Folder path_: the full path of the folder
- _New name_: the new folder name

---

### Touch Folder

Creates the folder if it does not exist, and sets its last access time to the current time. The last write time is not changed.

- _Folder path_: the full path of the folder

---

### Get Folders

Finds the folders that match a folder filter and runs the _Body_ once for each one, with the full folder name. It works like a For Each loop over the matched folders.

- _Folder path variable name_: the name of the variable the full folder name is written to on each iteration
- _Folder filter_: opens the folder filter window, used to choose which folders match; see [Folder filter](../../../../job-tasks-folder-filter)
- _Body_: the activities that run for each matched folder

Use `{RPA(FolderName)}` in the child activities to get the current folder name, with the variable name you set in place of `FolderName`.

---

### Wait For Folder

Waits for a folder to exist and writes the result to the _Result_ variable: "True" if the folder appears before the time runs out, and "False" if it does not.

- _Folder path_: the full path of the folder to wait for
- _Wait for folder_: how long to wait, in milliseconds, "10000" by default
- _Throw exception_: when checked, which is the default, the activity fails if the folder does not appear in time
- _Result_: in the Properties pane, the name of the variable the result is written to

:::warning

With _Throw exception_ cleared, a folder that never appears is only written to the output, and the sequence continues. Unless a later activity tests the _Result_ variable, the Task reports success.

:::

---

### Tips

- _Create Folder_ and _Touch Folder_ both create a missing folder and leave an existing one in place, so neither needs a _Folder Exists_ check first
- Use _Empty Folder_ rather than _Delete Folder_ followed by _Create Folder_ when you clear a working folder. It keeps the folder's permissions and any shares that point at it
- Leave _Throw exception_ cleared on Wait For Folder and test the _Result_ variable with an [If (simple)](conditions) activity when a missing folder is a case you want to handle rather than an error
- Because the _Result_ value is the text "True" or "False", set the comparison _Type_ to "String" in the If activity that reads it
