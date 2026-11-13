---
sidebar_label: 'Excel Macros'
hide_title: 'true'
---

## Robot Task Activities - Excel Macros

The Excel Macros category has one activity, which runs a macro in an open Excel workbook.

![The Excel Macros category in the activity list, with the Run Macro activity](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Macro/Macro.png)

The activity must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel).

---

### Run Macro

Runs an Excel macro, optionally with arguments.

![The Run Macro activity, with the Macro name, Arguments and Argument delimiter fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Macro/Run.png)

- _Macro name_: the name of the macro in the workbook
- _Arguments_: the arguments line passed to the macro; leave it empty to run the macro without arguments
- _Argument delimiter_: the character that splits the arguments line into separate arguments, "," by default

Each argument is passed to the macro as text. Variables are resolved in every field. The value the macro returns, if any, is written to the Task output.

In the example above, an arguments line of `1|2|3` with an argument delimiter of `|` passes three arguments to `TestMacro`.

---

### Tips

- The workbook that contains the macro must already be open. Use an [Excel Workbook](excel-workbook) _Open Workbook_ activity before Run Macro
- The workbook must be saved in a macro-enabled format such as `.xlsm`, and macros must be allowed by the Excel trust settings for the user the Robot Task runs as
- Choose an _Argument delimiter_ that cannot appear in the argument values themselves. The default comma is a poor choice when arguments contain numbers with thousands separators
- Keep _DisplayAlerts_ cleared on the parent [Excel](excel) container if the macro can raise an alert. In an unattended Job there is nobody to dismiss it, and the Task waits until it times out. A message box that the macro's own code shows is not suppressed by this setting
- Where the work can be done with the standard [Excel Cell](excel-cell), [Excel Row](excel-row) and [Excel Column](excel-column) activities, prefer those over a macro. The logic then stays visible in the Robot Task instead of being hidden in the workbook
