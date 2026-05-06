---
sidebar_label: 'Task System - Standby'
hide_title: 'true'
---

## Task System - Standby

The Standby Task can start Standby/Sleep on a local or remote computer. When doing this on a local computer it is also possible to wake up the computer at a specific time or after a certain time. A computer in standby mode uses approximately 35% of the normal power consumption and can be waked up at a certain time or through the LAN with the Wake up on LAN Task.
 
In Standby mode, your computer might appear to be turned off but it could automatically restart. So shut down your computer completely when it's not in use e.g. on an airplane. Standby is not appropriate for long term use, on many laptops, overnight is probably pushing it on standby. And it has one important limitation, everything is in memory not saved to the hard drive.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Standby.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
**Hibernate**

**Local host** / **Remote host**

Select **Local host** to put the local computer into standby. Select **Remote host** to put a remote computer into standby and enter the hostname in the field alongside the radio button.

**Force**

When checked, forces the suspend/standby without sending a permission request to running applications.

**Wake up**

**Wake up**

When checked, enables the wake up options below and schedules the computer to wake from standby automatically.

**At a certain date and time**

Wakes up the computer at the specified date and time. Only available when **Wake up** is checked.

**At a certain time**

Wakes up the computer at the specified time of day. Only available when **Wake up** is checked.

**After a certain time (hour,minute,second)**

Wakes up the computer after the specified duration. Only available when **Wake up** is checked.


:::info Note

**Remark on Wake Up** 

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::
