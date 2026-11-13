---
sidebar_label: 'Task Sharepoint - Get List Item'
hide_title: 'true'
---
## Task SharePoint - Get List Item

The SharePoint - Get list item(s) Task returns the items of a list on a SharePoint site that match a CAML query, with the fields you choose, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Get list item(s) tab with the Connection, Title list, CAML Query box and the Field(s) grid](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Get%20list%20items.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get list item(s) tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Title_: the title of the list. Click the button next to the box to show the lists of the site
- _CAML Query_: the query in CAML format that selects the items. The default, `<View><Query></Query></View>`, selects all items. The button next to the box opens the CAML query builder
- _Field(s)_: one row for each field of the list, with the columns _Use_ and _Name_. Check _Use_ for each field to return. Click _Refresh fields_ to fill the grid with the fields of the list in _Title_

Variables are resolved in _Title_, _CAML Query_ and the field names.

### Get list item(s): Output tab

The ***Output*** tab sets the format of the result:

- _Output to standard output_ (default) or _Output to file_: where the result is written
- _Include field names_: write the names of the checked fields as the first line
- _Field separator_, _Text qualifier_ and _Line break_: the character between fields, the character around each value, and the line break between items
- _Indent XML_: not used by this Task
- _File output settings_: with _Output to file_, the Credential to write the file as, _File path_, _Append to file_ and _Include BOM (if UTF8)_

### Output and errors

The output of the Task is one line for each item, with the values of the checked fields in the order of the grid. A person or lookup field returns the display value; several people are separated by ";". When the list cannot be read or the query is not valid, the Task fails with the error from SharePoint.
