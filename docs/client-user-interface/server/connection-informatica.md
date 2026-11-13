---
sidebar_label: 'Connection - Informatica'
hide_title: 'true'
---

## Connection - Informatica

The Informatica Connection stores the address, sign-in and security settings that the [Informatica - Run Job](job-tasks/informatica-tasks/run-job) Task uses to connect to Informatica Cloud.

The Connection works only with Informatica Cloud. It does not connect to an Informatica installation on your own servers.

### Common settings

![Informatica Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Informatica/Informatica.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For an Informatica Connection, no _Test_ button is shown, and _Timeout_ and _Code page_ are not used.
 
### Main settings

![Informatica Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Informatica/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Login_ are required.

:::warning

When this Connection logs on, it sets the SSL and TLS versions for the whole VisualCron Server process to SSL 3, TLS 1.0, TLS 1.1, TLS 1.2 and TLS 1.3, and the Server accepts any server certificate for HTTPS calls in the Server process, including the certificate of the Informatica server. Make sure that the Server reaches Informatica Cloud only through networks and proxies that you trust.

:::

- _Address_: the host name of your Informatica Cloud server, without `https://` or a path. VisualCron adds `https://` and the API path, and uses the same host to log on and to run jobs
- _Login_: the user name of your Informatica Cloud account
- _Password_: the password for that account
