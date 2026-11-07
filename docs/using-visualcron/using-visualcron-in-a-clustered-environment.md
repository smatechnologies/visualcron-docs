---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Using VisualCron in a failover cluster

You can run VisualCron in a Windows Server failover cluster, so that the VisualCron Server keeps running when the computer it runs on fails. VisualCron uses the Failover Clustering feature that is built into Windows Server.

### How it works

- One VisualCron installation in a folder on a shared cluster disk, installed from each node in turn
- The VisualCron service added to the cluster as a Generic Service role, together with the shared disk and a network name
- The role running on one node at a time; when that node fails, or when you move the role, the cluster starts the VisualCron service on another node
- Settings and Jobs kept in the settings folder on the shared disk, so the node that takes over uses the same ones

Use a disk that is added to the cluster as a normal cluster disk for the VisualCron role, not a Cluster Shared Volume. Every node can reach a Cluster Shared Volume at the same time.

For how Failover Clustering itself works, see Microsoft's [Failover Clustering overview](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview).

### Licensing and maintenance

The *Windows Failover Cluster* window in the Client, and support for VisualCron in a failover cluster, need an active maintenance or subscription. See [Maintenance](maintenance).

To activate VisualCron, see [Activation on a cluster](individual-node-activation). For the licenses you need, see [Choosing the right license](choosing-the-right-license) and [License and activation](license-and-activation).

The Server setting *Installed in cluster environment* decides what the Server ties its activation to:

- Selected: the drive that VisualCron is installed on
- Cleared: the Windows system drive of the node where the activation was made

Select *Installed in cluster environment* before you activate. See [Install VisualCron on both nodes in the same shared folder](install-visualcron-on-both-nodes).

### Before you start

You need:

- An Active Directory domain
- A server for the iSCSI target that holds the shared disks
- Two servers to use as cluster nodes
- An active maintenance or subscription

### Steps

1. [Install the Windows failover cluster](installing-windows-failover-cluster): prepare the servers, create the iSCSI disk and create the cluster
2. [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster): add the VisualCron disk to the cluster, install VisualCron from each node in turn with *Installed in cluster environment* selected, create the Generic Service role, set its failover properties, activate and test failover

### What happens on failover

When the role moves to another node, because a node fails or because you move it:

- The VisualCron service stops, or is lost if the node fails, and Jobs running on that node stop
- The cluster moves the shared disk and starts the VisualCron service on the other node
- The Server reads its settings and Jobs from the settings folder on the shared disk
- Unless the Server status is "Off" (see [Main - Server On/Off](../client-user-interface/server/server-on-off)), it runs once each active Job that has *Run missed Job once at start* selected and that should have run while the service was stopped
- The Job and Task log history and the stored output stay on each node, because the Output cache folder is a local folder by default; after a failover, the Client shows the history of the node that runs the role
- Clients lose their connection; connect again by the role's network name

:::warning

VisualCron must run on only one node at a time. Nothing in VisualCron stops a second node from starting the service against the same settings, so leave starting and stopping the service to the cluster.

Keep the default settings folder, under the installation folder on the shared disk. Moving the settings folder of a clustered Server is not covered in this guide.

:::

### The Windows Failover Cluster window

In the Client, the *Windows Failover Cluster* window shows the failover cluster that the connected Server runs in. To open it, go to *Servers* -> *Failover* -> *Windows Failover Cluster*. You need an active maintenance or subscription, and permission to read Server settings. See [Main - User Permissions](../client-user-interface/server/main-user-permissions). If the *Failover* group is not shown, it may be hidden on the ***Features*** tab of the Client settings. See [Settings - Client Settings](../client-user-interface/file/client-settings).

When the window opens, it reads the cluster information. To read it again, for example with a different Credential, select the Credential and click *Get cluster information*. Without a Credential, the Server reads the cluster as the account that the VisualCron service runs as. The window also saves in the Server settings whether the Server runs in a cluster, and the Credential used.

The window shows one of these statuses:

- "VisualCron is Running inside Failover Cluster"
- "VisualCron not Running inside Failover Cluster"
- "Can't get Failover Cluster status and information"

When the Server runs inside a cluster, the window has these tabs:

- ***Cluster***: the cluster name, the current host server, the quorum and witness, and the number of nodes, networks, volumes and generic services
- ***Nodes***: each node's state, version, network interfaces and disks
- ***Networks***: the cluster networks and their network interfaces
- ***Volumes***: the cluster disks, with *Change state* to bring the selected disk online or take it offline
- ***Generic services***: each Generic Service role with its owner node, state, failover period and restart settings, network name and disks, with *Change state* to bring the role online or take it offline

:::warning

Taking the VisualCron role or its disk offline with *Change state* stops the VisualCron Server that the Client is connected to, and Jobs running on it stop. The Client then loses its connection. To bring the role or disk online again, use *Failover Cluster Manager*.

:::

To move the role to another node, use *Failover Cluster Manager*. See [Move the role to another node manually](manually-changing-current-node).

### Next step

[Install the Windows failover cluster](installing-windows-failover-cluster)