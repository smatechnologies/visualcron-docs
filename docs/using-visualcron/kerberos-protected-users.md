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

The connection needs an SPN or UPN identity: the **DNS Identity** type carries no Windows credentials to a remote Server, so an Active Directory logon over it is refused.

To make a Client connection authenticate with Kerberos, complete the following steps:

1. In the Client, open **File > Servers > Manage servers** and select the connection.
2. Confirm that **Is a local server** is cleared and that **Server** is the Server's host name, not an IP address.
3. Select **Use Active Directory logon**.
4. Set **Identity type** to **SPN identity** if the VisualCron Service runs as Local System, or to **UPN identity** if it runs under a domain user account.
5. Set **Principal name** to the matching value shown in **Server > Settings > Users/Logon**: `HOST/<server FQDN>` for SPN identity, or the service account's UPN, for example `username@contoso.com`, for UPN identity.
6. Select **Update**, then connect.

If the Client is connected to that Server when you select **Use Active Directory logon**, and the identity is still **DNS Identity** with an empty **Principal name**, the Client fills in steps 4 and 5 for you from the values the Server reports for itself. Check the filled-in values; they stay editable until you select **Update**. For the exact conditions, see [manage servers](../client-user-interface/file/manage-servers).

If the identity type does not match the service account, the connection fails with a message saying that the Server does not offer the Windows-authentication endpoint this connection asked for, and naming the identity type to switch to.

Connections saved before this release are not changed on upgrade. Repeat these steps for each connection that uses Active Directory logon. A connection that already has **SPN identity** with a principal name that is not in `service/host` form, for example a bare `server.contoso.com`, is refused the next time you save it until you correct the value.

### Configure the Server's Active Directory lookup

The Server's lookup can use Kerberos only when it binds with a qualified account name. When the Server binds with a stored credential, it sends the user name as follows:

| Credential user name | Credential Domain | Name sent to Active Directory |
|---|---|---|
| A UPN, for example `svc-vc@contoso.com` | Any | The UPN, unchanged |
| Already qualified, for example `CONTOSO\svc-vc` | Any | The name, unchanged |
| A bare name, for example `svc-vc` | The AD domain, for example `CONTOSO` | `CONTOSO\svc-vc` |
| A bare name | Empty, `.`, or the Server computer's own name | `svc-vc`, bare |

A bare name can only authenticate over NTLM, which Active Directory refuses for members of the **Protected Users** group. With no credential at all, the Server binds as its own service account.

To make the Server's lookup use Kerberos, complete the following steps:

1. Open **Server > Main settings > Settings > Users/Logon**.
2. Set **AD Server** to the domain controller's fully qualified domain name, with port 389, or 3268 for the Global Catalog. Do not use 636 or 3269 if you also turn on **Force sealed connection**.
3. Under **Credential**, either remove the credential so that the Server binds as its own service account, or use a credential whose user name is a UPN or whose **Domain** is the Active Directory domain.
4. Optionally, select **Force sealed connection (encrypted LDAP)** to require that every bind encrypts its LDAP traffic.
5. Select **Test**. A failed Test shows the same explanation the Server writes to its log for a failed logon.
6. Save the settings.

**Force sealed connection** makes every bind the Server performs with these settings request sealing, which encrypts the LDAP traffic with the session key of whichever protocol Windows negotiated. Both Kerberos and NTLM can seal, so the setting does not block NTLM and does not by itself make a bind use Kerberos; the qualified bind name does that. A bind that cannot be sealed fails instead of running unencrypted. The setting also applies to the AD user and AD group searches in [user permissions](../client-user-interface/server/main-user-permissions). For the setting's details see [Users/Logon](../client-user-interface/server/settings-users-logon).

### Reading the messages

| Where | Message | Meaning and action |
|---|---|---|
| Client, on connect | The Server rejected the Windows authentication handshake before login was attempted | Windows could not get a Kerberos ticket for the principal name in use and the Server refused NTLM. The message names the identity type in use and what to correct: for SPN identity, an SPN that is not in `service/host` form or is not registered; for UPN identity, a principal name that is not the service account's UPN, or a Server entered by IP address. |
| Client, on connect | The Server is running but does not offer the Windows-authentication endpoint this connection asked for | The Server publishes the other endpoint. Switch to UPN identity for a Server running under a domain user account, or to SPN identity for one running as Local System. |
| Client, on connect | This may indicate that the Server has not been fully started ... it did not offer the Windows-authentication endpoint this connection asked for | Either the Server is still starting, or it publishes the other endpoint. Wait and try again, then switch the identity type as the message describes. |
| Client, on login | The Server did not receive a Windows identity from this connection, so Active Directory logon cannot proceed | The connection uses DNS Identity, which carries no Windows credentials to a remote Server. Set the identity type to SPN identity or UPN identity with the correct principal name. |
| Client, on login | Unhandled AD error occurred. Please view server log file | The Server's Active Directory lookup failed. The Server log names the cause. |
| Server log | Active Directory refused the account in the 'AD Credentials' Server setting because of an account restriction (data 52f) | Typically a Protected Users member whose bind used NTLM because the credential has a bare user name. Give the credential the account's domain, enter its user name as a UPN, or clear 'AD Credentials' so the Server binds as its own service account. Logon-hour or workstation restrictions on the account give the same code. |
| Server log | Active Directory refused the credentials VisualCron bound with | The credential is wrong, or it cannot authenticate over NTLM. Give the credential the account's domain or a UPN user name, clear 'AD Credentials', or use an account that is not in Protected Users. |
| Client, on Save or Test | 'Force sealed connection' cannot be combined with an LDAPS port (636 or 3269) in 'AD Server' | Sealing was requested over an LDAPS port, which a domain controller always refuses. Remove the port or use 389 / 3268, or turn sealing off and keep LDAPS. |
| Server log | Active Directory refused the authentication method ... 'Force sealed connection' ... LDAPS | The same combination reached the Server, for example through settings saved outside the Client. Correct it as in the row above. |

### Known limitations

- A connection with **Is a local server** selected uses named pipes, where the identity type is not used. Connect by host name if the local account is in Protected Users.
- The Server publishes the SPN endpoint only when the service runs as Local System. Network Service and Local Service currently get the UPN endpoint, and the Client does not fill in an identity for them.
- Earlier releases ignored the **Domain** of an AD lookup credential. A credential whose Domain names another computer that is not part of Active Directory, rather than the AD domain, is now sent as `COMPUTER\user` and may be refused. Correct the Domain, or clear it.
