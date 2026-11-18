---
sidebar_label: 'Connection - IBM Cognos Analytics'
hide_title: 'true'
---

## Connection - IBM Cognos Analytics

The IBM Cognos Analytics Connection stores the address, sign-in and security settings that the IBM Cognos Analytics - Run report and IBM Cognos Analytics - Run job Tasks use to connect to IBM Cognos Analytics.

### Common settings

![IBM Cognos Analytics Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IBM%20Cognos%20Analytics/IBM%20Cognos%20Analytics.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For an IBM Cognos Analytics Connection, no _Test_ button is shown, and _Timeout_ and _Code page_ are not used. The Cognos Tasks use the Task timeout.
 
### Main settings

![IBM Cognos Analytics Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IBM%20Cognos%20Analytics/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_, _Port_ and _Username_ are required.

:::warning

The IBM Cognos Analytics Connection connects to the server over HTTP. The user name, the password and the report data are sent without encryption. Use this Connection only on a network that you trust.

:::

- _Address_: the host name or IP address of the IBM Cognos Analytics server, without `http://`, a port or a path. VisualCron adds the scheme, the port and the path of the Cognos dispatcher
- _Port_: the port of the Cognos dispatcher. The default is "9300". The value "0" is not accepted
- _Authentication type_: how the Tasks log on:
  - "Harmony LDAP": log on with _Username_ and _Password_ to the Cognos namespace with the ID "Harmony LDAP", the only namespace supported
  - "Anonymous": connect without logging on
- _Username_: the user name to log on with. It is required, also with "Anonymous"
- _Password_: the password for that user
