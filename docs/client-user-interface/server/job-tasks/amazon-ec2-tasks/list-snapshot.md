---
sidebar_label: 'Task Amazon EC2 - List Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - List Snapshot

The Amazon EC2 - List snapshots Task lists EBS snapshots visible to the selected Connection, optionally narrowed by a filter. The set of visible snapshots includes public snapshots (available to any AWS account), private snapshots owned by the account on the Connection, and private snapshots owned by another account that have granted explicit create-volume permissions to this account.

The Task wraps the AWS Tools for PowerShell `Get-EC2Snapshot` cmdlet — the value entered in the *Filter* field is passed straight through as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Snapshot(s).png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2Snapshot -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter.

> Leaving *Filter* empty returns **every** visible snapshot, which includes the very large set of public snapshots in the region. To list only the snapshots owned by your account, use the `owner-alias` or `owner-id` filter as shown below.

:::tip Example

```powershell
@{Name="owner-alias"; Values="self"}
```

:::

For the full list of available filter names (`status`, `volume-id`, `start-time`, `tag:<key>`, etc.) see the AWS documentation for the `Get-EC2Snapshot` cmdlet.

**Output**

For each matching snapshot, the Task writes a single pipe-delimited line to standard output containing the following columns, in order:

`Description | OwnerId | Progress | SnapshotId | StartTime | State | VolumeId | VolumeSize`

`StartTime` is emitted as a short date.
