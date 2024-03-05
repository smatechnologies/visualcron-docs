---
sidebar_label: 'Task Process - Execute Script'
hide_title: 'true'
---

## Task Process - Execute Script

This Task type is a version of the Execute Task - specialized for script execution. This Task executes VBScripts and JScripts.

![](../../../static/img/taskprocessexecutescript.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**File path**

This is the full path to the script file.
 
**Notes:**

* This Task will return error if the standard error is not empty.
* Please view standard error or standard output column for more information.
* The standard error column will contain details about row number when failed.
 
**Troubleshooting**
 
**Input Error: There is no script engine for file extension**

Make sure you are using quotes properly in the arguments. Use double quotes for folders/arguments with a space in it.