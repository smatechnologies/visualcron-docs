---
sidebar_label: 'Task Process - Execute Script'
hide_title: 'true'
---

## Task Process - Execute Script

This Task type is a version of the Execute Task - specialized for script execution. This Task executes VBScripts and JScripts.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/Execute%20Script.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Script file**

Select this option to execute a script from an existing file. When selected, enter the full path to the script file in the **File path** field. The rightmost button opens a file browser for selection.
 
**Script text**

Select this option to enter the script inline. When selected, type or paste your VBScript or JScript directly into the script editor below. This is useful for short scripts that you want to manage within VisualCron rather than as external files.
 
**Notes:**

* This Task will return error if the standard error is not empty.
* Please view standard error or standard output column for more information.
* The standard error column will contain details about row number when failed.
 
**Troubleshooting**
 
**Input Error: There is no script engine for file extension**

Make sure you are using quotes properly in the arguments. Use double quotes for folders/arguments with a space in it.
