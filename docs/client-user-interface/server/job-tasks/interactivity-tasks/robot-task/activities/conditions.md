---
sidebar_label: 'Conditions'
hide_title: 'true'
---

## Robot Task Activities - Conditions

The Conditions activities choose which activities run next, based on a comparison or a value.

![The Conditions category in the activity list, with the If (simple) and Switch activities](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/Conditions.png)

---

### If (simple)

Compares a left operand with a right operand, using the selected operator and type, then runs either the _Then_ body or the _Else_ body.

![The If (simple) activity, with the Left operand, Operator, Right operand and Type fields and the Then and Else bodies](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/If.png)

- _Left operand_: the first value to compare; Variables are resolved first
- _Operator_: the comparison to make
- _Right operand_: the second value to compare; Variables are resolved first
- _Type_: the data type both operands are converted to before the comparison: "Boolean", "Decimal", "Double", "DateTime", "Int16", "Int32", "Int64" or "String"
- _Then_: the activities that run when the comparison is true
- _Else_: the activities that run when the comparison is false

Either body may be left empty. Both operand fields accept VisualCron Variables, so you can compare a value read from a list, a cell or an earlier activity's Result variable.

The operators you can use depend on the _Type_:

- "String": "Equal", "NotEqual", "Contains", "NotContains", "RegExMatch" and "RegExNoMatch"
- "Decimal", "Double", "Int16", "Int32", "Int64" and "DateTime": "Equal", "NotEqual", "Larger", "LargerOrEqual", "Smaller" and "SmallerOrEqual"
- "Boolean": "Equal" and "NotEqual"

Any other combination, and the "NotCheck" operator, makes the activity fail with an error. With a type other than "String", at least one operand must have a value, and a value that cannot be converted to the type also makes the activity fail. "String" comparisons are case-sensitive.

#### Using the RegExMatch operator

The "RegExMatch" operator tests the left operand against a regular expression given as the right operand, so the _Then_ and _Else_ bodies act on a match or no match. "RegExNoMatch" is the reverse. The expression matches if it is found anywhere in the value, so add `^` and `$` when the whole value must match. This is useful for validating data before it is used.

For example, to confirm that a date read from a data file is in `MM-dd-yyyy` format before entering it in an application that only accepts that format:

- _Left operand_: the date value, for example `{USERVAR(lvDateReformat|GetCell|{RPALOOP(a381|Iterations)}|Date|false)}`
- _Operator_: "RegExMatch"
- _Right operand_: `^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d{2}$`
- _Type_: "String"

That expression matches:

- A two-digit month from `01` to `12`
- A `-` separator
- A two-digit day from `01` to `31`
- A `-` separator
- A four-digit year beginning with `19` or `20`, giving a range of 1900 to 2099

The expression checks the format only. It does not reject a date that does not exist, such as `02-31-2024`.

Records that match are processed in the _Then_ body. Records that do not match fall through to the _Else_ body, where they can be written to an exception log for manual correction. See [Data Processing & Logging](../data-processing-logging) for the logging pattern.

---

### Switch

Evaluates a value and runs the case whose key matches the result. If no key matches, the _Default_ activity runs.

![The Switch activity, with the Expression field, the Default activity and the Add new case link](../../../../../../../static/img/RPA/Robot%20Tasks/Conditions/Switch.png)

- _Expression_: the value to evaluate; Variables are resolved first, and each case key is compared with the result
- _Default_: the activity that runs when no case key matches
- _Add new case_: adds a case, with a key and the activity that runs when the key matches

A key matches only when it is exactly the same text as the result, including upper and lower case.

:::warning

If no case key matches and no _Default_ activity is set, the Switch activity fails with an error. Set a _Default_ activity whenever the value can be something you did not plan for.

:::

Switch is a cleaner alternative to a chain of nested If activities when you branch on one value with several known outcomes, such as a status code or a record type.

---

### Tips

- Set the _Type_ to match the data you are comparing. To compare numbers or dates as larger or smaller, use a numeric type or "DateTime": the "String" type supports only equality, contains and regular expression operators
- A Result variable written by an earlier activity, such as _File Exists_, holds the text "True" or "False". Comparing it with the "String" type and "True" as the right operand works
- Use the _Display name_ property to describe what the condition tests, for example `Check If Date Format Is Valid`, rather than leaving the default name
