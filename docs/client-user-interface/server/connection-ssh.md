---
sidebar_label: 'Connection - SSH'
hide_title: 'true'
---

## Connection - SSH

The SSH Connection stores the address, sign-in and security settings that the [Net - SSH](job-tasks/net-tasks/ssh) Task uses to connect to an SSH server, for example to run commands on a Linux or Unix server. SSH (Secure Shell) encrypts the sign-in, the commands and their output between the VisualCron Server and the SSH server.

:::warning

SSH Connections accept any server host key. The Server does not compare the key with a stored key, so it cannot tell the real server from another server that answers at the same address. Confirm the server's host key with its administrator before you use the Connection. With *Log received messages to task output* selected, the Task output shows the MD5 fingerprint of the key that the server sent, as pairs of hexadecimal digits separated by colons. Ask the administrator for the MD5 fingerprint of the key to compare with it.

:::

### Common settings

![SSH Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSH/SSH.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy). SSH Connections have no *Test*. *Timeout* is "0" on a new SSH Connection. It is how long, in seconds, the Server waits for the SSH server; with "0", commands have no time limit from the Connection, and the timeout settings of the Net - SSH Task apply.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![SSH Connection, Main settings tab, with the Server and Credentials groups and the Override authentication options](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSH/SSH%20Setting.png)

- _Address_: the host name or IP address of the SSH server
- _Port_: "22" on a new Connection
- _Authentication type_: "Password" or "Public key". With "Public key", *Password* is hidden and *SSH key* is shown
- _Username_: the account on the server
- _Password_: the account's password, for password and keyboard logons
- _SSH key_: for "Public key", the key to log on with, chosen from the keys stored in [Global - SSH Keys](global-ssh-keys). The key's passphrase is stored with the key
- _Override authentication_: the logon methods the Server tries:
  - _Auto authentication_: try password and keyboard-interactive logon. While it is selected, the two options below are unavailable. Cleared on a new Connection
  - _Password authentication_: selected on a new Connection
  - _Keyboard authentication_: keyboard-interactive logon. Cleared on a new Connection

With "Public key", the Server also tries a public key logon with the *SSH key*.

### Encryption

![SSH Connection, Encryption tab, with the four algorithm lists](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSH/Encryption.png)

The ***Encryption*** tab has one list each for *Encryption algorithms*, *Key exchange algorithms*, *MAC algorithms* and *Public key algorithms*, each with its own option to choose the algorithms automatically. They are selected on a new Connection. Clear one to choose the allowed algorithms in its list, with *Select all* and *Deselect all*. For SSH Connections:

- _Auto adjust MAC algorithms_: while it is selected, the Server offers only "hmac-md5", "hmac-sha1" and "hmac-sha2-256". If the server needs another MAC algorithm, clear it and select that algorithm
- _Auto adjust key exchange algorithms_: keep it selected. A manual selection in *Key exchange algorithms* is not applied as the list shows it
- _Auto adjust by component_ and the *Public key algorithms* list: not used by SSH Connections

The server must support at least one of the algorithms you allow, or the connection fails.

### Extra settings

![SSH Connection, Extra settings tab, with the shared settings, SSH version support, New line, Emulation and the log options](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSH/Extra%20Settings.png)

- _Transfer type_: not used by SSH Connections
- _KeepAlive_: not used by SSH Connections. To send keepalives, use *SendKeepAlive every* in the [Net - SSH](job-tasks/net-tasks/ssh) Task
- _SSH version support_: "1" and "2". Both are selected on a new Connection
- _New line (server system)_: what the Server sends at the end of each line it types. "Cr (\*nix)" sends a carriage return and "CrLf (Windows)" sends a carriage return and a line feed. "Cr (\*nix)" on a new Connection
- _Emulation_: the terminal type the Server asks for: "ANSI", "TTY", "VT100", "VT220", "VT320" or "VT52". "VT100" on a new Connection
- _Log sent messages to task output_: writes the messages that the Server sends into the Task output
- _Log received messages to task output_: writes the messages from the SSH server, including the MD5 fingerprint of the host key, into the Task output

:::warning

SSH version 1 is allowed by default. It is obsolete and not secure. Clear "1" in *SSH version support* unless the server supports only SSH version 1.

:::

### Proxy

![SSH Connection, Proxy tab, with the proxy type, address, port, test URL, authentication and credential fields and the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSH/Proxy.png)

SSH Connections can use "HTTP Proxy", "SOCKS4" and "SOCKS5" proxies, and use *Authentication*.

:::warning

A new Connection has *Authentication* "Not set" and *Use credentials* selected. With "HTTP Proxy" and those settings, the Server sends the SSH *Username* and *Password* to the proxy instead of the proxy account. Set *Authentication* to "Basic", "Digest" or "NTLM" to send the proxy *Username* and *Password*.

:::
