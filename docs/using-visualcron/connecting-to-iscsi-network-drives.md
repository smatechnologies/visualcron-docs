---
sidebar_label: 'Connecting to iSCSI Network Drives'
hide_title: 'true'
---

## Connecting to iSCSI Network Drives

Start the iSCSI initiator then connect to your SAN drives:

* Click Start > Windows Administrative Tools > iSCSI Initiator.
* Ensure the drives are set to allow simultaneous connections. This is configured on your SAN. Make sure you have granted access to your cluster servers.
* Open iSCSI initiator.
* Click the Targets tab.
 
* In Target, enter the IP address for the SAN.
* Click Quick Connect. Or you can click to Refresh to auto discover targets.
* Your advertised drives are displayed.
* Highlight a drive; then click connect to connect to drive.
 
When a drive is connected, click Done. Click the Volumes and Devices tab.
 
* Click *Auto Configure*.
* Click *OK*.
* When you are connected on the first machine, click **Start > WIndows Administrative tools > Computer Management > Disk Management**.
 
Your disks appear as Unknown and Offline. They also display the size you configured on the SAN (eg: 16GB). You need to bring the disks online by Right-clicking the disk number  and selecting *Online*.
 
Initialize the disks:

* Right-click the disk number next to one of the new drives. Select Initialize disk.
* In the box that appears, ensure that your new disk have a tick mark next to them.
 
Set as *MBR*.
 
* Click *OK*.
* Configure the new drive. Right-click on the drive.
 

Select *Create New Simple Volume*. Leave the defaults in place. Choose a drive letter to assign.
Label your drive f.ex.  as ClusterStorage
 
Once this is done for your first node (Server), repeat these steps on your additional nodes (Servers). For example, from the two listed servers above (Server1 and Server2), you must connect the iSCSI drives on both systems before they will be available for your cluster.
 
As the simple volume is now configured, you only need to initialize the disks on the other Nodes, not recreate the Volume.