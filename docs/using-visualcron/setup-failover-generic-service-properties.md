---
sidebar_label: 'Setup Failover Generic Service Properties'
hide_title: 'true'
---

## Set up the failover properties of the role

This is Part 2, step 7 of 8 in [Install and set up VisualCron on the failover cluster](install-and-setup-visualcron-on-failover-cluster). In this step you set how the cluster handles failures of the VisualCron role, and whether it moves the role back after a failover.

:::warning

Each move of the role stops the VisualCron service on one node and starts it on another, and Jobs running on the first node stop. Moving the role back to its first node after a failover (failback) is another such move.

:::

The ***Failover*** tab of the role's properties has these settings:

- *Maximum failures in the specified period* and *Period (hours)*: how many failures of the role the cluster handles within the period before it leaves the role failed
- *Prevent failback* or *Allow failback*: whether the cluster moves the role back to its preferred owner when that node is available again. Failback needs a preferred owner, set on the ***General*** tab of the role's properties

With *Prevent failback*, the role does not move back by itself when the preferred node returns.

To change the failover properties, complete the following steps:

1. In *Failover Cluster Manager*, select *Roles*.
2. Right-click the role you created in [Add the Generic Service role](add-generic-service), which has the network name you entered there, and select *Properties*. You can also select the role and click *Properties* in the *Actions* pane. The properties window of the role opens.
3. Click the ***Failover*** tab.
4. Set *Maximum failures in the specified period* and *Period (hours)*.
5. Select *Prevent failback*, unless you need the role back on one specific node.
6. Click *OK*.

Result: The cluster uses the new failover settings for the VisualCron role.

In the Client, the ***Generic services*** tab of the *Windows Failover Cluster* window shows the role's failover period and restart settings. To check the maximum failures and failback, use *Failover Cluster Manager*. See [Using VisualCron in a failover cluster](using-visualcron-in-a-clustered-environment).

### Next step

[Activation on a cluster](individual-node-activation), then [Test failover](install-and-setup-visualcron-on-failover-cluster#test-failover)
