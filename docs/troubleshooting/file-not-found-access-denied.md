---
sidebar_label: 'File Not Found / Access Denied'
hide_title: 'true'
---

## File Not Found / Access Denied

### Symptom

A Task that works with files fails with "File not found" or "Access denied", although the file exists.

### Cause

With *Background execution*, the default execution context of a Task, the Task runs from the VisualCron service (see [Task Main Settings - Execution Context](../client-user-interface/server/task-main-settings-execution-context)). The service runs as the Local System account by default:

- On the network, Local System acts as the computer account, which usually has no rights on shares
- Drive letters that you mapped yourself do not exist for the service

### Fix

Use a UNC path, such as "\\server\share\file.txt", instead of a mapped drive letter. Then give the Task an account that can open the file, in one of these ways.

#### Add a Credential to the Task (recommended)

VisualCron then runs the Task as that user. Use an account that has access to the file, usually the one you use to open it yourself. See [Global - Credentials](../client-user-interface/server/global-credentials).

After the change, run the Task again. It finds the file.

#### Run the service under another account

In Windows *Services*, change the *Log On* account of the *VisualCron* service, then restart the service when no Jobs are running. Every Task without a Credential then runs as that account. When you upgrade, the setup program asks for the password of that account.

:::warning

The account must be able to write to the VisualCron installation folder and to its settings, log and data folders. Tasks that use a Credential may behave differently when the service runs under a Windows account instead of Local System. After the change, run a Task that uses a Credential to test it.

:::