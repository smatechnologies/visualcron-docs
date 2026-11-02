---
sidebar_label: 'Task Messaging - XendApp'
hide_title: 'true'
---

## Task Messaging - XendApp

The Messaging - XendApp Task sends messages of multiple content types directly to a phone or other device, combining the best features of SMS and email. See [http://xendapp.com](http://xendapp.com) for more information.

XendApp is a free platform for delivering instant messages to any device (phone or tablet) using notification services. Registration can be done [here](https://xendapp.com). The Task uses the [XendApp Connection](../../../server/connection-xendapp).

![XendApp tab with the Connection, Provider and Channel, and Message groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/XendApp.png)

:::warning

This Task uses a XendApp Connection; see [Connection - XendApp](../../connection-xendapp). The Connection calls the XendApp services over HTTP, without transport encryption: the user name and password of the Connection and _Subject_ are sent in clear text. _Encrypt body_ encrypts the body only.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### XendApp tab

#### Connection

- _Connection_: the XendApp Connection of the account that sends the messages

  The Task uses the proxy set on the Connection.

#### Provider and Channel

- _Provider_: the XendApp provider to send through. Required
- _Channel_: the channel of the selected provider. Required

  The list is filled when you select a provider.

- _Refresh_: lists the providers of the Connection's account

#### Message

- _Subject_: the subject of the message. Required, up to 100 characters
- _Expire message in_: the number of day(s) after which the message expires, from "1" to "90"; "30" by default
- _Content type_: "Plain text" or "HTML"
- _Body_: the text of the message
- _Encrypt body_: when selected, the message body is encrypted before sending

Variables are resolved in _Subject_ and _Body_.

### Output and errors

When the message is sent, the output of the Task shows its message ID.

:::warning

If XendApp rejects the message, the error is written to standard error, and the Task reports success.

:::
