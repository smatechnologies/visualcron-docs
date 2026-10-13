---
sidebar_label: 'Task Messaging - Slack - Send Message'
hide_title: 'true'
---

## Task Messaging - Slack - Send Message

The Slack - Send message task sends a message to a Slack channel or directly to a Slack user.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/slack%20-%20send%20message.png)

**Task Messaging - Slack - Send Message > Main settings** tab

**Send to**

Choose who receives the message. Each mode has its own row: a radio button, then that mode's box and a refresh button on the same line. Only one row is active at a time.

* **To channel**: sends the message to a Slack channel. Select or type the channel in the box on the same row. The refresh button next to the box loads the channels from Slack.
* **To user**: sends the message as a direct message to one Slack user. Select or type the user in the box on the same row. The refresh button next to the box loads the users you have a direct message conversation with.

The box for the mode that is not selected is disabled and is saved empty. Switching modes does not carry the old value across. If the active box is empty when you click OK, the editor asks for the missing value ("You must set the channel name." or "You must set the user name.").

Loading the user list in **To user** mode requires the `im:read` OAuth scope on the Slack connection. See Troubleshooting on the [Connection - Slack](../../../client-user-interface/server/connection-slack) page.

