---
sidebar_label: 'Task Exchange - Delete Exchange Objects'
hide_title: 'true'
---

## Task Exchange - Delete Exchange Objects

The Delete Exchange objects Task deletes every appointment, contact or task in an Exchange mailbox that matches the filter properties.

![Delete Exchange objects tab, with the mailbox address, the Credential, the forms-based authentication option and the object type and filter property list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Exchange%20Tasks/Delete%20Exchange%20Objects.png)

:::warning

This Task connects to the mailbox with WebDAV and accepts any server certificate, so an address that starts with "https://" does not prove the identity of the server. With _Use Forms-based authentication_ checked, the user name and password of the Credential are posted to the server in a form; with an address that starts with "http://", anyone who can see the traffic can read them. Use an address that starts with "https://", on a network you trust.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete Exchange objects tab

- _Mail box URL_: the WebDAV address of the mailbox, in the form `https://<server>/exchange/<mailbox>`
- _Credentials_: the Credential that signs in to the mailbox. A Credential is required; without one the Task fails with a Credential-not-found error. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials)
- _Use Forms-based authentication_: signs in through the forms-based (Outlook Web Access) sign-in page. When cleared, Windows authentication is used
- **Exchange object type and filter properties**: the object type, "Appointment" (default), "Contact" or "Task", and the properties an object must match. An object matches when every listed property has the listed value. Click _Add_ to add a property, _Remove_ to remove the selected one, and _Up_ and _Down_ to move it. Values may contain Variables

:::warning

With no filter properties, every object of the selected type in the mailbox is deleted. Run the Get Exchange object(s) Task with the same filter first to see what would be deleted.

:::

### Output and errors

The output is the number of objects deleted. If the Task fails partway, the objects deleted before the failure stay deleted.

If the mailbox cannot be reached or the request fails, the error is written to the error output and the Task fails.