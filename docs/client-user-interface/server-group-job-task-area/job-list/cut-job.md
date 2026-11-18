---
sidebar_label: 'Cut Job'
hide_title: 'true'
---

## Cut Job

The `Cut Job '<Job name>'` item marks a Job to be moved to another Server with [Paste Job](paste-job).

:::warning

When you paste a cut Job onto another Server, the Job is deleted from the source Server even if you click ***Cancel*** in the paste window, if the Job could not be added to the target Server, or if you do not have the Add permission there. A cut Task is deleted the same way, on the same Server or on another. To move a Job safely, use [Copy Job](copy-job), paste it, check the copy on the target Server, and then [delete](delete-job) the original.

:::

1. Right-click the Job in the Server/Group/Job/Task grid.
2. Click `Cut Job '<Job name>'`.
3. Right-click a Job in the target group, or the Server row of the target Server.
4. Click `Paste Job '<Job name>'`.

You can also press Ctrl+X to cut the selected Job and Ctrl+V to paste it. The warning above applies in the same way.

What the paste does depends on the target:

- **Another Server**: the Job is added to the target Server and then deleted from the source Server
- **The same Server**: the Job is not moved. The Client asks whether to clone the Job. Click ***Ok*** to add a copy with the same name to the group you pasted into. The original stays

![Job right-click menu with the Cut Job item highlighted](../../../../static/img/Client%20User%20Interface/Toolbar/Cut%20Job.png)
