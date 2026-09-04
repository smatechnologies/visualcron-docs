---
sidebar_label: 'Servers - Load Balancer'
hide_title: 'true'
---

## Servers - Load Balancer

:::info Availability

Load Balancing requires VisualCron **11.2.1** or later and a **Pro Subscription** license. It is not included in Pro Perpetual. If the license does not include the feature, the Broker does not start and Load balancing Flows do not run.

:::

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

To set the components up in the correct order, see [Deploying Load Balancing](load-balancing-deployment).

### What the Load Balancer does and does not do

The Broker gives the Scheduler role to **one** connected Server at a time. That Server monitors Triggers and runs the Jobs they fire. All other connected Servers are Spare Agents: they stay in the Off state and do not monitor Triggers, although the Broker can still send them a specific Job to run.

This means the default behavior is failover, not load spreading. Adding Servers to a Broker does not by itself divide the existing workload between them.

Work is spread across Servers in two ways, and both are configured explicitly:

* **Per Job** — set an execution mode other than *Execute locally only* on the Job's *Agent distribution* tab. See [Execution Distribution](execution-distribution).
* **Per Server** — use [Load balancing Flows](load-balancing-flows) to change what a Server does when it comes under load, for example queueing new Jobs while CPU is high.

If the goal is to reduce CPU or memory usage on a single Server, review the Job and Task settings on that Server first. Load Balancing distributes work between Servers; it does not reduce the amount of work a Job performs.
