---
sidebar_label: 'Task Amazon EC2 - List Volume'
hide_title: 'true'
---

## Task Amazon EC2 - List Volume

The Amazon EC2 - List volume(s) Task lists EBS volumes on the selected Connection, optionally narrowed by a filter. The Task wraps the AWS Tools for PowerShell `Get-EC2Volume` cmdlet — the value entered in the *Filter* field is passed straight through as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Volume(s).png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2Volume -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter. Leave the field empty to return every volume on the Connection.

:::tip Example

```powershell
@{Name="status"; Values="available"}
```

:::

For the full list of available filter names (`attachment.instance-id`, `availability-zone`, `volume-type`, `tag:<key>`, etc.) see the AWS documentation for the `Get-EC2Volume` cmdlet.

**Volume IDs**

A space-separated list of volume IDs to restrict the listing to. The field is exposed in the UI but is **not currently sent to AWS** by the Task — the underlying `-VolumeIds` parameter is not wired up in the current build, so any value entered here is ignored at run time. Use the *Filter* field with `volume-id` for now if you need to limit the listing to specific volumes.

**Output**

For each matching volume, the Task writes a single pipe-delimited line to standard output containing the following columns, in order:

`AvailabilityZone | CreateTime | Iops | Size | SnapshotId | State | VolumeId | VolumeType`
