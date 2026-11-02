---
sidebar_label: 'Task Image - Join'
hide_title: 'true'
---

## Task Image - Join

The Image join Task joins two images, side by side horizontally or top to bottom vertically, and saves the result as a new image.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

Images can fail to join when their properties differ too much.

### File filter for file 1 tab

Selects the first image; see [Job Tasks - File filter](../../job-tasks-file-filter). The Task uses only the first file that the filter finds.

### File filter for file 2 tab

Selects the second image, in the same way. The Task uses only the first file that the filter finds.

### Destination tab

![Image join Task, Destination tab, with Join mode, Destination folder, File name and Overwrite options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20join.png)

- _Join mode_: "Horizontal" (default) or "Vertical"
- _Destination folder_: the folder to save the joined image in. Accepts Variables
- _Use same folder as first file_: saves in the folder of the first image instead of _Destination folder_
- _File name_: the file name of the joined image. Accepts Variables
- _Use same file name as first file_: uses the file name of the first image instead of _File name_
- _Overwrite options_: what to do when a file with the destination name already exists
  - "Overwrite - always if existing" (default)
  - "Overwrite - if newer"
  - "Overwrite - if destination size is", with a size condition: "Same", "Smaller" (default), "Larger", "Smaller or larger" or "Different"
  - "Append if destination is smaller - otherwise overwrite"
  - "Append if destination is smaller - otherwise overwrite if newer"
  - "Append if destination is smaller - otherwise skip"
  - "Do not overwrite if existing"

:::warning

The overwrite options do not protect an existing file. Only "Overwrite - always if existing", "Append if destination is smaller - otherwise overwrite" and "Overwrite - if destination size is" with "Same" delete the existing file before the join. With every other option the Task does not delete the existing file before the join; whether the join then replaces it or fails is not controlled by the overwrite option. No option appends. To keep an existing file, use a destination name that is not in use, for example with a Variable in _File name_.

:::

:::warning

Do not select both _Use same folder as first file_ and _Use same file name as first file_. The destination is then the first image itself: with "Overwrite - always if existing", the Task deletes the first image before it joins the images, so the join fails and the first image is lost.

:::

### Output and errors

When the join succeeds, the path of the joined image is the Task output.

When either File filter finds no file, the Task fails with a file-not-found error. When the images cannot be joined, the Task fails. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).
