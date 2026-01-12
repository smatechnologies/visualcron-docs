---
sidebar_label: 'Stop Job'
hide_title: 'true'
---

## Stop Job

When a Job is defined, right-click on the Job or Task in the Server/Group/Job/Task grid and select *Stop Job '`<Job name>`'* to stop a Job that is currently executing.

![](../../../../static/img/Client%20User%20Interface/Toolbar/Stop%20Job.png)
 
:::info Note

In case of such a forced stop, the Job receives the final result status "Failure".

If, at the same time, the executed or interrupted Tasks inside the Job did not set their own error exit code, then the exit code for the Job will be set to 77777.

:::