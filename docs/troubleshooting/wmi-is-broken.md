---
sidebar_label: 'WMI is Broken - Setup Fails'
hide_title: 'true'
---

## WMI is Broken - Setup Fails

### Symptom

VisualCron setup fails, or the Server logs errors from WMI (Windows Management Instrumentation) queries.

### Cause

VisualCron depends on WMI. The setup program uses it to read and set the VisualCron service settings, and the Server uses it for system information. If the WMI repository on the computer is damaged, these calls fail.

To check for a damaged repository, run `wmimgmt.msc`, right-click *WMI Control (Local)* and select *Properties*. An error on the ***General*** tab points to a WMI problem.

### Fix

:::warning

Repairing or resetting the repository restarts the Windows Management Instrumentation service and the services that depend on it. Run these commands in a maintenance window, when no Jobs are running.

:::

To repair the WMI repository, complete the following steps:

1. Open Command Prompt as an administrator.
2. Check the repository:

   ```cmd
   winmgmt /verifyrepository
   ```

   If the result says that the repository is consistent, the repository is not the cause, so do not repair or reset it. Stop here, and contact your Windows administrator about other WMI causes.

3. Back up the repository. If the backup fails because the repository is badly damaged, continue with the next step.

   ```cmd
   winmgmt /backup "%TEMP%\wmi-backup.rec"
   ```

4. Repair the repository:

   ```cmd
   winmgmt /salvagerepository
   ```

5. Check the repository again:

   ```cmd
   winmgmt /verifyrepository
   ```

6. If the setup program failed, run setup again. If the errors were in the Server log, restart the *VisualCron* service when no Jobs are running.

   Setup completes, or the Server log shows no more WMI errors.

If the repository is still not consistent after step 5, reset it.

:::warning

Resetting the repository returns it to its initial state. Settings that other programs added to WMI are lost, and those programs may need to be repaired or reinstalled. Ask your Windows administrator before you continue.

:::

To reset the WMI repository, complete the following steps:

1. Open Command Prompt as an administrator.
2. Reset the repository:

   ```cmd
   winmgmt /resetrepository
   ```

3. If the setup program failed, run setup again. If the errors were in the Server log, restart the *VisualCron* service when no Jobs are running.

   Setup completes, or the Server log shows no more WMI errors.

If WMI still fails, contact your Windows administrator or Microsoft support.