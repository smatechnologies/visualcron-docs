---
sidebar_label: 'Supported Permissions'
hide_title: 'true'
---

## Supported Permissions

This page lists every permission in the _Add/Edit user group_ window, and what each action controls. Use it when you design a group. For how groups, users and overrides work, see [Main - User Permissions](../server/main-user-permissions).

In the table:

- "Yes": you can check or clear the box
- "Always": the box is grayed out and always granted
- blank: the box is grayed out and never granted

The table shows a group you create with _Add_. The built-in Viewers group has some boxes grayed out in other places.

:::warning

A new group starts with every "Yes" box checked, except _Add_, _Edit_, _Execute_ and _Delete_ on _Remote file explorer_. Clear every action the group must not have before you save it.

:::

| Permission | What it controls | Read | Add | Edit | Execute | Delete |
|---|---|:---:|:---:|:---:|:---:|:---:|
| Audit log | _Read_: open the audit log | Yes | | | | |
| Certificates | _Read_: view Certificates and export them, private keys included. _Add_, _Edit_, _Delete_: manage Certificates | Yes | Yes | Yes | | Yes |
| Client connections | _Read_: see the Clients connected to the Server | Yes | | | | |
| Client settings | Not used | Yes | | Yes | | |
| Cloud settings | _Read_: open the VisualCron Cloud windows. _Delete_: remove the Server from the cloud. Other cloud actions need _Read_ on _Server settings_. _Add_, _Edit_ and _Execute_ are not used | Yes | Yes | Yes | Yes | Yes |
| Conditions | View, add, edit and delete Conditions | Always | Yes | Yes | | Yes |
| Connections | View, add, edit and delete Connections. _Execute_: browse the remote system through a Connection, and use the Connection in a run that a user starts. That is a single _Run Job_ or _Run Task_ started from a Client, or a Task run requested through the Web API with a user (`Task/Run`). Runs started by the schedule or by a Trigger, _Run selected Jobs_, and Jobs started through the Web API (`Job/Run`) are not tied to a user, so no check is made. This check uses the group's _Connections_ row only, not overrides on the Connection | Yes | Yes | Yes | Yes | Yes |
| Credentials | View, add, edit and delete Credentials. For _Read_ and _Execute_, see [Credentials permission](../server/main-user-permissions#credentials-permission) | Yes | Yes | Yes | Yes | Yes |
| Execution distribution | _Read_: open the windows in the _Execution distribution_ group. _Edit_: change load balancing flows, broker and distributed execution settings. _Add_ and _Delete_ are not used | Yes | Yes | Yes | | Yes |
| Exit codes | View, edit and delete exit codes | Yes | Always | Yes | | Yes |
| Export settings | _Read_: open the _Export settings_ window. _Edit_ and _Execute_: start the export. See the warning below | Yes | | Yes | Yes | |
| Health levels | _Edit_: change the predefined Server health levels. _Read_, _Add_ and _Delete_ are not used | Yes | Yes | Yes | | Yes |
| Import settings | _Read_: open the _Import settings_ window. _Edit_ and _Execute_: start the import. See the warning below | Yes | | Yes | Yes | |
| Jobs | View, add, edit, run and delete Jobs | Yes | Yes | Yes | Yes | Yes |
| License | _Read_: view the license. _Execute_: activate or deactivate the license. The desktop Client checks _Execute_, except when it activates a Server that runs a trial license. The Server checks _Execute_ only for requests through the Web API | Yes | | | Yes | |
| Log | _Read_: view the Server log | Yes | | | | |
| Network drives | View, add, edit and delete network drives | Yes | Yes | Yes | | Yes |
| Notifications | View, add, edit and delete Notifications | Always | Yes | Yes | | Yes |
| Object finder | _Read_: open the Object finder | Yes | | | | |
| PGP Key Rings | _Read_: view key rings and export keys, private keys included. _Add_, _Edit_, _Delete_: manage key rings. _Delete_ is checked by the desktop Client only | Yes | Yes | Yes | | Yes |
| Processes | _Read_: open the running processes. _Delete_: stop a running Job or Task, and end a process with _End process_ in the Task manager. See the note below | Yes | | | | Yes |
| Remote file explorer | _Read_: browse and download files on the Server. _Add_: create files and folders, paste and copy. _Edit_: rename, move and change attributes. _Delete_: delete files and folders. _Execute_ is not used. See the warning below | Yes | Yes | Yes | Yes | Yes |
| Server settings | _Read_: open the Server settings window. _Edit_: apply changes with _Apply settings_ | Yes | | Yes | | |
| Server sync | View, add, edit and delete Server sync settings. _Execute_ is not used | Yes | Yes | Yes | Yes | Yes |
| SQL Explorer | _Read_: open SQL Explorer. _Execute_: run queries | Yes | | | Yes | |
| SSH keys | _Read_: view SSH keys and export them, private keys included. _Add_, _Edit_, _Delete_: manage SSH keys | Yes | Yes | Yes | | Yes |
| Task manager | _Read_: open the Task manager. _Edit_: manage services and change process priority. _Execute_: start a process. _Delete_: end a process tree with _End process tree_. Ending a single process with _End process_ needs _Delete_ on _Processes_. See the warning below | Yes | | Yes | Yes | Yes |
| Task repository | View, add, edit and delete Tasks in the Task repository. _Execute_ is not used | Yes | Yes | Yes | Yes | Yes |
| Tasks | View, add, edit, run and delete Tasks | Yes | Yes | Yes | Yes | Yes |
| Time exceptions: Collections | View, add, edit and delete time exception collections | Yes | Yes | Yes | | Yes |
| Time exceptions: Exceptions | View, add, edit and delete time exceptions | Yes | Yes | Yes | | Yes |
| Triggers | View, add, edit and delete Triggers | Yes | Yes | Yes | | Yes |
| User permissions | View users and groups (always granted). _Add_, _Edit_ and _Delete_: manage users and groups | Always | Yes | Yes | | Yes |
| Variables | View, add, edit and delete Variables | Yes | Yes | Yes | | Yes |

:::warning

- _Import settings_ lets a user replace users, groups, Credentials and other settings. The _Import settings_ window offers only the object types the user may add, but the Server runs the import itself with full rights and does not check the user's other permissions
- _Export settings_ exports the selected settings, Credentials and users included. The _Export settings_ window offers only the objects the user has _Read_ on, but the Server does not check _Read_ on what it exports
- Give these two permissions only to administrators

:::

:::warning

_Read_ on _Remote file explorer_ is granted to every new group and to Viewers. It lets a user download any file the VisualCron service account can read. Clear it for groups that must not see the Server's files.

:::

:::warning

The _Task manager_ permissions are checked by the desktop Client only. The Server does not check them when it receives a request to start or end a process or to control a service. The same applies to _Delete_ on _Processes_ when it is used for _End process_. Give logons to the Server only to people you trust with the processes and services on the Server computer.

:::

:::note

Pausing or resuming a running Job or Task needs _Execute_ on _Processes_. That box is grayed out, so the Server refuses pause and resume requests from the Client.

:::
