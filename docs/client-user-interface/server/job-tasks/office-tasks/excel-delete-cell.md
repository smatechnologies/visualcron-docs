---
sidebar_label: 'Task Office - Excel - Delete Cell'
hide_title: 'true'
---

## Task Office - Excel - Delete Cell

The Excel - Delete cell(s) Task deletes cells, rows or columns from a worksheet in an Excel file and saves the result.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Delete%20cell.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Select Excel file**

Select the full path to the Excel file.

**Password**

Enter the password for the Excel file, if it is password protected.

**Worksheet**

**Use first worksheet** / **Use specific worksheet**

Select **Use first worksheet** to use the first worksheet in the workbook. Select **Use specific worksheet** to choose a specific worksheet.

**Worksheet**

Select the worksheet to delete cells from. Only available when **Use specific worksheet** is selected. Click the **Get** button to populate the list with worksheets from the selected file.

**Cell coordinates**

**Cell by position**

Deletes a single cell identified by its row and column position.

* **Row** — The row number of the cell.
* **Column** — The column number of the cell.

**Cell by reference (i.e. A3)**

Deletes a single cell identified by its reference.

* **Cell reference** — The cell reference (for example, A3).

**Cells by position range**

Deletes a range of cells identified by row and column positions.

* **Row** — The starting row of the range.
* **Column** — The starting column of the range.
* **End row** — The ending row of the range.
* **End column** — The ending column of the range.

**Cell by reference range (i.e. B2)**

Deletes a range of cells identified by cell references.

* **Cell reference** — The starting cell reference of the range.
* **End cell reference** — The ending cell reference of the range.

**Delete rows**

Deletes entire rows.

* **Row numbers** — The row numbers to delete. Separate several rows with a comma and use a hyphen for a range (for example, `1,3,5-8`).

**Delete columns**

Deletes entire columns.

* **Column numbers** — The column letters to delete (for example, `A`). Separate several columns with a comma (for example, `A,C,F`).

**Shift cells direction**

Select how the remaining cells move to fill the space left by the deleted cells.

* **Shift cells left** — Moves the cells to the right of the deleted cells to the left. This is the default.
* **Shift cells up** — Moves the cells below the deleted cells up.

**Save to..**

* **Same file** — Overwrites the original source file.
* **Same folder but use file mask** — Saves to the same folder with a new file name specified in File mask.
* **Different folder and use file mask** — Saves to a different folder with a new file name.

**Folder**

The destination folder path. Only available when **Different folder and use file mask** is selected.

**File mask**

The file name to use for the saved file. Available when **Same folder but use file mask** or **Different folder and use file mask** is selected.
