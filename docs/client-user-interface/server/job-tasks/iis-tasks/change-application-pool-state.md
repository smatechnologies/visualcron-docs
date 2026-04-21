---
sidebar_label: 'Task IIS - Change Application Pool State'
hide_title: 'true'
---

## Task IIS - Change Application Pool State

The IIS - Change Application Pool State Task starts, stops, or recycles an existing application pool in Internet Information Services (IIS). Recycling an application pool restarts the worker process, which can resolve memory leaks or hung processes without a full stop and start.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Change%20state%20of%20the%20app%20pool.png)

**Connection**

To use IIS Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Application pool parameters**

**Application pool name**

The name of the application pool to manage. Click the *Refresh* icon to populate the drop-down list with available application pools.

**Operation**

The operation to perform on the application pool. Available options are:
- *Start* – Starts the application pool
- *Stop* – Stops the application pool and terminates its worker process
- *Recycle* – Gracefully restarts the application pool worker process without dropping active connections
