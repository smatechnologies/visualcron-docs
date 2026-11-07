---
sidebar_label: 'Task XML - Delete Node'
hide_title: 'true'
---

## Task XML - Delete Node

The Delete Node Task deletes nodes, or one attribute of nodes, from an XML file. It deletes every node that the XPath expression selects.

![Delete Node tab with the Credentials, File name, XPath expression and Attribute (optional) fields and the Namespaces list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Delete%20Node.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

Every node that the XPath expression selects is deleted, not only the first one, together with its child nodes. Check what the expression selects in the XML Browser before you run the Task.

The Task saves its changes to the XML file itself and keeps no copy of the original file.

The Task reads and saves the file under the account of the VisualCron Server. A Credential selected in _Credentials_ is not used.

:::

### Delete Node tab

- _Credentials_: A Credential can be selected, but the Task does not use it. The account of the VisualCron Server needs read and write access to the file
- _File name_: The full path of the XML file
- _XPath expression_: The XPath expression that selects the nodes to delete. To build the expression, click the button next to the field and select a node in the XML Browser; the button is available when _File name_ is set
- _Attribute (optional)_: The name of an attribute. When set, only this attribute is removed from each selected node, and the nodes are kept. A selected node that does not have the attribute is left as it is
- _Namespaces_: The namespace prefixes and URIs that the XPath expression can use. When the list is empty, the Client fills it with the namespaces declared in the file, with the prefix "x" for a default namespace. Use _Add_, _Edit_ and _Remove_ to change the list, and _Reload_ to read the namespaces from the file again. At run time, only the namespaces in this list are used

Variables can be used in _File name_, _XPath expression_ and _Attribute (optional)_.

### Output and errors

- When the XPath expression selects no node, the Task fails with the error "Node does not exist", and the file is not changed
- The Task writes no output
