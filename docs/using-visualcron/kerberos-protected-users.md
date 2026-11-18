---
sidebar_label: 'Kerberos-Only Authentication and AD Protected Users'
hide_title: 'true'
---

## Kerberos-only authentication and AD Protected Users

Windows normally negotiates between Kerberos and NTLM without telling you which one it used. A domain that enforces Kerberos refuses NTLM outright, for example for accounts in the Active Directory _Protected Users_ group. Two parts of VisualCron authenticate against Active Directory, and each fails in its own way when NTLM is refused:

- **The Client connection to the Server:** when a connection uses _Use Active Directory logon_, the Client authenticates the Windows user to the VisualCron Server
- **The Server's Active Directory lookup:** after the connection is authenticated, the Server looks the user up in Active Directory with the Credential on the **_Users/Logon_** tab, to confirm the account and read its groups

This page describes how to configure both so that they use Kerberos, and how to read the messages you get when they do not.

### Before you start

Confirm the following on the Server computer:

- the account the VisualCron Service runs under. Open the Windows Services console, open the properties of **VisualCron Service** and read the **Log On** tab. Local System is the installer default
- for Local System, that the service principal name `HOST/<server FQDN>` is registered for the computer account. Run `setspn -l <server DNS name>` in a Windows command prompt. Windows registers this name on every computer joined to a domain
- that Clients reach the Server by a host name that resolves to its fully qualified domain name, not by IP address. No Kerberos ticket can be issued for an IP address

### Configure the Client connection

The connection needs "SPN identity" or "UPN identity". "DNS Identity" carries no Windows credentials to a remote Server, so an Active Directory logon over it is refused.

To make a Client connection authenticate with Kerberos, complete the following steps:

1. Go to ***File*** -> ***Servers*** -> ***Manage Servers***, select the connection, and click ***Edit***.
2. Make sure _Is a local server_ is cleared and _Server_ is the Server's host name, not an IP address.
3. Select _Use Active Directory logon_.
4. In the _Identity type_ list, select "SPN identity" if the VisualCron Service runs as Local System, or "UPN identity" if it runs as a domain user account.
5. In the _Principal name_ field, enter the matching value from the **_Users/Logon_** tab of the Server settings: `HOST/<server FQDN>` for "SPN identity", or the service account's UPN, for example `svc-vc@contoso.com`, for "UPN identity".
6. Click ***Update***, then connect.

The connection logs on with Kerberos.

If the Client is connected to that Server when you select _Use Active Directory logon_, and the connection still has "DNS Identity" with an empty _Principal name_, the window fills in steps 4 and 5 for you. Check the filled-in values. They stay editable until you click ***Update***. For the exact conditions, see [Servers - Manage Servers](../client-user-interface/file/manage-servers).

If the identity type does not match the service account, the connection fails with a message that the Server does not offer the Windows-authentication endpoint this connection asked for. The message names the identity type to switch to.

Connections saved before this release are not changed on upgrade. Repeat these steps for each connection that uses Active Directory logon. A connection with "SPN identity" and a principal name that is not in `<service>/<host>` form, for example a bare `vcserver.contoso.com`, cannot be saved again until you correct the value.

### Configure the Server's Active Directory lookup

The Server's lookup can use Kerberos only when the name it sends to Active Directory is qualified: a UPN, or `DOMAIN\user`. A Credential with a bare user name and the AD domain as its _Domain_ is sent as `DOMAIN\user`. A bare user name with no _Domain_ can only authenticate over NTLM. For the full rules, see **Credential** in [Settings - Users/Logon](../client-user-interface/server/settings-users-logon).

To make the Server's lookup use Kerberos, complete the following steps:

1. Go to ***Server*** -> _Main settings_ -> _Settings_, and select the **_Users/Logon_** tab.
2. In the _AD Server:_ field, enter the domain controller's fully qualified domain name. Use port 389, or 3268 for the Global Catalog, if you plan to check _Force sealed connection (encrypted LDAP)_.
3. In the _Credential_ list, either clear every Credential, so that the Server queries Active Directory as its own service account, or check a Credential whose user name is a UPN or whose _Domain_ is the AD domain.
4. (Optional) Check _Force sealed connection (encrypted LDAP)_ to require that every query encrypts its LDAP traffic.
5. Click _Test_. A failed _Test_ shows the same explanation of the likely cause that the Server writes to its log for a failed logon.
6. Save the settings.

