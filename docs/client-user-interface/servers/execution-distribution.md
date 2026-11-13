---
sidebar_label: 'Execution Distribution'
hide_title: 'true'
---

## Execution Distribution

:::info Availability

Load Balancing requires VisualCron **11.2.1** or later and a **Pro Subscription** license. See [Load Balancer](load-balancer) for the full feature overview.

:::

**Execution Distribution** is a setting up of a certain Job so that execution of the Job can be performed not only on the local Server, but also on one or more Servers connected to the Broker.

Distributed execution is configured on the _Agent distribution_ tab in the Job editing form:

![Agent distribution tab of the Job window with the execution modes and the list of agents](../../../static/img/lb_job_agentdistribution.png)

**Supported Job execution modes**
 
* _Execute locally only_

This is the default execution mode.
 
* _Execute on one agent according to selection mode_

Job execution request is sent to the Broker to whom the current Server is connected. The Broker determines on which of the connected Servers the Job should be actually executed.
 
* _Execute on specific number of agent instances_

This mode is similar to the previous one, but the Broker selects a Server for Job execution (and sends the request) the specified number of times.
 
* _Execute on all online agents_

Job execution request is sent to the Broker, which in turn sends a request to each of the connected Agents, taking into account additional filters configured on the Broker's side.
 
* _Execute on specific agents_

If the specified Agents include the current Server, the Job is forced to be executed locally first. Then a request is sent to the Broker for execution on the other specified Agents.
 
**Agent selection and filtering**
 
Load balancer settings specify the method according to which the Agents are selected for Job execution (on the “Distributed execution” tab).

![Distributed execution tab of the Load balancer window with the agent selection modes and filters](../../../static/img/lb_settings_distributedexecution.png)

There are the following ways of Agent selection:  
 
* _Round-robin_ (for each subsequent Job execution, the next Agent is selected);
* _First_ (the first connected Agent is selected);
* _Random_ (any connected Agent);
* _Best health_ (the Agent with the best Server Health level).
 
There are also two optional filters for selecting Agents to execute the Job:
 
* _Filter agents by global condition_ (is configured on the _Global filter condition_ tab)
* _Filter agents by list_
 
The filtering condition can be, for example, not to run the Job on the Agent, where at least one Job is already running:

![Global filter condition tab of the Load balancer window with one Total running Jobs condition](../../../static/img/lb_settings_filtercondition.png)

See the [Load balancing Conditions](load-balancing-conditions) topic for information on configuring load balancing conditions, as well as supported filtering conditions.
 
 
**Distributed execution history**
 
For a Job with distributed execution settings, the _Log history_ item of the Job context menu has two sub-items: _Local execution history_ and _Distributed execution history_.

![Job context menu with Log history expanded to Local execution history and Distributed execution history](../../../static/img/lb_job_loghistory.png)

If _Distributed execution history_ is chosen, a history request is sent to each required (and currently available) Agent, then the results are combined and sent back to the user.

![Job Result Output window showing the start reason and the agents the Job ran on](../../../static/img/lb_job_resultoutput.png)

:::info Note

The full history of distributed execution is displayed only when requesting history on the Server from which the Job was originally sent to the Broker for execution.

:::
