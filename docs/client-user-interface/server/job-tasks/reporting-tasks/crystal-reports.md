---
sidebar_label: 'Task Reporting - Crystal Reports'
hide_title: 'true'
---

## Task Reporting - Crystal Reports

The Crystal Reports Task allows you to output Crystal reports in various formats like PDF, Excel and to printer. With this Task you can specify in-parameters and record filter. The record filter can further narrow down the report query.
 
This Task uses the [Crystal Reports Connection](../../../server/connection-crystalreports). It requires runtime files to be installed on the Server. You can find this in the Connection.
 
**Crystal reports > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Reports%20settings.png)

**Report file**

This is the path to the report. If located on a network drive you need to specify the Source Credential)

**Report file**

The full path to the Crystal Reports file.
 
**Source Credential**

If the report file is on a network drive, select a Credential to authenticate access.
 
**Connection details**

Select one or more Connections depending on how many database connections your report uses.

**Override default database in DSN**

When checked, overrides the default database specified in the DSN. Enter the database name in the field below.

**Refresh report's data**

When checked, refreshes the report's data before generating the output.

**Destination and output**

**Destination type**

Select the output destination: file or printer.
 
**Output format**

Select the output file format. Available when the destination type is set to file.

**Destination file**

The full path to the output file.
 
**Destination Credential**

If the output file is on a network drive, select a Credential to authenticate access.

**Required 32 bit runtime library** / **Required 64 bit runtime library**

Links to download the Crystal Reports runtime library required by the server. Install the version that matches your VisualCron server's bitness.
 
**Crystal reports > Parameters** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Parameters.png)

Your report might include required or optional parameters. Click **Import parameters** to automatically import the parameters defined in the report. You must configure the Connection settings in the Task before clicking Import parameters, otherwise VisualCron cannot query the report for parameters.

Use **Add**, **Edit**, and **Delete** to manage parameters manually. You can also edit a parameter by double-clicking on it.
 
**Crystal reports > Record filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Record%20Filter.png)

**Add record filter**

Use the controls in this group to build and add filter conditions to the record filter expression.

**Column**

Select a report column to filter on. Click **Reload** to populate the list with columns from the connected report.

**Condition**

Select the comparison condition to apply to the selected column.

**Value**

Enter the value to compare against. Click **Add** to append the condition to the record filter.

**Record filter**

Displays the current record filter expression, similar to a SQL WHERE clause. You can also type or edit the filter expression directly in this field.
 
**Crystal reports > Printer** sub tab

The Printer tab is available when **Printer** is selected as the destination type.

**Select printer**

Select the printer to use for output.

**Printer settings**

**Page range**

**All pages** / **Pages**

Select **All pages** to print the entire report. Select **Pages** to print a specific range and enter the page numbers or range in the field below (for example, `2-4`).

**Pages**

**Number of copies**

The number of copies to print.

**Collated**

When checked, prints multiple copies in collated order.

**Orientation**

**Portrait** / **Landscape**

Select the page orientation for printing. Defaults to **Portrait**.

**Crystal reports > Export settings** sub tab

**Text export settings**

**Characters per inch**

The number of characters per inch for text-format export output.

**Lines per page**

The number of lines per page for text-format export output.
 
### Troubleshooting
 
*Could not load file or assembly 'CrystalDecisions.ReportAppServer.DataDefModel, Version=13.0.3500.0*

Make sure you installed the Crystal Reports runtime 13.0.24.
