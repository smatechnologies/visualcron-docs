---
sidebar_label: 'Task Office - Excel - Search Worksheets'
hide_title: 'true'
---

## Task Office - Excel - Search Worksheets

The Excel - Search worksheets Task searches an Excel file for a text and returns every matching cell. Each match is written on its own line as the cell address followed by the cell content.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Search%20worksheets.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Select Excel file**

Select the full path to the Excel file.

**Password**

Enter the password for the Excel file, if it is password protected.

**Find what**

**Search text**

Enter the text to search for.

**Options**

**Within**

* **Workbook** — Searches all worksheets in the workbook. This is the default.
* **Worksheet** — Searches one worksheet only. Select the worksheet in the list, or click the **Get** button to populate the list with worksheets from the selected file. The Task fails if no worksheet with this name exists.

**Search**

* **By Rows** — Searches row by row. This is the default.
* **By Columns** — Searches column by column.

**Look in**

* **Values** — Searches the cell values. This is the default.
* **Formulas** — Searches the cell formulas.
* **Comments** — Searches the cell comments.

**Match case**

When checked, the search is case sensitive.

**Match entire cell contents**

When checked, a cell only matches if its entire content equals the search text.

**Search worksheets > Output** tab

**Output to standard output** / **Output to file**

Select **Output to standard output** to write the results to the standard output of the Task. Select **Output to file** to write them to a file.

**File path**

The full path of the output file. Only available when **Output to file** is selected.

**Append to file**

When checked, the output is added to the end of the file instead of replacing its contents.

**Include BOM (if UTF8)**

When checked, a byte order mark is written at the start of the file when the encoding is UTF-8.

**Credentials**

The Credential used to write the output file. Only available when **Output to file** is selected.

**Include field names**

When checked, the first line of the output contains the column names **Address** and **Value**.

**Field separator**

The character placed between the cell address and the cell content.

**Text qualifier**

The character placed around the cell content.

**Line break**

The character(s) used to separate the matches.
