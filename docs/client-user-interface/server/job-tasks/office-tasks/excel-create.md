---
sidebar_label: 'Task Office - Excel - Create'
hide_title: 'true'
---

## Task Office - Excel - Create

The Excel - Create Task can create an Excel file from a CSV file or Variable.
 
**Excel - Create > Source** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create.png)

**Source**

You can select File if the source for conversion is one or more files. You can also select Value/Variable if the source comes from a previous Task for example.
 
**Format**

You need to adjust format controls so they fit the format of the incoming file. The text qualifier is any surrounding character.
 
**Excel - Create > File filter > Location** sub tab

If you have selected File as source you are able to set the standard VisualCron [File filter](../../../server/job-tasks-file-filter) values.
 
**Excel - Create > Columns** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create%20Columns.png)

In the columns tab you can override existing columns or set columns if they do not exist. It is possible to override name and also format of column. Default format is `@` which is a string. You can see different format options when editing or adding a column.
 
For faster addition of new columns we recommend using *Import headers*. This lets you import any existing first row of the document (in the same format you specified in the **Source** tab).
 
**Column header source**

You can choose to use the existing columns in the file but then it is not possible to apply formatting. If you add columns manually and select "Use columns from definition above" you are able to control name, width, format and order.
 
**Include column headers in destination file**

You can deselect this option if you do not want to include any existing headers in file.
 
**Add->Format**

[http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm)
 
**Excel - Create > Output** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office%20Tasks/Excel%20Create%20Output.png)

**Save to..**

Depending on if you have selected File or Variable as source different options are available. If you have selected File all options are available and if you have selected Variable only *Different folder and use file mask* is available. When using Variable option the file mask must be the full name of the file.
 
**Credential**

If you are planning to save on a network location you can select a Credential.
 
**Password protection**

If you want to protect the file with Excel password authentication you can check this value and enter a password.
 
**Sheet**

The created Excel sheet name.