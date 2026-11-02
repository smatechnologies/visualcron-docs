---
sidebar_label: 'Settings - Log Settings'
hide_title: 'true'
---

## Settings - Log Settings

The **_Log settings_** tab controls what the Server logs and where: the Server log file, the Windows event log, the log database with its retention limits, and how much Task output is stored. Use it to keep the logs you need without filling the disk. This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)). It has four sub tabs: **_Settings_**, **_Error and diagnostics_**, **_Database settings_** and **_Output settings_**.

### Settings sub tab

_Server_ -> _Main settings_ -> _Settings_ -> **_Log settings_** -> **_Settings_**

![The Settings sub tab of Log settings with Extended debug logging (checked in this screenshot), Log to event log, and Server events in the Log to file box](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Log%20Settings.png)

- _Extended debug logging_: writes extra debug entries to the Server log, for example the result lines of Variable conditions. VisualCron support may ask you to turn it on. Turn it off again afterwards, because it adds load to the Server and makes the log grow faster. Unchecked by default
- _Log to event log_: also writes the Server's log entries to the Windows event log. Unchecked by default
- _Log to file_ -> _Server events_: writes the Server's log entries to a file in the _Log folder_ (see [Settings - Folders](settings-folders)), by default the `log` folder in the VisualCron installation folder (`C:\Program Files (x86)\VisualCron\log` on 64-bit Windows). Checked by default

The Server starts a new log file each day, named "log_server`<yyyyMMdd>`.txt", as soon as it logs its first entry that day. The Client writes its own log file, "log_client`<yyyyMMdd>`.txt", in the Client's log folder, by default `%LOCALAPPDATA%\VisualCron\log` of the Windows user who runs the Client. You turn that on, and can change the folder, in the Client settings (see [Settings - Client Settings](../file/client-settings)).

:::note

The built-in Job "Delete old log files" runs every day at 23:10. It deletes ".txt" files in the _Log folder_ that were created more than one month ago. To keep log files longer, change the age condition of its Task, or deactivate the Job (see [Task File - Delete File](job-tasks/file-tasks/delete-file)).

:::

### Error and diagnostics sub tab

_Server_ -> _Main settings_ -> _Settings_ -> **_Log settings_** -> **_Error and diagnostics_**

![The Error and diagnostics sub tab with Send unhandled server errors to VisualCron and Send anonymous diagnostics and usage data, both checked](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Error%20Handling.png)

- _Send unhandled server errors to VisualCron_: sends details of unexpected Server errors to VisualCron, so that the errors can be found and fixed. Checked by default
- _Send anonymous diagnostics and usage data_: sends anonymous diagnostics and usage data to VisualCron to help improve the product. Checked by default

:::note

Both options are on when VisualCron is installed. If your security policy does not allow the Server to send data outside your network, uncheck both and click _Apply settings_.

:::

### Database settings sub tab

