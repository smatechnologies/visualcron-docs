---
sidebar_label: 'Task Office - Excel - Recalculate'
hide_title: 'true'
---

## Task Office - Excel - Recalculate

![Excel - Recalculate Task window on the File filter tab, with the Location settings for the files to recalculate](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Recalculate.png)

The Excel - Recalculate Task recalculates the formulas in existing Excel workbooks and saves each workbook in place. It cannot refresh data from other data sources; for that, use the [Office - Macro](office-macro) Task.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***Excel - Recalculate*** tab, which has the sub tabs ***File filter*** and ***Recalculate***.

### File filter tab

The ***File filter*** tab selects the workbooks to recalculate; see [Task - File filter](../../job-tasks-file-filter). The Credential on its ***Location*** tab is used to read and save the workbooks.

When no file matches the filter, the Task raises a "file not found" error, which you can handle on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

:::warning

Each workbook is saved over the original file. Password-protected workbooks are not supported.

:::

### Recalculate tab

![Recalculate tab of the Excel - Recalculate Task, with the Recalculate settings and Cell coordinates groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Recalculate%20Settings.png)

**Recalculate settings**

- _Auto detect_: Selected by default; the Task detects the format of each workbook
- _Excel format_: When _Auto detect_ is cleared, treats every workbook as "Excel 2007" or "Excel 97 To 2003"

  The format decides how the workbook is read and recalculated; the file keeps its format when it is saved.

An Excel 97-2003 workbook is always recalculated as a whole: the worksheet and cell settings below apply only to Excel 2007 and later workbooks.

- _Use workbook_: Recalculates every formula in the workbook
- _Use first worksheet_: Recalculates the first worksheet
- _Use specific worksheet_: Recalculates the worksheet with the name you enter or select

  Click _Get_ to list the worksheets of a file found by the ***File filter*** tab.

**Cell coordinates**

Not available with _Use workbook_. Row and column numbers start at "1", and the fields can contain Variables.

- _All cells_: Recalculates every cell of the worksheet
- _Cell by position_: One cell, by _Row_ and _Column_
- _Cells by position range_: The cells from _Row_ and _Column_ to _End row_ and _End column_
- _Cell by reference (i.e. A3)_: One cell, by _Cell reference_, for example "A3"
- _Cell by reference range (i.e. B2)_: The cells from _Cell reference_ to _End cell reference_, for example "B2" to "D10"

### Output and errors

The output of the Task is the path of each workbook it recalculated, one per line. A workbook that cannot be opened or saved raises an error, and the Task continues with the next file.
