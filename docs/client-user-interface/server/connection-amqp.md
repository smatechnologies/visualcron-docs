---
sidebar_label: 'Connection - AMQP'
hide_title: 'true'
---

## Connection - AMQP

The Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for message-oriented middleware. It provides message orientation, queuing, routing (including point-to-point and publish-and-subscribe), reliability, and security. VisualCron supports AMQP version 1.0 or later.

The AMQP Connection stores connect and authentication properties for AMQP message brokers.

The AMQP Connection is used in:

* [AMQP - Send message Task](../../client-user-interface/server/job-tasks/messaging-tasks/amqp-send-message)
* [AMQP - Trigger](../../client-user-interface/server/event-trigger-amqp)
 
Currently, the following broker types are supported:

* RabbitMQ
* Azure Service Bus

**Manage Connections > Add > AMQP > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AMQP/AMQP.png)

**Name**

The name of the Connection to uniquely identify it.

**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Code page**

Code page being used.

**Manage Connections > Add > AMQP > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AMQP/Settings.png)

**Address**

The host name or IP address of the AMQP broker.

**Port**

The port of the AMQP broker. Default port is 5672 for AMQP and 5671 for AMQPS. When Azure Service Bus is selected as the broker type, the port is automatically set to 5671.

**Broker Type**

The message broker to connect to. Available options:

* _RabbitMQ_ - connects to a RabbitMQ broker. Default port: 5672, default schema: AMQP.
* _Azure Service Bus_ - connects to an Azure Service Bus namespace. Default port: 5671, schema is automatically set to AMQPS.

**Authentication type**

The authentication method to use. Available options:

* _Password_ - authenticate using a username and password.
* _Certificate_ - authenticate using a certificate; a certificate selector is shown. A username and password may still be required to access the Management HTTP API when listing queues.
 
**Username**

The user name for the AMQP broker.
 
**Password**

The password for the AMQP broker.

**Certificate** _(Certificate authentication only)_

Select the certificate to use for authentication.
 
**Schema**

The connection schema. Use `AMQP` for unencrypted connections (port 5672) or `AMQPS` for encrypted connections (port 5671). Azure Service Bus requires AMQPS.
 
**Path**

The virtual host path for RabbitMQ connections. The default value is `/`. For Azure Service Bus this field is not used.
 
**Connection string**

Used for administrative purposes such as retrieving a list of queues.

* For RabbitMQ: the URL of the RabbitMQ Management HTTP API, for example `http://localhost:15672/api/queues`.
* For Azure Service Bus: the connection string in the format `Endpoint=sb://xxx.servicebus.windows.net/;SharedAccessKeyName=yyy;SharedAccessKey=zzz`. This is automatically constructed from the Address, Username, and Password fields.

**Disable Server Certificate Validation**

When checked, VisualCron skips validation of the server's SSL/TLS certificate. Use this only when connecting to a broker with a self-signed or untrusted certificate.
