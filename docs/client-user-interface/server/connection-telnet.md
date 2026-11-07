---
sidebar_label: 'Connection - Telnet'
hide_title: 'true'
---

## Connection - Telnet

The Telnet Connection stores the address, sign-in and prompt settings that the Net - Telnet Task uses to connect to a Telnet server.

:::warning

Telnet sends the user name, the password and all data unencrypted. Use an [SSH Connection](connection-ssh) where the server supports SSH.

:::

### Common settings

![Telnet Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telnet/Telnet.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy). Telnet Connections have no *Test*. *Timeout* is how long, in seconds, the Server waits for each prompt, and *Code page* is the character set of the terminal session.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![Telnet Connection, Main settings tab, with the Server, Credentials, New line and Emulation groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telnet/Settings.png)

- _Address_: the host name or IP address of the Telnet server
- _Port_: "23" on a new Connection
- _Username_: required. The Server types it at the login prompt
- _Password_: the Server types it at the password prompt
- _New line (server system)_: what the Server sends at the end of each line it types. "Cr (\*nix)" sends a carriage return and "CrLf (Windows)" sends a carriage return and a line feed. "Cr (\*nix)" on a new Connection
- _Emulation_: the terminal type: "ANSI", "TTY", "VT100", "VT220", "VT320" or "VT52". "VT100" on a new Connection

### Extra settings

![Telnet Connection, Extra settings tab, with the prompt pattern fields, Width and Height](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telnet/Extra%20Settings.png)

The Server logs on by waiting for each prompt and then typing the next value. A pattern matches when the server's output contains it.

- _Login prompt pattern_: text in the prompt that asks for the user name. When it is empty, the Server waits for ":"
- _Password prompt pattern_: text in the prompt that asks for the password. When it is empty, the Server waits for ":"
- _Command prompt pattern_: text in the prompt that shows the server is ready for a command
- _Command prompt regex pattern_: a regular expression for a command prompt that changes. Used only when *Command prompt pattern* is empty. When both are empty, the Server waits for ">"
- _Width_: the terminal width in characters. "80" on a new Connection
- _Height_: the terminal height in lines. "25" on a new Connection

:::warning

A new Telnet Connection shows values in *Login prompt pattern*, *Password prompt pattern* and *Command prompt pattern* that are not Telnet prompts. Replace them with text from your server's prompts, or clear them to use the defaults above. Otherwise the Server does not recognize the prompts, and the logon fails.

:::

### Proxy

Telnet Connections can use "HTTP Proxy", "SOCKS4" and "SOCKS5" proxies. They send the proxy *Username* and *Password* when *Use credentials* is selected, and do not use *Authentication*.
