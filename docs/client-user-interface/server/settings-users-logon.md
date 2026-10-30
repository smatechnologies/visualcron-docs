---
sidebar_label: 'Settings - Users/Logon'
hide_title: 'true'
---

## Settings - Users/Logon

In the main menu S**erver > Main settings > Settings** dialog, there are a set of important setting groups/tabs. In this tab, the users and logon settings are managed.
 
**Main > Settings > Users/Logon** tab

![](../../../static/img/serversettingsuserslogonad.png)

**Only allow local connections**

This setting closes the remote port 16444 for incoming connections. Local login is only possible.
 
**Allow Active Directory logon**

VisualCron has two different authentication systems; one internal and one that is extended by Active Directory. This box needs to be checked in order to allow AD logon.
 
**AD Server**

When using Active Directory logon you need to specify server name or IP address. This will be used as default when working with [user permissions](../server/main-user-permissions).
Add :636 to make secure LDAP connections, for example **adhostname:636**. Otherwise a non-secure connection is used.
The name of the AD server can also be specified in the extended format: HostName:PortNumber/DistinguishedName. For example: **contoso.com:636/DC=contoso,DC=com**

Use a fully qualified domain name rather than a NetBIOS name or an IP address when Kerberos is required: no Kerberos ticket can be issued for a name that has no service principal.

:::caution

Do not combine an LDAPS port (636 or 3269) with **Force sealed connection**. A domain controller refuses to seal a connection that TLS already protects, so every logon bind would fail. While **Allow Active Directory logon** and **Force sealed connection** are both on, Save, Test and **Find AD users** on this tab refuse an LDAPS port in **AD Server**, and Save also refuses when an AD user or group in [user permissions](../server/main-user-permissions) has an LDAPS port in its own AD Server. With sealing on, use port 389, or 3268 for the Global Catalog; sealing encrypts the traffic itself.

:::

**Credential**

The AD Server Credential that will be used as default when working with [user permissions](../server/main-user-permissions).

Leave it empty to bind as the account the VisualCron Service runs under, which for Local System is the computer account.

When you use a credential, the Server binds with `DOMAIN\user` if the credential has a bare user name and a **Domain**, so that Windows can request a Kerberos ticket for the account. A user name that is already a UPN, such as `user@contoso.com`, or already qualified, such as `CONTOSO\user`, is sent unchanged. A credential with no Domain, with `.` as its Domain, or with the Server computer's own name as its Domain is sent as the bare user name, which can only authenticate over NTLM. Active Directory refuses NTLM for members of the **Protected Users** group, so for such an account set the credential's **Domain** to the Active Directory domain, for example `CONTOSO`, or enter its user name as a UPN.

:::note

Earlier releases ignored the credential's Domain. A credential whose Domain names another computer that is not part of Active Directory is now sent as `COMPUTER\user` and may be refused. Correct the Domain, or clear it.

:::

**Force sealed connection (encrypted LDAP)**

Off by default. When on, every Active Directory bind the Server makes with these settings requests sealing, which encrypts the LDAP traffic with the session key of whichever protocol Windows negotiated. A bind that cannot be sealed fails instead of running unencrypted, and the reason is logged. Kerberos and NTLM can both seal, so this setting does not block NTLM and does not make a bind use Kerberos. Whether a credential can use Kerberos depends on the bind name, as described under **Credential**.

The setting applies to the logon lookup, the Test button, the scheduled check of AD groups, and the **Find AD user** and **Find AD group** searches in [user permissions](../server/main-user-permissions). Those searches run on the Client computer and bind to the domain controller from there. The setting is only available, and only takes effect, while **Allow Active Directory logon** is on. A Client from an earlier release that saves these settings leaves the setting as it is on the Server.


## Test button

Press **Test** to check that the VisualCron Server can bind to the AD Server with the values currently on this tab, saved or not. Access is required to authorize connecting AD users: to verify that the user exists and to obtain the list of AD groups the user belongs to, which determines the user's permissions.

The Test binds the same way a logon does. It uses the **AD Server**, the first **Credential** in the list, and the **Force sealed connection** state as they are on the form; **Force sealed connection** applies only while **Allow Active Directory logon** is on. With no credential it binds as the account the VisualCron Service runs under. A failed Test shows the same explanation the Server writes to its log for a failed logon, naming the likely cause. The Test requires permission to edit Server Settings.

**Additional testing**

If the Test is unsuccessful, **Force sealed connection** is off, and an LDAPS port is used (636 or 3269), the Server also tries a direct LDAPS bind. To make use of this, first turn on [extended debug logging](../server/settings-log-settings), apply the settings, then open the Users/Logon tab again and specify the AD Server in the extended format HostName:PortNumber/DistinguishedName, for example contoso.com:636/DC=contoso,DC=com. Server log messages starting with "GotADTest" then help determine the source of the problem. This second bind does not run while **Force sealed connection** is on, because a logon has no such fallback.

 
**Users/Logon** 

screen also displays the UPN and SPN values the VisualCron Server derives for its own service account and uses to create its Windows-authentication endpoint.

Only one of the two applies, depending on the account the VisualCron Service runs under: the SPN when the service runs as Local System, the UPN when it runs as a domain user account. Enter the value that applies in a Client connection that uses Active Directory logon: the SPN with **SPN identity**, or the UPN with **UPN identity**. When the Client is connected to this Server and you select **Use Active Directory logon** on a connection that still has **DNS Identity** and no principal name, the Client fills the value in for you. For details, see [manage servers](../file/manage-servers).

**UPN**

The User Principal Name of the service account. The UPN is in the form username@domain. For example, when the service is running in a user account, it may be **```username@contoso.com```**
 
**SPN**

The Service Principal Name: the fully qualified name of the Server computer prefixed with the `HOST/` service class, for example **HOST/server.contoso.com**. A bare host name without the `HOST/` prefix is not an SPN and cannot be used to obtain a Kerberos ticket. To list the SPNs registered for the Server computer, run `setspn -L <server name>` at a command prompt.
