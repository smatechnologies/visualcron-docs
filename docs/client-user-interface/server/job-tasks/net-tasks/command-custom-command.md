---
sidebar_label: 'Command - Custom Command'
hide_title: 'true'
---

## Command - Custom Command

The "Custom command" command type sends one or more FTP commands that VisualCron has no command type for. Not every FTP server supports every command. To find out which commands a server supports, send the `HELP` command with _Log received messages to task output_ selected on the FTP Connection; see [Connection - FTP](../../connection-ftp). The server's replies are then written to the Task output.

:::warning

"Custom command" works only with FTP and FTPS Connections. The _Add/Edit command_ window does not accept it with an SFTP Connection. With an SCP Connection the command can be saved, but the Server does not send the commands, and the Task continues as if they had been sent. To run commands on an SSH server, use the SSH Task; see [Task Net - SSH](ssh).

:::

Commands that need a data connection, such as `STOR` (upload), `RETR` (download), `NLST` and `LIST`, are not supported. Use the "Upload", "Download" and "List file(s)" command types instead.

### Custom command tab

![Custom command tab of the Add/Edit command window, with the Custom command(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Custom%20Command.png)

- _Custom command(s)_: one or more FTP commands, one per line

  Each line is sent to the server as a separate command, in order. Blank lines are skipped, and Variables are replaced before the commands are sent. The field is required.

The Task output lists the commands that were sent. VisualCron does not check the server's reply to each command. To see the replies, select _Log received messages to task output_ on the Connection, and check them in the Task output.
