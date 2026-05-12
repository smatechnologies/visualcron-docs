---
sidebar_label: 'Task VMWare - [Guest] Kill Process'
hide_title: 'true'
---

## Task VMWare - [Guest] Kill Process

The VMWare - Kill process Task kills a process in the guest operating system.

**[Guest] Kill process(es) > Connection** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Kill%20Process.png)

The Connection sub tab is the same for all VMWare Task types. See [Start VM](start-vm) for details.

**[Guest] Kill process(es) > VM Task settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Kill%20Process%20Settings.png)

**Identify process by**

Select how to identify the process to kill. Available options:

* _Process Id_ - identify the process by its numeric process ID
* _Process name_ - identify the process by its executable name

**Process Id**

The process ID of the process to kill. Click the *Refresh* icon to populate the drop-down list with the IDs of the processes currently running in the guest. Used when *Identify process by* is set to _Process Id_.

**Process name**

The name of the process to kill. Click the *Refresh* icon to populate the drop-down list with the names of the processes currently running in the guest. Used when *Identify process by* is set to _Process name_.
