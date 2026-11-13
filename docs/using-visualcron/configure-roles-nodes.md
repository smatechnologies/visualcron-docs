---
sidebar_label: 'Configure Roles / Features on Nodes'
hide_title: 'true'
---

## Configure roles and features on the nodes

This is Part 1, step 2 of 5 in [Install the Windows failover cluster](installing-windows-failover-cluster). In this step you join every node to the domain and add the Failover Clustering feature. The nodes need no server roles.

### Join the node to the domain

To join a node to the domain, complete the following steps:

1. On the network adapter that connects the node to the production network, set the DNS server address to the IP address of the domain and storage server on the production network.
2. Open *System Properties*.
3. Select the ***Computer Name*** tab.
4. Click *Change...*.
5. Under *Member of*, select *Domain*.
6. Enter the domain name.
7. Click *OK*.
8. Enter the credentials of a domain account that can join computers to the domain.
9. Click *OK*.
10. Restart the node when Windows asks you to. The node is a member of the domain.

### Select the Failover Clustering feature

To select the feature, complete the following steps:

1. In *Server Manager* -> *Dashboard*, click *Add roles and features*. The *Add Roles and Features Wizard* opens on *Before you begin*.
2. Click *Next*. The *Select installation type* page opens.
3. Select *Role-based or feature-based installation*.
4. Click *Next*. The *Select destination server* page opens.
5. Select the node you are signed in to.
6. Click *Next*. The *Select server roles* page opens.
7. Click *Next* without selecting a role. The *Select features* page opens.
8. Select *Failover Clustering*. If its tools are not installed yet, the *Add features that are required for Failover Clustering?* window opens.
9. Click *Add Features*.

### Install the feature

To install the feature, complete the following steps:

1. Click *Next*. The *Confirm installation selections* page opens.
2. Check that *Failover Clustering* and its tools are listed.
3. Click *Install*. The feature is installed.
4. When the installation is complete, click *Close*.
5. If the wizard says that a restart is needed, restart the node.

### Start the Microsoft iSCSI service

To start the service, complete the following steps:

1. Click *Start* -> *Windows Administrative Tools* -> *iSCSI Initiator*.
2. If Windows says that the Microsoft iSCSI service is not running, click *Yes* to start it and have it start automatically.
3. Close *iSCSI Initiator*.

Repeat these procedures on every node.

Result: Every node is in the domain, has the Failover Clustering feature, and runs the Microsoft iSCSI service.

### Next step

[Create an iSCSI virtual disk for the cluster](create-iscsi-network-drive)