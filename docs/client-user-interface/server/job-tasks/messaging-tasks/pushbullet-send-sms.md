---
sidebar_label: 'Task Messaging - Pushbullet - Send SMS'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send SMS

The Pushbullet - Send SMS Task sends an SMS to a phone number through one of your linked Pushbullet devices. A device is a phone that you have linked to Pushbullet.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20SMS.png)

**Connection**

Select an existing global [Pushbullet Connection](../../../server/connection-pushbullet) for storing the connection credentials.

**Phone number**

The recipient phone number.

**Body**

The text of the SMS.

**Pushbullet - Send SMS > Sending device(s)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20SMS%20sending%20device.png)

The Sending device(s) sub tab lets you choose which of your linked Pushbullet devices is used to send the SMS. At least one device must be selected.

* _Send from all devices_ - when checked, the SMS is sent from every linked device and the grid is disabled
* _Refresh_ - queries the selected Connection and populates the grid with the available devices
* _Select all_ / _Deselect all_ - quickly toggle the *Use* column for every row in the grid
* The grid - check the *Use* column on the rows to choose individual sending devices
