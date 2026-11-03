---
sidebar_label: 'Windows Command Does Not Execute Correctly'
hide_title: 'true'
---

## Windows Command Does Not Execute Correctly

### Symptom

A program or script works when you double-click it, but not when an Execute Task runs it.

### Cause

With *Background execution*, the default execution context of a Task, the VisualCron service runs commands as the Local System account. Local System has a different environment from your user account:

- other environment variables
- no mapped drives
- other rights

A program that is not in a Windows folder or on the system PATH is also not found by name.

### Fix

#### Run the Task as your user

To run the Task as your user, complete the following steps:

1. On the ***Server*** tab, click *Credentials*.
2. Create a Credential with the user name, password and domain or computer name that you use to run the program. Passwords are case-sensitive. See [Global - Credentials](../client-user-interface/server/global-credentials).
3. Edit the Execute Task.
4. Under *Run Task as*, select the Credential.
5. Click *OK*.
6. Run the Job again.

   The program runs with the same rights as when you start it yourself.

#### Enter the full path of the program

Programs in Windows folders such as "C:\Windows\System32", or in a folder on the system PATH, are found by name. Other programs are not.

To use the full path, complete the following steps:

1. Enter the full path of the program in *Command*, for example "C:\Program Files\MyApp\myapp.exe".
2. Run the Job again.

   The program starts.

:::tip

*Working directory* sets the folder the program runs in. It is used to find the program only when *Use shell execute* is selected, and with *Use shell execute* the Task output cannot be captured. Use the full path in *Command* instead.

:::