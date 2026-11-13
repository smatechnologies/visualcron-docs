---
sidebar_label: 'Task System Restore - Create Restore Point'
hide_title: 'true'
---

## Task System Restore - Create Restore Point

The Create restore point Task creates a Windows System Restore point on the Server computer or on a remote computer.

 ![Create restore point tab, with the Credential, the scope and the restore point settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Restore%20Tasks/Create%20Restore%20Point.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create restore point tab

**Credentials**

The Credential used to connect to the remote computer. Use it only with _Remote_: Windows does not accept a user name and password for a connection to the local computer, and the Task fails. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials).

**Scope**

- _Local_ (default): creates the restore point on the Server computer
- _Remote_: creates the restore point on another computer
- _Hostname_: the name of the remote computer. Type it or select it from the list of network computers. Available with _Remote_

**Create restore point**

- _Description_: a short description of the restore point. It may contain Variables
- _Event type_: the type of system change event, "Begin system change" (default), "End system change", "Begin nested system change" or "End nested system change"
- _Restore point type_: the reason for the restore point, "Application modification" by default. Other values include "Application installation", "Application removal", "Device driver installation", "Checkpoint" and "Critical update"

### Output and errors

The output is "Create restore point - success". If Windows does not create the restore point, the output gives the return code and the Task fails.
