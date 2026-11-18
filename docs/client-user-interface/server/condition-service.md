---
sidebar_label: 'Condition - Service'
hide_title: 'true'
---

## Condition - Service

The _Service_ condition checks the status of a Windows service, on the VisualCron Server computer or on another computer. Use it, for example, to run a Job only when a database service is running, or to skip a Task while a service is stopped for maintenance.

This page describes the **_Service_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "Service" -> **_Service_** tab

![Add/Edit condition window, shown smaller than its default size so the Service name box is cut off, with the Service tab open, showing the Credentials list set to No Credential, Local selected, an empty and disabled Hostname box, and Has status set to "Running"](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Service.png)

### Credentials

Select a Credential when the Server needs another Windows account to read the service status, for example on a remote computer. See [Global - Credentials](global-credentials). Leave "No Credential" to check the status with the account the VisualCron service runs under. The Credential is also used when the Server loads the list of services of a remote computer for this window, so the list shows what the Server computer can reach.

Use the _Filter.._ box to search the list. To manage Credentials, click the button to the right of the _Filter.._ box. If the selected Credential no longer exists, or the user who started the run is not allowed to read and use it, the check runs with the account the VisualCron service runs under.

### Service

Select where the service runs:

- _Local_: the VisualCron Server computer (the default)
- _Remote_: the computer in _Hostname_

#### Hostname

Enabled when _Remote_ is selected. Type the name of the computer, or select it from the list. The window lets you save _Remote_ without a hostname, and the check then returns a Match Error.

#### Service name

The name of the service to check. Type it, or select it from the list:

- With _Local_ selected, the list shows the services of the Server computer
- With _Remote_ selected, click the refresh button to the right of the list to load the services of the computer in _Hostname_, using the selected Credential

The list shows service names, the short names Windows uses, such as "Spooler", not display names.

Enter a service name. The window lets you save the condition without one, and the check then returns a Match Error. _Hostname_ and _Service name_ are used exactly as entered: Variables are not replaced in these fields.

### Match

#### Has status

Matches when the service has the status you select: "Stopped", "StartPending", "StopPending", "Running", "ContinuePending", "PausePending" or "Paused". The default is "Running". Any other status does not match. The status is read once, when the condition is evaluated. The check does not wait for a pending status to change.

If the service does not exist, the computer cannot be reached, or access is denied, the condition returns a Match Error and an error is logged.

:::tip

To act when a service is not running, select "Running" and set the action you want on _On Match None_. See [Conditions - Actions](conditions-actions).

:::
