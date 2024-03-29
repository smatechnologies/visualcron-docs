---
sidebar_label: 'Add New Drive as Shared Drive to Cluster Nodes'
hide_title: 'true'
---

## Add New Drive as Shared Drive to Cluster Nodes

At now on both nodes new iSCSI shared drive is unallocated and offline

On both nodes you need to go to *iSCSI Initiator Properties*, to the *Volumes and Drives* tab.

And click to *Auto Configure* button. Current node will update information about shared drive.

After that you need to close this window by pressing *OK* button.
 
When you are connected on the first machine, click **Start > WIndows Administrative tools > Computer Management > Disk Management**.

Your disks appear as Unknown and Offline. They also display the size you configured on the SAN (eg: 10GB). You need to bring the disks online by *Right-clicking* the disk number  and selecting Online.

Initialize the disks:

*Right-click* the disk number next to one of the new drives. Select Initialize disk.

In the box that appears, ensure that your new disk have a tick mark next to them.

Set as *MBR*.

Click *OK*.
Configure the new drive. Right-click on the drive.

Select *Create New Simple Volume*. Leave the defaults in place. Choose a drive letter to assign.

Label your drive f.ex. as *VisualCronStorage*

Click *Next*.
 
Once this is done for your first node, repeat these steps on your additional nodes. you must connect the iSCSI drives on both systems before they will be available for your cluster.
 
As the simple volume is now configured, you only need to *initialise* the disks on the other Nodes, *not recreate the Volume*. *Shared drive* should have the same *disk letters* on *both nodes*.