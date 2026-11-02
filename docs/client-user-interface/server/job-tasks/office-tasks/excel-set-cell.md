---
sidebar_label: 'Task Office - Excel - Set Cell'
hide_title: 'true'
---

## Task Office - Excel - Set Cell

The Excel - Set cell Task writes a value, or a table of values, into existing Excel workbooks, starting at a cell you choose. It is similar to the [Excel - Create](excel-create) Task, but updates workbooks instead of creating new ones.

The input is a value or a Variable. Each line of the input becomes a row and each field a cell, starting at the start cell and going right and down. For example, with the start cell at row 2, column 2, a field separator of "Comma" and this input:

```text
col1row1,col2row1
col1row2,col2row2
```

the values are written to the cells from row 2, column 2 to row 3, column 3 ("B2" to "C3").

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***Excel - Set cell*** tab, which has the sub tabs ***Source***, ***File filter***, ***Column format***, ***Target*** and ***Output***.

### Source tab

![Source tab of the Excel - Set cell Task, with the Input value box and the Format group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell.png)

- _Input value_: The value or Variable to write

  Its format must match the settings below so that rows and fields are split correctly. Values are written as text unless the ***Column format*** tab sets another type.

**Format**

- _Field separator_: The character between fields, "Tab" by default
- _Text qualifier_: The character around field values, if any; none by default

  A separator inside a qualified value still splits the field.

- _Line break_: The character between rows, "CrLf" by default

  With an Excel 97-2003 workbook and "CrLf", an empty row is written between the rows of the input. Use "Lf" or "Cr" with input that matches, or a ".xlsx" workbook.

### File filter tab

![File filter tab of the Excel - Set cell Task, with the Location settings for the workbooks to update](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20File.png)

The ***File filter*** tab selects the workbooks to update; see [Task - File filter](../../job-tasks-file-filter). The Credential on its ***Location*** tab is used to read the workbooks.

When no file matches and the _Include file mask_ names one file without wildcards, the Task creates that workbook in the filter folder.

:::warning

When no file matches a file mask with wildcards, the Task writes nothing, and the Task reports success.

:::

### Column format tab

![Column format tab of the Excel - Set cell Task, with the Add/Edit column window open](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Column.png)

The list sets the format of the written columns, in order: the first entry applies to the first field of each row, and so on. Click _Add_, _Edit_ or _Delete_ to change the list.

The _Add/Edit column_ window has these settings:

- _Type_: How the field is written: "Text", "Number", "Date" or "Formula"

  A "Number" or "Date" field that cannot be converted is written as text. A "Formula" field gets a leading "=" if it has none.

- _Format_: The Excel number format of the cells, "@" (text) by default

  For the format codes, see [http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm).

- _Horizontal alignment_: The alignment of the cells
- _Width_ and _Auto fit_: The column width

### Target tab

![Target tab of the Excel - Set cell Task, with the Worksheet and Cell coordinates groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Target.png)

**Worksheet**

- _Use first worksheet_: Writes to the first worksheet
- _Use specific worksheet_: Writes to the worksheet with the name you enter; it can contain Variables

  If a ".xlsx" workbook has no worksheet with that name, the Task adds it.

- _Clear cells before updating_: Clears the whole worksheet before the values are written, not only the target cells

:::warning

_Clear cells before updating_ removes every value on the worksheet. With a ".xlsx" workbook it also removes the cell formatting.

:::

**Cell coordinates**

- _Cell by position_: The start cell by _Row_ and _Column_, starting at "1"
- _Cell by reference (i.e. A3)_: The start cell by _Cell reference_, for example "A3"

The coordinates can contain Variables.

### Output tab

![Output tab of the Excel - Set cell Task, with the Save to.., Credentials and Password protection groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Output.png)

**Save to..**

- _Same file_: The default; saves the updated workbook over the original file
- _Same folder but use file mask_: Saves to the folder of the ***File filter*** tab with the name from _File mask_
- _Different folder and use file mask_: Saves to _Folder_ with the name from _File mask_
- _Folder_: The destination folder
- _File mask_: The name of the saved file, "*.xlsx" by default

_Folder_ and _File mask_ can contain Variables.

:::warning

With _Same file_, the default, each workbook is saved over the original file. An existing file with the destination name is also replaced without warning.

:::

- _Credentials_: The Credential used to save ".xlsx" workbooks; see [Credentials](../../global-credentials)

  An Excel 97-2003 destination file is created with the Credential of the ***File filter*** tab.

  Select a Credential in the combo box, or click the _Settings_ icon to add or edit Credentials.

**Password protection**

- _Use password when accessing file_: Opens protected workbooks with the password you enter, and saves them with the same password
- _Remove password when saving_: With _Use password when accessing file_, saves the workbooks without a password

  The Task does not clear _Use password when accessing file_ after it removes the password.

- _Only remove password_: Writes no values, so only the password settings apply; the ***Source*** tab is not available

  To remove a password, also select _Use password when accessing file_ and _Remove password when saving_.

### Output and errors

The output of the Task is the path of each workbook it saved.

:::warning

With an Excel 97-2003 workbook (".xls"), errors while the workbook is opened, updated or saved are not reported: the workbook is left unchanged or, with _Same file_, can be left empty, and the Task reports success. Check the workbook after the Task runs, or use a ".xlsx" workbook, where such errors stop the Task.

:::
