---
sidebar_label: 'WMI is Broken - Setup Fails'
hide_title: 'true'
---

## WMI is Broken - Setup Fails

VisualCron is dependant on WMI and WMI needs to be fully working at the server side of VisualCron.
 
WMI, or Windows Management Instrumentation, is a Microsoft Windows component that publishes information about system objects. It's commonly used to perform Tasks like gathering statistics about system behavior or retrieving meta data about the computer or its applications (such as reading system logs, obtaining or modifying Registry values, manipulating remote desktops, and so on).
Unfortunately, it's easy for WMI to become damaged, and if that happens, the system may begin behaving very strangely. You may start seeing errors, some of them with the notice "Windows Management Instrumentation might be corrupted." (That message usually occurs if you're trying to edit WMI properties.)
 
One quick way to find out if WMI is broken is to enter wmimgmt.msc into the Start | Run box. This launches the WMI Management Infrastructure console, and if you get an error doing this, odds are WMI is broken.
 
If WMI is broken, how can it be fixed? The only Microsoft-endorsed way to repair WMI is to reinstall Windows. But for most of us, that isn't a practical approach. Another method is to force WMI to repair itself. Of all the WMI repair techniques I've seen, this five-step approach seems to work the best. (However, it may not work on all systems.)  
 
1. At the command line, type net stop winmgmt. You may get a warning that other services need to be stopped as well; type Y and continue
2. Open Explorer and go to the folder called %SystemRoot%\System32\WBEM\Repository
3. Delete that folder and everything in it
4. Reboot the system normally
5. On the next login, open a command prompt and type the following commands in this order: winmgmt /clearadap winmgmt /kill winmgmt /unregserver winmgmt /regserver winmgmt /resyncperf
 
This procedure will force the WINMGMT service to re-register itself as well, although, if WMI is damaged, re-registering can be a problem. If this approach does not work, an in-place upgrade (i.e., a reinstall) might be required.