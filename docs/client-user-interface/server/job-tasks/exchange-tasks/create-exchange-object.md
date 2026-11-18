---
sidebar_label: 'Task Exchange - Create Exchange Object'
hide_title: 'true'
---

## Task Exchange - Create Exchange Object

The Create Exchange object Task creates an appointment, a contact or a task in an Exchange mailbox.

![Create Exchange object tab, with the mailbox address, the Credential, the forms-based authentication option and the object type and property list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Exchange%20Tasks/Create%20Exchange%20Object.png)

:::warning

This Task connects to the mailbox with WebDAV and accepts any server certificate, so an address that starts with "https://" does not prove the identity of the server. With _Use Forms-based authentication_ checked, the user name and password of the Credential are posted to the server in a form; with an address that starts with "http://", anyone who can see the traffic can read them. Use an address that starts with "https://", on a network you trust.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create Exchange object tab

- _Mail box URL_: the WebDAV address of the mailbox, in the form `https://<server>/exchange/<mailbox>`
- _Credentials_: the Credential that signs in to the mailbox. A Credential is required; without one the Task fails with a Credential-not-found error. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials)
- _Use Forms-based authentication_: signs in through the forms-based (Outlook Web Access) sign-in page. When cleared, Windows authentication is used
- **Exchange object type and properties**: the object type, "Appointment" (default), "Contact" or "Task", and the properties to set. Click _Add_ to add a property, _Remove_ to remove the selected one, and _Up_ and _Down_ to move it. Click _Required_ to replace the list with the required properties of the type. Values may contain Variables

### Output and errors

The output is a line that confirms the type of object created.

If the mailbox cannot be reached or the request fails, the error is written to the error output and the Task fails.