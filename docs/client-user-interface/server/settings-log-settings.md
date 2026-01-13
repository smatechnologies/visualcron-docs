---
sidebar_label: 'Settings - Log Settings'
hide_title: 'true'
---

## Settings - Log Settings

In the main menu **Server > Main settings > Settings** dialog, there are a set of important setting groups/tabs. In this tab, the log settings are managed.
 
**Main > Settings > Log settings > Settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Log%20Settings.png)

**Extended debug logging**

If you experience problems the VisualCron support may ask you to turn on extended debugging. When the support process is done you uncheck this option as it leverages the system.
 
**Log to event log**

Use Windows event log for logging.
 
**Log to file - Client events**

Controls if Client should write events to a file (placed in VisualCron X/log folder).
 
**Log to file - Server events**

Controls if Server should write events to a file (placed in VisualCron X/log folder).
 
**Log to file**

If any option is activated, a log file will be created and entries will be written into the log file. A new log file is created for each day. If no Job has been run during a day (with logging on) - no file will be created. The server/client log file names are "log_serverYYYYMMDD.txt"/"log_remoteYYYYMMDD.txt". By default the log files are located in the "C:\Program Files\VisualCron\log\" folder.
 
**Main > Settings > Log settings > Error handling** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Error%20Handling.png)

**Send unhandled server errors to VisualCron**

If you check this all errors are reported back to VisualCron. This way we can get enough information to detect and fix bugs as soon as possible.
 
**Main > Settings > Log settings > Database settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Database%20Settings.png)

VisualCron uses an internal database to log server events and Job/Task result/output and audit logging. These are stored in separate tables in an internal database. You can control how many and/or how long time this data should be stored in each table. It is possible to store these logs externally.
 
**Log to database**

This controls if the internal database should be used or not.
 
**Log DB location**

This controls if VisualCron should log to the internal SQL Compact database or any external database.
 
**Location**

Only visible when using Internal logging. This shows the location of the internal database (for debugging purposes).
 
**Connection**

Only visible when using External logging. Select an existing Connection. If Integrated Authentication is used you need to select a Credential.
 
**Credential**

Only visible when using External logging. Select a Credential if Integrated Authentication is used (Windows Auth).
 
**Create DB tables**

Creates the External DB tables in the selected Connection. The following tables are created:
* AuditLogs - stores the Audit logs
* DBVersions - controls the version of the database (for upgrades)
* GeneralLogs - stores the General logs
* JobLogs - stores the Job logs
* TaskLogs - stores the Task logs
 
**Size**

This shows the current size of the database.
 
**General/Audit/Job/Task Rows**

The current number of rows in the current log type
 
**General/Audit/Job/Task Range**

The date range of the current stored objects.
 
**General/Audit/Job/Task Keep a maximum of x rows in database**

This option controls how many rows to store. If unchecked then unlimited rows will be stored (or limited by number of days in setting below).
 
**General/Audit/Job/Task Delete rows older than x days**

This option controls how many days to store. If unchecked then unlimited days will be stored (or limited by number of rows in setting above).

**Please note:** If the row limit is hit first, this will limit the available date range.
 
**General/Audit/Job/Task Clear all**

This option deletes all entries for the current log type.
 
**Reset database completely**

If the database has exceeded maximum size you may have to manually delete it to restore. Here are the steps:
1. Open the **Main > Settings > Folders** tab and click on the Output cache folder > Open button.
2. Stop the VisualCron service
3. In the Explorer window enter the folder "log" and delete the file "VisualCron4.sdf"
4. Start the service again
 
**Main > Settings > Log settings > Output settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Output%20Settings.png)

**Limit output size**

If checked, Task output will be limited in the Task log table to the value you set below. It is recommended to have some kind of limitation so that the database file do not grow to fast which makes it hard to control and connection slow between Client and Server.
 
**Max output size**

This is the max output size we store in real time. If a Task has larger output than specified we cap at at this level.
