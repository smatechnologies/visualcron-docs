---
sidebar_label: 'Task Internal - Calculate Variable'
hide_title: 'true'
---

## Task Internal - Calculate Variable

The Calculate Variable Task adds, subtracts, multiplies or divides two numbers and stores the result in an existing User Variable.

![Calculate Variable Task settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/calculate%20variable.png)

**Store value in Variable...**

Select the User Variable to store the result in. Only User Variables of type Int32 or Double are listed; Job Variables and other types cannot be used. A new Task selects the first of these Variables here and for both values, so check all three before you save. The field after "=" previews the result with the current values, without the rounding for an Int32 Variable; it shows "Error calculating" and the reason when it cannot calculate.

**Left hand value**

*Existing variable* / *Other value*

With *Existing variable* (default), select an Int32 or Double User Variable. With *Other value*, enter a number and select its type, *Int32* (default) or *Double*; select *Double* for a number with decimals, because with *Int32* it is rounded. An empty *Other value* counts as 0. User Variables can be used in *Other value*; Job, Task and Trigger Variables are not replaced here.

**Operation**

*Addition ( + )* (default), *Subtraction ( - )*, *Multiplication ( x )* or *Division ( / )*.

**Right hand value**

*Existing variable* / *Other value*

The same as *Left hand value*. Defaults to *Existing variable*; *Other value* defaults to 1.

Each value can be a Variable or a number, and the Variable you store in can also be one of the values. For example:

* `<Variable> = <Variable> <operation> <other Variable>`
* `<Variable> = <Variable> <operation> <number>`, for example to add 1 to a counter
* `<Variable> = <number> <operation> <number>`

When the Task runs, numbers are read with the regional settings of the VisualCron Server, so use its decimal separator. The preview and *Validate value when saving* use the Client's regional settings.

The result takes the type of the Variable it is stored in. For an Int32 Variable, the result is rounded to the nearest whole number, and a result ending in .5 goes to the even number: 7 / 2 stores 4 and 5 / 2 stores 2.

If the right hand value is 0 in a division, a Double Variable stores "Infinity", "-Infinity" or "NaN" and the Task succeeds; an Int32 Variable is left with a value that cannot be read as a number, and the Task fails; set the Variable again with a Set User Variable Task or in the *Variables* window. Make sure the right hand value is not 0 before this Task runs, for example with a [Condition](../../../server/task-conditions).

**Validate value when saving**

This option is selected again each time you open the Task. When it is selected, the Task can be saved only if a Variable is selected to store the result in, a Variable is selected for each *Existing variable*, and each *Other value* is a number of its type. It does not calculate the result, so a division by zero is not caught.

**Result**

The output is `Variable '<name>' was updated to value: <value>`. The Task fails when the Variable to store in, or a Variable used as a value, does not exist, or when a value is not a number.

:::warning

When a user starts the Job, from the Client or through a Job/Task Control Task in a Job that user started, and is still connected when this Task runs, the change is saved and shown in Clients only if that user has the *Edit* permission for *Variables* (see [User permissions](../../../server/main-user-permissions)). Without it, the Task still succeeds and the new value is used on the Server, but Clients do not show it, and it is written to disk only the next time User Variables are saved; if the VisualCron service restarts before then, the new value is lost. Runs started by a Trigger are not affected. Give users who run this Job from the Client the *Edit* permission for *Variables*.

:::
