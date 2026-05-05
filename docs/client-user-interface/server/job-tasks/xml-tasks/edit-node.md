---
sidebar_label: 'Task XML - Edit Node'
hide_title: 'true'
---

## Task XML - Edit Node

The Edit Node Task lets you change a specific node value or attribute in a XML file.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Edit%20Node.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
**File name**

The full path to the XML file.
 
**XPath expression**

XPath is a query language used for finding a specific object within XML. Enter the query manually or use the XPath browser by clicking the button.
 
**Attribute (optional)**

If a specific attribute should be edited then set the attribute name here.
 
**Value**

The new value to set in the node.
 
**Edit node**

Controls which matching nodes are edited. Options:

* **First** — Edit only the first node found by the XPath expression.
* **All** — Edit all nodes found by the XPath expression.

**Namespaces**

VisualCron tries to load all namespaces that a XML file contains. If you want to add one namespace manually you can click on Add. If you want to reload all namespaces you can click on Reload.
