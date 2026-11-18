---
sidebar_label: 'Event Trigger - SQL'
hide_title: 'true'
---

## Event Trigger - SQL

The SQL Trigger runs a query or a stored procedure through a database Connection when it starts and then at every *Polling interval* (default 60 seconds). It starts the Job when the result meets the condition on the ***Condition*** sub tab. This Trigger does not use *Run delay* or *Expire after being triggered*: every match starts the Job.

The result is every value the query returns, in all rows, columns and result sets, joined into one text with nothing between them. For example, two rows with the values 1 and 2 give the result `12`. A *String* condition is checked against that text. For the other data types, the joined text is converted to the chosen *Data type*. Several numeric values therefore become one number (1 and 2 give 12), which is compared without an error. No rows, or a text that cannot be converted, counts as an error (see *On error reconnect attempts*). For *Boolean*, the value must be the text `True` or `False`.

The settings are on the ***SQL*** tab, ***Connection*** sub tab.

![The Connection sub tab of the SQL tab in the Add/Edit event window: Database Connection and Credential for integrated security lists, Command timeout 0 seconds, On error reconnect attempts 60 and On error reconnect interval (seconds) 10](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQL.png)

**Database Connection**

Select an existing SQL [Connection](global-connections). If none exists, click the icon next to the list to add one; it can then be selected in the combo box.

**Credential for integrated security**

Use only with a Connection that uses Windows authentication: the query then runs as this Windows user, who needs access to the database. Use a [Credential](global-credentials) with the *Load profile* option. When you save, the Client warns you and asks whether to continue in these cases:

* The Connection uses Windows authentication, the VisualCron service runs as Local System and no Credential is selected
* A Credential is selected but the Connection does not use Windows authentication
* The Credential does not have *Load profile*

You can save anyway.

**Command timeout**

How many seconds the query may run before it fails (up to 99999). The default, 0, means no limit.

**On error reconnect attempts**

The number of failed queries in a row before the Trigger stops checking (1 to 500; default 60). From the start, that many failures in a row stop it; after a successful query, one fewer does (59 with the default). Each error is written to the log. Any error counts: the database cannot be reached, the query fails, or the result cannot be read as the chosen *Data type*.

When the Trigger stops because the Connection is missing, or because the *String* condition is not supported (see *Condition*), it is deactivated. For any other error, it stops checking but still shows as active. Fix the cause, then deactivate and activate the Trigger, or save the Job.

**On error reconnect interval (seconds)**

How many seconds to wait before the next try (1 to 500; default 10).

The query is on the ***SQL*** tab, ***Trigger*** sub tab, ***Text*** tab.

![The Text tab of the Trigger sub tab with a SELECT query in the Query editor](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQL%20Trigger.png)

Enter the query. The Trigger runs the query on the selected tab: ***Text*** or ***Stored Procedure***.

:::warning

The SQL Trigger passes the query text to the database as typed: Variables in it are not replaced, although *Extended Trigger debug logging* shows the query with them replaced. The SQL Task does replace them. To pass a value from a Variable, use a stored procedure parameter: parameter values accept Variables.

:::

A stored procedure is set on the ***SQL*** tab, ***Trigger*** sub tab, ***Stored Procedure*** tab.

![The Stored Procedure tab of the Trigger sub tab: Name of Stored Procedure with a refresh icon, an empty Parameters list with Name, Value and Direction columns, and Add, Edit and Delete buttons](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQL%20Trigger%20Stored.png)

Select the *Name of Stored Procedure*: click the refresh icon next to the list to load the stored procedures of the selected Connection, then select one. Selecting a procedure replaces the *Parameters* list with that procedure's parameters. A name you type is saved only when it matches an entry in the list, so load the list and select the procedure.

The *Parameters* grid below shows all parameters for the stored procedure. Use the *Add*, *Edit*, and *Delete* buttons (also available from the grid's context menu) to manage parameters.

Click *Add* to open the parameter window, and set:

* *Name* and *Value*. The value accepts Variables
* *Use null value*: sends NULL instead of the value
* *Validate value*: when checked, the value is checked against the *Data type* when you click *OK*. Clear it if the value is a Variable that has no value yet
* *Data type* and *Parameter direction*
* *Size*: *Auto*, *Max*, or *Specific* with the size in the box next to it

The values of output parameters are available in the [Result Variables](#result-variables).

![Clicking Add on the Stored Procedure tab opens the Parameter window: Name, Value, Use null value, Validate value, Data type, Parameter direction and Size](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQL%20Trigger%20Stored%20Procedure.png)

The condition is on the ***SQL*** tab, ***Condition*** sub tab.

![The Condition sub tab of the SQL tab: Condition Equal (=), Data type String, Value to compare with, and If value is the same as last time with Fire Trigger selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQL%20Condition.png)

**Data type**

Select how the result is read. The default is *String*. The conditions offered depend on the data type.

* **String**
* **Boolean**
* **Int32**
* **Int64**
* **Decimal**
* **Double**

**Condition**

The comparison between the result and *Value to compare with*. The default is *Equal (=)*.

* *Boolean*: *Equal (=)*, *Not equal (!=)*
* *String*: *Equal (=)*, *Not equal (!=)*, *Contains (=%)*, *Regex - match*, *Regex - no match*. String comparisons are case-sensitive
* *Int32*, *Int64*, *Decimal*, *Double*: *Equal (=)*, *Not equal (!=)*, *Larger than (>)*, *Larger than or equal (>=)*, *Smaller than (<)*, *Smaller than or equal (<=)*, and *Contains (=%)*, which checks whether the number, written as text, contains the value

:::warning

*Not contains (!=%)* is offered for *String* but is currently not supported when the Trigger runs: every check is logged as an error and counts as a failed query, until the Trigger is deactivated. Use *Regex - no match* instead, with the text as the pattern (escape characters that have a meaning in regular expressions).

:::

**Value to compare with**

The value the result is compared with. Accepts Variables; click the icon to insert one. For the numeric and Boolean types, it must be a valid value of that type.

**If value is the same as last time**

What to do when the condition matches and the result is the same as the result of the previous query (whether or not that one matched):

* *Fire Trigger*: the default. Start the Job every time the condition matches
* *Do not fire Trigger*: do not start the Job again until the result changes
* *Disable Trigger*: deactivate the Trigger instead of starting the Job

### Result Variables

When the Trigger fires, it sets these result Variables:

* `SQL.Result.QueryResult`: the result of the query that fired the Trigger
* `SQL.QueryResult`: the result of the latest query, whether or not it fired the Trigger. Until the Trigger has fired once, it returns a "[Result not set …]" text
* `SQL.Result.Parameter.Value|<parameter name>`: the value of an output parameter

For example, `{TRIGGER(Active|LastTrigger|SQL.Result.QueryResult)}` returns the result that fired the Trigger that started the run, and `{TRIGGER(Active|LastTrigger|SQL.Result.Parameter.Value|MyParameter)}` returns the output parameter `MyParameter`. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. See [Variables](global-variables) for how *Last trigger* and the other keys work.
