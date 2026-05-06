---
sidebar_label: 'Task Office - Excel - Set Cell'
hide_title: 'true'
---

## Task Office - Excel - Set Cell

The Excel - Set cell Task sets one or more values in an Excel sheet starting on a specific position.
 
This task is similar to the Excel - Create Task. The difference is that this Task updates an existing document (or multiple documents).
 
The update is based on a Variable or direct value and the update starts in the cell position/reference and sheet that the user has specified. From that start point VisualCron will create a "table" based on content. The actual content could be a single cell but it can also be a table.
 
For example if the start position is 2,2 and the value is:

"col1row1,"col2row1"

"col1row12,"col2row2"

The output will be placed in 2,2 to 3,3:
 
**Excel - Set cell > Source** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell.png)

**Input value**

The input value can either be hard coded string or Variable. It is important that input value matches format so that lines and columns are split in the right way. Please note that if you need another format than Text format in excel you need to specify column format in "Column format" tab.
 
**Format**

**Field separator**

Select the character used to separate fields in the input value.

**Text qualifier**

Select the character used to surround field values in the input value.

**Line break**

Select the character used to indicate a new row in the input value.
 
**Excel - Set cell > File filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20File.png)

If you have selected File as source you are able to set the standard VisualCron [File filter](../../../server/job-tasks-file-filter) values.
 
**Excel - Set cell > Column format** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Column.png)

In the columns tab you can override column format. Default format is `@` which is a string. You can see different format options when editing or adding a column.
 
**Add->Format**

[http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm)
 
**Excel - Set cell > Target** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Target.png)

**Use first worksheet** / **Use specific worksheet**

Select **Use first worksheet** to use the first worksheet in the workbook. Select **Use specific worksheet** to choose a specific worksheet.

**Worksheet**

Select the worksheet to update. Only available when **Use specific worksheet** is selected.

**Clear cells before updating**

When checked, clears the target cells before writing the new values.
 
**Cell coordinates**

**Cell by position**

Identifies the starting cell by its row and column position.

* **Row** — The row number of the starting cell.
* **Column** — The column number of the starting cell.

**Cell by reference (i.e. A3)**

Identifies the starting cell by its reference.

* **Cell reference** — The cell reference (for example, A3).
 
**Excel - Set cell > Output** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Set%20Cell%20Output.png)

**Save to..**

* **Same file** — Overwrites the original source file.
* **Same folder but use file mask** — Saves to the same folder with a new file name specified in File mask.
* **Different folder and use file mask** — Saves to a different folder with a new file name.

**Folder**

The destination folder path. Only available when **Different folder and use file mask** is selected.

**File mask**

The file name to use for the saved file. Available when **Same folder but use file mask** or **Different folder and use file mask** is selected.

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
**Password protection**

**Use password when accessing file**

Check this option and enter a password if the Excel file is password protected.

**Remove password when saving**

When checked, removes the password from the file after writing. You need to specify the password for accessing the file the first time. After writing, the **Use password when accessing file** option will be unchecked so that the Task does not try to open it with a password anymore.

**Only remove password**

When checked, the Task only removes the password from the file without writing any cell values. The Source tab is disabled when this option is selected.
