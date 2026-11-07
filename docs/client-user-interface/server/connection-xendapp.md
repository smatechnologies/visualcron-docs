---
sidebar_label: 'Connection - XendApp'
hide_title: 'true'
---

## Connection - XendApp

The XendApp Connection stores the address, sign-in and security settings that the [Messaging - XendApp](job-tasks/messaging-tasks/xendapp) Task uses to connect to XendApp.

XendApp is a platform for delivering instant messages to any device (phone/tablet). It is a free service which uses notification services to deliver a message. You can create an account on the [XendApp registration page](https://xendapp.com/Register.aspx).

:::warning

The XendApp Connection connects to the XendApp services over HTTP. The user name, the password and the messages are sent without encryption. Use this Connection only on a network that you trust.

:::
 
### Common settings

![XendApp Connection, Common settings tab with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/XendApp/XendApp.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

For a XendApp Connection, _Timeout_ and _Code page_ are not used. _Test_ runs on the Client computer, not on the Server, through the proxy set on the ***Proxy*** tab. It checks _Username_ and _Password_ with XendApp and shows whether they are correct and whether the account is approved.

### Main settings

![XendApp Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/XendApp/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Username_ is required.

- _Username_: the user name of your XendApp account
- _Password_: the password of your XendApp account
- _Create an account at xendapp.com_: opens the XendApp registration page in your browser

### Proxy

The ***Proxy*** tab is on the ***Connection settings*** tab. The XendApp Task on the Server, and _Test_ on the Client computer, both connect through the proxy set here. With any _Proxy type_ other than "No proxy", they use the proxy as an HTTP proxy.
