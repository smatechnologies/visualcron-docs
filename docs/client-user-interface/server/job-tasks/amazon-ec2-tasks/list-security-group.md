---
sidebar_label: 'Task Amazon EC2 - List Security Group'
hide_title: 'true'
---

## Task Amazon EC2 - List Security Group

The Amazon EC2 - List security group Task lists EC2 security groups on the selected Connection, optionally narrowed by a filter. The Task wraps the AWS Tools for PowerShell `Get-EC2SecurityGroup` cmdlet — the value entered in the *Filter* field is passed straight through as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Security%20Group.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2SecurityGroup -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter. Leave the field empty to return every security group on the Connection.

:::tip Example

```powershell
@{Name="vpc-id"; Values="vpc-1a2b3c4d"}
```

:::

For the full list of available filter names (`group-name`, `tag:<key>`, `vpc-id`, `ip-permission.protocol`, etc.) see the AWS documentation for the `Get-EC2SecurityGroup` cmdlet.

**Output**

For each matching security group, the Task writes a single pipe-delimited line to standard output containing the following columns, in order:

`Description | GroupId | GroupName | OwnerId | VpcId`
