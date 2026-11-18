---
sidebar_label: 'Task System - Hibernate'
hide_title: 'true'
---

## Task System - Hibernate

The Hibernate Task puts the VisualCron Server computer or a remote computer into hibernation. On the Server computer, the Task can also set a time for the computer to wake up. A computer in hibernation uses about 1% of normal power consumption, and it can be woken at a set time or through the network with the [Wake up on LAN](wakeup-on-lan) Task.

Hibernation writes the contents of memory to a file on the hard disk and then turns the computer almost completely off. It takes longer than Standby, both to start and to resume, because resuming goes through much of the normal startup. A computer can stay in hibernation for days, and when it resumes, everything is as it was left.

![Hibernate Task settings, with the Credentials, Hibernate and Wake up groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Hibernate.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Hibernate tab

- _Credentials_: not used. With _Remote host_, the Task connects to the remote computer through WMI as the account of the VisualCron Server service, whatever Credential is selected; that account must be allowed to start programs on the remote computer
- _Local host_ (_Hibernate_ group): hibernates the VisualCron Server computer. Selected by default
- _Remote host_: hibernates the computer entered in the field next to it
- _Force_: selected by default. When selected, the computer hibernates at once; when cleared, Windows first sends a request to the running programs. Used only with _Local host_

With _Remote host_, the Task starts the Windows command `rundll32 powrprof.dll, SetSuspendState` on the remote computer. The Standby Task starts the same command, so whether the remote computer hibernates or sleeps depends on its own power settings. The Task reports success once the start request is sent, even when the remote computer does not start the command.

#### Wake up group

The options in this group are available only with _Local host_.

- _Wake up_: when selected, the Task sets a wake-up time before the computer hibernates
- _At a certain date and time_: wakes the computer at the date and time entered. Selected by default
- _At a certain time_: wakes the computer at the time entered, on the day the Task runs. A time that has already passed that day does not set a wake-up for the next day
- _After a certain time (hour,minute,second)_: meant to wake the computer after the hours, minutes and seconds entered

:::warning

With _After a certain time (hour,minute,second)_, only the seconds value is used and the hours and minutes are ignored, so the computer is set to wake within a minute, and the Task reports success. To wake the computer after a longer period, use _At a certain date and time_.

:::

On success, the output is "Hibernate success".

:::info Note

**Remark on Wake Up**

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::
