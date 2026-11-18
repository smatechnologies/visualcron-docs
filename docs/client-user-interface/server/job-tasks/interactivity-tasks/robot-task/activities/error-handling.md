---
sidebar_label: 'Error Handling'
hide_title: 'true'
---

## Robot Task Activities - Error Handling

The Error handling activities catch, raise and pass on errors inside a sequence, so that the sequence can react to a failure instead of stopping.

![The Error handling category in the activity list, with the Try Catch, Rethrow and Throw activities](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/Error%20Handling.png)

These are not VisualCron activities. They are the standard activities of the .NET [System.Activities.Statements](https://learn.microsoft.com/en-us/dotnet/api/system.activities.statements?view=netframework-4.8.1) namespace.

---

### Try Catch

Gives a structured way to handle errors in a sequence. It has a _Try_ block with the main logic, one or more _Catches_ for specific exception types, and an optional _Finally_ block for logic that must run whatever the outcome.

![A Try Catch activity with a Read File activity in the Try block, an Exception catch and an empty Finally block](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/TryCatch.png)

- _Try_: the activities that may raise an exception; they run in order
- _Catches_: each catch handles one exception type raised in the _Try_ block; add more catches to handle different types
- _Finally_: runs after the _Try_ block and any catch that ran, whether or not an exception occurred; use it for cleanup; this block is optional

If no exception occurs in the _Try_ block, the catches are skipped. If one occurs, control passes to the catch for that exception type. The _Finally_ block always runs last.

**Adding a catch for a specific exception type**

In the example below, a _Read File_ activity in the _Try_ block may fail if the file is not there yet. An `IOException` catch handles that case by waiting for the file, while a general `Exception` catch handles anything else.

![A Try Catch activity with an IOException catch that contains a Wait For File activity, followed by a general Exception catch](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/TryCatch%20Exception.png)

**Using the Finally block**

The _Finally_ block is the place for actions that must happen either way, such as sending a notification e-mail or closing an application that was opened in the _Try_ block.

![A Try Catch activity whose Finally block contains a sequence that starts Outlook and sends a message](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/TryCatch%20Finally.png)

Although the main purpose of Try Catch is handling exceptions, it can also be used to branch a sequence on purpose, by raising a controlled error with the _Throw_ activity.

---

### Errors Try Catch cannot handle

Some exceptions are outside the reach of Try Catch, including `OutOfMemoryException` and `ThreadAbortException`.

Try Catch handles the errors of VisualCron activities in general. It cannot catch the error in this case, where the sequence is stopped:

- **Web Macro activities.** If the error is caused by an element that is not found, check _Allow to ignore the element_ in that activity's settings

---

### Error settings on an activity

An alternative to Try Catch is the _Error settings_ property, in the Properties pane under **Error handling**, which VisualCron activities have. Web Macro activities do not have it.

![The Properties pane of an activity, with the Error settings property under Error handling](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/Error%20Settings.png)

Open the property to add rules that map an error type to an action.

![The Error handling settings window and the Add/Edit Error handling window, with the Activity Error and Activity Error Action fields](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/Error%20Handling%20Settings.png)

- _Activity Error_: the error type the rule applies to: "Unhandled errors" for every activity, plus "Window not found" for Windows activities, "Excel not found" for Excel activities and "Outlook not found" for Outlook activities. A Windows activity raises every error as an unhandled error, so to ignore a window that is not found, add the rule for "Unhandled errors"
- _Activity Error Action_: "Raise error" or "Ignore error"

A rule that ignores an error lets the sequence continue past the failing activity. The rules have no effect on the condition, loop, Flow, Label, Go to and Wait activities, which show the property but do not use it.

:::warning

An ignored error is written to the Task output as a message, not as an error. If nothing later in the sequence fails, the Task reports success even though that activity did not do its work. Use "Ignore error" only where skipping the activity is really acceptable, and log what was skipped.

An "Excel not found" rule applies to every error that Excel itself reports, not only a missing Excel. Ignoring it also ignores, for example, a failed save.

:::

Combining Error settings with Try Catch lets you build a sequence that copes with both expected and unexpected outcomes.

---

### Throw

Raises an exception. Use it to raise a controlled error, or to end the sequence when a specific condition is met.

![A Throw activity in the Then body of an If (simple) activity, with the Exception property open in the Expression Editor](../../../../../../../static/img/RPA/Robot%20Tasks/Error%20Handling/Throw.png)

The _Exception_ property takes a VB expression that creates the exception:

```vb
new System.ApplicationException("Your custom message here")
```

A typical use is inside the _Then_ body of an If activity: when a validation check fails, Throw raises a descriptive error that a surrounding Try Catch then handles. A Throw that no Try Catch handles makes the Task fail.

---

### Rethrow

Raises again, from inside a catch, the exception that the catch is handling. Use it when a catch must log or clean up but should still let the original exception continue.

---

### Tips

- Catch the most specific exception type you can. A bare `Exception` catch hides the real cause and makes failures hard to diagnose
- Prefer _Error settings_ with "Ignore error" for activities where a failure is genuinely acceptable, and Try Catch where you need to react to the failure
- For Web Macro activities, _Allow to ignore the element_ is the only option, since neither Try Catch nor Error settings applies
- Always write the details of a caught exception to a log before continuing, so that a skipped record can still be traced. See [Data Processing & Logging](../data-processing-logging)
