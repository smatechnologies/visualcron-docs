---
sidebar_label: 'Task Exchange - Get Exchange Object'
hide_title: 'true'
---

## Task Exchange - Get Exchange Object

The Get Exchange object(s) Task lists the appointments, contacts or tasks in an Exchange mailbox that match the filter properties.

![Get Exchange object(s) tab, with the mailbox address, the Credential, the forms-based authentication option and the object type and filter property list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Exchange%20Tasks/Get%20Exchange%20Object.png)

:::warning

This Task connects to the mailbox with WebDAV and accepts any server certificate, so an address that starts with "https://" does not prove the identity of the server. With _Use Forms-based authentication_ checked, the user name and password of the Credential are posted to the server in a form; with an address that starts with "http://", anyone who can see the traffic can read them. Use an address that starts with "https://", on a network you trust.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get Exchange object(s) tab

- _Mail box URL_: the WebDAV address of the mailbox, in the form `https://<server>/exchange/<mailbox>`
- _Credentials_: the Credential that signs in to the mailbox. A Credential is required; without one the Task fails with a Credential-not-found error. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials)
- _Use Forms-based authentication_: signs in through the forms-based (Outlook Web Access) sign-in page. When cleared, Windows authentication is used
- **Exchange object type and filter properties**: the object type, "Appointment" (default), "Contact" or "Task", and the properties an object must match. An object matches when every listed property has the listed value; with no properties, every object of the type is listed. Click _Add_ to add a property, _Remove_ to remove the selected one, and _Up_ and _Down_ to move it. Values may contain Variables

### Output and errors

The output has one line for each matching object: its name and its full address, separated by a tab. To use an address in the Delete Exchange object or Modify Exchange object Task, remove the _Mail box URL_ part from it.

If the mailbox cannot be reached or the request fails, the error is written to the error output and the Task fails.