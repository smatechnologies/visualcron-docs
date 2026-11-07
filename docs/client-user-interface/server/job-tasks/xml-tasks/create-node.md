---
sidebar_label: 'Task XML - Create Node'
hide_title: 'true'
---

## Task XML - Create Node

The Create Node Task adds a node to an existing XML file. An XPath expression selects the parent nodes, and the Task adds the new node, with its value and attributes, to each parent node it selects.

![Create Node tab, General sub tab, with the Credentials, File name, XPath expression, Name, Value and If node already exists fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Create%20Node.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

The Task saves its changes to the XML file itself and keeps no copy of the original file.

The Task reads and saves the file under the account of the VisualCron Server. A Credential selected in _Credentials_ is not used.

With "Skip" in _If node already exists_, the new node is still added to a parent that already has a child node with the same name, so that parent then has two nodes with that name.

:::

### General tab

- _Credentials_: A Credential can be selected, but the Task does not use it. The account of the VisualCron Server needs read and write access to the file
- _File name_: The full path of the XML file. The file must exist
- _XPath expression_: The XPath expression that selects the parent nodes. The new node is added to every node that the expression selects. To build the expression, click the button next to the field and select a node in the XML Browser; the button is available when _File name_ is set
- _Name_: The name of the new node
- _Value_: The text of the new node
- _If node already exists_: What the Task does when a parent node already has a child node with the same name. The default is "Fail"
    - "Ignore": The new node is added
    - "Skip": The new node is currently added, as with "Ignore"
    - "Overwrite": The existing child nodes with that name are removed, and the new node is added
    - "Fail": The Task fails, and the file is not saved
- _Namespace (optional)_: The namespace URI of the new node
- _Prefix_: The namespace prefix of the new node
- _Insert as first child node_: When selected, the new node is added before the existing child nodes of the parent. When cleared, the default, it is added after them

Variables can be used in all of these fields and in the attribute names and values.

The XPath expression is run without a namespace list, so it cannot use namespace prefixes. To select nodes in a namespace, use `local-name()`, for example:

```text
/*[local-name()='catalog']/*[local-name()='book']
```

### Attributes tab

![Create Node tab, Attributes sub tab, with the Name and Value grid and the Add and Remove buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Create%20Node%20Attributes.png)

The attributes in this list are added to the new node. Click _Add_ to add a row, then enter the _Name_ and _Value_ of the attribute. To delete a row, select it and click _Remove_.

### Output and errors

- The output of the Task is the whole XML document after the change. When the Task fails, the output can show changes that were not saved to the file
- When the XPath expression selects no node, the Task fails with the error "Node does not exist.", and the file is not changed
