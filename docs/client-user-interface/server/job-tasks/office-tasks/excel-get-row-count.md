---
sidebar_label: 'Task Office - Excel - Get Row Count'
hide_title: 'true'
---

## Task Office - Excel - Get Row Count

The Excel - Get row count Task counts the rows of a worksheet in an Excel workbook and writes the number to the output of the Task.

![Excel - Get row count Task settings, with the Credentials, Select Excel file and Worksheet groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Get%20Row%20Count.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Excel - Get row count tab

- _Credentials_: The Credential used to read the workbook, for example on a network share; see [Credentials](../../global-credentials)

  Select a Credential in the combo box, or click the _Settings_ icon to add or edit Credentials.

- _Select Excel file_: The full path of the workbook; it can contain Variables
- _Password_: The password that opens a protected workbook, used only when the workbook is encrypted

**Worksheet**

- _Use first worksheet_: Counts the rows of the first worksheet
- _Use specific worksheet_: Counts the rows of the worksheet with the name you enter or select

  Click _Get_ to list the worksheets of the workbook in _Select Excel file_. The Client reads that file, so the path must be reachable from the computer that runs the Client. The name can contain Variables.

### Output and errors

The output of the Task is the number of rows that the worksheet holds. A workbook or worksheet that cannot be read stops the Task with an error.
