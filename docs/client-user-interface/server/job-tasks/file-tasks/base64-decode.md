---
sidebar_label: 'Task File - Base64 - Decode'
hide_title: 'true'
---

## Task File - Base64 - Decode

The Decoding - Base 64 - decode Task decodes a file or value from Base64 format and writes the result to standard output or to a file.

**Base64 - decode > Main settings** sub tab

![Add Task dialog for the Base64 - decode Task, Main settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Base64%20-%20decode%20settings.png)

**Source**

Select File if you want to decode an existing file. When selecting File, the standard VisualCron [File filter](../../../server/job-tasks-file-filter) will be enabled. Select Value/Variable to use an existing value or Variable.

:::warning
The Task turns the decoded content into text, using the *Encoding* setting on the Task's
[Main settings](../../../server/job-tasks-task-main-settings) tab (UTF-8 by default), before it writes
the result. Use it for Base64 that contains text. If the Base64 content is a binary file, such as an
image, a PDF or a ZIP archive, the decoded result is not an exact copy of the original.
:::

**Remove non-supported characters**

Removes any characters that are not valid Base64 characters from the input before decoding.
 
**Base64 - decode > File filter** sub tab

This Task uses the standard VisualCron [File filter](../../../server/job-tasks-file-filter) to filter out files. This tab is only enabled when **File** is selected in Source.
 
**Base64 - decode > Destination** sub tab

![Base64 - decode Task, Destination sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Base64%20-%20decode%20destination.png)

**Destination**

Select **File** if you want to save the decoded content to file or select *Standard output* to pass the value to the output of the Task.
 
**Destination file**

You can choose to save files to same folder as where the original file was found by selecting Use same folder as source. If you select *Use custom destination folder* you are able to select a different destination folder for the saved file than source folder.

**Credential**

Select a Credential if you need specific permissions to write the destination file.
 
**Destination file mask**

Destination file mask is a quick way to change the file name to something else. By default it is using * which means that the same file name will be used for destination folder. If you are going to use `*` you need to use another destination folder. For example, to give decoded files a `".txt"` extension, set the mask to `"*.txt"`.

:::warning
The Task overwrites an existing destination file without asking. If *Use same folder as source* is
selected and *Destination file mask* is `"*"`, the destination is the source file itself, and it is
replaced by the result.
:::
 
**Post process mask with Variable**

This property gives you more advanced ways to change the file name. This option works best with *Destination file mask* set to `"*"`. When checking this property the new name will be stored in a temporary Variable `{NEWNAME()}`. You will be able to use this Variable for processing with other Variable functions. The default value of this field is `"{STRING(Replace|{NEWNAME()}|oldValue|newValue)}"`, which uses the String.Replace function from the Variables window. It uses the `{NEWNAME()}` as input Variable with options to set a value that you want to replace from original file name "oldValue" and the new value "newValue".
