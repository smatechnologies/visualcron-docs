---
sidebar_label: 'Task Amazon EC2 - List Instance'
hide_title: 'true'
---

## Task Amazon EC2 - List Instance

The Amazon EC2 - List instances Task lists existing EC2 instances on the selected Connection, optionally narrowed by a filter. The Task wraps the AWS Tools for PowerShell `Get-EC2Instance` cmdlet — the value entered in the *Filter* field is passed straight through as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Instance(s).png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2Instance -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter. Leave the field empty to return every instance on the Connection.

:::tip Example

```powershell
@{Name="instance-type"; Values=("t2.micro","m1.medium")}
```

:::

For the full list of available filter names (`instance-state-name`, `tag:<key>`, `vpc-id`, etc.) see the AWS documentation for the `Get-EC2Instance` cmdlet.

**Output**

For each matching instance, the Task writes a single pipe-delimited line to standard output containing the following columns, in order:

`Architecture | Hypervisor | ImageId | InstanceId | KernelId | KeyName | LaunchTime | PrivateDnsName | PrivateIpAddress | RootDeviceName | RootDeviceType | SubnetId | StateTransitionReason | VirtualizationType | VpcId`
