---
sidebar_label: '.NET (C#/VB.NET)'
hide_title: 'true'
---

## .NET (C#/VB.NET)

This page shows how to connect to a VisualCron Server from your own C# or VB.NET program with the VisualCron .NET API, and list the Server's Jobs. It is for developers who build integrations. For an overview of the API, see [VisualCron API](visualcron-api).

### Before you start

- **References:** add references to "VisualCronAPI.dll" and "VisualCron.dll" in the VisualCron installation folder, by default "C:\Program Files (x86)\VisualCron". The DLLs are built for .NET Framework 4.8. If a debugging session ends with "Debugger Detected", reference the copies in the "lib" subfolder instead (see [VisualCron API](visualcron-api#troubleshooting))
- **Namespaces:** add `using VisualCronAPI;` and `using VisualCron;` to your code file
- **More samples:** a C# sample project with more examples is installed in "API\samples\TestClient" in the installation folder
- **Video:** for an introduction, watch [Using the .NET API](https://www.youtube.com/watch?v=Ubh_4u6zD50)

### Example

The example connects to a remote Server with a user name and password or with Active Directory, lists the Jobs and disconnects. If the logon fails, `Connect` throws `Client.ClientLoginFailedException`, and its message gives the reason. If the Server cannot be reached, `Connect` throws a different exception, so add a general `catch` if your program must handle that too.

```csharp
// create Server object that holds all VisualCron objects like Jobs, Credentials, Connections etc.
Server s;
// create Client object that is used to connect to the Server
Client c = new Client();

// create a Connection object which tells how VisualCron should connect
Connection conn = new Connection();
// connect over the network to the Server at Address (Remote is the default connection type)
conn.ConnectionType = Connection.ConnectionT.Remote;
// specify the DNS name or IP address of the Server
conn.Address = "vcserver.contoso.com";
// optionally specify the port (default value is 16444)
conn.Port = 16444;

// these variables are defined for demonstration purposes: connect with username and password, or connect with AD credentials
bool connectWithUsernameAndPassword = false;
bool specifyUpnIdentity = true;
bool specifySpnIdentity = false;

if (connectWithUsernameAndPassword)
{
// specify username you want connect as (default "admin") - user must exist in the Manage user Permissions window at Server
 conn.UserName = "admin";
// specify password you want to connect with (default empty)
 conn.PassWord = "";
}
else
{
    // connect with your AD credentials (AD logon must be allowed on the Server)
    conn.UseADLogon = true;

    if (conn.ConnectionType == Connection.ConnectionT.Remote)
    {
        // for a remote connection with AD credentials, specify the Server identity: either UPN or SPN
        if (specifyUpnIdentity)
        {
            conn.EndpointIdentityType = EndpointIdentityT.UpnIdentity;
            // the UPN of the account that the VisualCron Server service runs as, in the form username@domain
            conn.PrincipalName = "svc-vc@contoso.com";
        }
        else if (specifySpnIdentity)
        {
            conn.EndpointIdentityType = EndpointIdentityT.SpnIdentity;
            // the service SPN: the host name of the Server prefixed with "HOST/"
            conn.PrincipalName = "HOST/vcserver.contoso.com";
        }
    }
}

try
{
    // connect to the Server; true synchronizes all Server objects to the Client
    s = c.Connect(conn, true);
}
catch (Client.ClientLoginFailedException ex)
{
    // the message gives the reason, for example a wrong password or a refused remote logon
    Console.WriteLine(ex.Message);
    return;
}

// loop through existing Jobs
foreach (JobClass j in s.Jobs.GetAll())
{
    // write Job name to console
    Console.WriteLine(j.Name);
}

// finally disconnect
s.Disconnect();
```

### Active Directory logon and Kerberos

These rules apply to programs that connect with `UseADLogon = true`, and to programs that call the Active Directory methods of the API:

- **Server identity:** a remote connection with `UseADLogon = true` needs `EndpointIdentityType` set to `EndpointIdentityT.SpnIdentity` or `EndpointIdentityT.UpnIdentity`, with a `PrincipalName`. Use `HOST/<server FQDN>` when the VisualCron Server service runs as Local System, or the service account's UPN when it runs as a domain user account. A connected `Server` reports both values as `PossibleSPN` and `PossibleUPN`, and `ActiveDirectoryAPI.SuggestConnectionIdentity` picks the one that applies
- **No Windows identity:** `Connect` throws `Client.ClientLoginFailedException` with the login result `ADSecurityContextFailure` when the Server received no Windows identity for an Active Directory logon, for example on a "DNS Identity" connection to a remote Server. Earlier releases returned a `Server` marked connected although no logon had taken place
- **Force sealed connection:** `ServerSettingsClass.ADForceSealedConnection` is the _Force sealed connection (encrypted LDAP)_ setting. When you send settings with `UpdateServerSettings`, also set `ADForceSealedConnectionSent = true`. Otherwise the Server keeps its current value
- **Active Directory methods:** `ActiveDirectoryAPI.GetUser`, `GetUsers`, `GetGroups`, `GetUserGroupMembership`, `CheckADCredential` and `CheckADCredentialDirectLDAP` keep their previous signatures. New overloads take a `forceSealedConnection` argument, which requests an encrypted (sealed) LDAP session. It does not block NTLM
- **Name sent to Active Directory:** these methods send `DOMAIN\user` when the Credential has a bare user name and a Domain. A UPN or an already qualified user name is sent unchanged. A Credential with no Domain, "." or the local computer name as its Domain is sent as the bare user name. See **Credential** in [Settings - Users/Logon](../client-user-interface/server/settings-users-logon)

### Related topics

- [VisualCron API](visualcron-api)
- [Kerberos-Only Authentication and AD Protected Users](kerberos-protected-users)
