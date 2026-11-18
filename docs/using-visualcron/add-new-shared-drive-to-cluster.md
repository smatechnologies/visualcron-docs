---
sidebar_label: 'Add New Drive as Shared Drive to Cluster Nodes'
hide_title: 'true'
---

## Prepare the VisualCron disk on the nodes

This is Part 2, step 2 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step every node picks up the disk from [Part 2, step 1](create-iscsi-drive-with-existing-target), and you create its volume on one node. Part 2, step 3 then adds the disk to the cluster.

### Pick up the disk on every node

To pick up the disk on a node, complete the following steps:

1. Click *Start* -> *Windows Administrative Tools* -> *iSCSI Initiator*.
2. On the ***Volumes and Devices*** tab, click *Auto Configure*.
3. Click *OK*.

Repeat this procedure on every node.

### Create the volume on one node

:::warning

Bring the disk online, initialize it and create its volume on one node only. Initializing writes a new partition table and erases the volume, including any VisualCron installation and settings on it. On the other nodes, leave the disk offline; the cluster brings it online on the node that owns it.

In Part 2, step 4, after the disk is in the cluster, each node installs VisualCron in turn to the same drive letter and folder on this disk. Keep the default settings folder, which is inside the installation folder.

Assign the drive letter once, here. Choose a letter that is not in use on any node. After you add the disk to the cluster, the cluster keeps that drive letter on whichever node owns the disk.

:::

To create the volume, complete the following steps on one node only:

1. Click *Start* -> *Windows Administrative Tools* -> *Computer Management*.
2. Select *Storage* -> *Disk Management*.
3. If the new disk is not listed, click *Action* -> *Rescan Disks*.
4. Bring the disk online and initialize it, as in steps 3 to 7 of [Bring the disk online on the first node](connecting-to-iscsi-network-drives#bring-the-disk-online-on-the-first-node).
5. Create its volume with the volume label "VisualCronStorage", as in [Create the volume on the first node](connecting-to-iscsi-network-drives#create-the-volume-on-the-first-node). The VisualCron disk has a volume and a drive letter.

### Next step

[Add the VisualCron disk to the cluster](add-shared-drive-to-cluster)