---
sidebar_label: 'Task Image - Filter'
hide_title: 'true'
---

## Task Image - Filter

The Image filter Task applies a filter to existing images to enhance or change them.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same folder but use file mask" and _File mask_ is `*`. The filtered image is then saved under the source file name in the source folder, so it replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### File filter tab

The ***File filter*** tab selects the images to filter; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image filter Task, Destination tab, with the filter options, the Save to options, Folder and File mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Filter.png)

- _Filter to ..._: the filter to apply. Only the selected one is used
  - "Gaussian Blur": blurs the image to reduce noise and detail, by the amount in the _Gaussian Blur_ field
  - "Grayscale" (default): converts the image to grayscale
  - "Sharpness": sharpens the image, by the amount in the _Sharpness_ field
  - "Sepia Tone": applies a sepia tone
  - "Smoothness": smooths the image, by the amount in the _Smoothness_ field
  - "Invert": inverts the colors
  - "Mean Removal": applies a mean removal effect
  - "Emboss": applies an emboss effect
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
