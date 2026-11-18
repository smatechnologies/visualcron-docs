---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Install and set up VisualCron on the failover cluster

This is Part 2 of [Using VisualCron in a failover cluster](using-visualcron-in-a-clustered-environment). In this part you add a shared disk for VisualCron to the cluster and install VisualCron on it from each node in turn. You then add the VisualCron service to the cluster as a Generic Service role, activate VisualCron and test failover.

### Requirements

- Two nodes in a Windows failover cluster; see [Install the Windows failover cluster](installing-windows-failover-cluster)
- An active maintenance or subscription; see [Maintenance](maintenance)
- The same VisualCron installation file for both nodes
- VisualCron licensing for the cluster; see [Choosing the right license](choosing-the-right-license) and [Activation on a cluster](individual-node-activation)

### Steps

1. [Create the VisualCron disk on the existing target](create-iscsi-drive-with-existing-target)
2. [Prepare the VisualCron disk on the nodes](add-new-shared-drive-to-cluster)
3. [Add the VisualCron disk to the cluster](add-shared-drive-to-cluster)
4. [Install VisualCron on both nodes in the same shared folder](install-visualcron-on-both-nodes), including the *Installed in cluster environment* option and the firewall on each node
5. [Add the Generic Service role](add-generic-service)
6. [Move the role to another node manually](manually-changing-current-node)
7. [Set up the failover properties of the role](setup-failover-generic-service-properties)
8. [Activation on a cluster](individual-node-activation)

### Test failover

To test failover after Part 2, step 8, complete the following steps:

1. In the Client, connect to the Server by the role's network name.
2. Note the Jobs on the Server.
3. Move the role to the other node. See [Move the role to another node manually](manually-changing-current-node).
4. Connect the Client again by the role's network name.
5. Check the activation status. See [Information - License](../client-user-interface/server/information-license).
6. Check that the same Jobs and settings are there.

Result: The Server runs on the other node with the same Jobs and settings. If the Server is not activated there, see [Activation on a cluster](individual-node-activation).

### Next step

[Create the VisualCron disk on the existing target](create-iscsi-drive-with-existing-target)
