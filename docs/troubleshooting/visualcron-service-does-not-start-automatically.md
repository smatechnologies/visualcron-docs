---
sidebar_label: 'The VisualCron Service Does Not Start Automatically'
hide_title: 'true'
---

## The VisualCron Service Does Not Start Automatically

### Symptom

When Windows starts, the VisualCron service does not start, and Jobs do not run until someone starts the service.

### Cause

- The startup type of the VisualCron service is not "Automatic"
- The account that the service logs on as is no longer valid, for example because its password has changed
- The service takes longer to start than Windows allows, which is more likely when the computer is heavily loaded at startup

### Fix

#### Check the service

:::warning

On a computer that runs only the Client, the VisualCron service is installed as "Disabled" on purpose. Leave it disabled there. Setting it to "Automatic" starts a Server on that computer, with a default "admin" user that has no password.

On a failover cluster node, the cluster controls the VisualCron service. Do not set the startup type to "Automatic" there; the cluster starts the service on the active node. See [Install and set up VisualCron on a failover cluster](../using-visualcron/install-and-setup-visualcron-on-failover-cluster).

:::

To check the VisualCron service, complete the following steps:

1. Open `services.msc`.

   Services opens.

2. Double-click *VisualCron*.

   The properties window of the service opens.

3. On the ***General*** tab, check *Startup type*.
4. If it is not "Automatic", select "Automatic", unless the warning above applies.
5. Click *Apply*.
6. Click the ***Log On*** tab.
7. If *This account* is selected, type the current password of that account in *Password*.
8. If *This account* is selected, type the same password in *Confirm password*.
9. Click *OK*.
10. Restart Windows at a time when no Jobs are running.

    The VisualCron service starts with Windows.

If the service still does not start, open Event Viewer (`eventvwr.msc`), go to *Windows Logs* -> *System*, and look for Service Control Manager errors that name VisualCron. A timeout error means the service needs more time to start.

#### Give the service more time to start

The VisualCron setup program sets the Windows service startup timeout, ServicesPipeTimeout, to "120000" milliseconds (120 seconds) when the current value is "60000" or lower. An installation with the MSI package alone does not change it. The value takes effect after Windows restarts. If you have not restarted Windows since you installed VisualCron with the setup program, restart it first.

| Item | Value |
|------|-------|
| Key | "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control" |
| Name | "ServicesPipeTimeout" |
| Type | "REG_DWORD" |
| Data | Time in milliseconds, higher than the current value and higher than "120000" |

:::warning

Editing the registry incorrectly can stop Windows from starting. Export the key before you change it. ServicesPipeTimeout applies to every service on the computer, not only to VisualCron. Do not set a value lower than the current value or lower than "120000", because a lower value gives every service less time to start. The change takes effect only after Windows restarts, so plan the restart for a maintenance window.

:::

To give the service more time to start, complete the following steps:

1. Open `regedit` as an administrator.

   Registry Editor opens.

2. Go to "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control".
3. Click *File* -> *Export*.
4. Under *Export range*, select *Selected branch*.
5. Save the file to a safe location.
6. If *ServicesPipeTimeout* does not exist in *Control*, right-click *Control*, and click *New* -> *DWORD (32-bit) Value*.
7. If you created the value, name it "ServicesPipeTimeout".
8. Double-click *ServicesPipeTimeout*.
9. Select *Decimal*.
10. In *Value data*, note the current value.
11. Type a value higher than both the current value and "120000", for example "180000".
12. Click *OK*.
13. Close Registry Editor.
14. Restart Windows at a time when no Jobs are running.

    The VisualCron service has the new time to start.