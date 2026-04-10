---
sidebar_label: 'Task IIS - Is Application Pool Exists'
hide_title: 'true'
---

## Task IIS - Is Application Pool Exists

With the Task IIS - Is Application Pool Exists you can check whether a named application pool exists on a local or remote IIS server. The task writes the result to the task output, which can be used in downstream job conditions or flow control tasks.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Is%20Application%20pool%20exists.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Application pool name**

The name of the application pool to check for. This field is required.

### Task output

The task writes one of the following values to its output:

- `Exists` — An application pool with the specified name was found on the target server.
- `Not exists` — No application pool with the specified name was found on the target server.

The output value can be read by subsequent tasks using the VisualCron Variables system (e.g., `{Task output}`), enabling conditional branching based on whether the pool exists.

:::info Note
The check is performed against the live IIS configuration on the connected server at the time the task runs. The result reflects the current state and is not cached between job executions.
:::
