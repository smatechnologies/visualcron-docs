---
sidebar_label: 'Add Generic Service'
hide_title: 'true'
---

## Add the Generic Service role

This is Part 2, step 5 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you add the VisualCron service to the cluster as a Generic Service role. The cluster then watches the service and starts it on another node when needed.

### Start the wizard

To start the wizard, complete the following steps:

1. In *Failover Cluster Manager*, select *Roles*. The list of roles is shown.
2. Click *Configure Role*. The *Before You Begin* page opens.
3. Click *Next*. The *Select Role* page opens.
4. Select *Generic Service*.
5. Click *Next*. The *Select Service* page opens.

### Choose the service, name and disk

To choose the service, the network name and the disk, complete the following steps:

1. Select the *VisualCron* service.
2. Click *Next*. The *Client Access Point* page opens.
3. Enter a network name for the role. Clients connect to the VisualCron Server by this name, on the Server port ("16444" by default).
4. If the network does not use DHCP, enter an IP address for the role.
5. Click *Next*. The *Select Storage* page opens.
6. Select the VisualCron disk.
7. Click *Next*. The *Replicate Registry Settings* page opens.

### Finish the wizard

To finish the wizard, complete the following steps:

1. Click *Next* without adding a registry key. The *Confirmation* page opens.
2. Check the settings.
3. Click *Next*. The wizard creates the role.
4. Click *Finish*.

Result: The role is listed under *Roles* with the network name you entered, and the VisualCron service runs on the node that owns the role.

:::note

No registry key needs to be replicated while both nodes use the default settings folder in the shared installation folder. Keep the default settings folder; moving the settings folder of a clustered Server is not covered in this guide.

:::

### Next step

[Move the role to another node manually](manually-changing-current-node)