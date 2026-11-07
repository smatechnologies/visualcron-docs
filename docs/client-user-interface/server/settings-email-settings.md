---
sidebar_label: 'Settings - Email Settings'
hide_title: 'true'
---

## Settings - Email Settings

The **_Email settings_** tab holds the default sender details that the Email Task uses. The SMTP server, port and logon are not set here: they belong to the SMTP Connection that the Task uses (see [Connection - SMTP](connection-smtp)). This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)).

_Server_ -> _Main settings_ -> _Settings_ -> **_Email settings_** tab

![The Email settings tab with the To email, From email and From name fields in the Default settings box](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Email%20Settings.png)

- _To email_: a default email address stored with the Server settings. If _From email_ is empty when the VisualCron service starts, the Server copies this address into _From email_. You can enter several addresses, separated by a semicolon and no space, for example "ops@example.com;admin@example.com"
- _From email_: the default sender address. Enter a single address. When you open an Email Task whose _From email_ or reply-to address is empty, the Task fills them with this address. The test window of an SMTP Connection also uses it as the From address when the Connection has no user name
- _From name_: the default sender name. When you open an Email Task whose _From name_ is empty, the Task fills it with this name. If you leave this field empty, the Server fills in the Server name when you click _Apply settings_

When you click _Apply settings_, VisualCron checks the addresses and shows "Your email does not seem to be valid!" if one is not valid.

:::note

If _From email_ is empty and _To email_ holds several addresses, the copy at service start puts all of them into _From email_, and that is not a valid sender address. Keep _From email_ filled in with one address.

:::