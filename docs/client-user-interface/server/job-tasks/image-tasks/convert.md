---
sidebar_label: 'Task Image - Convert'
hide_title: 'true'
---

## Task Image - Convert

The Image convert Task converts images to another format: BMP, JPEG, GIF, PNG or TIFF.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same folder but use file mask" and _File mask_ is `*`. The converted image is then saved under the source file name in the source folder, so it replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### File filter tab

The ***File filter*** tab selects the images to convert; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image convert Task, Destination tab, with Convert to format, the Save to options, Folder and File mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Convert.png)

- _Convert to format_: "BMP", "JPEG", "GIF", "PNG" (default) or "TIFF"
- _Jpeg quality_: the quality of the JPEG file. Shown only when _Convert to format_ is "JPEG". When the field is empty or not a number, the default quality is used
- _Save to.._: where the Task saves the result
  - "Same file": overwrites the source file
  - "Same folder but use file mask" (default): saves in the folder set in the File filter, with the name that _File mask_ gives. A file that the filter found in a subfolder is also saved in that folder, not in the subfolder
  - "Different folder and use file mask": saves in _Folder_, with the name that _File mask_ gives
- _Folder_: the folder to save to. Available with "Different folder and use file mask"
- _File mask_: the name of the saved file. The default, `*`, keeps the source file name. Available with both file mask options

The Task does not change the file extension. With `*` as _File mask_, or with "Same file", the converted image keeps the name and extension of the source file. To give the file the extension of the new format, enter a file mask such as `*.jpg`.

### Output and errors

The Task processes every file that the File filter finds. For each saved image, the path of the saved file is added to the Task output. When several files are processed, the paths follow one another with no separator.

When the File filter finds no file, the Task fails with a file-not-found error. When an image cannot be processed, the Task fails and does not process the remaining files; images saved before the failure are kept. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).
