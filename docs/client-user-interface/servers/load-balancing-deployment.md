---
sidebar_label: 'Deploying Load Balancing'
hide_title: 'true'
---

## Deploying Load Balancing

:::info Availability

Load Balancing requires VisualCron **11.2.1** or later and a **Pro Subscription** license. See [Load Balancer](load-balancer) for the full feature overview.

:::

This topic covers what to put in place before enabling the Load Balancer, the decisions to make first, and the order in which to configure the components. It does not recommend a specific topology or hardware configuration, because both depend on the environment. For the dependencies that apply to every environment, see [Requirements](../../requirements).

### Before you begin

Confirm the following on every Server that takes part:

* The license includes Load Balancing. Without it the Broker does not start and Flows do not run.
* The VisualCron version is 11.2.1 or later, and all participating Servers run the same version.
* The port used by the VisualCron Connection between the Servers is open. The default is `16444`.
* [Server object synchronization](sync-server-objects) is configured. Agents can only run a Job that exists on them, so synchronize the Jobs, Credentials and Connections the distributed Jobs depend on before enabling the Broker.

### Decide before you configure

**Where the Broker runs**

The Broker can run on any VisualCron Server, including a dedicated Server that is neither a Scheduler nor an Agent. Running it on a Server that also carries workload keeps the number of machines down. Running it on a dedicated Server keeps it available when the other Servers are under load, which matters if the Broker also controls the Scheduler role.

**Whether the Broker controls the Scheduler role**

If *Control the status of connected Server Agents* is enabled on the Broker, and *Allow the Broker to control this Server status* is enabled on a Server, the Broker decides which Server holds the Scheduler role and moves it automatically. If both are left off, the Scheduler role stays where it is set and is only changed manually from the *Server Agents* form.

Enable Broker control when the goal is automatic failover. Leave it off when Triggers must stay on a known Server.

**How Agents are selected for a distributed Job**

Set on the *Distributed execution* tab of the Load balancer settings:

* *Round-robin* — spreads executions evenly. A reasonable default when the Servers are equivalent.
* *First* — always uses the first connected Agent. Useful when one Server is preferred and the others are fallbacks.
* *Random* — spreads executions without tracking order.
* *Best health* — selects on current [Server Health](../server/health-server-health). Useful when the Servers are not equivalent, or when load varies through the day.

**Which Jobs are distributed**

Distribution is set per Job on the *Agent distribution* tab and is *Execute locally only* by default. Enabling the Broker does not change how existing Jobs run. See [Execution Distribution](execution-distribution).

### Order of configuration

To deploy the Load Balancer, complete the following steps:

1. Configure [Server object synchronization](sync-server-objects) between all participating Servers and confirm the Jobs to be distributed exist on each of them.
2. On the Server chosen to host the Broker, go to **Servers > Execution distribution > Load balancer** and check *Activate load balancing Broker on this Server*.
3. On each other Server, configure the connection to the Broker in the *Server Agent* group.
4. Confirm every Agent appears in the *Agents* tab, or in **Servers > Execution distribution > Server Agents**.
5. If the Broker is to control the Scheduler role, enable *Control the status of connected Server Agents* on the Broker and *Allow the Broker to control this Server status* on each controlled Server. Confirm that one Server shows status ON and the rest show OFF.
6. Set the Agent selection mode, and any Agent filter, on the *Distributed execution* tab.
7. Set the execution mode on each Job that is to be distributed, on the Job's *Agent distribution* tab.
8. Add any [Load balancing Flows](load-balancing-flows) last, once the Broker and Agents are stable.

### Test before deploying to production

The **Server Launcher** utility runs several VisualCron Server instances from a single installation, each with its own identifier and port. This allows a Broker and its Agents, Scheduler role switching, and distributed execution to be set up and tested on one computer before the configuration is applied to production Servers. See [Server Launcher](server-launcher).

### Capacity

There are no fixed sizing figures for a Broker, because the load depends on how many Agents connect to it rather than on how many Jobs run.

Each connected Agent sends statistics to the Broker no more often than once every three seconds, and additionally whenever its status or its Server Health changes. Broker load therefore grows with the number of Agents.

Each Agent also runs Jobs, so size each Agent as a normal VisualCron Server. To size from measured values rather than estimates, use the [Server Health](../server/health-server-health) dialog, the CPU charts in [Job result](../server/job-result), and the *Server: Computer report* in [Reports](../reports).
