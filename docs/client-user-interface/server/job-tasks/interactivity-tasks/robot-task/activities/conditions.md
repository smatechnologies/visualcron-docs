---
sidebar_label: 'Conditions'
hide_title: 'true'
---

## Robot Task Activities - Conditions

The **Conditions** category contains activities that control the flow of a sequence based on the result of an evaluation.

![](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/Conditions.png)

---

### If (simple)

Compares a left operand and a right operand using the specified operator and value type, then executes either the **Then** body or the **Else** body based on the result.

![](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/If.png)

| Setting | Description |
|---|---|
| Left operand | The first value to compare. Supports variables. |
| Operator | The comparison to perform, for example Equal, NotEqual, Contains, GreaterThan, RegExMatch. |
| Right operand | The second value to compare. Supports variables. |
| Type | The data type used for the comparison, for example String, Int32, Double, DateTime, Boolean. |
| Then | Activities executed when the condition evaluates to true. |
| Else | Activities executed when the condition evaluates to false. |

Either body may be left empty. Both operand fields accept VisualCron variables, so you can compare a value read from a list, a cell, or a previous activity's Result variable.

#### Using the RegExMatch operator

The **RegExMatch** operator compares the left operand against a regular expression supplied as the right operand, so the Then and Else blocks act on a match or no match condition. This is useful for validating data before it is used.

For example, to confirm that a date read from a data file is in `MM-dd-yyyy` format before feeding it into an application that only accepts that format:

| Field | Value |
|---|---|
| Left operand | The date value, for example `{USERVAR(lvDateReformat\|GetCell\|{RPALOOP(a381\|Iterations)}\|Date\|false)}` |
| Operator | `RegExMatch` |
| Right operand | `(0[1-9]\|1[0,1,2])-(0[1-9]\|[12][0-9]\|3[01])-(19\|20)\d{2}` |
| Type | `String` |

That expression matches:

- A two digit month from `01` to `12`
- A `-` separator
- A two digit day from `01` to `31`
- A `-` separator
- A four digit year beginning with `19` or `20`, giving a range of 1900 to 2099

Records that match are processed in the **Then** block. Records that do not match fall through to the **Else** block, where they can be written to an exception log for manual correction. See [Data Processing & Logging](../data-processing-logging) for the logging pattern.

---

### Switch

Evaluates a specified expression and executes the activity whose associated key matches the result of that evaluation. If no key matches, the **Default** activity is executed.

![](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/Switch.png)

| Setting | Description |
|---|---|
| Expression | The value to evaluate. Each case is matched against this result. |
| Default | The activity executed when no case key matches. |
| Add new case | Adds a case with a key and an activity to execute when the key matches. |

Switch is a cleaner alternative to a chain of nested If activities when you are branching on one value with several known outcomes, such as a status code or a record type.

---

### Tips

- Set the **Type** field to match the data you are actually comparing. Comparing numbers as `String` produces unexpected results, for example `"10"` is less than `"9"`.
- When comparing a Result variable from a previous activity, remember the value is the text `True` or `False`, so use `String` as the type and `True` as the right operand.
- Use the **Display name** property to describe what the condition tests, for example `Check If Date Format Is Valid`, rather than leaving it as `If (simple)`.
