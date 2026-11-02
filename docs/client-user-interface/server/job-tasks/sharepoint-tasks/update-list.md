---
sidebar_label: 'Task Sharepoint - Update List'
hide_title: 'true'
---
## Task SharePoint - Update List

The SharePoint - Update list Task changes the title, description and settings of a list on a SharePoint site, and can add columns to it, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Update list tab with the Connection, list settings and the Columns grid](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Update%20List.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Update list tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Title_: the current title of the list. Click the button next to the box to show the lists of the site
- _New title_: the title to give the list. The Task always sets the title to this value, so enter the current title to keep it
- _Description_: the description to give the list. The Task always sets the description to this value; an empty box clears the description
- _Template type_: not used by this Task. The template of an existing list cannot be changed
- _Quick launch_: "On" shows the list in the Quick launch of the site; "Off" and "DefaultValue" remove it
- _Enable attachments_, _Enable versioning_ and _Enable folder creation_: whether items can have attachments, whether versions are kept, and whether folders can be added. The Task always applies all three, so a cleared check box turns the setting off
- _Columns_: columns to add to the list, one row each with _SchemaXML_ and _DefaultView_. Click _Add_, _Edit_ or _Remove_ to change the rows. Existing columns are not changed. Read more about the schema here: [http://msdn.microsoft.com/en-us/library/office/ms457586.aspx](http://msdn.microsoft.com/en-us/library/office/ms457586.aspx)

Variables are resolved in _Title_, _New title_, _Description_ and the column schema.

### Output and errors

The Task does not write output. When no list has the title in _Title_, the Task fails with the error from SharePoint.
