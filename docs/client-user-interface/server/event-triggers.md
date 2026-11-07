---
sidebar_label: 'Event Triggers'
hide_title: 'true'
---

## Event Triggers

An Event Trigger starts a Job when something happens, instead of at a set time: for example when a file arrives, a
service stops, a mail is received or a Variable changes. Each Trigger type watches for one kind of event. The Trigger
runs on the VisualCron Server while the Job and the Trigger are active and the Server status is On (see *Ignore Server Off
(always run)* below).

Some types are told about an event as soon as it happens; others check at an interval (see *Polling interval*
below). The ***Main settings***, ***Timeout*** and ***Expires*** tabs are shown for every type and are described on
this page; some types do not support every setting (see *Run delay*, ***Timeout*** and ***Expires***). The tab named
after the type holds the settings of that type; see the page for the type.

:::info

An Event Trigger runs as the account the VisualCron service runs under, unless the Trigger uses a Credential. To
watch another computer, for example its event log or services, select a Credential of a user who has access on that
computer, or run the VisualCron service as such a user.

:::

:::warning

Some Event Triggers, such as the File Trigger, can fire several times a second, and each fire starts the Job. Make the
Trigger as specific as you can, for example with a narrow file mask, and see
[Triggers that fire once per item](#triggers-that-fire-once-per-item) for the Job settings that handle overlapping runs.

:::

### Event Trigger types

To add an Event Trigger, open the Job, go to the ***Triggers*** tab and click _Add_ -> _Event Trigger_, then click the
type. Types that are not available on your Server, and types hidden in the Client settings, are not listed.

![Triggers tab of the Add Job window with Add, Event Trigger open: a submenu of Event Trigger types from VisualCron to WebService](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Triggers.png)

These types are described on their own pages:

* [*VisualCron*](event-trigger-visualcron)
* [*MFT Server*](event-trigger-mft-server)
* [*Variable*](event-trigger-variable)
* [*File*](event-trigger-file)
* [*Remote file*](event-trigger-remote-file)
* [*Cloud file*](event-trigger-cloud-file)
* [*HTTP REST*](event-trigger-http-rest)
* [*RSS*](event-trigger-rss)
* [*SQL*](event-trigger-sql)
* [*Mail*](event-trigger-mail)
* [*Process*](event-trigger-process)
* [*PowerShell*](event-trigger-powershell)
* [*.NET code execute*](event-trigger-net-code-execute)
* [*Service*](event-trigger-service)
* [*Registry*](event-trigger-registry)
* [*Event log*](event-trigger-event-log)
* [*MSMQ*](event-trigger-msmq)
* [*Performance counter*](event-trigger-performance-counter)
* [*System start/shutdown*](event-trigger-system-start-shutdown)
* [*Session change*](event-trigger-session-change)
* [*Printer*](event-trigger-printer)
* [*Network*](event-trigger-network-change)
* [*AMQP*](event-trigger-amqp)
* [*Amazon SQS*](event-trigger-sqs)
* [*Azure Queue Storage*](event-trigger-azure-queue-storage)
* [*Slack*](event-trigger-slack)
* [*TCP*](event-trigger-tcp)
* [*Desktop trigger*](event-trigger-desktop)

Pages for Microsoft Teams, Sharepoint file, PeopleSoft, HTTP, WebService, Webmacro trigger and Folder are not yet
available.

The [*Custom*](event-trigger-custom) type (a custom WMI query) is not offered in the *Add* menu or in the type list
on the ***Main settings*** tab. Existing Custom Triggers can still be opened and changed.

### Triggers that fire once per item

Some Triggers fire once for each item they find and change or remove the item when they fire: for example, the
queue Triggers (MSMQ, AMQP, Azure Queue Storage and Amazon SQS) remove the message, the Mail Trigger can delete the
email, the Remote file and Cloud file Triggers can download and delete the file, and the HTTP REST Trigger with
*Immediately* has already answered the caller. The File Trigger fires once for each file, the RSS Trigger once for
each new feed item, and the TCP Trigger can fire several times in one conversation.

:::warning

If such a fire does not start the Job, its item is lost. *Do not start if job is already running* on the Job's
***Main settings*** tab is selected by default and skips a run while the Job is running. For these Triggers, also
select *Put Job in queue (does not skip Job - runs Job when running Job is finished)*. The queue is kept in memory and
is lost when the Server restarts. Do not use *Run delay* with these Triggers: the items of the fires it holds back do
not start a run. A Job time exception can also skip the run (see [Time exceptions](#time-exceptions)).

:::

### Result Variables

When a Trigger fires, it sets result Variables that tell the Job what happened, for example the name of the file a
File Trigger found. They are written `{TRIGGER(<JobId>|<TriggerId>|<Type>.Result.<Key>)}`. In the Job that the
Trigger starts, use the *Last trigger* form, `{TRIGGER(Active|LastTrigger|<Type>.Result.<Key>)}`, for example
`{TRIGGER(Active|LastTrigger|File.Result.Name)}`: it reads the result of the firing that started the run, even if
the Trigger fires again while the Job runs. Pick the Variables in the *Variables* window under the Job's Triggers;
each Trigger page lists or links its result Variables. See [Variables](global-variables).

If the Job has several Event Triggers of different types and another of them fires while the Job runs, the *Last
trigger* form returns an error text. Use the `<JobId>|<TriggerId>` form in that case.

A timeout fire (see [Timeout](#timeout)) has no event behind it: the result Variables of the Trigger type return an
error text in square brackets, for most types beginning `[TranslateVariable`, instead of a value. For the Variable
Trigger most of them return empty text.

### Time exceptions

While a [time exception](job-time-exceptions) of the Job is active, its Event Triggers do not start it. An event in
that time is not kept for later: it still counts toward *Run delay* and *Expire after being triggered*, but the run
it would have started is skipped.

* Types that check at an interval skip the check instead, so they see the event at their first check after the time
  exception: for example SQL, Remote file, Cloud file, RSS, Mail, PowerShell, .NET code execute, Amazon SQS, Variable,
  and File with *Use polling (Samba compatible)*
* Other types keep watching and drop the event: for example Event log, Process, Service, VisualCron, MSMQ, AMQP and
  Azure Queue Storage. A queue Trigger has then already removed the message

The File, Cloud file and Variable pages describe cases that behave differently.

### Main settings

The settings are on the ***Main settings*** tab.

![Add/Edit event window, Main settings tab of a File Trigger: event type button, Description, Active, Auto description, Auto refresh description, Run delay, an unavailable Polling interval, Credentials, Extended Trigger debug logging and Ignore Server Off](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Main%20Settings%20Tab.png)

The button at the top of the tab shows the type of the Trigger, for example *File*. To change the type, click it and
select another type in the list. The type tab is replaced with the settings of the new type; when you click *OK*,
only the settings of the selected type are saved. *MFT Server* is not in this list: to use it, add a new Trigger with
_Add_ -> _Event Trigger_ -> _MFT Server_.
 
**Description**

The text shown for the Trigger in the list of Triggers on the ***Triggers*** tab of the Job. Use it to tell the Triggers of a Job apart.
 
**Active**

When checked (default), the Trigger is active. Clear it to keep the Trigger inactive; you can activate it later.
 
**Auto description**

When checked (default), VisualCron creates the *Description* from the Trigger type and its settings when you click *OK*, if *Description* is empty or *Auto refresh description* is checked.
 
**Auto refresh description**

When checked (default), the description is created again each time you click *OK*, even if *Description* already contains text. Available only when *Auto description* is checked.
 
**Run delay**

*Run after the trigger has been triggered:* sets how many events it takes before the Trigger starts the Job. The
minimum and default is 1: every event starts the Job.

With a higher value, the first run comes after that number of events. After each run the count starts again at 1,
not at 0, so each later run needs one event fewer: with 2, the Job runs on the second event and then on every event;
with 5, it runs on the fifth event and then on every fourth. To run the Job once for every *K* events after the
first run, set *K* + 1. A timeout fire counts as a run and sets the count to 1. The count is kept in memory and starts
from zero when the Trigger restarts, for example when the Server restarts or the Job is saved.

The SQL, Desktop and Webmacro Triggers do not use *Run delay*, and some types count differently; see the page for
the type.

:::note

_Run delay_ counts fires of this one Trigger. To require several **different** Triggers to fire before the Job runs, use a dependency instead. See [Job Triggers](job-triggers).

:::
 
**Polling interval**

*Check every:* ... *Second(s)*: for the types that check at an interval, how often they check, from 1 to 9,999,999.
The default depends on the type: 60 seconds for most, 1 for VisualCron, 5 for Azure Queue Storage, 120 for
WebService, 300 for RSS and 3600 for HTTP.
The field is unavailable for types that are told about events as they happen, such as Registry, TCP and File (unless
*Use polling (Samba compatible)* is checked on the File tab). Some types show the field but use it differently or
not at all, for example: the HTTP REST Trigger uses it as a wait in milliseconds (default 1000), the Event log Trigger as the time
between attempts to restart watching, and the Printer Trigger does not use it. Each Trigger page says how its type
uses the value. A short interval means more checks and more load on the Server and on the system being checked.
 
**Remote event**

*Computer name:* for the types that can watch another computer: Event log, Process, Registry, Service, Performance
counter and Custom. Enter the name or IP address of the computer; the default "." is the computer the VisualCron
Server runs on. The account the Trigger runs as (see *Credentials*) must be allowed to read that information on the
remote computer. The Printer, Desktop and Webmacro Triggers show the field without using it to select a computer.

**Credentials**

Select the Credential the Trigger runs as, for example to connect to a remote computer, or *No Credential* to use the
account the VisualCron service runs under. Click the *Settings* icon to open *Manage credentials* and add or edit
one. See [Credentials](global-credentials). The group is shown only for some types; types such as PowerShell have
their own Credential on the type tab.

For the Process, Registry, Service and Custom Triggers, select a Credential only for a remote computer: with the
default computer ".", a Credential makes the connection fail.

**Extended Trigger debug logging**

When checked, the Trigger writes more detail to the Server log, for example the full text of an error and the value
it read at each check. Use it while you troubleshoot a Trigger that does not fire as expected, then clear it.
 
**Ignore Server Off (always run)**

When checked, the Trigger keeps watching while the Server status is Off, and it starts the Job when it fires.

### Timeout

The settings are on the ***Timeout*** tab.

![Add/Edit event window, Timeout tab: Use timeout with Hour(s), Minute(s) and Second(s), and the Fire trigger timeout action](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Timeout.png)

Use the timeout to act when an expected event does not happen. The Trigger fires when its event happens; the timeout fires when the Trigger has not fired for the time you set.

**Use timeout**

Check this to use the timeout (cleared by default). While it is cleared, the time fields and *Timeout action* are unavailable.

**If trigger has not fired in x time**

The longest time the Trigger can go without firing, in *Hour(s)*, *Minute(s)* (0 to 59) and *Second(s)* (0 to 59).
 
**Timeout action**

*Fire trigger* is the only action: when the time runs out, the Trigger starts the Job as if its event had happened.

For example, a File Trigger watching for a nightly file from a supplier can be given a timeout of 8 hours. If the
file arrives, the Trigger fires normally and the Job processes it. If the file never arrives, the timeout fires the
Trigger anyway, and the Job can send an alert about the missing file.

The time is counted from when the Trigger starts, for example when the Server starts or the Job is saved, and again
from each fire, even if the Job then does not start. Events held back by *Run delay* do not restart it. While
nothing happens, the timeout fires again after each further period: with a timeout of 1 hour, the Job is started
every hour until an event arrives. If one alert is enough, add a Job condition, or set an *Expiration date* on the
***Expires*** tab; *Expire after being triggered* does not count timeout fires.

A timeout fire resets the *Run delay* count, and Job time exceptions still apply. Its result Variables return an
error text (see [Result Variables](#result-variables)). To tell the two cases apart in the Job, add a
[Variable condition](condition-variable) that checks that a result Variable, for example
`{TRIGGER(Active|LastTrigger|File.Result.Name)}`, does not contain `[TranslateVariable`. For the Variable Trigger,
check that `{TRIGGER(Active|LastTrigger|Variable.Result.Variable.EvaluatedExpression)}` is not empty.

The MSMQ, MFT Server, Session change, Printer, AMQP, Slack, Azure Queue Storage, Amazon SQS, Microsoft Teams and
PeopleSoft Triggers do not support the timeout: it never fires for them.

:::warning

Set a time greater than zero. With 0 hours, 0 minutes and 0 seconds, the timeout fires about every second and starts
the Job each time.

:::
 
### Expires

The settings are on the ***Expires*** tab.

![Add/Edit event window, Expires tab: Expiration enabled, Expiration date with date and time, Expire after being triggered with time(s), and the Inactivate trigger and Delete trigger expire actions](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Expires.png)

**Expiration enabled**

Check this to make the Trigger expire, then select when it expires and what happens then.

* *Expiration date*: the Trigger expires at the date and time you enter, by the clock of the VisualCron Server
* *Expire after being triggered* ... *time(s)*: the Trigger expires after this number of events (minimum 1). Every
  event counts, including events held back by *Run delay*; timeout fires do not count. The event that reaches the
  number still starts the Job if *Run delay* allows it. The count is kept in memory and starts again at 0 when the
  Trigger restarts, for example when the Server restarts or the Job is saved

The SQL, Remote file, Cloud file, Sharepoint file, Desktop and Webmacro Triggers do not support *Expire after
being triggered*.

**Expire action**

* *Inactivate trigger* (default): the Trigger is kept but made inactive. Activate it again to use it
* *Delete trigger*: the Trigger is removed from the Job. With an *Expiration date*, this also removes a Trigger that
  is already inactive
