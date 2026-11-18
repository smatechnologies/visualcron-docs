---
sidebar_label: 'Task Image - Get EXIF Data'
hide_title: 'true'
---

## Task Image - Get EXIF Data

The Image get EXIF data Task reads the EXIF tags that you select from images and writes their values to the Task output.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### File filter tab

The ***File filter*** tab selects the images to read; see [Job Tasks - File filter](../../job-tasks-file-filter).

### Destination tab

![Image get EXIF data Task, Destination tab, with the Selected parameters grid and its Group and Tag columns](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20get%20EXIF%20data.png)

_Selected parameters_ lists the tags to read. Each row has a _Group_ (an IFD directory) and a _Tag_ in that group.

1. Click the empty row at the bottom of the grid.
2. Select the _Group_.
3. Select the _Tag_.

If a tag is not in the list, enter its number instead. To delete a row, right-click it and click _Delete_.

### Output tab

The Task window has an extra ***Output*** tab for this Task, with the _Output settings_:

- _Include tag name_: writes the tag before each value. The tag is written as its number in four hexadecimal digits, or as its name when _Verbose description_ is selected
- _Tag value separator_: the separator between the tag and its value. Default: "Tab"
- _Text qualifier_: the character written around each value. It is used only when _Verbose description_ is selected. Empty by default
- _Tags separator_: the separator written after each value. Default: "CrLf"
- _Files separator_: the separator written between the results of two files. Default: "CrLf"
- _Add file path into output_: starts the result of each file with the file path, followed by the tags separator
- _Verbose description_: writes the tag name instead of the tag number, and the description of each value instead of the raw value
- _Include group name_: writes the group in square brackets, followed by a colon, before each value, for example `[GPS]:`

### Output and errors

The Task reads every file that the File filter finds and writes the values to the Task output.

When the File filter finds no file, the Task fails with a file-not-found error. When a file cannot be read, the Task fails and does not read the remaining files. To change how the Task responds to these errors, see [Task - On error](../../task-on-error).
