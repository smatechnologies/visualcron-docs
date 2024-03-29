---
sidebar_label: 'Add Generic Service'
hide_title: 'true'
---

## Add Generic Service

Generic Service resource type allows us to handle failover based on a Windows Service status - in this case we track the VisualCron service.
 
At *Failover Cluster Manager* go to *Roles*. You will see current roles list.

Click to *Configure Role* to create a new role.

The *Before you begin* window is displayed. Click *Next*.

The *Select Role* window is displayed. Select *Generic Service* item at the role list and click Next.
 
The *Select Service* window is displayed/ Select *VisualCron* service in current list and click Next.

The *Client Access Point* window is displayed. Choose *NetBIOS* name for cluster role. This name can be used to connect to VisualCron server. Click *Next*.

The *Select Storage* window will be displayed. Select shared drive with installed VisualCron on it. This storage will be used on active node to run VisualCron service. Click *Next*.
 
The *Replicate Registry Settings* window is displayed. Here you can add additional registry settings if it’s needed. When it’s done, click *Next*.

The *Confirmation* window will be displayed. Check all settings and click *Next*.

After creation of *Generic Role* was successfully completed close window by clicking *Finish*.