---
sidebar_label: 'Connecting to iSCSI Network Drives'
hide_title: 'true'
---

## Connect the nodes to the iSCSI disk

This is Part 1, step 4 of 5 in [Install the Windows failover cluster](installing-windows-failover-cluster). In this step you connect every node to the iSCSI target from [Part 1, step 3](create-iscsi-network-drive). Then, on the first node only, you bring the disk online and create its volume.

Before you start, make sure every node is listed as an initiator of the target. On the domain and storage server, in *Server Manager* -> *File and Storage Services* -> *iSCSI*, right-click the target in the *iSCSI Targets* list, select *Properties*, and select *Initiators*.

### Connect each node to the target

To connect a node, complete the following steps:

1. Click *Start* -> *Windows Administrative Tools* -> *iSCSI Initiator*.
2. If Windows says that the Microsoft iSCSI service is not running, click *Yes* to start it and have it start automatically.
3. On the ***Targets*** tab, in *Target*, enter the IP address of the domain and storage server on the iSCSI network.
4. Click *Quick Connect*. The discovered targets are listed.
5. Select the target from Part 1, step 3.
6. If its status is not *Connected*, click *Connect*.
7. Click *Done*.
8. On the ***Volumes and Devices*** tab, click *Auto Configure*.
9. Click *OK*.

Repeat this procedure on every node. Every node must be connected before the disk is available to the cluster.

### Bring the disk online on the first node

:::warning

Bring the disk online and initialize it on one node only. Initializing writes a new partition table and erases the volume. On the other nodes, only connect to the target. Leave the disk offline there; the cluster brings it online on the node that owns it.

:::

To bring the disk online, complete the following steps on the first node only:

1. Click *Start* -> *Windows Administrative Tools* -> *Computer Management*.
2. Select *Storage* -> *Disk Management*. The new disk is shown as "Unknown" and "Offline", with the size you set for the disk.
3. Right-click the disk number and select *Online*.
4. Right-click the disk number and select *Initialize Disk*.
5. Make sure the new disk is selected.
6. Select a partition style. Failover clustering accepts MBR and GPT disks; MBR is limited to 2 TB.
7. Click *OK*. The disk is online and initialized.

### Create the volume on the first node

To create the volume, complete the following steps on the same node:

1. Right-click the disk's unallocated space and select *New Simple Volume*. The *New Simple Volume Wizard* opens.
2. Click *Next*. The *Specify Volume Size* page opens.
3. Click *Next* to keep the default size. The *Assign Drive Letter or Path* page opens.
4. Select a drive letter that is not in use on any node.
5. Click *Next*. The *Format Partition* page opens.
6. Check that the file system is *NTFS*.
7. In *Volume label*, enter a label such as "ClusterStorage".
8. Click *Next*.
9. Click *Finish*. The disk has a volume and a drive letter.

### Next step

[Create the failover cluster](create-the-failover-cluster)