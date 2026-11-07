---
sidebar_label: 'Task Image - Resize'
hide_title: 'true'
---

## Task Image - Resize

The Image resize Task resizes existing images to a size in pixels, to a percentage of the original size, to a file size, or to a new resolution.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same folder but use file mask" and _File mask_ is `*`. The resized image is then saved under the source file name in the source folder, so it replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### File filter tab

The ***File filter*** tab selects the images to resize; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image resize Task, Destination tab, with the Resize to options and their fields, the Save to options, Folder and File mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Resize.png)

- _Resize to ..._: the resize mode. Only the selected one is used
  - "Dimensions" (default): resizes to _Width_ and _Height_
  - "Percentage": resizes to the percentage in _Percent_
  - "File size": resizes to reach the file size in _File size (kB)_
  - "DPI": changes the resolution to _New DPI_
- _Width_: the target width in pixels. Available with "Dimensions". Default: "0"
- _Height_: the target height in pixels. Available with "Dimensions". Default: "0"
- _Percent_: the percentage of the original size. Available with "Percentage". Default: "100"
- _File size (kB)_: the target file size in kilobytes. Available with "File size". Default: "1000"
- _New DPI_: the target resolution in dots per inch. Available with "DPI". Default: "96"
- _Resample_: resamples the image, so that the number of pixels changes, instead of changing only the resolution setting of the file. Available with "DPI". Unchecked by default
- _Save to.._: where the Task saves the result
  - "Same file": overwrites the source file
  - "Same folder but use file mask" (default): saves in the folder set in the File filter, with the name that _File mask_ gives. A file that the filter found in a subfolder is also saved in that folder, not in the subfolder
  - "Different folder and use file mask": saves in _Folder_, with the name that _File mask_ gives
- _Folder_: the folder to save to. Available with "Different folder and use file mask"
- _File mask_: the name of the saved file. The default, `*`, keeps the source file name. Available with both file mask options

### Output and errors

The Task processes every file that the File filter finds. For each saved image, the path of the saved file is added to the Task output. When several files are processed, the paths follow one another with no separator.

When the File filter finds no file, the Task fails with a file-not-found error. When an image cannot be processed, the Task fails and does not process the remaining files; images saved before the failure are kept. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).

The value fields accept Variables. _Width_ and _Height_ must be whole numbers; a value that cannot be read as a number is read as "0".
