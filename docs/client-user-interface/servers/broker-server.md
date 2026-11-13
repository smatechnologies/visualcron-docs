---
sidebar_label: 'Broker Server'
hide_title: 'true'
---

## Broker Server

:::info Availability

Load Balancing requires VisualCron **11.2.1** or later and a **Pro Subscription** license. See [Load Balancer](load-balancer) for the full feature overview, and [Deploying Load Balancing](load-balancing-deployment) for the order in which to configure the components.

:::

**Broker Server** (Broker for short) - acts as a link between several VisualCron Servers, called Server Agents (hereinafter either Server or Agent for short).
 
Broker collects statistics from all connected Agents, sends different actions to the Agents for execution (e.g. execution of a certain Job), and most importantly: the Broker determines which of the controlled Agents should have the Scheduler role, i.e. start and monitor events of different Triggers.
Broker itself can run on any VisualCron Server, including a separate dedicated Server that does not additionally act as a Scheduler or Server Agent.

![Agents tab of the Load balancer window listing connected Server Agents with their status, health and roles](../../../static/img/lb_settings_agents.png)

There are three main functions of the Broker:

* Collecting statistics from connected Servers
* Distributed Execution of Jobs
* Managing status of connected Servers
 
### Collecting statistics from connected Servers

Collected statistics can be used in three different scenarios:

* to filter Servers on which Job can be executed with the configured [distributed execution](execution-distribution) mode;
* when checking compliance with the Condition configured in the [Load balancing Flow](load-balancing-flows), for launching certain Actions;
* when checking the [Switching Condition](#scheduler-switch-condition) when the current Server with the Scheduler role is to be replaced by another connected Server.
 
### Distributed Execution of Jobs

If distributed execution is configured for a Job, instead of launching the Job locally, the Server creates and sends an execution request to the Broker. The Broker combines the parameters of distributed execution of the Job with the parameters of Server selection for execution, and then sends execution requests to the selected Servers.
See the [Execution Distribution](execution-distribution) topic for more details.
 
### Managing status of connected Servers

The essence of load balancing on the Broker's side is to choose among all connected Server Agents the one that will monitor the status of Triggers, and run triggered Jobs. This Server is called the **Scheduler Agent**.
Agents other than the Scheduler are in the Off state (Spare Agents), i.e. they do not run or monitor triggers, although they can perform any task from the Broker, including the execution of a specific Job.
 
Note: the Broker controls the status only of those Agents that are connected in the appropriate mode (controlled by the Broker).
 
For more details, see the [Scheduler monitoring and controlling](#scheduler-monitoring-and-controlling) chapter below.
 
 
### Enabling Broker and connecting Server Agents
 
The Broker and the Server Agents are configured in the ***Load balancer*** window, opened from ***Servers*** -> ***Load balancer***.

![Main settings tab of the Load balancer window with the Broker Server and Server Agent groups](../../../static/img/lb_settings_main.png)

The Broker must be activated on one of the VisualCron Servers: check _Activate load balancing Broker on this Server_ in the ***Broker Server*** group.
On each other Server, check _Connect as Server Agent to the Broker below_ in the ***Server Agent*** group and select the VisualCron Connection to the Broker.

Set up object synchronization between the Servers first, from ***Servers*** -> ***Sync Server objects***. See [Sync Server Objects](sync-server-objects).
 
### Configuring Scheduler control mode

For the Broker to control the status of the connected Servers, check _Control the status (scheduler role) of connected Server Agents_ in the Broker settings. Also check _Allow the Broker to control this Server status_ in the settings of each Server that the Broker is to control.
If among the currently connected and monitored Servers there are none with the Scheduler role, the Broker will automatically select the Server that will become the Scheduler Agent after the configured timeout expires.
 
**Scheduler connection timeout**

Timeout is configured in the field _Connection timeout for the Server Agent with scheduler role_, the default value is 15 seconds.
 
### Scheduler switch condition

Check _Transfer scheduler role to another Server Agent if the Scheduler switch condition is met_ to also configure a switch condition, on the ***Scheduler switch condition*** tab.
Once the switching condition is met for the current Scheduler Agent, the Broker will try to switch the Scheduler role to another (spare) Agent.
 
An example of a switch condition is "Server Health is [Very bad] for 5 minutes":

![Scheduler switch condition tab of the Load balancer window with one Health status condition](../../../static/img/lb_settings_switchcondition.png)

See the [Load balancing Conditions](load-balancing-conditions) topic for information on configuring load balancing conditions, as well as supported scheduler switch conditions.
 
### Scheduler monitoring and controlling
 
The status of the connected Servers can be monitored and controlled both on the ***Agents*** tab of the ***Load balancer*** window and in the ***Server Agents*** window, opened from ***Servers*** -> ***Agents***.

![Server Agents window listing connected Server Agents with their status, health and roles](../../../static/img/lb_agents.png)

The Scheduler role can be pre-configured on one of the connected Servers. One Server (the Scheduler Agent) should have status ON, and the rest status OFF (Spare Agents).
Further, the Broker controls the Scheduler role among the connected Servers in accordance with the established algorithm.
 
### Scheduler role control algorithm
 
_Case 1. No Scheduler Agent is detected_

(corresponding Server was disconnected, or its status became OFF, or the "Allow the Broker to control this Server status" checkbox was cleared)
 
* the Broker waits for the Scheduler Agent to connect within the configured timeout;
* if there is no connection, the Broker attempts to select a new Scheduler Agent among the connected Spare Agents;
* the Agent with the best Server Health is selected and, if possible, the switching condition should not be met for it;
* if an Agent has been selected, the Broker sends a request to it to turn on the Scheduler role.
 
_Case 2. Scheduler switch condition is met for the current Scheduler Agent_ 

* the Broker attempts to select a new Scheduler Agent among the connected Spare Agents;
* but it does not take into account Agents for which the Scheduler switch condition is also met;
* if the new Scheduler Agent is selected, the Broker sends successive requests to turn off the old Agent and turn on the chosen one.
 
_Case 3. Two Scheduler Agents are detected connected at the same time_
 
* the Broker chooses among them the Agent for which the switching condition is not met, then the Agent with better Server Health;
* the chosen Agent remains, and the Broker sends to the second Agent a request to turn off the Scheduler role.
 
_Case 4. User sends a manual "Turn on" request from the "Server Agents" form_
 
the Broker sends a request to the current Scheduler Agent (if any) to turn off the Scheduler role;
then (after a successful response, or after a 5 second timeout) the Broker sends a “turn on” request to the Agent specified by the user.
 
_Case 5. User sent a manual "Turn off" request from the "Server Agents" form_
 
* the Broker sends a request to the Agent specified by the user, to turn off the Scheduler role;
* at the same time, the Broker checks if there is another connected Scheduler Agent, and if not, the Broker tries to select a new Scheduler Agent;
* the selection does not take into account Agents for which the Scheduler switch condition is met;
* if a new Agent has been selected, the Broker sends a request to it to turn on the Scheduler role.
