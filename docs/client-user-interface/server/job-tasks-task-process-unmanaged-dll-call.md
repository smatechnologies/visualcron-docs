---
sidebar_label: 'Task Process - Unmanaged dll Call'
hide_title: 'true'
---

## Task Process - Unmanaged dll Call

Executes a method with parameters on an unmanaged dll.

![Add Task window, Unmanaged dll call tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/Unmanaged%20dll%20Call.png)

**Credentials**

The function call runs as the user of the selected [Credential](global-credentials). Select a Credential in the combo box, or click the *Settings* icon to open *Manage credentials* and add or edit one. With *No Credential*, the Task runs as the account the VisualCron service runs under. This applies with *Load user profile* selected on the Credential (the default); without it, the Credential is used only for network access (see [Local login and Load user profile](global-credentials#local-login-and-load-user-profile)).
 
**Select dll/exe file**

The full path to the native DLL. If you move this Task to another Server, move the DLL as well. The browse button opens a file browser.
 
**Force 32 bit execution**

Select for a 32-bit DLL; a 64-bit process cannot load it. Applies on a 64-bit operating system.
 
**Function name**

The exact name of a function the DLL exports.
 
**Return type**

Select the return type of the function. The default is *Int32*.
 
**Calling convention**

Set the calling convention used to invoke the function. Options are:

* *Cdecl* — C-style convention; the caller cleans up the stack. Required for variadic (variable-argument) functions
* *FastCall* — not supported by .NET interop; do not use it
* *StdCall* — the callee cleans up the stack. Standard for most Win32 API functions (default)
* *ThisCall* — for non-static C++ member functions; the object pointer would have to be the first parameter, and parameters have no pointer type, so this is rarely usable
* *Winapi* — maps to the platform-default convention (StdCall on x86/x64 Windows)
 
**Output format**

Select how the function's return value is serialized:

* *ToString representation of output* — calls `.ToString()` on the return value (default). Arrays are comma-separated.
* *XML representation of output* — serializes the return value as XML.
 
**Parameters**

Add each parameter the function takes: right-click the grid and select *Add*. Parameters are passed in grid order. Double-click a row to edit its value. String parameters are passed as ANSI strings.
