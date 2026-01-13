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
 
**Source Credential**

If report file is on network drive you need to select a Credential.
 
**Connection details**

Select one ore more Connections here depending on how many database connections your report uses.
 
**Destination file type**

You can choose to output to file or printer.
 
**Output format**

A range of output formats exist when you select File destination type option.
 
**Destination Credential**

If the output file is on a network you need to specify a Credential.
 
**Crystal reports > Parameters** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Parameters.png)

Your report might include required or optional parameters. If parameters are already defined you can click on "Import parameters". This will import and list your parameters. You can then edit any parameter by double clicking on it (or press Edit). Import parameters button require that you have setup your Connection settings in the Task before pressing - otherwise VisualCron will not be able to query for parameters.
 
**Crystal reports > Record filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Reporting%20Tasks/Record%20Filter.png)

The record filter allows you to choose from existing columns in the report and specify filters - similar like WHERE in a SQL query. This way you can filter the report.
 
You can manually write the query in the Record filter text box or click "Reload" to load all existing columns, choose a condition, write a value and then press Add.
 
**Crystal reports > Printer** sub tab

The printer tab lets you control various printer settings if you have chosen Printer as output type.
 
**The Crystal Reports Connection**
 
### Troubleshooting
 
*Could not load file or assembly 'CrystalDecisions.ReportAppServer.DataDefModel, Version=13.0.3500.0*

Make sure you installed the Crystal Reports runtime 13.0.24.