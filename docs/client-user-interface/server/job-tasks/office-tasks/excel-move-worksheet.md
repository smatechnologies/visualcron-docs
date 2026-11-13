---
sidebar_label: 'Task Office - Excel - Move Worksheet'
hide_title: 'true'
---

## Task Office - Excel - Move Worksheet

The Excel - Move worksheet Task moves an existing worksheet to a new position in an Excel file and saves the file afterwards.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Move%20Worksheet.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Select Excel file**

Select the full path to the Excel file.

**Password**

Enter the password for the Excel file, if it is password protected.

**Worksheet**

**Worksheet name**

Select the worksheet to move. Click the **Get** button to populate the list with worksheets from the selected file. The Task fails if no worksheet with this name exists.

**Worksheet position**

* **Add worksheet to the beginning** — Moves the worksheet to the first position in the workbook.
* **Add worksheet to the end** — Moves the worksheet to the last position in the workbook. This is the default.
* **Insert worksheet before active one** — Moves the worksheet in front of the worksheet that is currently active in the workbook.
* **Insert worksheet after specified** — Moves the worksheet directly after another worksheet. Select that worksheet in the list next to the option, or click **Get** to populate the list. If the specified worksheet is the last one, the worksheet is moved to the end.
