---
sidebar_label: 'Task Messaging - Pushbullet - Send Link'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send Link

The Pushbullet - Send link Task sends a link to one or more Pushbullet devices, contacts and/or channels.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20link.png)

**Connection**

Select an existing global [Pushbullet Connection](../../../server/connection-pushbullet) for storing the connection credentials.
 
**Title**

The notification title.
 
**Link**

The URL that the user is taken to when clicking the notification title.
 
**Body**

The message text shown in the notification.

**Pushbullet - Send link > Recipients** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20link%20recipients.png)

The Recipients section has three nested sub tabs — *Devices*, *Contacts* and *Channels* — that let you choose where the link is delivered. At least one recipient must be selected across the three tabs.

Each recipient sub tab works the same way:

* _Send to all_ - when checked, the link is sent to every recipient of that type and the grid is disabled
* _Refresh_ - queries the selected Connection and populates the grid with the available recipients
* _Select all_ / _Deselect all_ - quickly toggle the *Use* column for every row in the grid
* The grid - check the *Use* column on the rows to choose individual recipients
