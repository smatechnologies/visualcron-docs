---
sidebar_label: 'Connection - Crystal reports'
hide_title: 'true'
---

## Connection - Crystal reports

The Crystal reports Connection stores the address, sign-in and security settings that the [Reporting - Crystal reports](job-tasks/reporting-tasks/crystal-reports) Task uses to connect to the databases of a Crystal report. In the Task, select one Connection for each database connection that the report uses. See [How the Task applies the Connections](#how-the-task-applies-the-connections).
 
### Runtime binaries

The Crystal reports Task needs the SAP Crystal Reports runtime on the computer where the VisualCron Server runs. Install the 32-bit or 64-bit version that matches your machine. For VisualCron 9.9.7 and later, runtime version 30 is required:

- [Crystal Reports runtime version 30, 32-bit](https://origin.softwaredownloads.sap.com/public/file/0020000000195592021)
- [Crystal Reports runtime version 30, 64-bit](https://origin.softwaredownloads.sap.com/public/file/0020000000195602021)
 
### Common settings

![Crystal reports Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Crystal%20Reports/Crystal%20Reports.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For a Crystal reports Connection, no _Test_ button is shown, and _Timeout_ and _Code page_ are not used. The Crystal reports Task uses the Task timeout.
 
### Main settings

![Crystal reports Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Crystal%20Reports/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

- _Address_: the name of the ODBC or OLE DB data source (DSN) that the report uses. It must match the name shown in the ODBC Data Source Administrator exactly. Create the DSN as a System DSN on the Server computer, because User DSN entries are not available across users. If the report uses a User DSN, create a System DSN with the same name. The DSN sets the target database
- _Username_: the user name of the database credentials that the data source uses. With _Integrated security_, the Windows user name
- _Password_: the password for that user
- _Integrated security_: when selected, the Task runs the report as the Windows user given in _Username_ and _Password_, and connects to the database with Windows authentication. This applies only when one Connection is selected in the Task

### How the Task applies the Connections

With one Connection selected, the Task sets the server name of each report table to _Address_. It then uses _Integrated security_, or passes _Username_ and _Password_.

With more than one Connection selected, the Task matches each report table to the Connection whose _Address_ equals the server name stored in the report and whose _Username_ equals the user ID stored in the report. Only the password of the matching Connection is used, and _Integrated security_ is not applied.

When a report table has no stored user ID, the Task leaves its connection details as they are.
 
### Troubleshooting

#### Find the cause of a failing report

To find the cause of a failing report, complete the following steps:

1. In the Crystal reports Task, select _Extended Task debug logging_ on the ***Main settings*** tab. See [Task - Main Settings](job-tasks-task-main-settings).
2. Run the Task.
3. Open the log.

The log shows, for each report table, the server name, user name and database name that the Task used, and whether a password was set.

Common causes:

- _Address_ does not match the name of the System DSN
- The DSN exists only as a User DSN
- The report does not use the System DSN
- _Username_ or _Password_ does not match the database credentials
- A Connection is missing for one of the report's database connections

#### Could not load file or assembly 'CrystalDecisions.ReportAppServer.ClientDoc, Version=13.0.4000.0'

Install the Crystal Reports runtime version that VisualCron requires (see [Runtime binaries](#runtime-binaries)), in the 32-bit or 64-bit version that matches your machine. Then restart the VisualCron Server service.
