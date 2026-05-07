---
sidebar_label: 'Task Amazon EC2 - Delete Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - Delete Snapshot

The Amazon EC2 - Delete snapshot Task deletes a single EBS snapshot owned by the account on the selected Connection. The Task wraps the AWS Tools for PowerShell `Remove-EC2Snapshot -Force` cmdlet, so the deletion is unconditional — there is no per-Task confirmation prompt.

:::tip Note 

Because EBS snapshots are stored incrementally, deleting a snapshot does not always free space proportional to the snapshot's size: only blocks that are not referenced by any other snapshot are actually removed. Subsequent snapshots of the same volume remain valid and complete.

:::

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Delete%20Snapshot.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Snapshot**

The ID of the snapshot to delete. Click the *Refresh* icon to query the selected Connection and populate the drop-down with snapshots from that account/region. Variables can be entered manually if the snapshot ID is determined at run time (for example, the snapshot ID returned by a preceding [Create Snapshot](create-snapshot) Task). Only one snapshot can be deleted per Task — to delete several, chain multiple Delete Snapshot Tasks.

**Output**

On success, the Task writes the deleted snapshot ID to standard output.
