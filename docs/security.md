---
sidebar_label: 'Security'
hide_title: 'true'
---

## Security

This page collects the security points that affect how you set up a VisualCron Server, with links to the pages that explain them.

### Checklist for a new Server

- Set a password for the default "admin" user: [Users and groups](client-user-interface/server/main-user-permissions#users-and-groups)
- Check which group new users and AD groups get, because Administrators is the default: [Default groups](client-user-interface/server/main-user-permissions#default-groups)
- Do not treat Viewers as read-only: [Default groups](client-user-interface/server/main-user-permissions#default-groups)
- Clear what a new group must not have, because it starts with nearly every right: [Permissions and actions](client-user-interface/server/main-user-permissions#permissions-and-actions)
- Give _Import settings_, _Export settings_ and _Task manager_ only to administrators: [Supported Permissions](client-user-interface/server/supported-permissions)
- Know what happens when _Execute_ on a Credential is missing, and that Credentials reach every logged-on Client: [Credentials permission](client-user-interface/server/main-user-permissions#credentials-permission)
- Know which keys a user with _Read_ can export: [Global - Certificates](client-user-interface/server/global-certificates), [Global - PGP Key Rings](client-user-interface/server/global-pgp-key-rings), [Global - SSH Keys](client-user-interface/server/global-ssh-keys)
- Choose strong key settings when you create certificates and PGP keys: [Global - Certificates](client-user-interface/server/global-certificates), [Global - PGP Key Rings](client-user-interface/server/global-pgp-key-rings)
- Close the Server port in the firewall if only local logons are wanted, because _Only allow local connections_ does not close it and does not refuse Web API logons: [Settings - Users/Logon](client-user-interface/server/settings-users-logon)
- Use a secure port for the AD server, and check its certificate: [When Test fails over secure LDAP](client-user-interface/server/settings-users-logon#when-test-fails-over-secure-ldap)
- Restrict the Web API: [Settings - Web API](client-user-interface/server/settings-web-api)
- Check the Local Security Policy settings for interactive logon: [Archived Security](security/archived-security)

### Task manager permissions for the Viewers group (13.2.1)

:::warning

The Viewers group is not read-only. Check what it allows before you use it (see [Default groups](client-user-interface/server/main-user-permissions#default-groups)).

:::

As of VisualCron 13.2.1, the Viewers group created on a new Server does not have _Delete_ on _Task manager_. Groups that already exist are not changed.

In the Task manager, _End process_ needs _Delete_ on _Processes_, and _End process tree_ needs _Delete_ on _Task manager_. To let a group end processes from the Task manager, give it those permissions. The desktop Client checks them, but the Server does not (see [Supported Permissions](client-user-interface/server/supported-permissions)).

### Remote file explorer access

:::warning

_Read_ on _Remote file explorer_ is granted to every new group and to Viewers. It lets a user download any file the VisualCron service account can read. Clear it for groups that must not see the Server's files.

:::

The remote file windows let a user browse the Server's file system:

- _Read_: browse and download files
- _Add_: create files and folders, paste and copy
- _Edit_: rename, move and change attributes
- _Delete_: delete files and folders

The Server checks these actions on every request, and the windows hide the commands a user is not allowed to use.

A new group gets _Read_ only. On a new Server, Administrators also have _Add_, _Edit_ and _Delete_. For least privilege, check that only the groups that need to change the Server's files have these actions.

### Client and Server versions

:::note

Run the same VisualCron version on the Client and the Server. When the versions differ, the Client shows a "Version mismatch" warning after logon.

:::

### Stored passwords

VisualCron stores Credential passwords and Connection passwords encrypted.
