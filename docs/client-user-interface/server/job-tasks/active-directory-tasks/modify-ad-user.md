---
sidebar_label: 'Task Active Directory - Modify AD User'
hide_title: 'true'
---

## Task Active Directory - Modify AD User

The Modify AD User Task enables, disables, deletes or renames an Active Directory user, or resets the user's password.

![Modify AD User tab with the Credentials list, Path, the Select user button and Action](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Modify%20AD%20User.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Modify AD User tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have carried out the change as the account of the VisualCron Server service.

- _Path_: the LDAP path of the user. Click _Select user_ to pick it
- _Action_: "Disable" (default), "Enable", "Delete", "Rename" or "Reset password"
  - "Rename" changes the user's common name (CN) to _New value_. The logon names do not change
  - "Reset password" sets the password to _New value_ and also unlocks the account if it is locked out
  - "Delete" deletes the user
- _New value_: the new name or the new password. It is shown only for "Rename" and "Reset password". The box shows the value as it is typed; the Task stores it encrypted

:::warning

With "Delete", the Task deletes the user at _Path_. VisualCron cannot undo the deletion.

:::

### Output and errors

The Task writes no output. When Active Directory rejects the request, for example because the account does not have permission or the object does not exist, the Task fails with the error that Active Directory returns.

### Troubleshooting

**Error 0x80072035**

Active Directory returns error 0x80072035 ("The server is unwilling to process the request") when the password does not meet the domain's password policy, for example its length, complexity or password history rules. Use a password that meets the policy.
