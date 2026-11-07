---
sidebar_label: 'Task Office - Excel - Get Cell'
hide_title: 'true'
---

## Task Office - Excel - Get Cell

The Excel - Get cell Task reads the value of one cell, a range of cells or whole columns from a worksheet of an Excel workbook and writes the values to the output of the Task.

![Excel - Get cell Task settings, with the Credentials, Select Excel file, Worksheet and Cell coordinates groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Get%20Cell.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***Excel - Get cell*** tab and on the ***Output*** tab of the Task window.

### Excel - Get cell tab

- _Credentials_: The Credential used to read the workbook, for example on a network share; see [Credentials](../../global-credentials)

  Select a Credential in the combo box, or click the _Settings_ icon to add or edit Credentials.

- _Select Excel file_: The full path of the workbook; it can contain Variables
- _Password_: The password that opens a protected workbook, used only when the workbook is encrypted

**Worksheet**

- _Use first worksheet_: Reads the first worksheet
- _Use specific worksheet_: Reads the worksheet with the name you enter or select

  Click _Get_ to list the worksheets of the workbook in _Select Excel file_. The Client reads that file, so the path must be reachable from the computer that runs the Client. The name can contain Variables.

**Cell coordinates**

Row and column numbers start at "1".

- _Cell by position_: One cell, by _Row_ and _Column_
- _Cell by reference (i.e. A3)_: One cell, by _Cell reference_, for example "A3"
- _Cells by position range_: The cells from _Row_ and _Column_ to _End row_ and _End column_
- _Cell by reference range (i.e. B2)_: The cells from _Cell reference_ to _End cell reference_, for example "B2" to "D10"
- _Get all cells_: Every row of the worksheet, for the first columns up to _Number of columns_
- _Get by column numbers_: Every row of the worksheet, for the columns in _Column numbers_

  Separate column numbers with commas and give ranges with a hyphen, for example `1,3,5-7`.

All coordinate fields can contain Variables.

### Output tab

These settings shape the output of the Task:

- _Field separator_: The character between cells of a row, "Tab" by default
- _Text qualifier_: None (the default), `"` or `'`, written around every cell value of a range
- _Line break_: The character between rows, "CrLf" by default
- _Include column names_: Adds a first line with the column letters ("A", "B" and so on)

  It has no effect with _Get by column numbers_.

### Output and errors

The output of the Task is the text of the cells as Excel displays it, with the rows separated by the _Line break_ character. A workbook, worksheet or cell that cannot be read stops the Task with an error.
