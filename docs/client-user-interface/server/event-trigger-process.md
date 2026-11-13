---
sidebar_label: 'Event Trigger - Process'
hide_title: 'true'
---

## Event Trigger - Process

The Process Trigger fires when a process with a given name starts or ends, on the Server computer or on a remote computer. It uses WMI, which checks for started and ended processes at the *Polling interval* (*Check every*) on ***Main settings***, by default every 60 seconds. A process that starts and ends between two checks can be missed; lower the interval to watch short-lived processes.
 
The settings are on the ***Process*** tab.

![Process tab of the Add/Edit event window with the Process name field, the Select button and Process event type set to Process start](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Process.png)

**Process information**

**Process name**

The name of the process, including its extension, for example "WINWORD.EXE". Click *Select* to open *Active processes*, which lists the processes running on the Server, and double-click a process to use its name. The name must match exactly, but case does not matter. Wildcards such as `*` and `?` are not supported. The field can contain Variables.

If no process has that name, the Trigger does not fire and nothing is logged. Check the spelling and the extension.
 
**Process event type**

Select the event that fires the Trigger:

* *Process start*: a process with that name starts (default)
* *Process end*: a process with that name ends

To watch processes on another computer, enter its name or IP address in *Computer name* on ***Main settings*** (the default "." is the Server computer). Select a Credential with WMI access under *Credentials* only for a remote computer: with *Computer name* ".", a Credential makes the connection fail.

:::warning

If VisualCron cannot connect to WMI or the query fails when the Trigger starts, the Trigger is deactivated; it does not try to reconnect. Check the log, correct the computer name or the Credential, and activate the Trigger again.

With a Credential, an error while the Trigger watches for processes also deactivates it. Without a Credential, a WMI connection that is lost after the Trigger has started is not detected: the Trigger still shows as active, but its event no longer fires it (a timeout, if set, still fires), and nothing is logged. If a Process Trigger that watches a remote computer stops firing, deactivate and activate the Trigger. To notice when the Trigger has gone silent, set a timeout on the ***Timeout*** tab.

:::

### Result Variables

Each time the Trigger fires, it sets result Variables for the process, for example its name, `{TRIGGER(Active|LastTrigger|Process.Result.Name)}`. With *Last trigger* (`Active|LastTrigger`), a Variable reads the result of the firing that started the run. All Process Trigger result Variables are described in [Variables](global-variables).
