---
sidebar_label: 'Main - User Permissions'
hide_title: 'true'
---

## Main - User Permissions

User permissions control who can log on to a VisualCron Server and what each person can do there. Use this page to add users and Active Directory (AD) groups, to put users into groups, to set what each group may do, and to give a group different rights on one Job, Credential or Connection.

### Users and groups

A user is a user name and password that can log on to the Server. Permissions are not set on the user. They are set on groups, and a user belongs to one or more groups. A user can do something if any of their groups allows it. A user who belongs to no group can log on but cannot do anything.

Users can be internal VisualCron users, or AD users who log on with their Windows account. See [Active Directory logon](#active-directory-logon).

You manage users and groups in two windows:

- **_Server_** -> _Main settings_ -> _User permissions_: users and AD groups
- **_Server_** -> _Main settings_ -> _Group permissions_: groups and their permissions, in the _Manage group permissions_ window

Every user who belongs to a group can open both windows, because _Read_ on _User permissions_ is always granted. Adding, editing or deleting users and groups needs _Add_, _Edit_ or _Delete_ on _User permissions_. Your own user is an exception. The desktop Client lets you change its name, user name, email and password without _Edit_. The Server accepts changes a user makes to their own user record, including group membership, from programs other than the desktop Client.

:::warning

A new Server has the user "admin" with no password, in the Administrators group. Set a password for it right after you install VisualCron, or create your own administrator user and then delete "admin".

The Server creates "admin" again, with no password, when no users remain: at the next start, or after an import that leaves no users. Keep at least one administrator user. If "admin" appears again, set its password at once.

:::

The user list also has a built-in user for the VisualCron tray client, in the group _VisualCron system group (limited)_. It can log on only from the Server computer. The Client does not let you edit it, and the Server creates it again if it is missing. Leave it as it is.

### Active Directory logon

By default, users log on with an internal VisualCron user name and password. To let users log on with their Windows account, two settings are needed:

- On the Server: check _Allow Active Directory Logon_ on the **_Users/Logon_** tab (see [Settings - Users/Logon](../server/settings-users-logon))
- On the Client: select _Use Active Directory logon_ in the _Add/Update server_ window (see [Servers - Manage Servers](../file/manage-servers))

**_Server_** -> _Main settings_ -> _Settings_ -> **_Users/Logon_**

![Users/Logon tab of the Settings window with Only allow local connections, Allow Active Directory Logon, AD Server, the Credential list, Test, SPN and UPN](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/User%20Settings.png)

**_File_** -> _Manage servers_ -> _Add_

![Add/Update server window with Use Active Directory logon selected under Credentials](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/Manage%20Servers.png)

### The User permissions window

The window has two tabs:

- **_Users_**: internal users and AD users
- **_AD groups_**: the AD groups whose members may log on

A green check icon marks an active user or AD group, and a red cross marks an inactive one. An inactive user cannot log on.

On the **_Users_** tab, the columns are _User name_, _Name_, _AD_ (whether this is an AD user), _Email_, _Domain_, _AD host name_, _ExpiryDate_ and _Blocked_. _ExpiryDate_ is the date the password expires. When password rules are off, it shows 12/31/9999.

The toolbar buttons _Add_, _Edit_, _Clone_, _Delete_ and _Audit log_ act on the tab that is selected. _Clone_ opens a new user (or AD group) filled in with a copy of the selected one, groups and password included. Change the user name and enter a new password before you click _OK_.

Right-click a user for more actions:

- _Deactivate_ / _Active_: turns logon off or on for the user
- _Block_ / _Unblock_: blocks logon for the number of minutes in _Lock account for_ on the **_Password rules_** tab of the Settings window. Blocking applies to internal users only. If _Lock account for_ is "0", the block ends at once
- _Update password_: shown on your own user when you cannot edit users, so that you can change your own password
- _Audit log_ and _Versions.._: show the changes made to the user

**_Server_** -> _Main settings_ -> _User permissions_

![User permissions window, Users tab, listing two built-in users with the User name, Name, AD, Email, Domain, AD host name, ExpiryDate and Blocked columns](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/User%20Permissions.png)

### Add or edit a user

_Add_, _Edit_ and _Clone_ open the _Add/Edit user_ window. It has two tabs, **_Credentials_** and **_Groups_**.

**_Server_** -> _Main settings_ -> _User permissions_ -> **_Users_** -> _Add_ -> **_Credentials_**

![Add/Edit user window, Credentials tab, with Is AD user, Use permissions from AD groups, Name, Username, Password, Email, Active and Expire](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/Add%20Edit%20User.png)

**Is AD user (click on Search button to add AD user)**

Checked when the user is an AD user. You cannot check it yourself. Click the Search button next to _Name:_ and select the user in Active Directory, and the box is checked for you. For an AD user, _Name:_, _Username:_ and _Password:_ cannot be edited.

**Use permissions from AD groups**

Available for AD users only. When checked, the user gets the groups of the AD groups they belong to (see [How AD users get their permissions](#how-ad-users-get-their-permissions)), and the **_Groups_** tab is unavailable. When cleared, the groups checked on the user's own **_Groups_** tab apply.

**Name:**

The display name, shown in the user list and in the Server log.

**Username:**

The name used to log on. It must be unique.

**Password:**

The password used to log on. When _Implement password rules_ is on (**_Password rules_** tab of the Settings window), a password you enter must meet those rules. An empty password is still accepted, so always enter one.

**Email:**

The user's email address. For an AD user created at first logon, it is filled in from Active Directory.

**Active**

When cleared, the user cannot log on.

**Expire**

:::note

_Expire_ saves the user and closes the window at once. Click _OK_ to save any other changes first, then open the user again and click _Expire_.

:::

Marks the user's password as expired. The desktop Client then asks an internal user for a new password at the next logon, but only when _Implement password rules_ and _Force user to change the password the first login_ are both on (**_Password rules_** tab).

#### Groups tab

Check the groups the user belongs to. For a new user, the default group for new users is checked for you. On a new Server, that is Administrators, which has full rights. Clear it unless the user needs full rights (see [Default groups](#default-groups)). If no group is checked, the Client asks you to confirm before it saves the user.

### Add an AD group

On the **_AD groups_** tab, _Add_ opens the _Add AD group_ window. Members of an active AD group listed here may log on, with the VisualCron groups you choose for it.

**_Server_** -> _Main settings_ -> _User permissions_ -> **_AD groups_** -> _Add_

![Add AD group window, AD group tab, with Group name, Active and Let users inherit (not clone) permissions](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/AD%20Add%20User.png)

The **_AD group_** tab has these fields:

**Group name:**

The AD group. You cannot type it. Click the Search button and select the group in Active Directory.

**Active**

When cleared, members who follow their AD groups can no longer log on through this AD group or get its groups. Users who got a copy of its groups (see the next field), and AD users with their own groups, are not affected. To stop them, deactivate or delete them on the **_Users_** tab.

**Let users inherit (not clone) permissions**

Checked by default. Decides how a new AD user, created when they first log on, gets their permissions:

- Checked: the user follows the AD groups they belong to, and _Use permissions from AD groups_ is checked on the user
- Cleared: the user gets a copy of this AD group's VisualCron groups once, and after that keeps their own **_Groups_** tab. The user can then log on even after they leave the AD group, or after the AD group is deactivated

The **_Default VisualCron group(s)_** tab lists the VisualCron groups that members of this AD group get. For a new AD group, the default group for new users is checked for you. On a new Server, that is Administrators, so every member who logs on would get full rights. Clear it unless they need them (see [Default groups](#default-groups)).

### How AD users get their permissions

When an AD user logs on, the Server finds the user in Active Directory and reads their AD group membership. Then:

- **The user is already on the Users tab:**
  - an inactive user is refused
  - with _Use permissions from AD groups_ checked, the user must belong to at least one active AD group on the **_AD groups_** tab, or logon is refused
  - otherwise the user's own groups apply, and their AD group membership is not checked
- **The user is not on the Users tab yet:**
  - the user must belong to at least one active AD group on the **_AD groups_** tab, or logon is refused
  - the Server then adds the user to the **_Users_** tab as an AD user
  - if any of the user's active AD groups has _Let users inherit (not clone) permissions_ cleared, the user gets a copy of that group's VisualCron groups. Otherwise the user follows their AD groups

A user who follows their AD groups gets the VisualCron groups of every active AD group they belong to. The list is read again at each logon:

- a change to an AD group's VisualCron groups applies at once, and so does deactivating it
- an AD group you add to the **_AD groups_** tab applies from the user's next logon

### Groups

You can manage groups in two places:

- the _Manage group permissions_ window (**_Server_** -> _Main settings_ -> _Group permissions_)
- the **_Groups_** tab of the _Add/Edit user_ window, which has the same _Add_, _Edit_, _Clone_, _Delete_ and _Audit log_ buttons

_Add_, _Edit_ and _Clone_ open the _Add/Edit user group_ window.

**_Server_** -> _Main settings_ -> _User permissions_ -> _Add_ -> **_Groups_**

![Groups tab of the Add/Edit user window listing the Administrators, Viewers and VisualCron system group (limited) groups, with Administrators checked](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/Groups%20Tab.png)

_Add/Edit user group_ window

![Add/Edit user group window for the Administrators group, with Name, Description, Default group for new users, an older version of the automatic rights option, and the permission grid with Read, Add, Edit, Execute and Delete columns](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20User%20Permissions/Group%20Permissions.png)

**Name:**

The name of the group.

**Description:**

Optional text that describes the group.

**Default group for new users**

When checked, this group is checked for you when you add a user or an AD group. Only one group can be the default, so checking it on one group clears it on the others.

A clone of the default group has _Default group for new users_ checked, and saving the clone makes it the default. Clear the box unless the clone should become the default.

**Auto full rights on new objects**

Checked by default. Controls whether members of the group automatically get full rights on the Jobs, Credentials and Connections they create.

When checked, and the group lacks any of _Read_, _Edit_, _Delete_ or _Execute_ for that object type, the Client adds an override to the new object when a member creates it. The override gives the group _Read_, _Edit_, _Delete_ and _Execute_ on that object. Members can then manage what they create without an administrator granting rights on each new object. When the group already has those rights, no override is added.

This option has no effect for an AD user who has _Use permissions from AD groups_ checked. It applies to internal users, and to AD users who have their own groups.

**Use group permissions only (ignore per-object overrides)**

Cleared by default. When checked, every override for this group is ignored, both those that grant and those that deny. This covers overrides on a Job (and so on its Tasks), a Credential or a Connection. Only the group's own permissions apply. A group that relied on a deny override gets its own right back. See [Override permissions on one object](#override-permissions-on-one-object).

To create a group with limited rights, complete the following steps:

1. Click **_Server_** -> _Main settings_ -> _Group permissions_, and then click _Add_.
2. Enter _Name:_ and, if you want, _Description:_.
3. In the grid, clear every action the group must not have. Check in particular _Add_, _Edit_ and _Delete_ on _User permissions_, and _Import settings_ and _Export settings_ (see [Permissions and actions](#permissions-and-actions)).
4. Click _OK_.
5. Click **_Server_** -> _Main settings_ -> _User permissions_, select a user who needs the group, and click _Edit_. On the **_Groups_** tab, check the new group, clear Administrators unless the user needs full rights, and click _OK_.

For an AD group, check the new group on the **_Default VisualCron group(s)_** tab of the _Add AD group_ window instead.

### Permissions and actions

The grid in the _Add/Edit user group_ window has one row per permission and five actions:

- _Read_: view the object, or open its window
- _Add_: create a new object
- _Edit_: change an existing object
- _Execute_: run or use the object
- _Delete_: remove the object

Not every action applies to every permission. A grayed-out box cannot be changed: it is either always granted or never granted. For example, _Log_ has only _Read_.

:::warning

A new group starts with every box checked that can be changed, except _Add_, _Edit_, _Execute_ and _Delete_ on _Remote file explorer_. This includes _Add_, _Edit_ and _Delete_ on _User permissions_, which let a member manage users and groups, and so give themselves full rights. It also includes _Import settings_ and _Export settings_.

Clear every action the group must not have before you click _OK_.

:::

For the list of permissions and what each action controls, see [Supported Permissions](../server/supported-permissions).

### Credentials permission

The _Credentials_ row controls the _Manage credentials_ window and the Credentials a user can work with. For more, see [Global - Credentials](../server/global-credentials#credential-permissions).

- _Read_: open the _Manage credentials_ window. The window, and the Credential lists in Tasks, show only the Credentials the user has _Read_ on, overrides included
- _Add_: add Credentials
- _Edit_: change Credentials
- _Execute_: use the Credential in a run. When a user starts the run, the Server checks _Read_ and _Execute_ on the _Credentials_ row of that user's groups, for each Credential the run uses. That is a single _Run Job_ or _Run Task_ started from a Client, a test of a saved Credential, or a Task run requested through the Web API with a user (`Task/Run`). Runs started by the schedule or by a Trigger, _Run selected Jobs_, and Jobs started through the Web API (`Job/Run`) are not tied to a user, so no check is made. Overrides on the Credential, and _Use group permissions only (ignore per-object overrides)_, are not taken into account for this check. When you run a single Task, the desktop Client also checks _Execute_ on the _Credentials_ row of your groups, even for a Task that uses no Credential. If that check fails, the Client does not start the Task and shows "You are not allowed to use this Credential in this Task"
- _Delete_: delete Credentials

:::warning

If the check on _Execute_ or _Read_ fails, the Server does not use the Credential:

- a Task that starts a separate program, such as the Execute Task, runs as the VisualCron service account
- a Task that uses the Credential inside VisualCron fails with an error

Do not rely on clearing _Execute_ to keep a group from running a program with a Credential's rights, because the program then runs as the service account. Also limit who has _Edit_ on the Jobs, and _Add_ and _Edit_ on the Tasks, that use the Credential.

:::

:::warning

After a Credential is added or changed, the Server sends the Credential to every logged-on Client, including users who have no _Read_ on it. Do not rely on _Read_ to keep a Credential from a user who can log on to the Server. Give logons only to people you trust with your Credentials.

:::

#### A program runs as the service account

An Execute Task, or another Task that starts a separate program, ran as the VisualCron service account instead of the Credential's account. The user who started the run lacks _Read_ or _Execute_ on the Credential. Give that user's group _Read_ and _Execute_ on the _Credentials_ row, or let a user who has them start the run. An override on the Credential does not change this check.

#### A Task that uses a Credential fails when a user starts it

The Task works on schedule but fails when a particular user runs it manually or as a Task through the Web API (`Task/Run`). That user lacks _Read_ or _Execute_ on the Credential. Give the user's group both on the _Credentials_ row. An override on the Credential does not change this check.

### Override permissions on one object

You can give a group different rights on one Job, Credential or Connection. In the Job, Credential or Connection editor, click _Permissions.._ to open the _Override permissions for this object_ window.

The window lists every group with _Read_, _Add_, _Edit_, _Execute_ and _Delete_. Change the boxes for a group to override its permissions on this object only:

- a green cell grants what the group's own permissions deny
- a red cell denies what they grant

Only groups whose boxes differ from their own permissions are saved as overrides.

An override changes the rights of that group only. A user who belongs to another group that has the right still has it.

An override on a Job also applies to the Tasks in that Job. For a group with an override on a Job, the override's boxes replace the group's _Tasks_ row for those Tasks. To add a Task to a Job, the group needs _Edit_ on the Job. The desktop Client also checks _Add_ on _Tasks_, or _Add_ in the Job's override if the group has one. A group without an override on the Job uses its _Tasks_ row.

A group with _Use group permissions only (ignore per-object overrides)_ checked ignores all overrides.

Overrides on a Credential or Connection decide who can view, edit, delete and export it. They do not change the check the Server makes when a run uses the Credential or Connection. That check uses the group's _Credentials_ or _Connections_ row only (see [Credentials permission](#credentials-permission)).

### Default groups

When the Server starts with no groups at all, as on a new installation, it creates two groups:

- **Administrators**: every action in the grid, except _Execute_ on _Remote file explorer_. Administrators is the default group for new users
- **Viewers**: meant for monitoring, but not read-only (see the warning below)

Both are ordinary groups that you can edit, clone or delete. A Server that already had groups before an upgrade does not get them.

The group _VisualCron system group (limited)_ is used by VisualCron's own components. Do not assign it to users. The Client does not let you edit or delete it.

:::warning

Because Administrators is the default group for new users, it is checked for you when you add a user or an AD group. Clear it unless the user or AD group needs full rights, or make another group the default.

:::

:::warning

The Viewers group is not read-only. Viewers have:

- _Read_ on every permission, including _Server settings_, _Credentials_, _Variables_ and _User permissions_
- _Execute_ on _Connections_ and _Credentials_
- _Add_, _Edit_ and _Delete_ on _SSH keys_

With these rights, a Viewer can:

- export private keys of Certificates, PGP key rings and SSH keys (see [Global - Certificates](../server/global-certificates), [Global - PGP Key Rings](../server/global-pgp-key-rings) and [Global - SSH Keys](../server/global-ssh-keys))
- download any file the VisualCron service account can read, through the remote file windows
- browse remote systems through a Connection

Some of these boxes are grayed out and cannot be cleared in Viewers, such as _Read_ on _Credentials_ and on _Jobs_. For users who must not have these rights, create a new group with _Add_, clear what they must not have (see [Permissions and actions](#permissions-and-actions)), and use that group instead of Viewers.

:::
