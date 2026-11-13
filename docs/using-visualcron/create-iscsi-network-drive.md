---
sidebar_label: 'Create a iSCSI Network Drive'
hide_title: 'true'
---

## Create an iSCSI virtual disk for the cluster

This is Part 1, step 3 of 5 in [Install the Windows failover cluster](installing-windows-failover-cluster). In this step you create the first iSCSI virtual disk on the domain and storage server, and an iSCSI target that gives every node access to it. [Part 2, step 1](create-iscsi-drive-with-existing-target) adds the VisualCron disk to this same target.

:::warning

In this guide, this first disk is for the cluster quorum (the disk witness). Do not install VisualCron on it. VisualCron gets its own disk in [Part 2, step 1](create-iscsi-drive-with-existing-target).

:::

### Create the virtual disk

To create the virtual disk, complete the following steps:

1. On the domain and storage server, in *Server Manager*, go to *File and Storage Services* -> *iSCSI*.
2. Click *To create an iSCSI virtual disk, start the New iSCSI Virtual Disk Wizard*. The wizard opens on *Select iSCSI virtual disk location*.
3. Select the disk or volume to store the iSCSI virtual disk on.
4. Click *Next*. The *Specify iSCSI virtual disk name* page opens.
5. Enter a name and, if you want, a description.
6. Click *Next*. The *Specify iSCSI virtual disk size* page opens.
7. Enter the size of the disk. A disk witness needs at least 512 MB; 1 GB is enough.
8. Click *Next*. The *Assign iSCSI target* page opens.

### Create the target

To create the target, complete the following steps:

1. Select *New iSCSI target*.
2. Click *Next*. The *Specify target name* page opens.
3. Enter a target name and, if you want, a description.
4. Click *Next*. The *Specify access servers* page opens.

### Give every node access

To give the nodes access, complete the following steps:

1. Click *Add*. The *Add initiator ID* window opens.
2. Select *Query initiator computer for ID*.
3. Click *Browse*. The *Select Computer* window opens.
4. Enter the name of a node. To search Active Directory instead, click *Advanced*.
5. Click *OK*.
6. Click *OK* in *Add initiator ID*. The node is added to the access servers.
7. Repeat steps 1 to 6 for every node. If a node has already connected to this server, you can select it from the initiator cache on the target server instead.

### Finish the wizard

To finish the wizard, complete the following steps:

1. When every node is listed, click *Next*. The *Enable authentication* page opens.
2. If you use CHAP, set it up.
3. Click *Next*. The *Confirm selections* page opens.
4. Check the settings.
5. Click *Create*.
6. On the *View results* page, when the virtual disk is created, click *Close*. The new iSCSI virtual disk and its target are listed under *iSCSI*.

### Next step

[Connect the nodes to the iSCSI disk](connecting-to-iscsi-network-drives)