The Server stores its logs in a log database: Job and Task runs with their output, the Audit log, the Server log and more. By default this is an internal SQL Server Compact database on the Server computer. You can use an external SQL database instead (see [Move logging to an external database](#move-logging-to-an-external-database)).

_Server_ -> _Main settings_ -> _Settings_ -> **_Log settings_** -> **_Database settings_**

![The Database settings sub tab with Log to database checked, Log DB location Internal, the Copy database button, the location and size of the internal database, and the row and day limits of each log](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Database%20Settings.png)

- _Log to database_: logs to the log database, internal or external. Checked by default. When unchecked, the Server does not store Job and Task runs, output or other log entries in a database
- _Log DB location_: "Internal" (default) or "External"
- _Copy database_: copies log data from one log database to another (see [Move logging to an external database](#move-logging-to-an-external-database))

With "Internal", the _Database info_ box shows the _Location_ and _Size_ of the internal database file.

With "External", the _External database info_ box shows:

- _Connection_: the SQL Connection of the external database (see [Connection - SQL](connection-sql))
- _Credential_: the Credential the Server uses to connect, if the database uses Windows authentication
- _Create DB tables_: creates the log tables in the external database. Available until the tables exist. If you click _Apply settings_ with "External" before the tables exist, VisualCron shows "First you have to click create tables in the database!" and does not save. _Create DB tables_ acts at once, without _Apply settings_
- _Drop all tables_: shown next to _Create DB tables_. When checked, _Create DB tables_ deletes the existing log tables first, after you confirm
- _Command Timeout (seconds, 0 for infinite timeout)_: how long the Server waits for a database command. The default is "90"

_Create DB tables_ creates these tables: "AuditLogs", "ConnectionLogs", "DBVersions", "EventLogs", "GeneralLogs", "HealthLogs", "JobLogs", "NotificationLogs", "ServerStats", "TaskLogs" and "TransferLogs".

:::warning

_Drop all tables_ deletes all log data in the external database's log tables. Use it only for a database whose log data you do not need.

:::

#### Limits for each log

Below the database box, each log has its own box: _General logs_, _Audit logs_, _Job logs_, _Task logs_, _Notification logs_, _Server stats_, _Health logs_, _Event logs_, _Connection logs_ and _Transfer logs_. Each box shows:

- _Rows_ and _Range_: the number of rows and the date range of that log
- _Keep a maximum of_ `<n>` _rows in database_: when checked, the Server deletes the oldest rows above this number. Up to "1000000"
- _Delete rows older than_ `<n>` _days_: when checked, the Server deletes rows older than this number of days. Up to "365"
- _Clear all_: deletes all rows of that log
- _Recreate table_ (external database only): deletes the log's table and creates it again, empty
- _Rebuild indexes_ (external Microsoft SQL Server database only) and _Indexes average fragmentation_: rebuild the table's indexes at once, without _Apply settings_, and show how fragmented they are
- _Query statistics_: statistics of the database queries for that log; double-click to expand or collapse

The _DB version_ box shows the version of the log database.

:::warning

_Clear all_ and _Recreate table_ delete the rows at once, without asking you to confirm. They do not wait for _Apply settings_, and _Cancel_ does not bring the rows back. They act on the database selected on this sub tab, also when that is not the database the Server logs to, and they are not written to the Audit log.

:::

The default limits are:

| Log | Keep a maximum of | Delete rows older than |
|---|---|---|
| General logs | 5000 rows, checked | 14 days, unchecked |
| Audit logs | 20000 rows, checked | 30 days, checked |
| Job logs | 10000 rows, checked | 30 days, checked |
| Task logs | 20000 rows, checked | 30 days, checked |
| Notification logs | 10000 rows, checked | 30 days, checked |
| Server stats | 100000 rows, unchecked | 30 days, checked |
| Health logs | 10000 rows, checked | 30 days, checked |
| Event logs | 10000 rows, checked | 30 days, checked |
| Connection logs | 10000 rows, checked | 30 days, checked |
| Transfer logs | 10000 rows, checked | 30 days, checked |

#### How the limits are applied

The Server does not apply the limits when you click _Apply settings_. A cleanup applies them about every 11 hours, counted from when the VisualCron service started. The internal database is also cleaned up when it is full (see [Internal database size and cleanup](#internal-database-size-and-cleanup)). If the service is restarted more often than every 11 hours, the scheduled cleanup does not run.

When both limits of a log are checked, the cleanup applies both: it keeps no more than the maximum number of rows, and no rows older than the number of days. Whichever removes more rows decides what is left. For example, with _Delete rows older than_ "15" days and _Keep a maximum of_ "20000" rows on the Task log, a Server that writes 10000 Task log rows a day keeps only about two days of Task history. To keep the full number of days, raise the row limit or uncheck it.

### Output settings sub tab

_Server_ -> _Main settings_ -> _Settings_ -> **_Log settings_** -> **_Output settings_**

![The Output settings sub tab with Limit output size 20480 characters, Max output size 2147483647 characters, and Store full output with its two retention policies, unchecked](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Output%20Settings.png)

- _Limit output size_: how many characters of each Task's output are stored in its Task log entry and with the Task's last result. The default is "20480". You cannot turn this limit off. _Store full output_ (below) keeps a full copy in addition
- _Max output size_: the most output, in characters, a Task can produce while it runs. The default is "2147483647". Output beyond this size is not cut off: the Task stops with the error "Output out of range. Please check Max output size on Server settings" and exit code "77777", unless its _On error_ tab ignores the error type "Output data out of range". Flow conditions, _On error_ conditions, Conditions that check a Task's output, Variables that return a Task's output, and Run Task and Web API requests that return output work with the output up to this size, not with the limited output
- _Store full output_: also stores each Task's full output, up to _Max output size_, in the Task log, so that you can view the complete output of earlier runs. Available only while _Log to database_ is checked. Unchecked by default
- _Retention policy (# executions)_: when checked, the Server keeps the full output only for the most recent number of Task runs. The count covers all Task runs in the Task log, not each Task or Job
- _Retention policy (days)_: when checked, the Server keeps the full output only for Task runs from the last number of days

:::warning

Lower _Max output size_ only if you are sure that no Task produces more output. A Task whose output grows past the limit stops with an error instead of keeping part of its output.

:::

When the full output of a run falls outside the retention policies, the cleanup cuts it back to _Limit output size_. The run itself stays in the Task log under the Task log limits. If no retention policy is checked, the full output is kept as long as the run stays in the Task log. Trimming happens in the regular cleanup (see [How the limits are applied](#how-the-limits-are-applied)), not at once.

When you first check a retention policy, VisualCron fills in the matching Task log limit from the **_Database settings_** sub tab. While that Task log limit is checked, a retention policy cannot be higher than it:

- If you lower the Task log limit below a retention policy, VisualCron asks whether to lower the retention policy too. If you answer no, the Task log limit is set back.
- If a retention policy is higher than the Task log limit when you click _Apply settings_, VisualCron lowers it to the limit, shows a message, and leaves the window open so that you can check the values.

:::note

Full output can be large, and it is stored in the same log database. With the internal database, which is limited to about 4 GB, use the retention policies to keep full output for a shorter time than the Task log itself.

:::

### Move logging to an external database

You can log to an external SQL database instead of the internal database, and copy the existing log data to it.

1. Create a SQL Connection to the external database (see [Connection - SQL](connection-sql)).
2. On the **_Database settings_** sub tab, set _Log DB location_ to "External", select the _Connection_ and, if needed, the _Credential_, and click _Create DB tables_.
3. To copy the existing log data, click _Copy database_.

   ![The Database settings sub tab with the Copy database button marked](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database.png)

4. In the _Copy Database_ window, on the **_Source_** tab, select where to copy from, for example "Internal". For each log, you can set _Copy from_ and _Copy to_ dates.

   ![The Source tab of the Copy Database window with Internal selected and the rows, range and Copy from and Copy to dates of each log](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database%201.png)

5. On the **_Destination_** tab, select "External" and the _Connection_ and _Credential_ of the external database. Click _Create DB tables_ if the tables do not exist yet.

   ![The Destination tab of the Copy Database window with External selected and the Connection and Credential lists](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database%202.png)

6. Click _Start copy_. The **_Log_** tab shows the progress. If you close the window during the copy, the copy continues in the background and you can no longer cancel it.

   ![The Log tab of the Copy Database window during a copy, with Copy in progress entries and the Cancel copy button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database%203.png)

   ![The Copy completed message on the Log tab of the Copy Database window](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database%204.png)

7. Make sure _Log to database_ is checked and _Log DB location_ is "External", and click _Apply settings_.

   ![The Database settings sub tab with Log to database and Log DB location External marked, and the External database info box with a Connection selected, No Credential and Command Timeout 90](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Copy%20Database%205.png)

:::warning

On the **_Destination_** tab, _Clear all_ and _Recreate table_ delete the rows of the destination database at once, without asking you to confirm. If _Drop all tables_ is checked there, _Create DB tables_ deletes the existing log tables of the destination first, after you confirm.

:::

### Internal database size and cleanup

The internal database is a SQL Server Compact database. Its file can grow to about 4 GB. Not all of that space can be used for data, because the database needs room to work.

When the file is larger than about 3.5 GB at a cleanup, the Server cleans more than the limits ask for. For every log, it keeps at most 80% of the current rows, and it still applies the day limits. If the file has not shrunk by more than 5% after that, the Server compacts the database.

:::warning

If the file is still not more than 5% smaller after compacting, the Server replaces the internal database with an empty one. Then all Job and Task history, Task output, Audit log entries and other log data in the internal database are lost.

To avoid this, keep the limits low enough that the file stays well below about 3.5 GB, or log to an external database (see [Move logging to an external database](#move-logging-to-an-external-database)).

:::

To see that new data is stored, check that new runs appear in the Client's logs.

If the database keeps fewer days than you set although the settings have not changed, the Server now writes more rows a day (for example because there are more Jobs), so the row limits are reached sooner. Raise the row limits, or uncheck them and use only the day limits.

### Reset the internal database

If the internal database is full or damaged, and the Server has not already replaced it by itself (see [Internal database size and cleanup](#internal-database-size-and-cleanup)), you can delete it. The Server then starts with an empty internal database.

:::warning

Deleting the internal database deletes all Job and Task history, Task output, Audit log entries and other log data in it. Copy the data to an external database first if you need it (see [Move logging to an external database](#move-logging-to-an-external-database)).

:::

1. On the Server computer, open the _Output cache folder_. On the **_Folders_** tab, _Open_ opens it in Windows Explorer when the Client runs on the Server computer.
2. Stop the VisualCron service.
3. In the "log" folder, delete the file "VisualCron4.sdf".
4. Start the VisualCron service.
