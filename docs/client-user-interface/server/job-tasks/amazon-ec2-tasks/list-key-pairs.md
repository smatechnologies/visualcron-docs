---
sidebar_label: 'Task Amazon EC2 - List Key Pairs'
hide_title: 'true'
---

## Task Amazon EC2 - List Key Pairs

The Amazon EC2 - List key pair(s) Task is intended to list EC2 key pairs on the selected Connection, optionally narrowed by a filter. The supporting AWS code wraps the AWS Tools for PowerShell `Get-EC2KeyPair` cmdlet, with the *Filter* field passed as the cmdlet's `-Filters` argument.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Key%20Pair.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Filter**

Optional filter expression in the same syntax accepted by `Get-EC2KeyPair -Filters`. Use a PowerShell hashtable with `Name` and `Values` entries; combine multiple hashtables in an array to apply more than one filter.

:::tip Example

```powershell
@{Name="key-name"; Values="websvr-keypair"}
```

:::

For the full list of available filter names (`fingerprint`, `key-name`, `tag:<key>`, etc.) see the AWS documentation for the `Get-EC2KeyPair` cmdlet.
