---
sidebar_label: 'Task Messaging - Pushbullet - Send Link'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send Link

The Pushbullet - Send link Task sends a notification with a link to people, devices or channels, using a Pushbullet Connection.

![Pushbullet - Send link tab, Send link tab with the Connection group and the Title, Link URL and Body fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20link.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Pushbullet - Send link: Send link tab

- _Connection_: the Pushbullet Connection to send with; see [Connection - Pushbullet](../../connection-pushbullet)

  The Task uses the proxy set on the Connection.

- _Title_: the title of the notification
- _Link URL_: the address that opens when the recipient selects the notification
- _Body_: the text of the notification

Variables are resolved in _Title_, _Link URL_ and _Body_.

### Pushbullet - Send link: Recipient(s) tab

![Pushbullet - Send link tab, Recipient(s) tab with the People, Devices and Channels tabs](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20link%20recipients.png)

The ***Recipient(s)*** tab has three tabs, ***People***, ***Devices*** and ***Channels***. Select at least one recipient on them, or the Task cannot be saved.

Each tab has:

- _Send to all people_, _Send to all devices_ or _Send to all channels_: sends to every recipient of that kind; the grid is then unavailable
- The grid: select _Use_ on each recipient to send to
- _Select all_ and _Deselect all_: select or clear _Use_ on every row
- _Refresh_: loads the people, devices or channels of the Connection's account into the grid, and clears every _Use_ check box

:::warning

_Send to all channels_ is currently not applied: the link goes only to the channels selected in the grid. A Task with only _Send to all channels_ selected can be saved, but no channel receives the link.

:::

### Output and errors

The output of the Task is the response from Pushbullet. If Pushbullet rejects the push, the Task fails.
