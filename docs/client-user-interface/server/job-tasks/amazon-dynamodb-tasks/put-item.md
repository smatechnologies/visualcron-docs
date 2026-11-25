---
sidebar_label: 'Task Amazon DynamoDB - Put Item'
hide_title: 'true'
---

## Task Amazon DynamoDB - Put Item

The Amazon DynamoDB - Put item Task writes one item to an Amazon DynamoDB table, using an Amazon Connection. When the table has no item with the same primary key, the Task creates the item. When an item with that key exists, the Task replaces it.

![DynamoDB - Put item Task settings, with the Connection, Table name, Index name, and Attribute items fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20DynamoDB%20Tasks/Put%20Item.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions***, and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### DynamoDB - Put item tab

#### Connection

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task

The Task signs in with the _Access Key ID_ and _Secret Access Key_ of the Connection and connects to its _Region_. The other settings of the Connection do not apply to this Task.

#### Parameters

- _Table name_: the table to write to. Click the refresh button to fill the list with the tables of the account. The Client asks for a table name before it saves the Task
- _Index name_: the primary key of the table. Click the refresh button to fill the list. The list shows one entry, with the table name and the names of its key attributes. Select it to show the _Index comparison_ and _Attribute filters_ sections. When _Index name_ is empty, the Task ignores both sections and writes only the _Attribute items_, without a condition

#### Index comparison

This section sets the primary key of the item. It shows the key attributes of the table, each with its data type.

- _Partition key_: the value of the partition key. The comparison is always "="
- _Sort key_: the value of the sort key. This row appears only when the table has a sort key. The comparison list offers only "=", because a write needs the exact value of every key attribute

The Task adds both key values to the item. When _Partition key_ is empty, the Task ignores the _Index comparison_ section, and the item takes its key from _Attribute items_ instead.

:::note

Tasks saved in an earlier version can hold a range comparison for the sort key, such as "Between" or ">". The Task runs them with "=" and the first value. When you open such a Task, the comparison shows "=" and the first value. When you save it, the Task stores "=" and drops the second value.

:::

#### Attribute filters

Attribute filters make the write conditional. When the list has at least one filter, DynamoDB checks the existing item with the same primary key. It writes the item only when that item matches the key values and every filter. When no such item exists, or a filter does not match, DynamoDB rejects the write. Filters therefore replace an existing item and never create a new one. When the list is empty, the Task writes the item without a condition.

To add a filter, click _Add_. To change a filter, select it and click _Edit_, or double-click it. _Delete_ removes the selected filter, and _Clear all_ removes every filter. Each filter has these fields:

- _Name_: the name of the attribute to check
- The data type of the attribute: "String", "Number", or "Binary"
- The comparison, for example "=", "<>", "Between", "Exists", or "Begin with". For "Between", enter a second value in the _And_ field. "Exists" and "Not exists" take no value
- The value to compare with. For "Binary", enter the bytes as decimal numbers separated by commas, or click _Add/Edit Multi-Value_

The Task skips a filter whose value is empty, except for "Exists" and "Not exists".

#### Attribute items

Attribute items are the other attributes of the item. To add an attribute, click _Add_. To change an attribute, select it and click _Edit_, or double-click it. _Delete_ removes the selected attribute, and _Clear all_ removes every attribute. Each attribute has these fields:

- _Name_: the name of the attribute
- The data type of the attribute: "String", "Number", or "Binary"
- The value of the attribute. For "Binary", enter the bytes as decimal numbers separated by commas, or click _Add/Edit Multi-Value_

The Task skips an attribute whose value is empty. When an attribute has the same name as a key attribute in _Index comparison_, the Task uses the _Index comparison_ value.

All values accept Variables: the table name, the key values, the filter values, and the attribute values. Attribute names do not accept Variables.

### Output and errors

When the write replaces an existing item, the Task writes one line for each attribute of the replaced item to the Task output, in the format `name="value"`. Only key attributes show their value. Other attributes show an empty value. When the write creates a new item, the Task output is "OK".

When the Server cannot find the Connection, the Task fails.

:::warning

When DynamoDB rejects the write, the Task writes the error message from DynamoDB to the Task error output, and the Task still ends with success. This includes a write that fails an attribute filter. To make a rejected write fail the Task, add an _If error output_ condition on the ***On error*** tab; see [Task - On error](../../task-on-error).

:::

### Related topics

- [Connection - Amazon](../../connection-amazon)
- [Job - Tasks](../../job-tasks)
- [Task - On error](../../task-on-error)
