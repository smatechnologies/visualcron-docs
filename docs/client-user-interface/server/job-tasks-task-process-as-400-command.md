---
sidebar_label: 'Task Process - AS/400 Command'
hide_title: 'true'
---

## Task Process - AS/400 Command

The Process - AS/400 Command Task lets you execute a command on an AS/400 server. The AS/400 Control Language (CL) is a scripting language for the AS/400 midrange platform bearing a resemblance to the IBM Job Control Language and consisting of an ever-expanding set of command objects (*CMD) used to invoke traditional AS/400 programs and/or get help on what these programs do.

![Add Task window, AS/400 Command tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/AS%20400.png)

**Connection**

Required. Select an AS/400 Connection, set up as described in [AS/400 Connection](../server/connection-as400).

:::warning

If no Connection is selected or the Connection no longer exists, the command is not run, and by default the Task still succeeds. If the connection or sign-on to the AS/400 fails, the Task fails with exit code 77777.

:::
 
**Full command**

Specify the command to call the program with any parameters according to the default format. For example:

```
CALL PGM(programName) PARM(param1 param2)
```

The command can contain Variables. The command's own output is not returned to VisualCron; if the command fails, the Task fails with exit code 77777.
 
:::tip Note

The VisualCron Server needs IBM i Access for Windows (formerly IBM Client Access), including its 32-bit components.

:::
