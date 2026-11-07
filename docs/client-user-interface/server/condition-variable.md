---
sidebar_label: 'Condition - Variable'
hide_title: 'true'
---

## Condition - Variable

The _Variable_ condition compares two values. Each value can be fixed text, Variables, or both (see [Global - Variables](global-variables)). Use it, for example, to run a Task only when a Job Variable has a given value, or when a number in a Task's output is above a limit.

This page describes the **_Variable_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "Variable" -> **_Variable_** tab

![Add/Edit condition window with the Variable tab open, showing empty Value 1 and Value 2 boxes, each with a Variables button, Type set to "String" and Condition set to "Equal (=)"](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Variable.png)

### Value 1

The left side of the comparison. Click the Variables button to the right of the box to select a Variable.

### Type

The type both values are converted to before they are compared: "Boolean", "Decimal", "Double", "Int32", "Int64" or "String". The default is "String". The operators in _Condition_ depend on the type. If the selected operator is not available for a new type, _Condition_ changes to "Equal (=)".

### Condition

How _Value 1_ is compared with _Value 2_:

- "Boolean": "Equal (=)", "Not equal (!=)"
- "String": "Equal (=)", "Not equal (!=)", "Contains (=%)", "Not contains (!=%)", "Regex - match", "Regex - no match"
- "Decimal", "Double", "Int32" and "Int64": "Equal (=)", "Not equal (!=)", "Larger than (>)", "Larger than or equal (>=)", "Smaller than (<)", "Smaller than or equal (<=)"

The operators read from _Value 1_ to _Value 2_. For example, "Larger than (>)" matches when Value 1 is larger than Value 2, and "Contains (=%)" matches when Value 1 contains Value 2.

:::warning

"Regex - no match" is listed for "String", but it always returns a Match Error, so the Condition Set takes its _On Match Error_ action. To act when a value does not match a pattern, select "Regex - match" and set the action you want on _On Match None_. See [Conditions - Actions](conditions-actions).

:::

### Value 2

The right side of the comparison. For "Regex - match", this is the regular expression. Click the Variables button to the right of the box to select a Variable.

### How values are compared

- Variables in both values are replaced first, with the values of the Job, and the Task, whose Condition Set is being checked
- "String" comparisons are case-sensitive: "Done" does not equal "done"
- "Regex - match" matches when the pattern is found anywhere in _Value 1_. Use "^" and "$" to match the whole value
- Regular expressions are case-sensitive unless the pattern starts with "(?i)"
- "Boolean" accepts only "True" or "False", in any letter case, and ignores spaces around the value
- Numbers are read with the number format, such as the decimal separator, of the regional settings the VisualCron service runs with
- A value that cannot be converted to the selected type, for example an empty value or text for "Int32", gives a Match Error, and an error is logged

:::note

A _Variable_ condition writes its result to the log only when _Extended debug logging_ is checked in the Server's log settings, see [Settings - Log Settings](settings-log-settings). The _Extended debug logging_ checkbox of the Condition Set does not apply to this condition type.

:::
