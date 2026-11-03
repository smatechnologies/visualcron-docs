---
sidebar_label: 'Create the Failover Cluster'
hide_title: 'true'
---

## Create the failover cluster

This is Part 1, step 5 of 5 in [Install the Windows failover cluster](installing-windows-failover-cluster). In this step you validate the nodes and create the cluster from one node. The wizard also creates the cluster's access point: the cluster name and IP address that you use to administer the cluster.

### Start the wizard and select the nodes

To select the nodes, complete the following steps:

1. Sign in to one node with a domain account that is a local administrator on every node and can create computer objects in Active Directory.
2. Click *Start* -> *Windows Administrative Tools* -> *Failover Cluster Manager*.
3. Click *Create Cluster*. The *Create Cluster Wizard* opens on *Before You Begin*.
4. Click *Next*. The *Select Servers* page opens.
5. Enter the name of a node.
6. Click *Add*. The node is listed.
7. Repeat steps 5 and 6 for every node. To find a node instead, click *Browse*.
8. Click *Next*. The *Validation Warning* page opens.

### Validate the nodes

:::warning

Fix every error that the validation report lists before you create the cluster. If the report lists errors, cancel the wizard, fix the errors, and start again from *Create Cluster*. Warnings do not stop the wizard; read them before you continue.

:::

To validate the nodes, complete the following steps:

1. Select *Yes* to run the validation tests.
2. Click *Next*. The *Validate a Configuration Wizard* opens.
3. Click *Next*. The *Testing Options* page opens.
4. Select *Run all tests (recommended)*.
5. Click *Next*. The *Confirmation* page lists the tests to run.
6. Click *Next*. The tests can take several minutes.
7. On the *Summary* page, click *View Report*.
8. Check the results in the report.
9. Click *Finish*. The *Create Cluster Wizard* continues on the *Access Point for Administering the Cluster* page.

### Create the cluster

To create the cluster, complete the following steps:

1. In *Cluster Name*, enter a name for the cluster.
2. If the nodes use static IP addresses, select only the production network in the list of networks.
3. If you selected a network in step 2, enter a free IP address for the cluster on that network. The cluster name and IP address are registered in DNS.
4. Click *Next*. The *Confirmation* page lists the settings for the new cluster.
5. Select *Add all eligible storage to the cluster*. The wizard adds the disk from [Part 1, step 3](create-iscsi-network-drive).
6. Click *Next*. Wait while the wizard creates the cluster.
7. On the *Summary* page, click *Finish*. The cluster is created.

### Check the quorum disk

To check the quorum disk, complete the following steps:

1. In *Failover Cluster Manager*, select *Storage* -> *Disks*.
2. In the *Assigned To* column, check that the disk from [Part 1, step 3](create-iscsi-network-drive) is shown as the disk witness.
3. If it is not, right-click the cluster and select *More Actions* -> *Configure Cluster Quorum Settings*. The *Configure Cluster Quorum Wizard* opens.
4. In the wizard, select the disk from Part 1, step 3 as the disk witness. See [Configure and manage quorum](https://learn.microsoft.com/en-us/windows-server/failover-clustering/manage-cluster-quorum).

Result: The cluster uses the disk from [Part 1, step 3](create-iscsi-network-drive) as its disk witness.

### Next step

Part 1 is complete. Go to Part 2: [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster).