---
sidebar_label: 'Task XML - Edit Node'
hide_title: 'true'
---

## Task XML - Edit Node

The Edit Node Task changes the value of a node, or of one of its attributes, in an XML file.

![Edit Node tab with the Credentials, File name, XPath expression, Attribute (optional), Value and Edit node fields and the Namespaces list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Edit%20Node.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

The Task saves its changes to the XML file itself and keeps no copy of the original file.

Without an attribute, the new value replaces the whole content of the node. If the node has child nodes, they are removed.

When _Attribute (optional)_ is set and a selected node does not have that attribute, nothing is changed in that node, no error is raised, and the Task reports success.

:::

### Edit Node tab

- _Credentials_: The Credential the Task uses to read and save the file. Select a Credential in the list, or click the icon next to it to open _Manage credentials_. With no Credential, the file is accessed under the account of the VisualCron Server
- _File name_: The full path of the XML file
- _XPath expression_: The XPath expression that selects the node to edit. To build the expression, click the button next to the field and select a node in the XML Browser; the button is available when _File name_ is set
- _Attribute (optional)_: The name of an attribute. When set, the new value is written to this attribute instead of to the node
- _Value_: The new value. The field must not be empty
- _Edit node_: Which of the selected nodes are changed. The default is "First"
    - "First": Only the first node that the XPath expression selects
    - "All": Every node that the XPath expression selects
- _Namespaces_: The namespace prefixes and URIs that the XPath expression can use. When the list is empty, the Client fills it with the namespaces declared in the file, with the prefix "x" for a default namespace. Use _Add_, _Edit_ and _Remove_ to change the list, and _Reload_ to read the namespaces from the file again

At run time, the Task also adds the namespaces declared in the file, with the prefix "x" for a default namespace ("xx" if "x" is already in use). With "First", when the XPath expression selects nothing, the Task tries it again with a namespace prefix added to each step of the path that has none.

Variables can be used in _File name_, _XPath expression_, _Attribute (optional)_, _Value_ and the namespace prefixes and URIs.

### Output and errors

- The output of the Task is the inner XML of the edited node. With "All", it is the inner XML of the last edited node
- When the XPath expression selects no node, the Task fails, and the file is not changed. With "First", the error is "Node does not exist."
