---
sidebar_label: 'Task Image - Crop'
hide_title: 'true'
---

## Task Image - Crop

The Image crop Task cuts an area out of existing images and removes the rest.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same folder but use file mask" and _File mask_ is `*`. The cropped image is then saved under the source file name in the source folder, so it replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### File filter tab

The ***File filter*** tab selects the images to crop; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image crop Task, Destination tab, with Top, Left, Width and Height, the Save to options, Folder and File mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20crop.png)

_Crop position and dimensions_:

- _Top_: the number of pixels from the top edge of the original image to where the crop starts. Default: "0"
- _Left_: the number of pixels from the left edge of the original image to where the crop starts. Default: "0"
- _Width_: the width of the cropped area in pixels. Default: "20"
- _Height_: the height of the cropped area in pixels. Default: "20"

:::info Note

The maximum values of _Top_ and _Left_ are set by the pixels of the original image. _Width_ and _Height_ apply to the image that is left after _Top_ and _Left_. When _Width_ or _Height_ is "0", the full width or height after _Left_ or _Top_ is used.

:::

- _Save to.._: where the Task saves the result
  - "Same file": overwrites the source file
  - "Same folder but use file mask" (default): saves in the folder set in the File filter, with the name that _File mask_ gives. A file that the filter found in a subfolder is also saved in that folder, not in the subfolder
  - "Different folder and use file mask": saves in _Folder_, with the name that _File mask_ gives
- _Folder_: the folder to save to. Available with "Different folder and use file mask"
- _File mask_: the name of the saved file. The default, `*`, keeps the source file name. Available with both file mask options

### Output and errors

The Task processes every file that the File filter finds. For each saved image, the path of the saved file is added to the Task output. When several files are processed, the paths follow one another with no separator.

When the File filter finds no file, the Task fails with a file-not-found error. When an image cannot be processed, the Task fails and does not process the remaining files; images saved before the failure are kept. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).

The value fields accept Variables. A value that is not a whole number is read as "0".
