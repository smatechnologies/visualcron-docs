---
sidebar_label: 'Task Messaging - XendApp'
hide_title: 'true'
---

## Task Messaging - XendApp

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/XendApp.png)

The Messaging - XendApp Task send messages of multiple content types directly to your phone or other device. Combining the best features of SMS and email. See [http://xendapp.com](http://xendapp.com) for more information.
 
XendApp is a platform for delivering instant messages to any device (phone/tablet). It is a free service which uses notification services to deliver a message. Registration can be done [here](https://xendapp.com).The XendApp Task uses the [XendApp Connection](../../../server/connection-xendapp).
 
 
**Connection**

The instant messaging sender is centrally stored in [Connections](../../../server/global-connections). You need to create a Connection representing the user you want to send the message from.
 
**Provider**

The XendApp provider to send the message through. Click the _Refresh_ button to populate the list from the selected connection. Selecting a provider automatically loads its available channels.
 
**Channel**

The channel belonging to the selected provider. Populated automatically when a provider is selected.
 
**Subject**

The subject line of the message. This field is required and has a maximum length of 100 characters.
 
**Content type**

The format of the message body. Available options:

* _Plain text_ - sends the body as plain text
* _HTML_ - sends the body as HTML-formatted content
 
**Body**

The body text of the message.
 
**Encrypt body**

When checked, the message body is encrypted before sending.

**Expire message in**

The number of days after which the message expires. Minimum is 1, maximum is 90, default is 30.
