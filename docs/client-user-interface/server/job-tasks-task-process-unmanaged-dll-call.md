---
sidebar_label: 'Task Process - Unmanaged dll Call'
hide_title: 'true'
---

## Task Process - Unmanaged dll Call

Executes a method with parameters on an unmanaged dll.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/Unmanaged%20dll%20Call.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Select dll/exe file**

This is the full path to the assembly file. If you move this Task to another place you need to move the assembly file as well. The file selection button open the explorer to select the file.
 
**Force 32-bit execution**

Check this if you want your dll to execute in 32 bit mode. Otherwise it will be default of the system (most likely 64 bit).
 
**Function name**

Type the name of a public function.
 
**Return type**

Select return type of the method.
 
**Calling convention**

Set the calling convention used to invoke the function. Options are:

* *Cdecl* — C-style convention; the caller cleans up the stack. Required for variadic (variable-argument) functions.
* *FastCall* — passes the first arguments in registers; rarely needed outside low-level or compiler-generated code.
* *StdCall* — the callee cleans up the stack. Standard for most Win32 API functions (default).
* *ThisCall* — passes the `this` pointer in the ECX register; used for non-static C++ member functions.
* *Winapi* — maps to the platform-default convention (StdCall on x86/x64 Windows).
 
**Output format**

Select how the function's return value is serialized:

* *ToString representation of output* — calls `.ToString()` on the return value (default). Arrays are comma-separated.
* *XML representation of output* — serializes the return value as XML.
 
**Parameters**

Lists the parameters of the selected function. Double-click a row to edit its value. Right-click the grid to access Add, Edit, and Delete options.
