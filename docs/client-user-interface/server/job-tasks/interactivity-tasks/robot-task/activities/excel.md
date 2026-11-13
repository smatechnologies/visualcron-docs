---
sidebar_label: 'Excel'
hide_title: 'true'
---

## Robot Task Activities - Excel

The Excel activities start Microsoft Excel or attach to it, set how it behaves, and quit it. Every other Excel activity must be placed inside one of the two container activities, _New Excel_ or _Attach to Excel_.

![The Excel category in the activity list, with the New Excel, Attach to Excel, Quit Excel, Set Excel Visibility, Set Excel Interactivity, Set Display Alerts and Set Full Screen Mode activities](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/Excel.png)

Excel must be installed in the desktop session the Robot Task runs in.

### Required nesting

The Excel activities work on an Excel application supplied by a parent container, either _New Excel_ or _Attach to Excel_. Activities from the [Excel Workbook](excel-workbook), [Excel Sheet](excel-sheet), [Excel Cell](excel-cell), [Excel Row](excel-row), [Excel Column](excel-column) and [Excel Macros](excel-macros) categories go inside the container's _Do_ body. Most Excel activities outside a container are reported as a validation error; _Run Macro_ fails when it runs.

```text
Sequence
  New Excel
    Do
      Create Workbook
      Set Cell value
      Save as Workbook
      Close Workbook
      Quit Excel
```

---

### New Excel

Starts a new Excel application and makes it the one the child Excel activities in its _Do_ body work on.

![The New Excel activity with an empty Do body](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/New.png)

#### Properties

![The Properties pane of the New Excel activity, with the DisplayAlerts, IsInteractive, IsVisible and WaitForReady properties](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/New%20Settings.png)

- _DisplayAlerts_: whether Excel shows alerts and messages, such as overwrite confirmations; cleared by default
- _IsInteractive_: whether Excel accepts keyboard and mouse input; checked by default; when cleared, Excel blocks all input except input to windows opened by your code
- _IsVisible_: whether the Excel window is visible; checked by default
- _WaitForReady_: how many seconds to wait for Excel to be ready, "120" by default; if Excel is not ready in time, the activity fails

When the _Do_ body ends, VisualCron releases its connection to Excel but does not close Excel. Add a _Quit Excel_ activity to close it.

---

### Attach to Excel

Attaches to an Excel application that is already running in the session, and makes it the one the child Excel activities in its _Do_ body work on. It has the same properties as _New Excel_, and applies them to the running Excel when it attaches. If no Excel is running, the activity fails.

If more than one Excel application is running in the session, Windows decides which one Attach to Excel uses. Keep only one Excel running when a sequence attaches to it.

Use Attach to Excel to return to a workbook that was opened earlier in the Task, for example to write to an exception log from inside a loop. See [Data Processing & Logging](../data-processing-logging).

---

### Quit Excel

Quits the Excel application.

![The Quit Excel activity](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/Quit.png)

This activity must be inside a parent Excel activity, either _New Excel_ or _Attach to Excel_.

:::warning

With _DisplayAlerts_ cleared, which is the default, Quit Excel closes every open workbook without saving it. Inside _Attach to Excel_ it quits the Excel that was already running, including workbooks a person has open. Save first with _Save Workbook_ or _Save as Workbook_.

:::

![A Quit Excel activity inside the Do body of a New Excel activity](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/Quit%20Excel.png)

---

### Set Excel Visibility

Shows or hides the Excel application.

![The Set Excel Visibility activity, with the Is Visible check box](../../../../../../../static/img/RPA/Robot%20Tasks/Excel/Set.png)

- _Is Visible_: check to show Excel, clear to hide it

---

### Set Excel Interactivity

Sets whether Excel accepts keyboard and mouse input. When this is cleared, Excel blocks all input except input to windows opened by your code.

- _Is Interactive_: check to accept input, clear to block it

---

### Set Display Alerts

Sets whether Excel shows alerts and messages, such as overwrite confirmations.

- _Display alerts_: check to show alerts, clear to suppress them

---

### Set Full Screen Mode

Turns Excel's full screen mode on or off.

- _Full screen_: check for full screen mode, clear for the normal window

---

### Tips

- _DisplayAlerts_ is cleared by default, so Excel does not stop an unattended Job with a confirmation such as "a file with this name already exists". The other side of this is that Excel then takes the default answer without asking: a _Save as Workbook_ to an existing path replaces that file
- Always end an Excel workflow with _Close Workbook_ followed by _Quit Excel_. Excel processes left running accumulate in the session and eventually use up its memory
- Put the _Quit Excel_ activity in the _Finally_ block of a [Try Catch](error-handling) activity so that Excel is closed even when the workflow fails partway through
- Clear _IsVisible_ for Jobs that run unattended, so that someone using the session cannot interfere with Excel
- Increase _WaitForReady_ on a busy machine. Excel can take several seconds to become responsive after it starts
