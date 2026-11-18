---
sidebar_label: 'Task Manager'
hide_title: 'true'
---

## Task Manager

The ***Task manager*** window works like the Windows Task Manager for the computer that runs the VisualCron Server. It shows the system processes, the running VisualCron Jobs, the internal VisualCron threads and the Windows services.

To open it, click ***Tools*** -> ***Explore*** -> ***Task manager***.

![Task manager window on the System processes tab with the process list and the buttons at the bottom](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Task%20Manager.png)

The window has four tabs: ***System processes***, ***VisualCron Jobs***, ***VisualCron Threads*** and ***Services***. The status bar shows the Server, the number of processes and the CPU, memory, handle and thread totals.

:::warning

The actions in the Task manager act on the Server computer. Ending a process or stopping a service there can stop other programs, VisualCron itself or Windows.

:::

### Search

The search field at the bottom filters the grid of the active tab. Type to filter by name or PID. Click ***Clear*** to reset the filter.

### System processes tab

Lists the processes running on the Server, with the columns _Name_, _PID_, _User name_, _CPU %_, _Working set_ (memory in KB), _Disk_ (KB/s) and _Network_ (KB/s). Right-click the column header area to show or hide columns.

Right-click a process for these items:

- ***End process***: ends the selected process
- ***End process tree***: ends the selected process and its child processes
- ***Set priority***: changes the CPU priority of the process to "Realtime", "High", "Above normal", "Normal", "Below normal" or "Low"
- ***Set affinity***: opens the ***Processor affinity*** window to choose which processors may run the process
- ***Open file location***: opens the folder that holds the program file
- ***Properties***: shows the Windows file properties of the program file
- ***Go to service(s)***: switches to the ***Services*** tab and selects the service that uses the process

The Client asks you to confirm before it ends a process or changes its priority. The right-click menu is not available for protected system processes, such as System, csrss and lsass.

The buttons at the bottom are ***Run new process*** (shown as ***Start new process*** after you switch tabs), which starts a program on the Server, and ***End process***.

### VisualCron Jobs tab

Lists the running VisualCron Jobs with their Tasks or Triggers and their real-time CPU usage. The grid is a tree; its layout depends on the selected view. The columns include _Name_, _Description_, _CPU time_ and _CPU %_; process rows also show _Started_ and _Runtime_.

On this tab, a combo box next to the search field limits the search to Job, Task or Trigger entries.

The buttons at the bottom are ***Start new job***, which starts a Job by name on the Server, and ***Stop***, which stops the selected running Job process.

### VisualCron Threads tab

Lists the internal VisualCron threads that are processing Jobs, Tasks and Triggers, with the columns _Started_, _Id_, _Thread name_, _Job name_, _Task/Trigger Name/Description_, _CPU time_ and _CPU %_. The search filters on thread name, Job name and Task or Trigger name. This tab has no buttons at the bottom.

### Services tab

Lists the Windows services on the Server, with the columns _Name_, _PID_, _Description_, _Status_, _Startup Type_ and _Log On As_.

Right-click a service for these items:

- ***Start***: starts the service, when it is stopped
- ***Stop***: stops the service, when it is running
- ***Restart***: restarts the service, when it is running
- ***Go to process***: switches to the ***System processes*** tab and selects the process of the service

The search filters on service name, description and PID.

The buttons at the bottom are ***Restart service***, available when the service is running, and a button that shows ***Start service*** for a stopped service or ***Stop service*** for a running one.
