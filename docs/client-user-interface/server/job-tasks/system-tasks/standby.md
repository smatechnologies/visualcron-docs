---
sidebar_label: 'Task System - Standby'
hide_title: 'true'
---

## Task System - Standby

The Standby Task puts the VisualCron Server computer or a remote computer into standby (sleep). On the Server computer, the Task can also set a time for the computer to wake up. A computer in standby uses approximately 35% of normal power consumption, and it can be woken at a set time or through the network with the [Wake up on LAN](wakeup-on-lan) Task.

In standby, the computer keeps its work in memory and only appears to be turned off. Standby is not suited to long periods: nothing is saved to the hard disk, so a power failure during standby loses the work in memory.

![Standby Task settings, with the Credentials, Hibernate and Wake up groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Standby.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Standby tab

- _Credentials_: not used. With _Remote host_, the Task connects to the remote computer through WMI as the account of the VisualCron Server service, whatever Credential is selected; that account must be allowed to start programs on the remote computer
- _Local host_ (_Hibernate_ group; the Client uses this group name on the Standby Task too): puts the VisualCron Server computer into standby. Selected by default
- _Remote host_: puts the computer entered in the field next to it into standby
- _Force_: selected by default. When selected, the computer goes into standby at once; when cleared, Windows first sends a request to the running programs. Used only with _Local host_

With _Remote host_, the Task starts the Windows command `rundll32 powrprof.dll, SetSuspendState` on the remote computer. The Hibernate Task starts the same command, so whether the remote computer sleeps or hibernates depends on its own power settings. The Task reports success once the start request is sent, even when the remote computer does not start the command.

#### Wake up group

The options in this group are available only with _Local host_.

- _Wake up_: when selected, the Task sets a wake-up time before the computer goes into standby
- _At a certain date and time_: wakes the computer at the date and time entered. Selected by default
- _At a certain time_: wakes the computer at the time entered, on the day the Task runs. A time that has already passed that day does not set a wake-up for the next day
- _After a certain time (hour,minute,second)_: meant to wake the computer after the hours, minutes and seconds entered

:::warning

With _After a certain time (hour,minute,second)_, only the seconds value is used and the hours and minutes are ignored, so the computer is set to wake within a minute, and the Task reports success. To wake the computer after a longer period, use _At a certain date and time_.

:::

On success, the output is "Standby success".

:::info Note

**Remark on Wake Up**

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::
