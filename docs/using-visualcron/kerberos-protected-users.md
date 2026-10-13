---
sidebar_label: 'Kerberos-Only Authentication and AD Protected Users'
hide_title: 'true'
---

## Kerberos-Only Authentication and AD Protected Users

Windows normally negotiates between Kerberos and NTLM without telling you which one it used. A domain that enforces Kerberos, for example by placing accounts in the Active Directory **Protected Users** group, refuses NTLM outright. Two parts of VisualCron authenticate against Active Directory, and each of them fails in its own way when NTLM is refused:

- The **Client connection** to the Server. The Client authenticates the Windows user to the VisualCron Server when a connection uses **Use Active Directory logon**.
- The **Server's Active Directory lookup**. After the connection is authenticated, the Server looks the user up in Active Directory, using the credential in **Users/Logon**, to confirm the account and read its groups.

This page describes how to configure both so that they use Kerberos, and how to read the messages you get when they do not.

### Before you start

Confirm the following on the Server computer:

- The account the VisualCron Service runs under. Open the Windows Services console, open the properties of **VisualCron Service** and read the **Log On** tab. **Local System** is the installer default.
- For Local System, that the service principal name `HOST/<server FQDN>` is registered for the computer account. Run `setspn -L <server name>` at a command prompt; the list should contain `HOST/<server FQDN>`. Windows registers this automatically on every domain-joined computer.
- That Clients reach the Server by a host name that resolves to its fully qualified domain name, not by IP address. No Kerberos ticket can be issued for an IP address.

### Configure the Client connection

To make a Client connection authenticate with Kerberos, complete the following steps:

1. In the Client, open **File > Servers > Manage servers** and select the connection.
2. Confirm that **Is a local server** is cleared and that **Server** is the Server's host name.
3. Select **Use Active Directory logon**.
4. Set **Identity type** to **Automatic (recommended)**. Leave **Principal name** empty; the Client derives it.
5. Select **Update**, then connect.

If the Server runs under a domain user account, the first connection with Automatic fails with a message saying the Server did not offer the endpoint the connection asked for. In that case set **Identity type** to **UPN identity**, enter the service account's UPN, shown in **Server > Settings > Users/Logon**, and connect once. Afterwards you can switch back to Automatic: the Client remembers the UPN.

Connections saved before this release are not changed on upgrade. Repeat these steps for each connection that uses Active Directory logon. A connection that already has **SPN identity** with a principal name that is not in `service/host` form, for example a bare `server.contoso.com`, is refused the next time you save it until you correct the value or select Automatic. For the individual identity types see [manage servers](../client-user-interface/file/manage-servers).

### Configure the Server's Active Directory lookup

To make the Server's lookup use Kerberos, complete the following steps:

1. Open **Server > Main settings > Settings > Users/Logon**.
2. Set **AD Server** to the domain controller's fully qualified domain name, with port 389, or 3268 for the Global Catalog. Do not use 636 or 3269 together with sealing.
3. Under **Credential**, either remove the credential so that the Server binds as its own service account, or keep a credential for an account that is allowed to use Kerberos.
4. Select **Force sealed connection (requires Kerberos, no NTLM fallback)**.
5. Select **Test**. A successful Test means the bind completed over Kerberos. A failed Test shows the same explanation the Server writes to its log for a failed logon.
6. Save the settings.

**Force sealed connection** makes every bind the Server performs with these settings request sealing, which only Kerberos provides. A bind that could only complete over NTLM is refused and the reason is logged, instead of the lookup silently downgrading and failing later with a misleading "user does not exist". The setting also applies to the AD user and AD group searches in [user permissions](../client-user-interface/server/main-user-permissions); those run on the Client computer and need a Kerberos path to the domain controller as well. For the setting's details see [Users/Logon](../client-user-interface/server/settings-users-logon).

### Reading the messages

| Where | Message | Meaning and action |
|---|---|---|
| Client, on connect | The Server rejected the Windows authentication handshake before login was attempted | Windows could not get a Kerberos ticket for the principal name in use and the Server refused NTLM. The message names the identity type in use and what to correct: an SPN not in `service/host` form, or a Server entered by IP address. Select Automatic and enter the Server by host name. |
| Client, on connect | The Server has not been fully started ... it did not offer the Windows-authentication endpoint this connection asked for | The Server is running but publishes the other endpoint. Switch to UPN identity for a Server running under a domain user account, or to Automatic for one running as Local System. |
| Client, on login | The Server did not receive a Windows identity from this connection | The connection uses DNS Identity, which carries no Windows credentials to a remote Server. Select Automatic. |
| Client, on login | Unhandled AD error occurred. Please view server log file | The Server's Active Directory lookup failed. The Server log names the cause, for example that Active Directory refused the credential because it cannot authenticate over NTLM. |
| Server log | Active Directory refused the credentials VisualCron bound with ... Clear 'AD Credentials' so the Server binds as its own service account | The lookup credential is an account that Active Directory refuses over NTLM, typically a Protected Users member. Remove it, use an account that is not in the group, or turn on Force sealed connection with an AD Server on port 389. |
| Server log | Active Directory refused the authentication method ... 'Force sealed connection' ... LDAPS | Sealing was requested over an LDAPS port. Remove the port or use 389 / 3268, or turn sealing off and keep LDAPS. |

### Known limitations

- A connection with **Is a local server** selected uses named pipes, where the identity type is not used. Connect by host name if the local account is in Protected Users.
- A Client from an earlier release cannot read a `servers.xml` that contains a connection saved with **Automatic**, and overwrites the file. Back it up before running an older Client with the same Windows profile.
- The Server publishes the SPN endpoint only when the service runs as Local System. Network Service and Local Service currently get the UPN endpoint.
