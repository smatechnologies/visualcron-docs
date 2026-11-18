---
sidebar_label: 'Task Messaging - Slack - Send Message'
hide_title: 'true'
---

## Task Messaging - Slack - Send Message

The Slack - Send message Task posts a message to a Slack channel or user, and can upload files with it, using a Slack Connection.

![Slack - Send message tab, Main settings tab with the Connection, Channel name, Send as user and Message groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/slack%20-%20send%20message.png)

:::warning

This Task uses a Slack Connection; see [Connection - Slack](../../connection-slack). The Task does not use the proxy set on the Connection.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::note

The Slack - Send message Task is part of the Advanced messaging feature of the license.

:::

### Slack - Send message: Main settings tab

- _Connection_: the Slack Connection to post with. Required
- _To channel_ and _To user_: in the _Channel name_ group, whether the message goes to a channel or to a user

  _To channel_ is selected on a new Task. Switching between the two clears _Channel name_.

- _Channel name_: the box under _To user_; with _To channel_, the channel to post to

  Required. A value that starts with "#", as in `#<channel name>`, is looked up by name among the first 200 public and private channels that the Connection can see. Any other value is passed to Slack as it is, for example a channel ID. The refresh button next to the field fills the list. With _To channel_, it lists the public channels as `#<channel name>`, followed by the private channels without "#". A private channel chosen from the list is therefore passed to Slack as it is, and is not looked up by name; type "#" in front of the name to have it looked up. With _To user_, it lists the user names that have a direct message conversation with the Connection.

  The lookup of a private channel by name needs the "groups:read" scope on the Slack app; see [Connection - Slack](../../connection-slack).

  With _To user_, the Task does not use _Channel name_, but the Task window still requires a value.

- _Send as user_: with _To user_, the Slack user name of the person who receives the message; with _To channel_, the user name sent to Slack for the post

  The refresh button next to the field lists the users of the workspace.

- _Message_: the text to post. Required
- _Send only first file_ and _Send one message per file_ (default): when the ***File filter*** tab matches files, upload only the first matching file, or every matching file, each with _Message_

Variables are resolved in _Channel name_, _Send as user_ and _Message_.

### Slack - Send message: File filter tab

Use the [File Filter](../../job-tasks-file-filter) to choose files to upload with the message. Without a source folder on this tab, the message is posted as text only. The Credential of the File filter is used to read the files.

### Output and errors

The output of the Task is "Success" for a message, and `<file name> sucessfully uploaded` for each uploaded file.

:::warning

If Slack rejects the message or a file, or the channel or user cannot be found, the error is written to standard error, and the Task reports success.

:::
