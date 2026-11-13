---
sidebar_label: 'Condition - Process'
hide_title: 'true'
---

## Condition - Process

The _Process_ condition checks whether a program is running on the VisualCron Server computer. Use it, for example, to skip a Job while another program is still running, or to run a Task only when a required program is running.

This page describes the **_Process_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "Process" -> **_Process_** tab

![Add/Edit condition window with the Process tab open, showing an empty Process name box with a Select button, and Is running set to "True"](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Process.png)

### Process information

#### Process name

Enter the file name of the program, including its extension, for example "notepad.exe". Or click _Select_ to open the _Active processes_ window, which lists the processes running on the Server computer, and double-click a process to use its name. You can use Variables in the name, see [Global - Variables](global-variables). The window does not let you save the condition with an empty name.

The name must match the program's file name exactly, and the comparison is case-sensitive: "Notepad.exe" does not match "notepad.exe". Partial names and wildcards are not supported.

:::note

The check sees only the processes that the account the VisualCron service runs under is allowed to inspect. A process it cannot inspect is treated as not running.

:::

### Match

#### Is running

Select "True" to match when at least one process with that name is running, or "False" to match when none is running. The default is "True".
