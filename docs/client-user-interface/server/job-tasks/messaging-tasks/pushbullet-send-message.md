---
sidebar_label: 'Task Messaging - Pushbullet - Send Message'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send Message

The Pushbullet - Send message Task sends a notification with a title and a message to people, devices or channels, using a Pushbullet Connection.

![Pushbullet - Send message tab, Message tab with the Connection group and the Title and Body fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20message.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Pushbullet - Send message: Message tab

- _Connection_: the Pushbullet Connection to send with; see [Connection - Pushbullet](../../connection-pushbullet)

  The Task uses the proxy set on the Connection.

- _Title_: the title of the notification
- _Body_: the text of the notification

Variables are resolved in _Title_ and _Body_.

### Pushbullet - Send message: Recipient(s) tab

![Pushbullet - Send message tab, Recipient(s) tab with the People, Devices and Channels tabs](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20message%20recipients.png)

The ***Recipient(s)*** tab has three tabs, ***People***, ***Devices*** and ***Channels***. Select at least one recipient on them, or the Task cannot be saved.

Each tab has:

- _Send to all people_, _Send to all devices_ or _Send to all channels_: sends to every recipient of that kind; the grid is then unavailable
- The grid: select _Use_ on each recipient to send to
- _Select all_ and _Deselect all_: select or clear _Use_ on every row
- _Refresh_: loads the people, devices or channels of the Connection's account into the grid, and clears every _Use_ check box

:::warning

_Send to all channels_ is currently not applied: the message goes only to the channels selected in the grid. A Task with only _Send to all channels_ selected can be saved, but no channel receives the message.

:::

### Output and errors

The output of the Task is the response from Pushbullet. If Pushbullet rejects the push, the Task fails.
