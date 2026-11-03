---
sidebar_label: 'Task Messaging - Slack - Send Message'
hide_title: 'true'
---

## Task Messaging - Slack - Send Message

The Slack - Send message task sends a message to a Slack channel, or to a Slack user through the Slack app that the connection uses.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/slack%20-%20send%20message.png)

**Task Messaging - Slack - Send Message > Main settings** tab

**Send to**

Choose who receives the message. Each mode has its own row: a radio button, then that mode's box and a refresh button on the same line. Only one row is active at a time.

* **To channel**: sends the message to a Slack channel. Select or type the channel in the box on the same row. The refresh button next to the box loads the public channels, shown with a leading `#`, and the private channels the Slack app can see, shown without one. A channel name must start with `#`. A value without a leading `#` is treated as a Slack channel ID, so add the `#` yourself to a private channel picked from the list.
* **To user**: sends the message to one Slack user. Select or type the user in the box on the same row. Use the Slack user name exactly as the list shows it, including upper and lower case. A display name or an email address does not match. A user who is not in the list can still be typed. The message comes from the Slack app and appears in that user's conversation with the app. It is not a direct message from your own Slack account. The refresh button next to the box loads the users the Slack app already has a conversation with.

The box for the mode that is not selected is disabled and is saved empty. Switching modes does not carry the old value across. If the active box is empty when you click OK, the editor asks for the missing value ("You must set the channel name." or "You must set the user name.").

When you open a task that has a connection selected, the list for the selected mode loads on its own. This automatic load shows no error and does not pick anything for you. Click the refresh button to reload a list or to load the list for the other mode. If the box is empty, a refresh puts the first item from the list in it. A refresh click is ignored while that refresh is still running, or if the last successful click on the same button was less than 10 seconds ago. Changing the connection empties both lists and keeps the text in each box.

In both modes the message is posted under the Slack app's own name. The task has no setting for a different sender name.

Loading the user list in **To user** mode requires the `im:read` OAuth scope on the Slack connection. See Troubleshooting on the [Connection - Slack](../../../client-user-interface/server/connection-slack) page.

