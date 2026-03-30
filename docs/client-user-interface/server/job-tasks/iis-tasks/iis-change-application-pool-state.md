---
sidebar_label: 'Task IIS - Change Application Pool State'
hide_title: 'true'
---

## Task IIS - Change Application Pool State

With the Task IIS - Change Application Pool State you can start, stop, or recycle an existing application pool on a local or remote IIS server. This task is useful for automating maintenance operations, deploying updates that require a pool restart, or managing resource usage on the server.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Change%20state%20of%20the%20app%20pool.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Application pool name**

The name of the existing application pool whose state you want to change. Click the *Refresh* button to populate the dropdown with available application pools from the connected server. This field is required.

**Operation**

The state change operation to perform on the application pool. Options:

- *Nothing* — No operation is performed. Use this as a placeholder or for testing.
- *Start* — Starts the application pool if it is currently stopped.
- *Stop* — Stops the application pool and terminates any active worker processes serving that pool.
- *Recycle* — Gracefully recycles the application pool worker process. The existing worker process continues serving in-flight requests while a new worker process starts up, minimizing downtime.

:::info Note
Stopping or recycling an application pool will affect all web sites and applications assigned to that pool. Connections being served by the pool at the time of the operation may be interrupted.
:::
