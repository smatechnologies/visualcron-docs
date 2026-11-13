---
sidebar_label: 'Connection - SAP'
hide_title: 'true'
---

## Connection - SAP

The SAP Connection stores the address, sign-in and security settings that the [SAP - R/3 Job execute](job-tasks/sap-tasks/r3-job-execute) Task uses to connect to an SAP system.
 
### Common settings

![SAP Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SAP/SAP.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For an SAP Connection, no _Test_ button is shown, and _Timeout_ and _Code page_ are not used.
 
### Main settings

![SAP Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SAP/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

A new Connection is prefilled with _System number_ "00", _Client_ "200", _Language_ "EN", _Pool size_ "5" and a sample _System ID_. Replace _System ID_, _System number_ and _Client_ with the values of your SAP system.

:::warning

The Connection connects directly to the SAP application server in _Address_. It has no settings for SNC or for a message server (load balancing), so the RFC traffic is not protected by SNC. Use this Connection only on a network that you trust.

:::

- _Address_: the host name or IP address of the SAP application server
- _Username_: the SAP user name
- _Password_: the password for that user

The following fields are in the _SAP Extra settings_ group:

- _System ID_: the SAP system ID (SID) of the SAP system
- _System number_: the system number of the SAP application server
- _Client_: the SAP client to log on to. One SAP system can have several clients, each with its own data
- _External user name_: the SAP Task does not use this field. As the external user name, the Task sends the SAP user set in the Task, or the Connection's _Username_ when the Task sets none
- _Language_: the logon language, as a two-letter code. The default is "EN"
- _Pool size_: the number of idle connections to the SAP system that are kept open for reuse. It does not limit how many connections are open at the same time. The default is "5"
 
### Troubleshooting

#### "Password logon no longer possible", "No RFC authorization for function module BAPI_XMI_LOGON" or "You have no authorization to log on to interface XBP"

The SAP user account is locked or lacks authorizations.

To resolve the error, complete the following steps:

1. Ask the SAP administrator to check that the SAP user is not locked and can log on with a password.
2. Ask the SAP administrator to check that the SAP user has RFC authorization for "BAPI_XMI_LOGON" and authorization to log on to the XBP interface.
3. Run the SAP Task again.

When the account is unlocked and has these authorizations, the SAP Task logs on.
