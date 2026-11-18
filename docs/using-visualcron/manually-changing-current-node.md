---
sidebar_label: 'Manually Changing Current Node for Generic Service'
hide_title: 'true'
---

## Move the role to another node manually

This is Part 2, step 6 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you move the VisualCron role to another node, for example before maintenance on the current node or to test failover.

:::warning

Moving the role stops the VisualCron service on the current node, and Jobs running there stop. Move the role when no important Jobs are running.

:::

To move the role, complete the following steps:

1. In *Failover Cluster Manager*, select *Roles*.
2. Right-click the role you created in [Add the Generic Service role](add-generic-service), which has the network name you entered there, and select *Move* -> *Select Node*. You can also select the role and click *Move* -> *Select Node* in the *Actions* pane. The *Move Clustered Role* window opens.
3. Select the node to move the role to.
4. Click *OK*.

Result: The cluster stops the VisualCron service on the current node and starts it on the selected node. The Server reads the same settings and Jobs from the shared disk. Unless the Server status is "Off" (see [Main - Server On/Off](../client-user-interface/server/server-on-off)), it runs once each active Job that has *Run missed Job once at start* selected and that should have run during the move. Connected Clients lose their connection; connect again by the role's network name.

### Next step

[Set up the failover properties of the role](setup-failover-generic-service-properties)