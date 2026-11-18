---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

Amazon Elastic Compute Cloud (EC2) is the part of Amazon Web Services (AWS) that rents out virtual computers, on which you run your own applications.

The Amazon EC2 Tasks manage EC2 instances, EBS snapshots and related resources. They use an Amazon [Connection](../../connection-amazon), the same Connection type that the Amazon S3 cloud transfer Tasks use.

:::note

The EC2 Tasks sign in with the _Access Key ID_ and _Secret Access Key_ of the Connection, connect to its _Region_, and use the settings on its ***Proxy*** tab. The other settings of the Connection, such as _Address_ and _Authentication type_, do not apply to them. Use "Password" authentication for a Connection that EC2 Tasks use, so that the Connection shows the _Access Key ID_ and _Secret Access Key_ fields.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

**Available EC2 Tasks**

Instance lifecycle:

* [Launch instance](launch-instance)
* [Start instance](start-instance)
* [Stop instance](stop-instance)
* [Reboot instance](reboot-instance)
* [Terminate instance](terminate-instance)

Snapshots:

* [Create snapshot](create-snapshot)
* [Delete snapshot](delete-snapshot)

List Tasks:

* [List instance(s)](list-instance)
* [List security group(s)](list-security-group)
* [List snapshot(s)](list-snapshot)
* [List volume(s)](list-volume)
* [List address(es)](list-address)
* [List key pair(s)](list-key-pairs)
