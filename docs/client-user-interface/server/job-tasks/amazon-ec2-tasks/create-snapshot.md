---
sidebar_label: 'Task Amazon EC2 - Create Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - Create Snapshot

The Amazon EC2 - Create snapshot Task creates a point-in-time snapshot of an Amazon EBS volume. The Task wraps the AWS Tools for PowerShell `New-EC2Snapshot` cmdlet. Snapshots are stored on AWS-managed S3 storage and are incremental — only blocks that changed since the previous snapshot of the volume are written. The Task issues the snapshot request and reports the resulting snapshot ID; it does not wait for the snapshot to finish copying (which can take minutes to hours depending on volume size).

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Create%20Snapshot.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Volume ID**

The ID of the EBS volume to snapshot. Click the *Refresh* icon to query the selected Connection and populate the drop-down with volumes available in that account/region. Variables can be entered manually if the volume ID is determined at run time. Required.

**Description**

Free-text description stored on the resulting snapshot in AWS. Helpful for identifying the snapshot later (for example a hostname, purpose or timestamp); accepts Variables. Optional.

**Output**

On success, the Task writes the new snapshot's ID to standard output. This makes it easy to feed into a later [Delete Snapshot](delete-snapshot) Task or any other step that needs the new ID.
