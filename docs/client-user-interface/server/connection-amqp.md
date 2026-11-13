---
sidebar_label: 'Connection - AMQP'
hide_title: 'true'
---

## Connection - AMQP

The AMQP Connection stores the address, sign-in and security settings that the [AMQP - Send message](job-tasks/messaging-tasks/amqp-send-message) Task and the [AMQP Trigger](event-trigger-amqp) use to connect to a message broker over Advanced Message Queuing Protocol (AMQP) 1.0. The supported broker types are RabbitMQ and Azure Service Bus.

### Common settings

![AMQP Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AMQP/AMQP.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings). The AMQP Connection has no _Test_ button and no ***Proxy*** tab.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

***Main settings*** is the only tab under ***Connection settings***.

![AMQP Connection, Main settings tab with the Server, Credential and Additional parameter groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AMQP/Settings.png)

_Address_

The host name or IP address of the broker. For Azure Service Bus, the host name of the namespace, for example `<namespace>.servicebus.windows.net`. Required.

_Port_

The port of the broker: usually "5672" for AMQP and "5671" for AMQPS. A new Connection starts at "5672". When you select "Azure Service Bus" in _Broker type_, a port of "0" or "5672" changes to "5671". When you select "RabbitMQ", a port of "0", "5671" or "5672" changes to "5671" or "5672" to match _Schema_.

_Broker type_

- "RabbitMQ": a RabbitMQ broker; on a new Connection, _Schema_ is "AMQP" and _Path_ is "/"
- "Azure Service Bus": an Azure Service Bus namespace; an empty _Schema_ or "AMQP" changes to "AMQPS"

_Authentication type_

- "Password": a user name and password, sent to the broker when the connection opens
- "Certificate": a client certificate; the _Certificate_ field is shown; use it with _Schema_ "AMQPS"

_Username_

For RabbitMQ, the user name on the broker. For Azure Service Bus, the name of the shared access policy. With "Certificate" authentication on RabbitMQ, the user name for the Management HTTP API, which the queue list needs.

_Password_

For RabbitMQ, the password on the broker. For Azure Service Bus, the key of the shared access policy. The Server logs on with the policy name and key, and uses them to build the connection string for the queue list.

_Certificate_

Shown with "Certificate" authentication. The client certificate, from [Certificates](global-certificates). Required with "Certificate". With "Certificate" authentication, the AMQP connection allows SSL 3 and TLS 1.0 to TLS 1.3.

_Schema_

"AMQP" for an unencrypted connection, or "AMQPS" for an encrypted one. Azure Service Bus needs "AMQPS". If _Schema_ holds any other value, the Server uses "AMQPS" when _Port_ is "5671", and "AMQP" otherwise.

:::warning

A new Connection starts with _Schema_ "AMQP" on port "5672". With _Schema_ "AMQP", the connection to the broker is not encrypted, and _Username_ and _Password_ are sent without encryption. To list RabbitMQ queues, the Server also sends _Username_ and _Password_ to the address in _Connection string_, which the editor fills in with an "http" address unless _Port_ is "5671". Where the broker supports it, use "AMQPS" on port "5671" and an "https" address in _Connection string_.

:::

_Disable Server Certificate Validation_

In the _Additional parameter_ group. When selected, the Server does not check the broker's certificate, on the AMQP connection and when it lists RabbitMQ queues.

:::warning

_Disable Server Certificate Validation_ is selected by default on a new Connection. While it is selected, the Server accepts any broker certificate. Clear it so that the Server checks the certificate of an AMQPS broker. With "Certificate" authentication, the Server accepts any broker certificate on the AMQP connection, whether the box is selected or not.

The Server applies the value of this box to the whole Server process each time an AMQP Task or Trigger connects. While any AMQP Connection with the box selected is in use, other AMQP connections from the Server can also skip the certificate check. To have broker certificates checked, clear the box on every AMQP Connection.

:::

_Path_

The virtual host path for RabbitMQ. The default is "/". For Azure Service Bus this field is not used.

_Connection string_

Used to list queues, for example when you pick a queue in a Task or Trigger.

- RabbitMQ: the base URL of the Management HTTP API, for example `http://<broker host>:15672/`; the editor fills it in from _Address_ and _Port_, with "https" on port "15671" when _Port_ is "5671", otherwise "http" on port "15672"; enter the base URL only, because VisualCron adds `api/queues` itself
- Azure Service Bus: a connection string of the form `Endpoint=sb://<namespace host>/;SharedAccessKeyName=<policy name>;SharedAccessKey=<policy key>`; when the field is empty, VisualCron builds it from _Address_, _Username_ and _Password_

Each time the Server lists RabbitMQ queues, it sets the SSL and TLS versions for the whole Server process to SSL 3 and TLS 1.0 to TLS 1.3.

### RabbitMQ address format

RabbitMQ 4.x enforces the AMQP 1.0 address syntax, which needs a typed prefix in the queue or exchange address of Send message Tasks and AMQP Triggers. RabbitMQ 3.x does not need the prefix.

If you see an error such as `Attach refused: {amqp_address_v1_not_permitted, ...}`, or the AMQP Trigger deactivates right after it starts, check that the address matches one of these formats:

| Intent | Address format |
|---|---|
| Send to a queue (through the default exchange) | `/queues/<queue name>` |
| Publish to an exchange with a routing key | `/exchanges/<exchange name>/<routing key>` |
| Publish to an exchange without a routing key | `/exchanges/<exchange name>` |
| Receive from a queue (Trigger) | `/queues/<queue name>` |

:::note

Tasks and Triggers set up for RabbitMQ 3.x with plain queue names, for example "my-queue", need the prefixed format after an upgrade to RabbitMQ 4.x.

:::
