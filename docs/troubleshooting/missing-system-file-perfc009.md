---
sidebar_label: 'VisualCron error: Missing System File perfc009.dat'
hide_title: 'true'
---

## VisualCron error: Missing System File perfc009.dat

### Symptom

A Task fails with exit code "77777", or a Process Condition fails, with the message "Missing system file perfc009.dat, go to supportpage of VisualCron for more information." The Task result shows:

```text
Process performance counter is disabled, so the requested operation cannot be performed.
```

### Cause

VisualCron checks whether a process is running, for example for *Don't start task if task process is already running* in an Execute Task, or for a Process Condition. Windows could not return process information, because its performance counter settings are damaged or the process counters are turned off.

### Fix

To repair the performance counters, complete the following steps:

1. Open Command Prompt as an administrator.
2. Back up the current counter settings:

   ```cmd
   lodctr /S:"%TEMP%\perfcounters-backup.ini"
   ```

3. Rebuild the counter settings:

   ```cmd
   lodctr /R
   ```

4. Check whether the process counters are turned on:

   ```cmd
   lodctr /Q:PerfProc
   ```

5. If the result shows that PerfProc is disabled, turn it on:

   ```cmd
   lodctr /E:PerfProc
   ```

6. Update the counters in WMI:

   ```cmd
   winmgmt /resyncperf
   ```

7. When no Jobs are running, restart the *VisualCron* service.
8. Run the Job again.

   The Task runs without the error.

If the error remains, contact your Windows administrator or Microsoft support.