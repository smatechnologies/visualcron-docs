---
sidebar_label: 'Task Office - Excel - Create'
hide_title: 'true'
---

## Task Office - Excel - Create

The Excel - Create Task creates an Excel workbook from delimited text, such as a CSV file, or from a value or Variable. Each line of the source becomes a row and each field a cell.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***Excel - Create*** tab, which has the sub tabs ***Source***, ***File filter***, ***Columns*** and ***Output***.

### Source tab

![Source tab of the Excel - Create Task, with the Source and Format groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create.png)

**Source**

- _File_: Creates one workbook from each file that the ***File filter*** tab finds
- _Value/Variable_: Creates one workbook from the text in the box, which can be a value or a Variable, for example the output of a previous Task

  Click the Variable button to insert a Variable.

**Format**

Set these to match the source text:

- _Field separator_: The character between fields, "Tab" by default
- _Text qualifier_: The character around field values, if any; none by default
- _Line break_: The character between rows, "CrLf" by default

### File filter tab

With _File_ as the source, the ***File filter*** tab selects the source files; see [Task - File filter](../../job-tasks-file-filter). The Credential on its ***Location*** tab is used to read the source files. The tab is not available with _Value/Variable_.

When no file matches the filter, the Task raises a "file not found" error, which you can handle on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

### Columns tab

![Columns tab of the Excel - Create Task, with the column list, the Column header source group and Include column headers in destination file](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create%20Columns.png)

The column list sets the header, width, format and type of each column, in order. Click _Add_, _Edit_ or _Delete_ to change the list, or _Import headers_ to paste the first line of the source and create one column for each header, using the separators from the ***Source*** tab.

The _Add/Edit column_ window has these settings:

- _Header caption_: The column header
- _Width_ and _Auto fit_: The column width
- _Format_: The Excel number format of the cells, "@" (text) by default

  For the format codes, see [http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm).

- _Horizontal alignment_: The alignment of the cells
- _Type_: How the field is written: "Text", "Number", "Date" or "Formula"

  A "Number" or "Date" field that cannot be converted is written as text. A "Formula" field gets a leading "=" if it has none.

When the list has columns, their type, format and alignment apply to the fields in that order, whichever header source is selected.

**Column header source**

- _Use columns from file/Variable_: The first line of the source is the header row
- _Use columns from definition above_: The headers come from the column list

**Include column headers in destination file**

- With _Use columns from definition above_, writes the headers from the column list as a bold first row
- With _Use columns from file/Variable_, writes the first line of the source in bold

When it is cleared, no header row is added, and the first line of the source is still written as an ordinary row.

### Output tab

![Output tab of the Excel - Create Task, with the Sheet, Save to.., Credentials, Password protection and Sheet name settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create%20Output.png)

- _Sheet_: The format of the new workbook

  "Excel97To2003" and "Excel97To2003Template" create an Excel 97-2003 workbook. All other choices currently create a standard Excel 2007 workbook (".xlsx").

**Save to..**

With _Value/Variable_ as the source, only _Different folder and use file mask_ is available.

- _Same folder but change extension_: Saves to the source folder with the source file name and the extension ".xls" for the Excel 97-2003 formats or ".xlsx" for the others
- _Same folder but use file mask_: Saves to the source folder with the name from _File mask_
- _Different folder and use file mask_: Saves to _Folder_ with the name from _File mask_

  With _Value/Variable_ as the source, _File mask_ must be the full file name, for example `report.xlsx`.

- _Folder_: The destination folder
- _File mask_: The name of the new file, "*.xlsx" by default

_Folder_ and _File mask_ can contain Variables.

:::warning

An existing file with the destination name is replaced without warning.

:::

- _Credentials_: The Credential used to save the new workbook; see [Credentials](../../global-credentials)

  Select a Credential in the combo box, or click the _Settings_ icon to add or edit Credentials.

**Password protection**

- _Password protect file with password_: Protects the new workbook with the password you enter below it

**Sheet**

- _Sheet name_: The name of the worksheet in the new workbook, "VisualCron" by default; it can contain Variables

### Output and errors

The output of the Task is the path of each workbook it created, one per line.
