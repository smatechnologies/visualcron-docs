---
sidebar_label: 'Event Trigger - MSMQ'
hide_title: 'true'
---

## Event Trigger - MSMQ

The MSMQ Trigger receives messages from a private or public Microsoft Message Queuing (MSMQ) queue, on the VisualCron Server computer or on another computer. Each message fires the Trigger once. The Trigger takes the message off the queue when it receives it, before the Job runs, so other programs that read the queue do not get it. Messages that are already in the queue when the Trigger starts are received too.

No Connection is needed. To use the message in the Job's Tasks, use the result Variables (see [Result Variables](#result-variables)).

This Trigger fires once per message and removes the message. If the run of the Job is skipped, for example because *Do not start if job is already running* is selected (the default), that message is lost. See *Triggers that fire once per item* in [Event Triggers](event-triggers#triggers-that-fire-once-per-item).

:::warning

A received message is also removed when the Job does not start because of a time exception of the Job, or because *Run after the trigger has been triggered* in the *Run delay* group on the ***Main settings*** tab is above 1 and the message does not complete the count. Do not use a time exception or a run delay above 1 with this Trigger when every message must be processed.

:::

When it starts, the Trigger registers an MSMQ trigger named "VisualCronTrigger" for the queue. If that MSMQ trigger is deleted later, the Trigger can be deactivated when it starts again. Open the Trigger in the Client and click *OK* to register a new one.

When an error occurs while the Trigger handles a message:

* If the result Variables cannot be set for the message, the error is written to the log and the Job does not start; the message has already been removed from the queue
* For a transactional queue, if receiving the message fails, the Trigger stops receiving messages but still shows as active, and nothing is written to the log; deactivate and activate the Trigger
* Most other errors deactivate the Trigger and are written to the log; the message has already been removed from the queue

The settings are on the ***MSMQ*** tab.

![MSMQ tab of the Add/Edit event window with the Scope group (Credential list, Local MSMQ and Remote MSMQ options, Host name) and the Queue list with its refresh button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20MSMQ.png)

**Scope**

**Credential**

Select a [Credential](../server/global-credentials) for the Trigger to run as when it connects to the queue, for example for a remote queue that needs a domain account. With *No Credential*, the Trigger uses the account that runs the VisualCron service. The Credential is used for local and remote queues. Click the settings button next to the list to open the *Manage credentials* window, where you can add a Credential.

**Local MSMQ / Remote MSMQ**

Choose whether the queue is on the VisualCron Server computer or on another computer:

* *Local MSMQ*: the queue is on the VisualCron Server computer
* *Remote MSMQ*: the queue is on another computer, which you enter in *Host name*

**Host name**

The host name or IP address of the computer that hosts the queue. Select a computer from the list or type the name. You can use Variables. The field is available only when *Remote MSMQ* is selected.

**Queue**

The queue to receive from. Click the refresh button to list the queues of the selected computer and select one, or type the queue path. For a private queue the list also shows its journal queue (`<queue>\Journal$`). Clicking the refresh button replaces the queue in the box with the first queue in the list, so select your queue again afterward. You can use Variables. A queue is required.

If the Trigger cannot open the queue when it starts, for example because the queue does not exist or the computer cannot be reached, the Trigger is deactivated and the error is written to the log.

### Result Variables

In the *Variables* window, the result Variables are under the Job's Trigger, *Result*. In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|MSMQ.Result.Message)}` returns the body of the message that started the run. See [Variables](global-variables).

When the Trigger fires, it sets these result Variables:

* `MSMQ.Result.Id`: the message ID
* `MSMQ.Result.Label`: the message label
* `MSMQ.Result.Message`: the message body as text
* `MSMQ.Result.ArrivedTime|<date format>`: when the message arrived in the queue
* `MSMQ.Result.SentTime|<date format>`: when the message was sent

The date format is optional, for example `{TRIGGER(Active|LastTrigger|MSMQ.Result.ArrivedTime|yyyy-MM-dd HH:mm:ss)}`.

### Troubleshooting

The following error means that the MSMQ Triggers component of Windows is not installed:

`Retrieving the COM class factory for component with CLSID {1D9F85C0-9666-11D2-8927-0008C70C0622} failed due to the following error: 80040154 Class not registered (Exception from HRESULT: 0x80040154 (REGDB_E_CLASSNOTREG)).`

To install the component, do one of the following:

* Windows client: in Control Panel, open _Programs and Features_ -> _Turn Windows features on or off_ and check _Microsoft Message Queue (MSMQ) Server_ -> _Microsoft Message Queue (MSMQ) Server Core_ -> _MSMQ Triggers_
* Windows Server: in Server Manager, open _Add Roles and Features_ -> _Features_ and check _Message Queuing_ -> _Message Queuing Services_ -> _Message Queuing Triggers_

![Windows Features window with MSMQ Triggers checked under Microsoft Message Queue (MSMQ) Server Core](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20MSMQ%20Windows.png)
