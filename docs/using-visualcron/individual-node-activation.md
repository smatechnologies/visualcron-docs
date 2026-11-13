---
sidebar_label: 'Individual Node Activation'
hide_title: 'true'
---

## Individual node activation

This page is the last step of [installing VisualCron on a failover cluster](install-and-setup-visualcron-on-failover-cluster). It explains how to activate VisualCron on the cluster nodes.

After nodes are created you can activate your nodes. You need either a unique activation or an unlimited one (like Site license) for each node.

To activate the cluster nodes, complete the following steps:

1. Connect the Client to the node that currently runs the VisualCron service.
2. Click *Server* -> *Main settings* -> *Settings*.
3. On the ***Main settings*** tab, make sure *Installed in cluster environment* is selected (see [Main - Settings](../client-user-interface/server/main-settings)).
4. Click *Apply settings*.
5. Activate the Server as described in [License and activation](license-and-activation).
6. Move the VisualCron service to the second node (see [Manually Changing Current Node for Generic Service](manually-changing-current-node)).
7. Connect the Client to the Server again.
8. Click *Server* -> *Information* -> *Server info*, and check *Activated* on the ***License*** tab.

If the second node shows "Activated: Yes", it is using the activation made on the first node. If it shows "Activated: No", contact [VisualCron support](https://www.visualcron.com/Contact.aspx).
