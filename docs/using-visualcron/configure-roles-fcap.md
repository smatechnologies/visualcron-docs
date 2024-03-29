---
sidebar_label: 'Configure Roles / Features on Failover Cluster Access Point (FCAP)'
hide_title: 'true'
---

## Configure Roles / Features on Failover Cluster Access Point (FCAP)

In the **Server Manager > Dashboard**, click Add roles and features.

![](../../static/img/clip333444069.png)

The Before you begin window is displayed. Click *Next*.

![](../../static/img/clip333444070.png)

The select *Installation Type* window is displayed. Select *Role-based or feature-based installation*. Click *Next*.

![](../../static/img/clip333444071.png)

The Select destination server window is displayed. Select the server that you are logged in on. Click *Next*.

![](../../static/img/clip333444072.png)

The *Select server roles* window is displayed. In the *Roles list*, select *File Server*, *iSCI Target Server*, *iSCI Target Storage Provider*.

![](../../static/img/clip333444073.png)

Click *Next*.
 
The Select features window is displayed. In the Features list, select *Failover Clustering*, *Failover Clustering Tools*. If it wasn’t installed before, the Add features that are required for Failover Clustering window will pop up. This window shows the dependencies that will be installed with this feature.

![](../../static/img/clip333444074.png)

Click *Add Features*. Click Next. The Confirm installation selections window is displayed. Check the setting to ensure all selected items to be installed.

Click *Install*. The chosen Role and Feature will be installed on your machine.

When the installation is complete, restart the machine to finalize the installation.

