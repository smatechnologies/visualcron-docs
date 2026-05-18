---
sidebar_label: 'Global - Credentials'
hide_title: 'true'
---

## Global - Credentials

Credentials are centrally stored in VisualCron for re-usage. Credentials might be needed in some of the following cases:

* Your Execute Task requires to run as a certain user to access certain rights
* You need to run an SQL with a trusted connection
* You need to do some kind of authentication against a web server
* Other permission request
 
Normally, all Tasks are launched from the VisualCron Server which runs as a service with LOCALSYSTEM account. That account may not have access to your network drives, certain folders etc. - that is why you need to use a Credential some times.
 
Credentials are encrypted when stored.
 
The Manage credentials window can be reached either from the main menu Server > Global objects > Credentials option.

![](../../../static/img/manage_credentials_list.png)

The Manage Credentials window displays the configured credentials in a grid with the following columns:

* **User@Domain** — the credential's username combined with its domain
* **Local** — whether the credential is configured for a local logon
* **Load profile** — whether the credential loads the user profile during logon

The toolbar above the grid provides the following buttons:

* **Add** — create a new credential
* **Edit** — edit the selected credential
* **Clone** — create a copy of the selected credential
* **Delete** — delete the selected credential
* **Copy Id to clipboard** — copy the internal credential identifier (GUID) to the clipboard
* **Audit log** — open the [Audit log](../tools/objects-audit-log) for credentials

Right‑clicking a credential opens a context menu that includes the toolbar commands plus the additional options **Versions** (view version history), **Object relations** (see which Jobs, Tasks, Triggers, or other objects reference this credential), and **Export** (export the selected credential).

### Editing a Credential

![](../../../static/img/manage_credentials_edit.png)

**Username**
 
Username for the user you want to logon. The field is an editable dropdown populated with users from the Server. When **Is Managed Service Account** is checked, the dropdown is repopulated with available (g)MSA accounts instead.
 
**Password**
 
Password for the user you want to logon. The field is masked with asterisks.
 
**Domain**
 
Domain or computer name/IP where you want to logon. The field is an editable dropdown populated with known computers/domains.

**Is Managed Service Account**

When checked, the credential is treated as a Managed Service Account (MSA) or Group Managed Service Account (gMSA). The Username dropdown switches to listing the available MSA accounts and the password is supplied automatically by Active Directory at runtime — the _Password_ field is no longer used. See the **(g)MSA accounts** section below for setup prerequisites.
 
**Local login**
 
This tells VisualCron to perform a local logon. This checkbox should be unchecked if you are using Credentials to gain access to a network drive (using a user/domain on another server as Credential).

**Test**

Validates the credential against the Server immediately, without saving. The Test button requires both _Local login_ and _Load profile_ to be enabled.

**Permissions**

Opens a permissions dialog where group-level permissions can be overridden for this credential individually.
 
### Load  profile
 
This is used on local accounts that are on the same server as VisualCron is installed. This option is only available if *Local login* is checked.
 
When checked, the following steps are taken:
 
Log on, then load the user profile in the "HKEY_USERS" registry key. The function returns after the profile is loaded. Loading the profile can be time-consuming, so it is best to use this value only if you must access the information in the "HKEY_CURRENT_USER" registry key or you have to access network resources. 
 
When not checked, the following steps are taken:
 
Log on, but use the specified credentials on the network only. The new process uses the same token as the caller, but the system creates a new logon session within LSA, and the process uses the specified credentials as the default credentials.  This value can be used to create a process that uses a different set of credentials locally than it does remotely. This is useful in inter-domain scenarios where there is no trust relationship. The system does not validate the specified credentials. Therefore, the process can start, but it may not have access to network resources. **If you just want to access a network drive** then you should specify the username, password and domain of the remote computer and use it with option "Network credentials only". To access network resources (from a local account) you have to use logon type: "With Profile". When you can - use "Network credentials only" as it is faster and takes less system resources. You must specify the UNC path. For example, you can't use the drive letter ```"Y:\yourfile.bat"```, you must use the path ```"\\server\folder\yourfile.bat"```.
 
**Extended debugging for server set to ON**
 
*In this case there are some additional options available for fine-tuning the login process*

![](../../../static/img/manage_credentials_edit_extended_debugging.png)

The additional options shown when Extended debugging is enabled are:

* **Execution API** — which underlying impersonation API to use. Available values are **API** and **API2**
* **Logon type** — Windows logon type passed to the impersonation API. Available values are **LOGON32_LOGON_INTERACTIVE**, **LOGON32_LOGON_NETWORK**, **LOGON32_LOGON_BATCH**, **LOGON32_LOGON_SERVICE**, **LOGON32_LOGON_UNLOCK**, **LOGON32_LOGON_NETWORK_CLEARTEXT**, **LOGON32_LOGON_NEW_CREDENTIALS**
* **Logon provider** — Windows logon provider. Available values are **LOGON32_PROVIDER_DEFAULT**, **LOGON32_PROVIDER_WINNT50**, **LOGON32_PROVIDER_WINNT40**, **LOGON32_PROVIDER_WINNT35**
* **SeTcbPrivilege** — enable the SeTcb (act as part of the operating system) privilege when impersonating
* **Suppress flow** — suppress the flow of execution context across asynchronous calls during impersonation
* **Override LT/LP** — override the default logon type and logon provider with the values selected above
* **Open desktop** — open the user's desktop on logon. When checked, the **Desktop path** field becomes editable for specifying the desktop name/path
* **Duplicate Token** — duplicate the access token for the impersonated session
* **Reset to default** — restore the impersonation options back to their default values

### (g)MSA accounts
 
For setting up a (g)MSA account please refer screenshot below for valid settings in AD environment and check some of the prerequisites below:
 
1. Run the following Powershell command ```Get-ADServiceAccount -Identity <gMSA-account> -Properties PrincipalsAllowedToRetrieveManagedPassword``` to check if VisualCron Server host can retrieve gMSA account password. Update gMSA account if not.
2. Check is VisualCron Server service is running under account that has "Act as part of the operating system" privilege.
3. Check both AD domain controller and VisualCron server host to have the following security option enabled:
   Group policy editor - Computer Configuration -> Windows Settings -> Security Settings -> Local policies -> Security options -> Network security: Configure encryption types allowed for Kerberos
```<select all, at least one that fits your company security polices should be enabled>```

![](../../../static/img/manage_credentials_edit_gmsa.png)

### Using and selecting a Credential
 
When you open the window, your current user name is written along with the name of your current computer/domain. Click on Add to create a centrally stored Credential. After adding the Credential it is available in all places where you can use Credentials. In those places you need to select the Credential you want to use like this:

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Credentials/Using%20Credential.png)

### Troubleshooting
 
*Error -1073741502*

See [Execute Task](../../client-user-interface/server/job-tasks-task-process-execute)
