---
sidebar_label: 'Task Sharepoint - Get List'
hide_title: 'true'
---

## Task Sharepoint- Get List

The SharePoint - Get List Task retrieves a list of Lists from the SharePoint library.
 
The SharePoint Tasks supports the following versions:

* SharePoint 2010
* SharePoint 2013
* SharePoint Online

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Get%20Lists.png)

**Connection**

To use SharePoint Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Title**

The displayed title for the list. Click the refresh button to list all available titles.
 
**CAML Query**

The query in CAML format to select one or more List items. Click the *CAML browser* button to open the CAML query builder dialog to help construct a valid query.
 
**Field(s)**

The grid lists the available fields for the selected list. Each row has a **Use** checkbox and a **Name** column showing the field name. Check the **Use** checkbox for each field you want included in the results. Click the *Refresh fields* button to populate the grid with all available fields from the selected list.

**Output** tab

Controls the format and destination of the task results. Options include field separator, text qualifier, line break style, and whether to send output to the standard task output or write it to a file. When writing to a file, a file path and optional credential can be specified.
