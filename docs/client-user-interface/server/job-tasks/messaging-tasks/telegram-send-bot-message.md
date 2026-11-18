---
sidebar_label: 'Task Messaging - Telegram - Send Bot Message'
hide_title: 'true'
---

## Task Messaging - Telegram - Send Bot Message

The Telegram - Send Bot message Task sends a message from a Telegram bot to users who have started a chat with the bot. The Task does not use a Connection: the bot token is entered in the Task. The Task connects to Telegram without a proxy. To create a bot and get its token from BotFather, see [Bots: An introduction for developers](https://core.telegram.org/bots).

![Telegram - Send Bot message tab, Message tab with the Token, Message and Message parse mode fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Telegram%20-%20send%20bot%20message.png)

:::warning

The bot token is stored in the Task settings without encryption and is shown as plain text in the Task window, so anyone who can open the Task can read it.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Telegram - Send Bot message: Message tab

- _Token_: the token of the bot. Required; Variables are not resolved in it
- _Message_: the text to send. Required; Variables are resolved
- _Message parse mode_: how Telegram reads the message: "Default" (plain text), "Html", "Markdown" or "MarkdownV2"

The Task cannot be saved while _Token_ or _Message_ is empty.

### Telegram - Send Bot message: Recipient(s) tab

- _Send to all users_: sends to every user in the grid, whether or not _Use_ is selected; the grid is then unavailable

  Only the users in the grid when the Task was last saved receive the message. To include users who started a chat with the bot later, click _Refresh_, then save the Task.

- The grid: select _Use_ on each user to send to
- _Select all_ and _Deselect all_: select or clear _Use_ on every row
- _Refresh_: loads the users of the bot into the grid, using _Token_, and clears every _Use_ check box

### Output and errors

The output of the Task is the response from Telegram. If Telegram rejects the token or the message, the Task fails.

:::warning

The Task window does not check that a recipient is selected. If no user is selected and _Send to all users_ is cleared, or the grid is empty, nothing is sent, and the Task reports success.

:::

### Troubleshooting

#### Recipient is not visible

A user appears on the ***Recipient(s)*** tab only after they have started a chat with the bot. Have each user send a message to the bot, then click _Refresh_.
