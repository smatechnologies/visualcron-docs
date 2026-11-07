---
sidebar_label: 'System.NotSupportedException'
hide_title: 'true'
---

## System.NotSupportedException: The Server Mode SSL Must Use a Certificate

### Symptom

The Server log contains "System.NotSupportedException: The server mode SSL must use a certificate with the associated private key".

### Cause

A VisualCron component that serves an encrypted (TLS) connection is using a certificate that has no private key, or whose private key the account of the VisualCron service cannot read.

### Fix

If the log also contains the "CN=vc" certificate error, follow [Certificate error in the log](i-cant-connect-to-visualcron-server#certificate-error-in-the-log).

If you selected your own certificate for an encrypted connection, check that certificate. To check the certificate, complete the following steps:

1. Open `certlm.msc` and go to *Personal* -> *Certificates*.
2. Double-click the certificate.

   The ***General*** tab shows "You have a private key that corresponds to this certificate" when the private key is present.

3. If the private key is present and the service logs on as an account other than Local System, right-click the certificate, select *All Tasks* -> *Manage Private Keys*, and allow *Read* for that account.
4. When no Jobs are running, restart the *VisualCron* service.

   The encrypted connection starts and the error no longer appears in the log.

If the private key is missing, import the certificate again in VisualCron. *Use user certificate* on the ***Web API*** tab uses the certificate stored in VisualCron, so importing it into Windows again does not fix it. To import the certificate again, complete the following steps:

1. On the ***Server*** tab, click *Certificates*.
2. Import the certificate again from a .pfx file that includes its private key. See [Global - Certificates](../client-user-interface/server/global-certificates).
3. On the ***Server*** tab, click *Settings*.
4. On the ***Web API*** tab, select the imported certificate for *Use user certificate*.
5. Click *Apply settings*.
6. When no Jobs are running, restart the *VisualCron* service.

   The encrypted connection starts and the error no longer appears in the log.

:::warning

If you replace a certificate, or switch from *Use user certificate* to *Use self signed certificate* on the ***Web API*** tab and click *Apply settings*, programs that call the Web API and trust the current certificate stop trusting the connection. Update those programs to trust the new certificate.

:::