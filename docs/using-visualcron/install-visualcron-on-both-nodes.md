---
sidebar_label: 'Install VisualCron on Both Nodes in the Same Shared Directory'
hide_title: 'true'
---

## Install VisualCron on both nodes in the same shared folder

This is Part 2, step 4 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you install VisualCron into one folder on the VisualCron disk, first on the node that owns the disk and then on the other node, and you set the Server options that the cluster needs.

:::warning

VisualCron must run on only one node at a time. Both nodes use the same program files and settings on the shared disk, and nothing in VisualCron stops a second node from starting the service. The setup program starts the VisualCron service and the VisualCron Tray Client when it finishes, so stop the service and exit the Tray Client when you finish on each node. From Part 2, step 5, the cluster starts and stops the service.

:::

Before you start, note:

- Same drive letter and folder for VisualCron on both nodes, for example "X:\VisualCron"
- Default settings folder, the "settings" subfolder of the installation folder, kept on the shared disk; moving it is not covered in this guide

The setup program installs the VisualCron service with the startup type "Automatic" each time it runs, including an upgrade. You change it to "Manual" in [Set the startup type](#set-the-startup-type).

### Install VisualCron on the first node

To install VisualCron on the node that owns the disk, complete the following steps:

1. In *Failover Cluster Manager*, go to *Storage* -> *Disks*.
2. In the *Owner Node* column, note the node that owns the VisualCron disk. This is the first node.
3. On the first node, run the VisualCron installation file.
4. When the installer asks what to install, select *VisualCron Client and Server*. The *VisualCron Client only* option disables the service.
5. In *Select Installation Folder*, enter or browse to the folder on the VisualCron disk, for example "X:\VisualCron". The default folder is under Program Files on the local drive.
6. Complete the installation. The setup program starts the VisualCron service on this node.

Result: VisualCron is installed on the VisualCron disk, and the Server runs on the first node.

### Set the Server options on the first node

:::note

Select *Installed in cluster environment* before you activate VisualCron in Part 2, step 8. With the option selected, the Server ties its activation to the drive that VisualCron is installed on. With the option cleared, it ties the activation to the Windows system drive of the node where the activation was made. See [Activation on a cluster](individual-node-activation).

:::

To set the Server options, complete the following steps:

1. Open the Client and connect to the Server on the first node.
2. If the "admin" user still has the empty password of a new Server, set a password for it. Do this before the Server port can be reached from other computers. See [Secure the admin user](../get-visualcron/download-install-upgrade-uninstall#secure-the-admin-user).
3. Go to *Server* -> *Main settings* -> *Settings*.
4. On the ***Main settings*** tab, select *Installed in cluster environment*.
5. If the firewall button reads *Firewall denies*, click it. The button changes to *Firewall allows*, and Windows Firewall on this node allows connections to the Server port.

   The rule allows connections from any remote address. To allow only the computers that run a Client, limit its remote addresses in Windows Defender Firewall; see [Firewall and network](../get-visualcron/antivirus-exclusions#firewall-and-network).
6. Click *Apply settings*.
7. Close the Client.
8. Right-click the [VisualCron Tray Client](visualcron-tray-client) icon in the notification area, and select *Exit*. The setup program started the Tray Client from the installation folder on the VisualCron disk.
9. In *Services* on the first node, stop the *VisualCron* service.

Result: The Server is set to run in a cluster, the Tray Client is closed, and the service is stopped on the first node.

### Install VisualCron on the second node

To install VisualCron on the second node, complete the following steps:

1. In *Failover Cluster Manager*, go to *Storage* -> *Disks*.
2. Select the VisualCron disk.
3. Click *Move Available Storage* -> *Select Node*.
4. Select the second node.
5. Click *OK*. The VisualCron disk comes online on the second node.
6. On the second node, check that the VisualCron disk has the same drive letter as on the first node.
7. Run the VisualCron installation file.
8. When the installer asks what to install, select *VisualCron Client and Server*.
9. In *Select Installation Folder*, enter the same folder as on the first node.
10. Complete the installation. The setup program starts the VisualCron service on this node.

Result: VisualCron is installed from the second node into the same folder, and the Server runs on the second node.

### Check the Server options on the second node

:::warning

The second node reads *Installed in cluster environment* from the shared settings folder, so the option is already selected there. If it shows cleared, this node is not using the shared settings folder. Do not change any setting on this node. Stop the VisualCron service on this node and contact VisualCron support.

:::

To check the Server options, complete the following steps:

1. Open the Client and connect to the Server on the second node.
2. Go to *Server* -> *Main settings* -> *Settings*.
3. On the ***Main settings*** tab, check that *Installed in cluster environment* is selected.
4. If the firewall button reads *Firewall denies*, click it. The button changes to *Firewall allows*. The button acts at once, without *Apply settings*.

   The rule allows connections from any remote address. To allow only the computers that run a Client, limit its remote addresses in Windows Defender Firewall; see [Firewall and network](../get-visualcron/antivirus-exclusions#firewall-and-network).
5. Close the Client.
6. Right-click the VisualCron Tray Client icon in the notification area, and select *Exit*.
7. In *Services* on the second node, stop the *VisualCron* service.

Result: VisualCron is installed on both nodes in the same folder, the firewall allows the Server port on both nodes, the Tray Client is closed, and the service is stopped on both nodes.

### Set the startup type

To keep the service from starting outside the cluster, complete the following steps:

1. In *Services* on the first node, set the startup type of the *VisualCron* service to "Manual".
2. In *Services* on the second node, set the startup type of the *VisualCron* service to "Manual".

Result: The VisualCron service starts only when the cluster starts it.

:::warning

An upgrade sets the startup type of the VisualCron service back to "Automatic", and the setup program starts the service on the node where you run it. After an upgrade, check the startup type of the VisualCron service on each node.

:::

### Next step

[Add the Generic Service role](add-generic-service)
