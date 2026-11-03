---
sidebar_label: 'Task Database - Sync Tables'
hide_title: 'true'
---

## Task Database - Sync Tables

The Sync table(s) Task copies one or more tables from a source Microsoft SQL Server database to a destination database, and on later runs applies the changes made at the source since the last run. It uses two SQL Connections. This Task requires that you download the Microsoft Sync Framework from [here](https://www.microsoft.com/en-us/download/details.aspx?id=19502).

:::warning

This Task uses SQL Connections; see [Connection - SQL](../../connection-sql). It works only when the source Connection uses the native Microsoft SQL Server provider. With any other source provider, nothing is copied, no error is raised, and the Task reports success.

When the copy itself fails, or when the tracking tables, triggers and procedures cannot be created at the source or the destination, the error is written to the error output only, and the Task reports success. Rows that could not be applied are counted in the output but raise no error. To have these cases fail the Task, add an error condition on the error output on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Sync table(s) tab

![Sync table(s) tab with the Credential, Source connection and Destination connection fields and the Table sync parameters](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Database%20Tasks/Sync%20table(s).png)

**Connection**

- _Credential_: The Windows user the Task runs as. Use it with Connections that use Windows authentication. See [Global - Credentials](../../global-credentials)
- _Source connection_: The SQL Connection to the database the tables are copied from. Select a Connection in the list, or click the icon next to it to open _Manage Connections_; see [Global - Connections](../../global-connections)
- _Destination connection_: The SQL Connection to the database the tables are copied to. A table that does not exist there is created

**Table sync parameters**

- _Table name(s)_: The tables to copy. Select one or more tables in the list
- _Schema name_: The schema in which the Task creates its tracking tables and procedures, in both databases. The default is "sync"
- _One time copy_: When selected, the tables are copied once, and the tracking objects are removed after the copy. When cleared, the default, the Task installs triggers on the source tables to track changes, so that the next run applies only the changes

Changes are copied in one direction only, from the source to the destination. Changes made in the destination are not copied back.

### Output and errors

- The output of the Task is a line with the number of changes applied, failed and in total

### Troubleshooting

**Retrieving the COM class factory for component with `CLSID {EC413D66-6221-4EBB-AC55-4900FB321011}` failed due to the following error: 80040154 Class not registered (Exception from `HRESULT: 0x80040154 (REGDB_E_CLASSNOTREG)`).**

Install the Microsoft Sync Framework. See link on top of this page.
