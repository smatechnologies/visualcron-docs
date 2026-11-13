---
sidebar_label: 'Robot Task Activities'
hide_title: 'true'
---

## Robot Task Activities

The Robot Task activities are the building blocks of a Robot Task sequence: each activity performs one operation, such as clicking an element, reading a file or setting a cell value in Excel.

To add an activity, drag it from the activity list into the Sequence of the Robot Task. The activity list groups the activities into categories, and the pages below describe the activities in each category and their settings. For the Robot Task itself, see [Task Interactivity - Robot Task](../overview).

### Flow control

| Category | Purpose |
|---|---|
| [Conditions](conditions) | Branch the sequence with If and Switch |
| [Loops](loops) | Repeat activities with While, Do While, For and For Each, jump with Flow, Label and Go to, and control iteration with End Loop and Continue Loop |
| [Error Handling](error-handling) | Catch, throw and rethrow exceptions |
| [Other](other) | Assign, Sequence and Wait |

### UI automation

| Category | Purpose |
|---|---|
| [Mouse](mouse) | Click, double-click, move the mouse and press or release mouse buttons |
| [Keyboard](keyboard) | Send key events and key presses |
| [Text](text) | Type text into a window or element |
| [Controls](controls) | Interact with UI elements through automation patterns |
| [Windows](windows) | Attach to, show, hide, close, maximize, minimize, restore, move and resize windows |
| [Image](image) | Capture screenshots of screens, windows and elements |
| [OCR](ocr) | Find and read on-screen text that is not exposed as a UI element |

### Web automation

| Category | Purpose |
|---|---|
| [Web Macro](web-macro) | Drive a web browser: navigate, click, populate fields, extract data, and download and upload files |
| [Element Path](element-path) | Reference for the three ways to identify an HTML element |

### Excel

| Category | Purpose |
|---|---|
| [Excel](excel) | Start, attach to and quit the Excel application |
| [Excel Workbook](excel-workbook) | Create, open, save, protect and inspect workbooks |
| [Excel Sheet](excel-sheet) | Create, select, rename, protect and reorder worksheets |
| [Excel Cell](excel-cell) | Read, write, copy, merge and clear cells |
| [Excel Row](excel-row) | Select, set, insert, delete and copy rows |
| [Excel Column](excel-column) | Select, set, insert, delete and copy columns |
| [Excel Macros](excel-macros) | Run a macro in the open workbook |

### Data and system

| Category | Purpose |
|---|---|
| [File](file) | Read, write, copy, move, archive and wait for files |
| [Folder](folder) | Create, copy, empty, enumerate and wait for folders |
| [List Variable](list-variable) | Build and change List Variables, including their rows and columns |
| [Variables](variables) | Set the value of a Job Variable or User Variable |
| [Clipboard](clipboard) | Set, get and clear the Windows clipboard |
| [Processes](process) | Start and close processes |

The activity list also has Outlook activities (start and close Outlook, and get, send, forward, reply to, save and display messages), a User input activity that asks for text while the Robot Task runs, and web browser extension activities that work with a third-party web browser. These activities are not described on these pages.

### Properties every activity has

Each activity has these properties in the Properties pane, in addition to its own settings:

- _Display name_: the name shown on the activity in the sequence and in the Task output. Give each activity a name that says what it does, such as `Populate The Address Field`, so a long sequence stays readable
- _Error settings_: rules that raise or ignore an error from this activity. The rules have no effect on the condition, loop, Flow, Label, Go to and Wait activities, which show the property but do not use it. See [Error Handling](error-handling)
- _Wait before_ and _Wait after_: the wait in milliseconds before and after the activity runs. When empty, the playback speed from the Robot Task settings is used. Not every activity has these two properties

### Output and errors

While a Robot Task runs, each activity writes its start, its result and its waits to the Task output.

- An activity that fails raises an error. Unless a [Try Catch](error-handling) activity or the activity's _Error settings_ handles the error, the sequence stops and the Task fails
- When _Error settings_ ignores an error, the sequence continues past the failing activity, the error is not written to standard error, and unless something else fails, the Task reports success
- Some activities write a problem to standard error and carry on. The sequence continues, and the Task fails when the sequence ends

### RPA result variables

Several activities write their outcome to a _Result_ property rather than to a Job Variable or User Variable. The value is an RPA variable that exists only while the Robot Task runs, and later activities read it with:

```text
{RPA(VariableName)}
```

For example, a _Folder Exists_ activity with its Result set to `Exists` is read in a later If activity as `{RPA(Exists)}`, which resolves to "True" or "False". Each category page says which of its activities have a Result property. To keep a value for a later Task in the Job, copy it into a Job Variable or User Variable with the [Set variable](variables) activity.
