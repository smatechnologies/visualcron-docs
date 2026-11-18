---
sidebar_label: 'Connection - SSRS'
hide_title: 'true'
---

## Connection - SSRS

The SSRS Connection stores the address, sign-in and security settings that the [Database - SSRS](job-tasks/database-tasks/ssrs) Task uses to connect to SQL Server Reporting Services (SSRS). The Task runs and exports reports through it.
 
### Common settings

![SSRS Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSRS/SSRS.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

For an SSRS Connection, no _Test_ button is shown, and _Timeout_ and _Code page_ are not used. The SSRS Task uses the Task timeout for its calls to the report server. When the Task has no timeout set, the calls do not time out.
 
### Main settings

![SSRS Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SSRS/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

- _Address_: the host name or IP address of the report server. Do not include `http://` or a folder path. VisualCron adds the report server folder, which is "reportserver" unless the Task sets another folder, and the path of the Reporting Services web service
- _Username_: the user name for the report server
- _Password_: the password for the report server

### Proxy

The ***Proxy*** tab is on the ***Connection settings*** tab. The SSRS Task sends its calls to the report server through the proxy set here. With any _Proxy type_ other than "No proxy", the Task uses the proxy as an HTTP proxy.
