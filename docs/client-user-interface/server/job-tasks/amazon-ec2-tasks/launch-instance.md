---
sidebar_label: 'Task Amazon EC2 - Launch Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Launch Instance

The Amazon EC2 - Launch instance Task launches one or more new EC2 instances from an AMI for which you have permission. The Task issues the RunInstances call and reports the reservation result; it does not wait for the instances to reach the *running* state.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Launch%20Instance.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

All five drop-downs below are populated by querying the selected Connection. Each one has a *Refresh* icon — click it to load the available values for that field. Selecting a Connection is required before any field can be refreshed; the *Image Id*, *Instance type*, *Subnet Id* and *Availability Zone* lists are scoped to the region of the selected Connection. *Instance type* additionally depends on the selected *Image Id*, so refresh it after picking an AMI.
 
**Key pair name**

The name of the SSH key pair to associate with the new instance(s). Click the *Refresh* icon to populate the drop-down with key pairs from the selected Connection. Required.
 
**Image Id**

The ID of the AMI (Amazon Machine Image) to launch. Click the *Refresh* icon to populate the drop-down with images available on the selected Connection. Required.

**Instance type**

The size of the instance to launch (for example `t3.micro`, `m5.large`). Click the *Refresh* icon to populate the drop-down with instance types compatible with the selected *Image Id*. Required, and should be refreshed after changing *Image Id*.

**Subnet Id**

The ID of the VPC subnet to launch the instance into. Click the *Refresh* icon to populate the drop-down with subnets in the region of the selected Connection. Required.

**Availability Zone**

The Availability Zone in which to launch the instance(s). Click the *Refresh* icon to populate the drop-down with the zones in the region of the selected Connection. Required.

**Number of instances to launch**

The number of instances to launch from the selected AMI. Defaults to `1`.
 
