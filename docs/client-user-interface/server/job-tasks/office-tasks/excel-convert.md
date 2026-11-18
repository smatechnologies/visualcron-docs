---
sidebar_label: 'Task Office - Excel - Convert'
hide_title: 'true'
---

## Task Office - Excel - Convert

![Excel - Convert Task window on the File filter tab, with the Location settings for the files to convert](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Convert.png)

The Excel - Convert Task converts Excel workbooks to another Excel format, or writes worksheet cells to a text file. The ***File filter*** tab selects the workbooks to convert.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***Excel - Convert*** tab, which has the sub tabs ***File filter*** and ***Convert settings***, and on the ***Output*** tab of the Task window.

### File filter tab

The ***File filter*** tab selects the workbooks to convert; see [Task - File filter](../../job-tasks-file-filter). The Credential on its ***Location*** tab is used both to read the workbooks and to write the converted files.

When no file matches the filter, the Task raises a "file not found" error, which you can handle on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

### Convert settings tab

![Convert settings tab of the Excel - Convert Task, with the Convert to.., Worksheet, Cell ranges and Save to.. groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Convert%20Settings.png)

- _Convert to.._: The format to convert to: "TextFile" (the default), "Excel2007", "Excel2007MacroEnabled", "Excel2007MacroEnabledTemplate", "Excel2007Template", "Excel97To2003" or "Excel97To2003Template"

  When a workbook already has the selected Excel format, the Task does not convert or save it.

- _Convert visible values_: With "TextFile" only, writes the text that each cell shows in Excel instead of the stored cell value

  When it is cleared, date cells are written with their date format and other cells with their stored value.

The **Worksheet** and **Cell ranges** groups apply only to "TextFile".

**Worksheet**

- _Use first worksheet_: Converts the first worksheet of each workbook
- _Use specific worksheet_: Converts the worksheet with the name you enter or select

  Click _Get_ to choose a workbook and list its worksheets. The name can contain Variables.

- _Password_: The password that opens protected workbooks, used only for a workbook that is encrypted

**Cell ranges**

- _Cells by position_: Converts the columns from _Column start_ to _Column end_ (column numbers, starting at "1") of every row

  Reading stops after more than 10 rows in a row that have no data in those columns.

- _Cells by position range_: Converts the rows from _Row start_ to _Row end_ and the columns from _Column start_ to _Column end_ (numbers, starting at "1")
- _Cell by reference range (i.e. B2)_: Converts the range from _Cell reference start_ to _Cell reference end_, for example "A1" to "D20"

Rows with no data in the selected columns are left out of the text file. The text file is written in UTF-8, with the field separator, text qualifier and line break set on the ***Output*** tab.

**Save to..**

- _Same file_: Writes the result into the source file

  In the current version, the source file is opened read-only, so saving fails with an error and the source file is not changed. Use one of the other options.

- _Same folder but change extension_: Saves to the source folder with the source file name and the extension of the selected format: ".txt", ".xlsx", ".xlsm", ".xltm", ".xltx", ".xls" or ".xlt"
- _Same folder but use file mask_: Saves to the source folder with the name from _File mask_
- _Different folder and use file mask_: Saves to _Folder_ with the name from _File mask_
- _Folder_: The destination folder, used only with _Different folder and use file mask_
- _File mask_: The name of the saved file, "*" by default, which keeps the source name

  _Folder_ and _File mask_ can contain Variables.

:::warning

An existing file with the destination name is overwritten without warning. With _Same folder but use file mask_ and the default _File mask_ `*`, or with _Different folder and use file mask_ and the source folder as _Folder_, the converted file gets the name of the source file and replaces the source workbook. Set a _File mask_ such as `*.txt`, or use _Same folder but change extension_.

The Task creates the destination file, or empties an existing one, before it converts the workbook. When a workbook already has the selected Excel format, the Task skips it and leaves that destination file empty. If the destination is the source file itself, for example _Same folder but change extension_ to the format the workbook already has, the source workbook is left empty, and the Task reports success.

:::

### Output tab

These settings apply only to "TextFile":

- _Field separator_: The character between fields: "Colon", "Semicolon", "Comma", "Pipe", "Tab" (the default), "Blankspace", "Tilde", "None", "Equal", "Cr", "CrLF" or "Lf"
- _Text qualifier_: None (the default), `"` or `'`, written around every field
- _Line break_: The character between rows: "Cr", "CrLf" (the default), "Lf", "Comma", "SemiColon", "Pipe", "Tab" or "NoLineBreak"

_Include column names_ has no effect for this Task.

### Output and errors

The output of the Task is the path of each file it saved. When several files are saved, the paths follow each other without a separator. A workbook that cannot be opened or saved stops the Task with an error.
