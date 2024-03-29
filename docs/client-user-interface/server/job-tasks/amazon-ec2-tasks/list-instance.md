---
sidebar_label: 'Task Amazon EC2 - List Instance'
hide_title: 'true'
---

## Task Amazon EC2 - List Instance

The Amazon EC2 - List instances lists existing instances according to the specified filter.

![](../../../../../static/img/taskamazonec2listinstances.png)

**Connection**

To use Amazon EC2 Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.
 
**Filter**

Filter for instances. 

:::tip Example 

`{"Name": "instance-type", "Values": ["t2.micro", "m1.medium"]}`

:::