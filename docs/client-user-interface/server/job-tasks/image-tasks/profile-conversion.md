---
sidebar_label: 'Task Image - Profile Conversion'
hide_title: 'true'
---

## Task Image - Profile Conversion

The Image profile conversion Task converts images from an input color profile to an output color profile.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

By default, _Save to.._ is "Same folder but use file mask" and _File mask_ is `*`. The converted image is then saved under the source file name in the source folder, so it replaces the original image. To keep the original, select "Different folder and use file mask" and enter another folder.

:::

### File filter tab

![Image profile conversion Task, File filter tab, with Credentials, Folder, Include file mask and the exclusion settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Settings.png)

The ***File filter*** tab selects the images to convert; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image profile conversion Task, Destination tab, with the profile fields, the Save to options, Folder and File mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Destination.png)

The profile fields are in the _Profile conversation parameters:_ group. They do not accept Variables.

- _Input profile file_: the path of the ICC color profile of the input image. Click the file button to browse for a profile file
- _Output profile file_: the path of the ICC color profile to apply to the output image. The field is required. Click the file button to browse for a profile file
- _Filter string for delete profile(s)_: a filter string for the embedded profiles to remove from the image during the conversion

![Image profile conversion Task, File filter tab, the same screenshot as the one shown for the File filter tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Settings.png)

- _Save to.._: where the Task saves the result
  - "Same file": overwrites the source file
  - "Same folder but use file mask" (default): saves in the folder set in the File filter, with the name that _File mask_ gives. A file that the filter found in a subfolder is also saved in that folder, not in the subfolder
  - "Different folder and use file mask": saves in _Folder_, with the name that _File mask_ gives
- _Folder_: the folder to save to. Available with "Different folder and use file mask"
- _File mask_: the name of the saved file. The default, `*`, keeps the source file name. Available with both file mask options

### Output and errors

The Task processes every file that the File filter finds. For each saved image, the path of the saved file is added to the Task output. When several files are processed, the paths follow one another with no separator.

When the File filter finds no file, the Task fails with a file-not-found error. When an image cannot be processed, the Task fails and does not process the remaining files; images saved before the failure are kept. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).
