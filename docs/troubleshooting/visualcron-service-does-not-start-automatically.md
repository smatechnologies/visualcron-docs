---
sidebar_label: 'The VisualCron Service Does Not Start Automatically'
hide_title: 'true'
---

## The VisualCron Service Does Not Start Automatically

### Cause

This issue may occur if the VisualCron Server service times out before it starts successfully. This issue is more likely to occur if your computer is heavily loaded.
 
### Resolution

:::warning

If you use Registry Editor incorrectly, you may cause serious problems that may require you to reinstall your operating system. Microsoft cannot guarantee that you can solve problems that result from using Registry Editor incorrectly. Use Registry Editor at your own risk.

:::

To resolve this issue, increase the time-out value for service startup process. When you increase this value, the VisualCron Server service has more time to load when the computer starts. To increase the service startup time, create the following registry entry: Subkey: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control Name: ServicesPipeTimeout Type: REG_DWORD Data: The number of milliseconds that you want to give the services to start in Typically, a data value of 45,000 is sufficient to keep the service from timing out. However, you can reduce or increase this value according to your specific startup requirements. For example, to use a time-out value of 60 seconds, assign a data value of 60,000 to the ServicesPipeTimeout registry entry. A larger data value does not decrease your computer's performance.
 
To create this registry entry, follow these steps:

1. Click Start, click Run, type regedit, and then click OK
2. Locate and then click the following registry subkey: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control
3. Right-click Control, point to New, and then click DWORD Value
4. In the New Value #1 box, type ServicesPipeTimeout, and then press ENTER
5. Right-click ServicesPipeTimeout, and then click Modify
6. Click Decimal, type the number of milliseconds that you want to wait until the service times out, and then click OK. For example, to wait 60 seconds before the service times out, type 60000
7. Quit Registry Editor, and then restart the computer