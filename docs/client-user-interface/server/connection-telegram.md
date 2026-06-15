---
sidebar_label: 'Connection - Telegram'
hide_title: 'true'
---

## Connection - Telegram

The Telegram Connection uses the free, cloud-based instant messaging service Telegram. Telegram client apps exist for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type. Telegram also provides optional end-to-end encrypted messaging.
 
The Telegram Connection is used in the following Task:

* [Telegram - User Send message](../../client-user-interface/server/job-tasks/messaging-tasks/telegram-user-send-message)
 
### Setting up a Telegram application

To use the Telegram Connection you need your own Telegram app. Create one [here](https://my.telegram.org/auth?to=apps) and then enter the *App app_id* and *App api_hash* values from the app in the *Connection settings > Main settings* tab.
 
When you authenticate the Connection, a login code is requested and sent to you. Enter that code in the *Code* field and save the Connection.
 
**Manage Connections > Add > Telegram > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telegram/Telegram.png)

**Name**

A descriptive name for the connection to distinguish it from other connections.

**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Code page**

Code page being used.

The **Connection settings** tab is divided into two sub-tabs: **Main settings** and **Proxy**.

**Manage Connections > Add > Telegram > Connection settings > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Telegram/Settings.png)

The **Credentials** group contains the following fields:
 
**App app_id**

Copy this value from the settings of your app online.
 
**App api_hash**

Copy this value from the settings of your app online.
 
**Code**

The login code that is sent to you when you authenticate the Connection. Enter it here and save the Connection.

**Create an app in my.telegram.org**

A link that opens the Telegram app registration page where you can create your own Telegram app to obtain the App app_id and App api_hash values.

**Manage Connections > Add > Telegram > Connection settings > Proxy** tab

**Proxy type**

Select the proxy type to be used.

**Address**

The host name or IP address of the proxy server.

**Port**

The port of the proxy server.

**Use credentials**

The credentials that are associated with the account.

**Domain**

The domain of the proxy server.

**Username**

The user name to access the proxy server.

**Password**

The password to access the proxy server.
