---
sidebar_label: 'Task Messaging - Pushbullet - Send SMS'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send SMS

The Pushbullet - Send SMS Task sends an SMS to a phone number through one of your linked Pushbullet devices, using a Pushbullet Connection. A device is a phone that you have linked to Pushbullet.

![Pushbullet - Send SMS tab, Send SMS tab with the Connection group and the Phone number and Body fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20SMS.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Pushbullet - Send SMS: Send SMS tab

- _Connection_: the Pushbullet Connection to send with; see [Connection - Pushbullet](../../connection-pushbullet)

  The Task uses the proxy set on the Connection.

- _Phone number_: the phone number to send the SMS to

  The Task window does not check the number.

- _Body_: the text of the SMS

Variables are resolved in _Phone number_ and _Body_.

### Pushbullet - Send SMS: Sending device(s) tab

![Pushbullet - Send SMS tab, Sending device(s) tab with the Devices list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20SMS%20sending%20device.png)

Choose the device that sends the SMS. Select a device in the grid, or select _Send from all devices_, or the Task cannot be saved.

- _Send from all devices_: makes the grid unavailable
- The grid: select _Use_ on the device to send from
- _Select all_ and _Deselect all_: select or clear _Use_ on every row
- _Refresh_: loads the devices of the Connection's account into the grid, and clears every _Use_ check box

:::warning

_Send from all devices_ is currently not applied: the SMS is sent only from the devices selected in the grid. A Task with only _Send from all devices_ selected can be saved without a sending device. Clear _Send from all devices_, then select the sending device in the grid.

:::

### Output and errors

The output of the Task is the response from Pushbullet. If Pushbullet rejects the SMS, the Task fails.
