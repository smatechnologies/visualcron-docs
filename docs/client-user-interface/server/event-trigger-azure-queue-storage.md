---
sidebar_label: 'Event Trigger - Azure Queue Storage'
hide_title: 'true'
---

## Event Trigger - Azure Queue Storage

The Azure Queue Storage Trigger is using the [Microsoft Azure Connection](../server/connection-microsoft-azure.md).

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Azure%20Queue%20Storage.png)

**Connection**

Select the Microsoft Azure Connection to use. The connection must be configured with the appropriate Azure credentials before use.

**Name**

Name of the queue. Click the refresh button to populate the list with available queues from the selected Connection.

**On error reconnect interval (seconds)**

The number of seconds to wait before attempting to reconnect after a connection error.

**On error reconnect attempts**

The number of times VisualCron will attempt to reconnect after a connection error before giving up.
