---
sidebar_label: 'Stop Job'
hide_title: 'true'
---

## Stop Job

The `Stop Job '<Job name>'` item stops a Job that is running.

1. Right-click the running Job in the Server/Group/Job/Task grid.
2. Click `Stop Job '<Job name>'`.

On a Task row, the item is `Stop Task '<Task name>'` and stops that Task. Stopping requires the Delete permission for processes.

![Job right-click menu with the Stop Job item highlighted](../../../../static/img/Client%20User%20Interface/Toolbar/Stop%20Job.png)

:::note

A stopped Job gets the result "Failure".

If none of the Tasks that ran or were stopped set their own error exit code, the exit code of the Job is set to 77777.

:::
