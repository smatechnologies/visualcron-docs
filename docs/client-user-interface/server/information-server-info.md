---
sidebar_label: 'Information - Server Info'
hide_title: 'true'
---

## Information - Server Info

The _Server info_ window shows details about the computer the Server runs on, the Server's license, the VisualCron Server service, the Server's time settings and how long your Client took to connect. Use it when you troubleshoot a Server or contact support.

To open it, click the main menu _Server_ -> _Information_ -> _Server info_.
 
### Machine tab

_Server_ -> _Information_ -> _Server info_ -> **_Machine_**

![Server info window, Machine tab, with the Connection, Operative system and Processor groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Server%20Info/Machine.png)

- _Connection_: the computer _Name_, the _Domain_, and the _Address_ the Client connects to, with its IP address
- _Operative system_: _Name_, _Service pack_ and _Architecture_
- _Processor_: _Name_, _Speed_ in MHz, _Processors_ and _Logical processors_

### License tab

_Server_ -> _Information_ -> _Server info_ -> **_License_**

![Server info window, License tab, with the Activated, Is unlimited, Edition, Activation code, Subscription type, Expires, Server Id and product fields; the license values are blurred](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Server%20Info/License.png)

- _Activated_: whether the Server is activated
- _Server Id_: the ID of this Server
- _Purchase license_: a link to buy a license, shown only when the Server is not activated

When the Server is activated, the tab also shows _Edition_ (the name of the edition), _Is unlimited_, _Activation code_, _Subscription type_, _Expires_, _Product id_, _Product name_, _Renewal product id_ and _Renewal product name_. _Activation code_ is shown only if you have the "License" permission with "Read"; otherwise the field reads "Hidden for permission reasons".

To activate or deactivate the license, see [Information - License](information-license).

### Service tab

_Server_ -> _Information_ -> _Server info_ -> **_Service_**

![Server info window, Service tab, with the Version group showing Version and Protocol version, and the VisualCron Service group showing Running as and Listening port](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Server%20Info/Service.png)

- _Version_: _Version_ (the Server version) and _Protocol version_
- _VisualCron Service_: _Running as_ (the account the service runs as) and _Listening port_ (the port Clients connect to)

### Environment tab

_Server_ -> _Information_ -> _Server info_ -> **_Environment_**

![Server info window, Environment tab, with the Time info group showing Time zone, UTC offset and UTC diff](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Server%20Info/Environment.png)

_Time info_ shows the Server's _Time zone_ and _UTC offset_, and the _UTC diff_: the difference between the Server's UTC offset and that of the computer running your Client.

### Connection tab

_Server_ -> _Information_ -> _Server info_ -> **_Connection_**

![Server info window, Connection tab, showing Main form load, Main form shown, Sync time and Total connection time in seconds](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Server%20Info/Connection.png)

Timings, in seconds, for your Client's connection to this Server. _Main form load_ and _Main form shown_ measure your Client's own start-up. _Sync time_ and _Total connection time_ measure the synchronization with the Server and the whole connection.

### Buttons and links

- _Refresh_: asks the Server to collect the information again
- _Clear memory_: asks the Server to release memory; this also empties the Server's in-memory list of recent log events and its cached Task output, and logs and output stored in the log database are not affected; no permission is needed to use it
- _Visit our forum for additional server info_: opens the VisualCron forum in your browser

The status bar shows when the information was last updated.
