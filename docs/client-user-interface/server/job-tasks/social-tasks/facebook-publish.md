---
sidebar_label: 'Task Social - Facebook - Publish'
hide_title: 'true'
---

## Task Social - Facebook - Publish

The Facebook - Publish Task publishes a message on a Facebook page, using a Facebook Connection.

The Task uses a Facebook Connection; see [Connection - Facebook](../../connection-facebook).

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Facebook - Publish: Message tab

- _Connection_: the Facebook Connection to use. Required
- _In page_: the name of the Facebook page to publish on, exactly as Facebook shows it, including upper and lower case. Required. The button next to the list lists the pages that the Connection can manage
- _Message_: the message to publish. Required

Variables are resolved in _In page_ and _Message_.

### Output and errors

The output of the Task is the ID of the published post. When Facebook rejects the message, the Task fails with the error from Facebook.

:::warning

When no page that the Connection can manage has the name in _In page_, the Task publishes nothing, and the Task reports success.

:::
