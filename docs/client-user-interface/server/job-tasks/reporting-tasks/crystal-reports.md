---
sidebar_label: 'Task Reporting - Crystal Reports'
hide_title: 'true'
---

## Task Reporting - Crystal Reports

The Crystal reports Task runs a Crystal Reports report and exports it to a file, in a format such as PDF or Excel, or sends it to a printer, using a Crystal Reports Connection for the database sign-in. Parameters and a record filter narrow down what the report shows.

The Task needs the Crystal Reports runtime on the Server; use the _Required 32 bit runtime library_ or _Required 64 bit runtime library_ link on the ***Main settings*** tab of the Task. See also [Connection - Crystal Reports](../../connection-crystalreports).

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The ***Crystal reports*** tab has five sub tabs: ***Main settings***, ***Parameters***, ***Record filter***, ***Printer*** and ***Export settings***.

### Crystal reports: Main settings tab

![Main settings tab of the Crystal reports Task, with the report file, the Connection details and the destination and output settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Reports%20settings.png)

**Report file**

- The report file field: the full path of the Crystal Reports file. Click the file button to browse for it
- The Credential below it: the Credential used to read the report file, for example on a network share. It is used only when a Connection is selected under **Connection details**

**Connection details**

- The Connection: one or more Crystal Reports Connections with the sign-in for the databases of the report
- _Override default database in DSN_: uses the database entered in the field below instead of the default database of the DSN
- _Refresh report's data_: refreshes the data of the report before it is exported or printed

:::warning

The record filter and the report file Credential are applied only when at least one Connection is selected. Without a Connection, the report is exported or printed without the record filter, and the Task reports success.

:::

**Destination and output**

- _Destination type_: "File" (default) or "Printer". With "Printer", the ***Printer*** tab is available and the file settings are not
- _Output format_: the export format, "PortableDocFormat" (PDF) by default. Other values include "Excel", "ExcelWorkbook", "WordForWindows", "RichText", "EditableRTF", "HTML32", "HTML40", "Text", "TabSeperatedText", "CharacterSeparatedValues" and "Xml"
- _Destination file_: the full path of the exported file
- The Credential below it: the Credential used to write the destination file
- _Required 32 bit runtime library_ / _Required 64 bit runtime library_: download links for the Crystal Reports runtime. Install the one that matches the Server

### Parameters tab

![Parameters tab of the Crystal reports Task, with the parameter list and the Add, Edit, Delete and Import parameters buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Parameters.png)

The list shows the parameters passed to the report, with their field type, range kind, values and whether they are required.

- _Import parameters_: reads the parameters defined in the report. Select the report file and a Connection first
- _Add_, _Edit_, _Delete_: change the list. Double-click a parameter to edit it

### Record filter tab

![Record filter tab of the Crystal reports Task, with the Add record filter group and the record filter expression](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Record%20Filter.png)

**Add record filter**

- _Column_: the report column to filter on. Click _Reload_ to fill the list from the report
- _Condition_: the comparison, "Equal" by default
- _Value_: the value to compare with. Click _Add_ to add the condition to the record filter

**Record filter**

The record selection formula of the report, built with **Add record filter** or typed directly. It may contain Variables.

### Printer tab

Available when _Destination type_ is "Printer".

- **Select printer**: the printer that prints the report
- **Page range**: "All pages" (default) or "Pages"
- _Number of copies_: "1" by default
- _Collated_: checked by default. Prints the copies collated
- **Orientation**: "Portrait" (default) or "Landscape"

:::note

The page numbers entered with "Pages" are not passed to the printer. To print part of a report, export it to a file and print the pages from there.

:::

### Export settings tab

Available when _Output format_ is "Text", "TabSeperatedText" or "RichText".

- _Characters per inch_: "16" by default
- _Lines per page_: "50" by default

### Output and errors

With "File", the output is the path of the exported file. With "Printer", the output names the printer the report was sent to.

### Troubleshooting

*Could not load file or assembly 'CrystalDecisions.ReportAppServer.DataDefModel, Version=13.0.3500.0*

Install the Crystal Reports runtime 13.0.24 on the Server.
