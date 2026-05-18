---
sidebar_label: 'Event Trigger - System Start/Shutdown'
hide_title: 'true'
---

## Event Trigger - System Start/Shutdown

The System Start/Shutdown Trigger is able to Trigger a Job when the computer has been startup or just before shutdown of the computer.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20System%20Start%20Shutdown.png)

The form contains two independent checkboxes — you can enable either or both. At least one option must be selected.

**Trigger when computer starts**

Fires the Job when the VisualCron Server detects that the computer has just started. This option is enabled by default. The event only fires when the system's last boot‑up time has occurred within 10 minutes of the VisualCron service startup, so it will not retrigger on subsequent client restarts.

**Trigger when computer shuts down**

Fires the Job just before the computer shuts down.
