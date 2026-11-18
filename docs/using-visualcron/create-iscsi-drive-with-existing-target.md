---
sidebar_label: 'Create iSCSI Drive with the Already Existing Target'
hide_title: 'true'
---

## Create the VisualCron disk on the existing target

This is Part 2, step 1 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you create a second iSCSI virtual disk for VisualCron on the domain and storage server, on the target from [Part 1, step 3](create-iscsi-network-drive). That target already gives every node access, so the wizard does not ask for access servers again.

VisualCron is installed on this disk. Its settings, log and data folders are inside the installation folder by default, so they are on this disk too. Keep the default settings folder. For the space to reserve, see [System Requirements](../get-visualcron/system-requirements).

### Create the virtual disk

To create the virtual disk, complete the following steps:

1. On the domain and storage server, in *Server Manager*, go to *File and Storage Services* -> *iSCSI*.
2. Right-click the list of iSCSI virtual disks and select *New iSCSI Virtual Disk*. The wizard opens on *Select iSCSI virtual disk location*.
3. Select the disk or volume to store the iSCSI virtual disk on.
4. Click *Next*. The *Specify iSCSI virtual disk name* page opens.
5. Enter a name and, if you want, a description.
6. Click *Next*. The *Specify iSCSI virtual disk size* page opens.
7. Enter the size of the disk.
8. Click *Next*. The *Assign iSCSI target* page opens.

### Assign the disk to the existing target

To assign the disk, complete the following steps:

1. Select *Existing iSCSI target*.
2. Select the target from Part 1, step 3.
3. Click *Next*. The *Confirm selections* page opens.
4. Check the settings.
5. Click *Create*.
6. On the *View results* page, when the virtual disk is created, click *Close*. The new iSCSI virtual disk is listed under *iSCSI*.

### Next step

[Prepare the VisualCron disk on the nodes](add-new-shared-drive-to-cluster)