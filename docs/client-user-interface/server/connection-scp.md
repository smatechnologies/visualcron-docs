---
sidebar_label: 'Connection - SCP'
hide_title: 'true'
---

## Connection - SCP

The SCP Connection stores the address and sign-in settings that the [Net - FTP/FTPS/SFTP/SCP](job-tasks/net-tasks/ftp) Task, the [Cloud - Sync file(s)](job-tasks/cloud-transfer-tasks/sync) Task and the [Event Trigger - Remote File](event-trigger-remote-file) Trigger use to connect to a server over SCP (Secure Copy). SCP copies files over an SSH connection. SCP Connections have no ***Proxy*** tab.

:::warning

SCP Connections accept any server host key. The Server does not compare the key with a stored key, so it cannot tell the real server from another server that answers at the same address. Confirm the server's host key with its administrator before you use the Connection.

:::

### Common settings

![SCP Connection, Common settings tab, with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SCP/SCP.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings). For SCP Connections:

- _Test_: the Server connects and logs on with the settings in the window, and lists the root folder of the server
- _Timeout_: how long, in seconds, the Server waits for the server. With "0", it waits up to about 24 hours
- _Code page_: not used for the connection. The SCP session always uses UTF-8

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![SCP Connection, Main settings tab, with the Server, Credentials and Log traffic groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SCP/SCP%20Setting.png)

- _Address_: the host name or IP address of the server
- _Port_: "22" on a new Connection
- _Authentication type_: "Password" or "Public key". With "Public key", *Password* is hidden and *SSH key* is shown
- _Username_: the account on the server. Enter it for both authentication types
- _Password_: the account's password, for "Password"
- _SSH key_: for "Public key", the key to log on with, chosen from the keys stored in [Global - SSH Keys](global-ssh-keys). The key's passphrase is stored with the key
- _Log sent messages to task output_: writes the messages that the Server sends into the Task output
- _Log received messages to task output_: writes the messages that the server returns into the Task output
