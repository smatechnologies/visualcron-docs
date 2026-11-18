---
sidebar_label: 'Task Net - SSH'
hide_title: 'true'
---

## Task Net - SSH

The SSH Task runs commands on a remote SSH server, for example a Linux or Unix server, and returns their output as the output of the Task. SSH servers are standard on Linux and are available for most other operating systems, so the Task lets you run work on computers that do not run VisualCron.

![SSH Task settings, with the Command type group, the commands grid, the Connection group and the Add/Edit SSH command window](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/SSH.png)

:::warning

This Task uses an SSH Connection; see [Connection - SSH](../../connection-ssh). The server host key is never checked; there is no setting for it.

A new Connection has the proxy _Authentication_ "Not set" with _Use credentials_ selected. With _Proxy type_ "HTTP Proxy", the Server then sends the user name and password of the SSH server to the proxy. To prevent this, set _Authentication_ to "Basic", "Digest" or "NTLM", or clear _Use credentials_.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Connection

Select the SSH Connection with the server's address and sign-in in the _Connection_ group. To add or change one, see [Global - Connections](../../global-connections) and [Connection - SSH](../../connection-ssh).

### Command type

- _Command type_: how the commands are sent:
  - "Send command" (default): runs each command on its own, waits for it to finish and collects all its output. Use it for commands that need no interaction
  - "Send Text": opens one interactive shell session and types each command into it, as a user would at a terminal. Use it for commands that depend on each other or need a terminal
- _Receive timeout_: "Send Text" only. How long, in seconds, the Task collects output after each text it sends

  Each text waits this long unless the session closes first. The default is "10".

- _SendKeepAlive every_: when selected, the Server sends keep-alive packets at the interval you set, in seconds, so that the server does not drop the connection

  Cleared by default. The interval is "30" by default, with a minimum of "5".

### Commands

The commands run in the order of the _Order_ column. The _Command/Text_ column shows each command. The toolbar above the grid has _Add_, _Edit_, _Clone_, _Delete_ and _Change order_.

To add a command, complete the following steps:

1. Click _Add_ on the toolbar.
2. In the _Add/Edit SSH command_ window, enter the command in _Text to send_.
3. (Optional, "Send command" only) In _Environment variables_, enter the variables that the command needs, one per line.
4. Click _OK_.

The command is added to the grid. To edit a command, double-click it, or select it and click _Edit_. To move a command, select it and set its position in _Change order_. You can also right-click the grid to _Add_, _Edit_, _Clone_ or _Delete_ a command.

With "Send command", the server's environment variables are not loaded automatically, so enter the ones the commands need in _Environment variables_.

### Output and errors

The output of each command is added to the output of the Task. To keep the outputs of different commands apart, use one Task for each command.

With "Send command", every command runs, even after one fails. When a command ends with a non-zero exit status, its message is written to the standard error output, the Task gets a non-zero exit code error (see [Task - On Error](../../task-on-error)), and the exit code of the Task is the last non-zero exit code.

:::warning

With "Send Text", the Task does not get the exit status of each command, so a command that fails does not make the Task fail. To detect a failure, check the output, for example with the output conditions on the ***On error*** tab.

:::
