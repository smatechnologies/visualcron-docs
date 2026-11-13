---
sidebar_label: 'Task Image - Overlay'
hide_title: 'true'
---

## Task Image - Overlay

The Image overlay Task places an image or a text over existing images.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same file", so the result replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### Image overlay: Main settings tab

![Image overlay Task, Main settings tab, with Overlay type, Relative position, Top, Left and the X and Y margins](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20overlay.png)

- _Overlay type_: "Image" (default) or "Text". The Client shows the ***Image*** tab or the ***Text*** tab to match
- _Relative position_ (_Alignment_ group): where the overlay is placed on the image: "Top center", "Top left", "Top right", "Center" (default), "Bottom center", "Bottom left", "Bottom right" or "Custom"
- _Top_: the vertical offset in pixels from the top edge of the image. Used only with "Custom". Default: "0"
- _Left_: the horizontal offset in pixels from the left edge of the image. Used only with "Custom". Default: "0"
- _X_ (_Margin_ group): the horizontal margin in pixels. Default: "20". Not available with "Top center", "Bottom center" and "Center"
- _Y_ (_Margin_ group): the vertical margin in pixels. Default: "20". Not available with "Center"

### FileFilter tab

The ***FileFilter*** tab selects the images to place the overlay on; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Image tab

![Image overlay Task, Image tab, with the Overlay image path field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20overlay%20image.png)

Shown when _Overlay type_ is "Image".

- _Overlay image path_: the full path and file name of the image to place over the image. Accepts Variables

### Text tab

Shown when _Overlay type_ is "Text".

- _Text string_: the text to place over the image. Accepts Variables
- _Font_: the font of the text. Default: "Tahoma"
- _Font size_: the size of the font. Default: "11". It must be a number, or the Task fails
- _Text color_: the color of the text. Default: "Black"
- _Background color_: shown in the Client, but not used when the Task runs

### Destination tab

![Image overlay Task, Destination tab, with the Save to options, Folder, File mask and Page range](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20overlay%20destination.png)

- _Save to.._: where the Task saves the result
  - "Same file" (default): overwrites the source file
  - "Same folder but use file mask": saves in the folder set in the File filter, with the name that _File mask_ gives. A file that the filter found in a subfolder is also saved in that folder, not in the subfolder
  - "Different folder and use file mask": saves in _Folder_, with the name that _File mask_ gives
- _Folder_: the folder to save to. Available with "Different folder and use file mask"
- _File mask_: the name of the saved file. The default, `*`, keeps the source file name. Available with both file mask options
- _Page range_: the pages of a multi-page image to place the overlay on
  - "All pages" (default)
  - "Pages": the page number or page range in the field below, for example `2-4`. Default: "1"

### Output and errors

The Task processes every file that the File filter finds. For each saved image, the path of the saved file is added to the Task output. When several files are processed, the paths follow one another with no separator.

When the File filter finds no file, the Task fails with a file-not-found error. When an image cannot be processed, the Task fails and does not process the remaining files; images saved before the failure are kept. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).

The value fields accept Variables. A value that is not a whole number is read as "0".
