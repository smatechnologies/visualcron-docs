---
sidebar_label: 'Task Amazon EC2 - List Address'
hide_title: 'true'
---

## Task Amazon EC2 - List Address

The Amazon EC2 - List address(es) Task lists Elastic IP addresses on the selected Connection, optionally narrowed by a filter. The Task wraps the AWS Tools for PowerShell `Get-EC2Address` cmdlet — the value entered in the *Filter* field is passed straight through as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Address(es).png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2Address -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter. Leave the field empty to return every Elastic IP address on the Connection.

:::tip Example

```powershell
@{Name="domain"; Values="vpc"}
```

:::

For the full list of available filter names (`allocation-id`, `association-id`, `instance-id`, `public-ip`, `tag:<key>`, etc.) see the AWS documentation for the `Get-EC2Address` cmdlet.

**Output**

The Task writes one line to standard output per matched Elastic IP address. Per-address fields (allocation ID, public IP, instance ID, etc.) are not currently parsed into the output line — the line itself is empty, so the standard output is mainly useful as a count of matching addresses. The Task succeeds when the underlying `Get-EC2Address` call succeeds.
