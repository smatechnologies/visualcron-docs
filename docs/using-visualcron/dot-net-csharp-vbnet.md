---
sidebar_label: '.NET (C#/VB.NET)'
hide_title: 'true'
---

## .NET (C#/VB.NET)

**.NET**

A c# project sample with a lot of functionality exists in the API folder of the installation folder.
 
We recommend looking at the basic tutorial for the API [here](../videotutorials) - then look at the API sample project.
 
Below is a quick sample in c#:
 
```csharp

// create Server object that holds all VisualCron objects like Jobs, Credentials, Connections etc.
Server s;
// create Client object that is used to connect to the Server
Client c = new Client();
 
// create a Connection object which tells how VisualCron should connect
Connection conn = new Connection();
// use remote connection method to connect to a Server instance on another computer (default local connection)
conn.ConnectionType = Connection.ConnectionT.Remote;
// specify the DNS name or IP of remote server
conn.Address = "192.168.0.73";
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
// set below to true to connect with your AD credentials (must be setup on Server to support)
 conn.UseADLogon = true;
 
if (conn.ConnectionType == Connection.ConnectionT.Remote)
 {
  // for the remote connection with AD credentials we can optionally specify Server identity: either UPN or SPN
  if (specifyUpnIdentity)
   {
     conn.EndpointIdentityType = EndpointIdentityT.UpnIdentity;
    // specify the UPN of the service account. The UPN is in the form username@domain. For example, when the service is running in a user account, it may be username@contoso.com
     conn.PrincipalName = "username@domain.com";
   }
  else if (specifySpnIdentity)
   {
     conn.EndpointIdentityType = EndpointIdentityT.SpnIdentity;
    // specify the explicit service SPN as the hostname part of the service endpoint address prefixed with the "host/" literal
     conn.PrincipalName = "HOST/hostname.domain.com";
   }
 }
}
 
// connect to Server, set sync to true to get all Server objects
s = c.Connect(conn, true);
 
// loop through existing Jobs
foreach (JobClass j in s.Jobs.GetAll())
{
// write Job name to console
 Console.WriteLine(j.Name);
}
 
// finally disconnect
s.Disconnect();

```