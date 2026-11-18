---
sidebar_label: 'Event Trigger - Slack'
hide_title: 'true'
---

## Event Trigger - Slack

The Slack Trigger fires on new messages that its [Slack Connection](../server/connection-slack) can see. While the Trigger is active, it keeps a real-time connection to Slack open. Each message that matches all conditions below fires the Trigger once; with every condition set to *Don't check*, every message fires it.

Every *Polling interval* seconds (***Main settings*** tab), the Trigger pings Slack to keep the connection open, or reconnects if the connection was lost.

:::warning

After the Trigger starts, it waits 60 seconds before it begins to watch messages, so messages posted in that minute do not fire it. If the connection to Slack is not ready after the 60 seconds, the Trigger stays active but never fires, also after later reconnects. Deactivate and activate the Trigger to start it again.

If the Connection is not authenticated, the Trigger stops and writes "Connection not authenticated" to the log, but still shows as active. Authenticate the Connection, then deactivate and activate the Trigger.

:::

The settings are on the ***Slack*** tab.

![Slack tab of the Add/Edit event window with the Connection list and the Text pattern, User name, Channel name and Received date groups, each set to Don't check](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Slack.png)

Each condition has an operator list and a value. *Don't check* (the default) turns the condition off and makes the value unavailable. The Trigger fires only when every condition that is not set to *Don't check* matches.

**Connection**

Select a [Slack Connection](../server/connection-slack). A Connection is required.

**Text pattern**

Compares the message text with the value. The comparison is not case-sensitive. You can use Variables.

* *Equal (=)* or *Not equal (!=)*: the text is (or is not) exactly the value
* *Contains (=%)* or *Not contains (!=%)*: the text contains (or does not contain) the value
* *Don't check*: turns the condition off
 
**User name**

Compares the Slack user name of the sender with a list of names. Enter one or more user names separated by semicolons (`;`) without spaces, for example `alice;bob`, or click the refresh button to list the users of the workspace and select one. A space after a semicolon becomes part of the next name, so that name never matches. The names are case-sensitive. You can use Variables; they are evaluated when the Trigger starts.

* *Contains (=%)*: the sender is one of the names in the list
* *Not contains (!=%)*: the sender is none of the names in the list
* *Equal (=)*: the sender is the first name in the list
* *Not equal (!=)*: the sender is not the first name in the list
* *Don't check*: turns the condition off

If a message has no sender, the condition is skipped for that message.
 
**Channel name**

Compares the channel the message was posted in with a list of channel names. Enter one or more channel names separated by semicolons without spaces, or click the refresh button to list the channels and select one. Public channels are listed with `#`, which the Trigger ignores. The names are case-sensitive, and the operators work as for *User name*. You can use Variables.

The Trigger looks up the channels by name when it starts, and a name it cannot find is left out. After you rename or add a channel, deactivate and activate the Trigger.

With several channels, *Equal (=)* and *Not equal (!=)* compare with the first of these channels in the order Slack lists them, not with the first name you entered. Enter only one channel for these operators.
 
**Received date**

Compares the time the message was posted with a date. Enter a date or click the Variables button to insert a date Variable.

* *Equal (=)* or *Not equal (!=)*: posted (or not posted) at exactly that time
* *Larger than (>)* or *Larger than or equal (>=)*: posted after (or at or after) that time
* *Smaller than (<)* or *Smaller than or equal (<=)*: posted before (or at or before) that time
* *Don't check*: turns the condition off

If the value is not a valid date, the condition passes.

### Result Variables

In the *Variables* window, the result Variables are under the Job's Trigger, *Result*. In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|Slack.Result.Text)}` returns the text of the message that started the run. See [Variables](global-variables).

When the Trigger fires, it sets these result Variables:

* `Slack.Result.Text`: the message text
* `Slack.Result.User`: the sender's user name
* `Slack.Result.Channel`: the channel name, without `#`; empty for a direct message
* `Slack.Result.CreatedTime|<date format>`: when the message was posted

The date format is optional, for example `{TRIGGER(Active|LastTrigger|Slack.Result.CreatedTime|yyyy-MM-dd HH:mm:ss)}`.

With *Expire after being triggered* on the ***Expires*** tab, `Slack.Result.Channel` is empty for the message that makes the Trigger expire, and `Slack.Result.User` is usually empty too.
