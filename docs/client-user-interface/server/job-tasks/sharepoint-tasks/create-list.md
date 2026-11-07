---
sidebar_label: 'Task Sharepoint - Create List'
hide_title: 'true'
---
## Task SharePoint - Create List

The SharePoint - Create list Task creates a list on a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Create list tab with the Connection, list settings and the Columns grid](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Create%20List.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create list tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Title_: the title of the new list
- _Description_: a description of the new list
- _Template type_: the SharePoint list template to create the list from. The default is "DocumentLibrary"
- _Quick launch_: "On" (default), "Off" or "DefaultValue", whether the list is shown in the Quick launch of the site
- _Enable attachments_, _Enable versioning_ and _Enable folder creation_: whether items can have attachments, whether versions are kept, and whether folders can be added to the list. All are cleared by default. The Create list Task does not save these three settings to the new list; to set them, run a [SharePoint - Update list](update-list) Task after it
- _Columns_: the columns to add to the list, one row each with _SchemaXML_ and _DefaultView_. Click _Add_, _Edit_ or _Remove_ to change the rows

Variables are resolved in _Title_, _Description_ and the column schema.

_Add_ and _Edit_ open the _Add/Edit column_ window:

![Add/Edit column window with the Schema XML box and the Default view check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Create%20List%20Schema.png)

- _Schema XML_: the definition of the column in the SharePoint field schema format. Read more here: [http://msdn.microsoft.com/en-us/library/office/ms457586.aspx](http://msdn.microsoft.com/en-us/library/office/ms457586.aspx)
- _Default view_: add the column to the default view of the list

For example, a single line of text column:

```xml
<Field Type="Text" DisplayName="Customer" Name="Customer" />
```

### Output and errors

The Task does not write output. When the list cannot be created, for example because a list with the same title exists, the Task fails with the error from SharePoint.
