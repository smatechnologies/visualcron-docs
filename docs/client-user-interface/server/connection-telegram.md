---
sidebar_label: 'Connection - Telegram'
hide_title: 'true'
---

## Connection - Telegram

The Telegram Connection stores the sign-in settings that the [Telegram - User Send message](job-tasks/messaging-tasks/telegram-user-send-message) Task uses to connect to Telegram.

### Set up the Telegram Connection

The Connection needs your own Telegram app and the phone number of the Telegram account. To set it up, complete the following steps:

1. On ***Main settings***, click _Create an app in my.telegram.org_. The Telegram app registration page opens.
2. Create a Telegram app.
3. Enter the app_id of the app in _App app_id_.
4. Enter the api_hash of the app in _App api_hash_.
5. On ***Common settings***, enter the phone number of the Telegram account, with the country code, in _Number_.
6. Click _Test_. VisualCron requests a login code, and the code is sent to the account.
7. On ***Main settings***, enter the login code in _Code_.
8. Click _OK_.

The Connection is saved with the login code and is ready for the Task.
 
### Common settings

![Telegram Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telegram/Telegram.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy). On a Telegram Connection, the first field is _Number_ instead of _Name_.

_Number_

The phone number of the Telegram account that sends the messages, with the country code. VisualCron logs on to Telegram with this number.

_Test_

Requests a login code for the account in _Number_. When the request succeeds, a message asks you to enter the code in _Code_ and save the Connection.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

The ***Connection settings*** tab holds two tabs: ***Main settings*** and ***Proxy***.

![Telegram Connection, Main settings tab with the Credentials group](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telegram/Settings.png)

The screenshot shows a _Use VisualCron registered app_ box from an earlier version. The current Client does not have it, and the Connection always uses your own Telegram app.

_App app_id_

The app_id of your Telegram app.

_App api_hash_

The api_hash of your Telegram app.

_Code_

The login code that _Test_ requests. Enter it, then click _OK_.

_Create an app in my.telegram.org_

Opens the Telegram app registration page in the web browser.

### Proxy

The Telegram - User Send message Task uses the settings on this tab.
