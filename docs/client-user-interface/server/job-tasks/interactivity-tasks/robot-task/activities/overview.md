---
sidebar_label: 'Robot Task Activities'
hide_title: 'true'
---

## Robot Task Activities

A Robot Task is built by dragging **activities** from the activity list into the task's Sequence. Each activity performs one well defined operation, such as clicking an element, reading a file, or setting a cell value in Excel.

Activities are organized into categories in the activity list. The pages below describe every activity in each category, along with its settings.

### Flow Control

| Category | Purpose |
|---|---|
| [Conditions](conditions) | Branch the sequence with If and Switch |
| [Loops](loops) | Repeat activities with While, Do While, For, and For Each, and control iteration flow |
| [Error Handling](error-handling) | Catch, throw, and rethrow exceptions |
| [Other](other) | Assign, Sequence, and Wait |

### UI Automation

| Category | Purpose |
|---|---|
| [Mouse](mouse) | Click, double click, move, and press mouse buttons |
| [Keyboard](keyboard) | Send key events and key combinations |
| [Text](text) | Type text into a window or element |
| [Controls](controls) | Interact with UI elements through automation patterns |
| [Windows](windows) | Attach to, show, hide, move, and resize windows |
| [Image](image) | Capture screenshots of screens, windows, and elements |
| [OCR](ocr) | Find and read on screen text that is not exposed as a UI element |

### Web Automation

| Category | Purpose |
|---|---|
| [Web Macro](web-macro) | Drive a web browser: navigate, click, populate fields, extract data, download and upload files |
| [Element Path](element-path) | Reference for the three ways to identify an HTML element |

### Excel

| Category | Purpose |
|---|---|
| [Excel](excel) | Start, attach to, and quit the Excel application |
| [Excel Workbook](excel-workbook) | Create, open, save, protect, and inspect workbooks |
| [Excel Sheet](excel-sheet) | Create, select, rename, protect, and reorder worksheets |
| [Excel Cell](excel-cell) | Read, write, copy, merge, and clear cells |
| [Excel Row](excel-row) | Select, set, insert, delete, and copy rows |
| [Excel Column](excel-column) | Select, set, insert, delete, and copy columns |
| [Excel Macros](excel-macros) | Run a macro in the open workbook |

### Data and System

| Category | Purpose |
|---|---|
| [File](file) | Read, write, copy, move, archive, and wait for files |
| [Folder](folder) | Create, copy, empty, enumerate, and wait for folders |
| [List Variable](list-variable) | Build and manipulate tabular List Variables, including rows and columns |
| [Variables](variables) | Set the value of a Job or User variable |
| [Clipboard](clipboard) | Set, get, and clear the Windows clipboard |
| [Process](process) | Start and close processes |

### RPA Result Variables

Several activities write their outcome to a **Result** property rather than to a Job or User variable. The value is an RPA variable that exists only for the duration of the Robot Task execution, and is referenced in later activities with:

```
{RPA(VariableName)}
```

For example, a **Folder Exists** activity with its Result set to `Exists` is read in a later If activity as `{RPA(Exists)}`, which resolves to `True` or `False`.

Activities that produce a Result variable are noted on each category page.

### Naming Activities

Every activity has a **Display name** property in the Properties pane. Set it on each activity you add so the sequence reads clearly. A name such as `Populate The Address Field` makes a sequence far easier to maintain than a column of activities all named `Populate field`.
