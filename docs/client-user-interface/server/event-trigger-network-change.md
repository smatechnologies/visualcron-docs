---
sidebar_label: 'Event Trigger - Network Change'
hide_title: 'true'
---

## Event Trigger - Network Change

The Network change Trigger is able to monitor changes on a network connection.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Network%20Change.png)

**Network adapters**

A multi-select checkbox list of the network adapters available on the VisualCron Server. Check one or more adapters to monitor. At least one adapter must remain selected.
 
**Event type**

A multi-select checkbox list of network change events. Check one or more of the following events to listen for. At least one event type must remain selected:

* **Disconnected** — fires whenever the network adapter goes offline
* **Connected** — fires whenever the network adapter goes online
* **Media disconnected** — fires whenever a network media is disconnected
* **IP address changed** — fires whenever the IP address changes
