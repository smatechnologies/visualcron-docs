---
sidebar_label: 'Loops'
hide_title: 'true'
---

## Robot Task Activities - Loops

The Loops activities repeat a body of activities, jump between points in a sequence, and end or skip loop iterations.

![The Loops category in the activity list, with While, Do While, For, For Each, Flow, Label, Go to, End Loop and Continue Loop](../../../../../../../static/img/RPA/Robot%20Tasks/Loops/Loops.png)

Each loop activity has a _LoopId_ property: a short ID, filled in when the activity is added, that loop variables use to refer to the loop. See [Loop Variables](#loop-variables).

---

### While

Runs the body while the condition is true. The condition is checked before each iteration, so if it is false at the start, the body never runs.

- _Left operand_ and _Right operand_: the two values to compare. Both accept variables and are resolved again before each check
- _Operator_: the comparison. "Boolean" supports "Equal" and "NotEqual". The number types and "DateTime" support "Equal", "NotEqual", "Larger", "LargerOrEqual", "Smaller" and "SmallerOrEqual". "String" supports "Equal", "NotEqual", "Contains" and "NotContains"
- _Type_: the value type of the comparison: "Boolean", "Decimal", "Double", "DateTime", "Int16", "Int32", "Int64" or "String"
- _MaxIterations_: in the Properties pane, the highest number of iterations allowed. Default: "1000"
- _Body_: the activities to repeat

### Do While

Runs the body while the condition is true. The condition is checked after each iteration, so the body always runs at least once. The settings are the same as for _While_.

:::note

When a _While_ or _Do While_ loop would run more than _MaxIterations_ times, the activity fails with the error "The maximum loop iteration has reached."

:::

---

### For

Runs the body for each value of a counter, from _For X_ up to, but not including, _To Y_.

![The For activity with the For X, To Y and Step fields and the Body](../../../../../../../static/img/RPA/Robot%20Tasks/Loops/For.png)

- _For X_: the start value of the counter
- _To Y_: the end value of the counter. The body does not run for this value
- _Step_: the amount added to the counter after each iteration. A negative step counts down. A step of "0" repeats the body without end, because the For activity has no _MaxIterations_ limit
- _Body_: the activities to run in each iteration

For example, _For X_ "1", _To Y_ "3" and _Step_ "1" runs the body twice, for 1 and 2. _For X_ must be smaller than _To Y_, or larger when _Step_ is negative. If the two are equal, the activity fails. All three fields accept variables, so the end value can come from a value read while the Task runs.

:::warning

To run the body once for each row of a list, starting at 1, set _To Y_ to the row count plus 1. With _To Y_ set to the row count itself, the last row is skipped and the Task reports success.

:::

---

### For Each

Runs the body once for each line in a block of text, such as the content of a data file or the value of a variable.

![The For Each activity with the For each row x in, Use column, Field separator, Text qualifier, Line break and Start row fields and the Body](../../../../../../../static/img/RPA/Robot%20Tasks/Loops/For%20Each.png)

- _For each row x in_: the text to loop through, for example `{USERVAR(List)}`
- _Use column_: the index of the column the loop reads from each line. Default: "0"
- _Field separator_: the character between columns, for example "Tab" or "Comma". Default: "Tab"
- _Text qualifier_: the character around values that contain the separator
- _Line break_: the line break the text uses, for example "CrLf". Default: "CrLf"
- _Start row_: the first line to process. Default: "1". Set it to "2" to skip a header line
- _Body_: the activities to run for each line

Empty lines are skipped.

---

### Flow

Runs the activities inside it in order, and lets _Go to_ activities jump to _Label_ activities. Place the Label and Go to activities directly inside the Flow: Go to finds only labels that are direct children of the Flow.

![The Flow activity with a Label activity and a Go to activity whose Label field is set](../../../../../../../static/img/RPA/Robot%20Tasks/Loops/Goto.png)

### Label

Marks a position that a _Go to_ activity can jump to.

### Go to

Jumps to the label chosen in its _Label_ field. Running continues from that Label rather than from the next activity. If the label is not found, the activity fails.

---

### End Loop

Ends the loop it is in. Running continues with the first activity after the loop.

### Continue Loop

Ends the current iteration and starts the next one from the top of the loop body.

Continue Loop is the key to clean exception handling inside a loop. When a record cannot be processed because of a problem with its data, write the record to an exception log and then use Continue Loop as the last activity in that branch. The loop moves on to the next record instead of stopping the whole Task or retrying the same record. See [Data Processing & Logging](../data-processing-logging) for a full walkthrough of that pattern.

---

### Loop variables

Loop activities expose values about the current iteration as variables. The number of the current iteration, starting at 1, is:

```text
{RPALOOP(a381|Iterations)}
```

The first parameter is the _LoopId_ of the loop, so the value differs per loop. To insert the reference rather than typing it, right-click the loop activity, point to _Loop Variables_ and click _Number of loop iteration so far_. This copies the reference, without the braces, to the clipboard. The same menu copies the other loop variables, such as the current value and the maximum number of iterations, and _Copy LoopId_ copies the ID alone.

A common use is passing the iteration number as the row number to a List Variable lookup:

```text
{USERVAR(lvDateReformat|GetCell|{RPALOOP(a381|Iterations)}|Date|false)}
```

---

### Tips

- Prefer _For Each_ over a counted _For_ loop when looping through a data file, so that the loop matches the number of records present
- Set _Start row_ to "2" when the source text has a header line, or the header is processed as data
- Put the activity that marks a record as complete at the very end of the loop body. A record is then marked as processed only if every step before it succeeded
- Avoid nesting more than two loops. Move the inner work into a separate Robot Task if the logic grows
