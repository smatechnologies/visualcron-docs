---
sidebar_label: 'I Cannot Connect to the VisualCron Server'
hide_title: 'true'
---

## I Cannot Connect to the VisualCron Server

### Symptom

The Client cannot connect to the Server, or the connection fails before the login.

### Cause

- The service is not running
- The address, port or firewall does not allow the connection
- The Server allows only local connections
- The certificate that the Server uses for Client connections is damaged (see [Certificate error in the log](#certificate-error-in-the-log))

### Fix

#### Check the connection

To find why the Client cannot connect, check the following, in this order:

1. **The service is running.** On the Server computer, open `services.msc` and check that *VisualCron* shows *Running*. If not, right-click it and select *Start*. If it does not stay running, see [VisualCron Service Does Not Start Automatically](visualcron-service-does-not-start-automatically).
2. **The address and port are correct.** In the Client, check the Server connection in *File* -> *Servers* -> *Manage Servers*. The default port is "16444".
3. **The port was not changed recently.** When you change the Server port, the Server listens on the new port from then on. Update the port in the Server connection of each Client. If a VisualCron firewall rule allowed the old port, VisualCron moved it to the new port, and the moved rule allows any address: limit it to the computers that run a Client, rather than adding another rule. If no rule exists, create an inbound TCP rule for the new port, only from those computers.
4. **The firewall allows the port.** The installer creates no firewall rule. Remote Clients need an inbound TCP rule for the Server port. Before you allow it, set a password for the "admin" user (see [Secure the admin user](../get-visualcron/download-install-upgrade-uninstall#secure-the-admin-user)), and allow the port only from the computers that run a Client. See [Firewall and network](../get-visualcron/antivirus-exclusions#firewall-and-network).
5. **Remote connections are allowed.** If *Only allow local connections* is selected on the ***Users/Logon*** tab of the *Settings* window (on the ***Server*** tab, click *Settings*), only Clients on the Server computer can log on. The Server log then shows `Allowing only local connection. IP: <address> refused`.
6. **The logs show the cause.** Open "server_startup.txt" and `log_server<yyyyMMdd>.txt` in the log folder. The default log folder is "C:\Program Files (x86)\VisualCron\log". A line with "is already using port" means another program holds the port. A line with "It is likely that certificate" means the certificate is damaged; see the next section.

The Client connects once the cause is fixed.

#### Certificate error in the log

The Server log or "server_startup.txt" contains:

```text
System.ArgumentException: It is likely that certificate 'CN=vc' may not have a private key that is capable of key exchange or the process may not have access rights for the private key.
```

The certificate that the Server uses for Client connections is damaged or cannot be read. You can re-create it with *Delete certificates* and *Create certificates* in the VisualCron Server window.

If the log also shows "AddressAlreadyInUseException" with this message while the Server ran in the VisualCron Server window, the Server has already removed every matching certificate, as *Delete certificates* does. Check the store in `certlm.msc`, and restore any certificate you need from a backup. When the Server runs as the Windows service, it does not remove certificates by itself.

:::warning

*Delete certificates* removes every certificate in the computer's Personal store (Local Computer) whose subject contains "vc" anywhere, in upper or lower case, not only VisualCron's certificate. Names such as "SVC01", "VCenter" or the IIS "WMSvc-..." certificate also match. The message that follows the click has no cancel: the certificates are removed.

Before you use it, open `certlm.msc`, go to *Personal* -> *Certificates*, and export every other matching certificate with its private key (*Yes, export the private key*) to a .pfx file. If a matching certificate cannot be exported with its private key, do not use *Delete certificates*. Instead, delete only the VisualCron certificate, issued to "vc", by hand in `certlm.msc`. Then follow all the steps below, and skip the click in step 4.

:::

:::note

While the VisualCron Server window is open, the full Server runs inside that window, as the Windows user who opened it. Scheduled Jobs may run while the window is open. Do these steps when no Jobs are scheduled, and close the window as soon as you finish step 7.

:::

To re-create the certificate, complete the following steps:

1. In `certlm.msc`, export the matching certificates, as described in the warning above.

   Do this before you open the VisualCron Server window: the Server starts in that window, and if it meets the certificate error, it removes the matching certificates by itself.

2. When no Jobs are running, open `services.msc`, right-click *VisualCron* and select *Stop*.
3. Open the VisualCron installation folder, right-click "VisualCronService.exe" and select *Run as administrator*.

   The VisualCron Server window opens.

4. If you did not delete the certificate by hand, click *Delete certificates*.

   If matching certificates exist, a message shows how many were found. A second message says "Done" and asks you to close the window and start the service. Do not close the window yet.

5. Click *OK* on each message.
6. Click *Create certificates*.
7. Click *OK* on each message.
8. Close the VisualCron Server window right away.
9. In `services.msc`, right-click *VisualCron* and select *Start*.
10. Wait about one minute, then connect with the Client.

    The Server creates a new certificate and the Client connects.

If the service logs on as an account other than Local System and the error returns, give that account read access to the private key of the new certificate: in `certlm.msc`, right-click the certificate, select *All Tasks* -> *Manage Private Keys*, and allow *Read* for the account.