AD logons on this Server then query Active Directory with Kerberos.

_Force sealed connection (encrypted LDAP)_ encrypts the LDAP traffic. Kerberos and NTLM can both seal, so the setting does not block NTLM and does not by itself make a query use Kerberos. The qualified name does that. For the setting's details, see [Settings - Users/Logon](../client-user-interface/server/settings-users-logon).

### Reading the messages

| Where | Message | Meaning and action |
|---|---|---|
| Client, on connect | The Server rejected the Windows authentication handshake before login was attempted | Windows could not get a Kerberos ticket for the principal name in use, and the Server refused NTLM. The message names what to check for the identity type in use: for "SPN identity", an SPN that is not in `<service>/<host>` form or is not registered; for "UPN identity", a principal name that is not the service account's UPN, or a Server entered by IP address; for "DNS Identity", switch to "SPN identity" or "UPN identity" |
| Client, on connect | The Server is running but does not offer the Windows-authentication endpoint this connection asked for | The Server publishes the other endpoint. Switch to "UPN identity" for a Server that runs as a domain user account, or to "SPN identity" for one that runs as Local System |
| Client, on connect | This may indicate that the Server has not been fully started ... it did not offer the Windows-authentication endpoint this connection asked for | Either the Server is still starting, or it publishes the other endpoint. Wait and try again, then switch the identity type as the message describes |
| Client, on login | The Server did not receive a Windows identity from this connection, so Active Directory logon cannot proceed | The connection uses "DNS Identity", which carries no Windows credentials to a remote Server. Set the identity type to "SPN identity" or "UPN identity" with the correct principal name |
| Client, on login | Unhandled AD error occurred. Please view server log file. | The Server's Active Directory lookup failed. The Server log names the cause, as in the rows below |
| Server log, _Test_ | Active Directory refused the account in the 'AD Credentials' Server setting because of an account restriction (data 52f) | Typically a _Protected Users_ member whose query used NTLM because the Credential has a bare user name. Give the Credential the account's domain, enter its user name as a UPN, or clear the Credentials so the Server queries as its own service account. Logon-hour or workstation restrictions on the account give the same code |
| Server log, _Test_ | Active Directory refused the credentials VisualCron bound with | The Credential is wrong, or it cannot authenticate over NTLM. Give the Credential the account's domain or a UPN user name, clear the Credentials, or use an account that is not in _Protected Users_ |
| Server log, _Test_ | The credential's Domain ('...') was sent with the user name. If it is not an Active Directory domain, clear it or correct it. | Follows the row above when the query sent the Credential's _Domain_. Earlier releases did not send it, so a _Domain_ that names a computer outside Active Directory now makes the query fail. Correct the _Domain_, or clear it |
| Client, on save or _Test_ | 'Force sealed connection' cannot be combined with an LDAPS port (636 or 3269) in 'AD Server' | Sealing was requested over a secure LDAP port, which a domain controller always refuses. Remove the port or use 389 or 3268, or clear _Force sealed connection (encrypted LDAP)_ and keep secure LDAP |
| Server log, _Test_ | Active Directory refused the authentication method ... 'Force sealed connection' ... LDAPS | The same combination reached the Server, for example through settings saved outside the Client. Correct it as in the row above |

### Known limitations

- a connection with _Is a local server_ checked uses named pipes, where the identity type is not used. Connect by host name if the local account is in _Protected Users_
- the Server publishes the SPN endpoint only when the service runs as Local System. Network Service and Local Service get the UPN endpoint, and the Client does not fill in an identity for them
- earlier releases ignored the _Domain_ of an AD lookup Credential. A Credential whose _Domain_ names a computer that is not part of Active Directory is now sent as `<computer>\<user name>`, and Active Directory may refuse it. Correct the _Domain_, or clear it

### Related topics

- [Servers - Manage Servers](../client-user-interface/file/manage-servers)
- [Settings - Users/Logon](../client-user-interface/server/settings-users-logon)
- [Main - User Permissions](../client-user-interface/server/main-user-permissions)
- [.NET (C#/VB.NET)](dot-net-csharp-vbnet)
