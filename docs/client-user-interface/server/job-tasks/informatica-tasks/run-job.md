---
sidebar_label: 'Task Informatica - Run Job'
hide_title: 'true'
---

## Task Informatica - Run Job

The Informatica - Run job Task starts a job in Informatica Cloud, using an Informatica Connection.

![Informatica - Run job tab, with the Connection, the job type, the Integration Service and the list of available jobs](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Informatica%20Tasks/Run%20Job.png)

:::warning

This Task uses an Informatica Connection; see [Connection - Informatica](../../connection-informatica). When it signs in, it sets the SSL and TLS versions for the whole Server process, including SSL 3 and TLS 1.0, and, unless another component has already set one, installs a certificate check that accepts any server certificate for HTTPS calls in the Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Process request tab

- _Informatica Service connection_: the Informatica Connection with the address and sign-in. Only Informatica Connections are listed
- _Job type_: the type of job to run: "DRS", "DSS", "Workflow", "AVS", "DMASK", "DQA", "MTT" or "PCS"
- _Integration Service_: the Informatica Integration Service. Click the refresh button to fill the list from the Connection
- _Available jobs_: the job to run. Click the refresh button to fill the list for the selected _Job type_; select the Connection and the job type first

### Output and errors

The Task starts the job and does not wait for it to finish. The output is "Job Run Successfully and job Id: " followed by the run ID that Informatica returns; check the result of the job in Informatica Cloud.

:::warning

If Informatica answers that the sign-in or the job request failed, the error is written only to the error output, and the Task reports success. To catch this, add an error condition on the error output on the ***On error*** tab; see [Task - On Error](../../task-on-error). If Informatica cannot be reached, the Task fails.

:::
