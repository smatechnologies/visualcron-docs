---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

### Failover Clustering

It is possible to use VisualCron in a failover clustered environment. We recommend using the built in Windows Server Feature [Failover Clustering](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview) for this.
 
A failover cluster is a group of independent computers that work together to increase the availability and scalability of clustered roles (formerly called clustered applications and services). The clustered servers (called nodes) are connected by physical cables and by software. If one or more of the cluster nodes fail, other nodes begin to provide service (a process known as failover). In addition, the clustered roles are proactively monitored to verify that they are working properly. If they are not working, they are restarted or moved to another node.
 
Failover clusters also provide Cluster Shared Volume (CSV) functionality that provides a consistent, distributed namespace that clustered roles can use to access shared storage from all nodes. With the Failover Clustering feature, users experience a minimum of disruptions in service.
 
Failover Clustering has many practical applications, including:
 
Highly available or continuously available file share storage for applications such as Microsoft SQL Server and Hyper-V virtual machines
Highly available clustered roles that run on physical servers or on virtual machines that are installed on servers running Hyper-V
 
You can read more about Windows Failover Cluster [here](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview).
 
### Licensing
 
A unique license (or unlimited license) needs to be activated on each node in the cluster.
 
However, VisualCron must be manually activated for each cluster.
 
### Installation and preparation
 
There are two major steps:
 
1. [Installing the Windows Failover Cluster](installing-windows-failover-cluster)
2. [Install and Setup VisualCron on Failover Cluster](install-and-setup-visualcron-on-failover-cluster)