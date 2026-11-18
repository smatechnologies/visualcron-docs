---
sidebar_label: 'Event Trigger - SQS'
hide_title: 'true'
---

## Event Trigger - SQS

The Amazon SQS Trigger reads messages from Amazon Simple Queue Service (SQS) queues, through an [Amazon Connection](../server/connection-amazon). Every *Polling interval* (***Main settings*** tab, default 60 seconds) it lists the queues in the Connection's region, reads up to 10 messages from each queue that matches *Queue*, and checks each message against the *Filters*. A message that matches all filters fires the Trigger once and is deleted from the queue right after the Trigger fires. During a time exception of the Job, the Trigger does not poll, so messages stay in the queue.

This Trigger fires once per message and deletes the message. If the run of the Job is skipped, for example because *Do not start if job is already running* is selected (the default), that message is lost. See *Triggers that fire once per item* in [Event Triggers](event-triggers#triggers-that-fire-once-per-item).

:::warning

A matching message is also deleted when *Run after the trigger has been triggered* in the *Run delay* group on the ***Main settings*** tab is above 1 and the message does not complete the count. Do not use a run delay above 1 with this Trigger when every message must be processed.

With *Queue* set to *Don't check* (the default), or with no queue checked, the Trigger reads every queue in the region of the Connection and deletes every message that matches the filters, including messages meant for other applications. Select the queues to watch.

:::

:::note

Messages that do not match the filters are not deleted. Because the Trigger has read them, SQS hides them from other readers until the visibility timeout of the queue has passed, and the Trigger reads them again at a later poll.

:::

With *Expire after being triggered* on the ***Expires*** tab, the Trigger finishes the poll in which it expires: the other matching messages that this poll read still start the Job and are deleted.

The settings are on the ***Amazon SQS*** tab.

![Amazon SQS tab of the Add/Edit event window with the Connection list, the Queue operator and list, the Filters group (SenderId, Message text, Min created DateTime, Max created DateTime, Attribute name) and the Options group](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQS.png)

**Connection**

Select the [Amazon Connection](../server/connection-amazon). The Trigger always signs in with the *Access Key ID* and *Secret Access Key* of the Connection and uses the Connection's *Region*. The *Address*, proxy and *Auto-accept server certificates* settings of the Connection are not used. A Connection is required.

If the Connection is deleted:

* When the Trigger starts without its Connection, it stops without an entry in the log but still shows as active; select another Connection, then deactivate and activate the Trigger
* While the Trigger runs, each poll writes an error to the log, and the Trigger is deactivated after the number of *On error reconnect attempts*; select another Connection, then activate the Trigger

**Queue**

Select the queues to watch. Click the refresh button to list the queues of the Connection, then check one or more queues; the checked queues are shown separated by commas. Queue names are compared without regard to case.

* *Contains (=%)*: watch the queues in the list
* *Not contains (!=%)*: watch every queue except those in the list
* *Equal (=)*: watch only the first queue in the list
* *Not equal (!=)*: watch every queue except the first one in the list
* *Don't check*: watch every queue in the region

With *Don't check*, or when no queue is checked, every queue is watched (see the warning above).

**Filters**

The filters apply to each message the Trigger reads. A filter set to *Don't check*, or with an empty value, is not applied. A message fires the Trigger only when all applied filters match. Text comparisons are not case-sensitive, and you can use Variables in the values.

**SenderId**

Compares the SenderId of the message with the value: *Contains (=%)*, *Not contains (!=%)*, *Equal (=)*, *Not equal (!=)* or *Don't check*. A message without a SenderId does not match.

**Message text**

Compares the message body with the value, with the same operators. A message with an empty body does not match.

**Min created DateTime**

Compares the time the message was sent with a date: *Equal (=)*, *Not equal (!=)*, *Larger than (>)* (sent after the date), *Larger than or equal (>=)*, *Smaller than (<)* (sent before the date), *Smaller than or equal (<=)* or *Don't check*. Enter a date or click the Variables button to insert a date Variable. If the value is not a valid date, the filter passes.

**Max created DateTime**

Works the same way as *Min created DateTime*. To match a time range, use one field with *Larger than (>)* and the other with *Smaller than (<)*.

:::note

The two date filters compare the sent time in UTC. Enter the date and time in UTC. A date Variable that returns local time shifts the comparison by the difference between local time and UTC.

:::

**Attribute name**

Compares the names of the message attributes with the value, with the same operators as *SenderId*. The filter matches when one attribute name matches. A message without message attributes does not match.

**Options**

**On error reconnect attempts**

The number of failed polls in a row before the Trigger is deactivated (1 to 500; default 5). After the first successful poll, the Trigger is deactivated after one failure fewer (4 with the default). Each failed poll is written to the log.

**On error reconnect interval (seconds)**

How long to wait after a failed poll before the next one (1 to 500; default 300).

### Result Variables

In the *Variables* window, the result Variables are under the Job's Trigger, *Result*. In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|AmazonSQS.Result.Message)}` returns the body of the message that started the run. See [Variables](global-variables).

When the Trigger fires, it sets these result Variables:

* `AmazonSQS.Result.Message`: the message body
* `AmazonSQS.Result.MessageId`: the message ID
* `AmazonSQS.Result.SenderId`: the SenderId of the message
* `AmazonSQS.Result.SentTime|<date format>`: when the message was sent, in local time
* `AmazonSQS.Result.ApproximateFirstReceiveTime|<date format>`, `AmazonSQS.Result.ApproximateReceiveCount`: when the message was first read and how many times it has been read
* `AmazonSQS.Result.MessageGroupId`, `AmazonSQS.Result.MessageDeduplicationId`, `AmazonSQS.Result.SequenceNumber`: the FIFO queue values of the message
* `AmazonSQS.Result.MessageAttributes|<attribute name>`: the value of a message attribute (a binary value as Base64); the attribute name is case-sensitive; without a name, the names of all attributes, one per line

The date format is optional, for example `{TRIGGER(Active|LastTrigger|AmazonSQS.Result.SentTime|yyyy-MM-dd HH:mm:ss)}`.
