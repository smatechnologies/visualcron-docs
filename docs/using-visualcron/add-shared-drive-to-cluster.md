---
sidebar_label: 'Add Shared Drive to Cluster'
hide_title: 'true'
---

## Add the VisualCron disk to the cluster

This is Part 2, step 3 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you add the VisualCron disk to the cluster, before VisualCron is installed, so that the cluster controls which node has the disk online.

:::warning

VisualCron must not run on two nodes at once. After this step, only the node that owns the VisualCron disk can use it.

:::

To add the disk, complete the following steps:

1. Click *Start* -> *Windows Administrative Tools* -> *Failover Cluster Manager*.
2. In the tree, expand the cluster and select *Storage* -> *Disks*.
3. Click *Add Disk*. The *Add Disks to a Cluster* window opens.
4. Select the VisualCron disk.
5. Click *OK*. The disk is added to the cluster as *Available Storage*, ready for the VisualCron role in [Add the Generic Service role](add-generic-service).

In the *Assigned To* column, the new disk shows *Available Storage*. The quorum disk from [Part 1, step 3](create-iscsi-network-drive) shows as the disk witness. Do not use the disk witness for VisualCron.

In the *Owner Node* column, note which node has the VisualCron disk. In the next step you install VisualCron on that node first.

### Next step

[Install VisualCron on both nodes in the same shared folder](install-visualcron-on-both-nodes)
