---
sidebar_label: 'Servers - Load Balancer'
hide_title: 'true'
---

## Servers - Load Balancer

**Load Balancer** component is primarily used to distribute the execution of Jobs more evenly among several synchronized VisualCron Servers.
In addition, Load Balancer can be used for the simultaneous execution of a Job on several or all of the Servers working in tandem. It can also be used to automatically configure different runtime settings for a particular Server depending on the load.
 
There are the following three main aspects of the Load Balancer:

* [Broker Server](broker-server)

The Load Balancer’s central part, which acts as a link between several VisualCron Servers, collecting statistics from connected Servers, sending various actions to the Servers for execution, and optionally determining on which of the controlled Servers the Scheduler role should be enabled.
 
* [Execution Distribution](execution-distribution)

Setting up of a certain Job so that execution of the Job can be performed not only on the local Server, but also on one or more Servers connected to the Broker.
 
* [Load balancing Flows](load-balancing-flows)

A set of Server-level rules to execute configured Actions when the specified load balancing Conditions are met.
 
Each of the aspects can be applied separately or in conjunction with the other aspects.