---
sidebar_label: 'Excel Workbook'
hide_title: 'true'
---

## Robot Task Activities - Excel Workbook

The Excel Workbook activities create, open, save, close, protect and inspect Excel workbooks.

![The Excel Workbook category in the activity list, from Activate Workbook to Get Info Workbook](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Workbook.png)

All activities in this category must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel). A _Workbook_ field takes the name of an open workbook, such as `Workbook1.xlsx`, matched exactly; an activity fails if that workbook is not open. Variables are resolved in every field.

**Selecting a workbook:** on activities that take a workbook name, click the _Click to select Excel element_ link, then select the workbook, hold `CTRL` and click. The workbook name is filled in automatically. Excel must already be running.

![The prompt shown in Excel while picking a workbook, asking to select the workbook and press CTRL while clicking](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Sample.png)

---

### Activate Workbook

Makes the workbook the active workbook.

![The Activate Workbook activity, with the Click to select Excel element link, a preview of the workbook and the Workbook field](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Activate.png)

- _Workbook_: the name of the open workbook

---

### Open Workbook

Opens a workbook file.

- _File name_: the full path of the workbook file

---

### Close Workbook

Closes the workbook. Same field as _Activate Workbook_.

:::warning

Close Workbook does not save the workbook. With _DisplayAlerts_ cleared on the parent container, which is the default, Excel does not ask about unsaved changes, and they are lost. Save the workbook first with _Save Workbook_ or _Save as Workbook_.

:::

---

### Close Workbooks

Closes all workbooks in the Excel application, without saving them, in the same way as _Close Workbook_.

:::warning

Unsaved changes in every workbook of that Excel application are lost without a prompt. Inside _Attach to Excel_, this includes workbooks that someone else opened in the session.

:::

---

### Create Workbook

Creates a new, empty workbook, which becomes the active workbook.

---

### Save Workbook

Saves the workbook to its current file. Same field as _Activate Workbook_.

---

### Save as Workbook

Saves the workbook to a new file. The workbook then belongs to the new file.

![The Save as Workbook activity, with the Workbook and File name fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Save.png)

- _Workbook_: the name of the open workbook to save
- _File name_: the full path of the new file
- _File format_: "Default" (Excel's default save format), "CSV", "XLS" or "XLSX"

:::warning

With _DisplayAlerts_ cleared on the parent container, which is the default, Excel does not ask before it replaces an existing file at _File name_. Use a unique file name for each run, or check first with a [File](file) _File Exists_ activity.

:::

---

### Save copy as Workbook

Saves a copy of the workbook to a file. Same _Workbook_ and _File name_ fields as _Save as Workbook_, without _File format_.

The difference from _Save as Workbook_ is that the open workbook stays connected to its original file, so later saves go to the original path rather than to the copy.

---

### Protect Workbook

Protects the structure of the workbook, so that sheets cannot be added, deleted, moved or renamed without the password.

![The Protect Workbook activity, with the Workbook and Password fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Protect.png)

- _Workbook_: the name of the open workbook to protect
- _Password_: the password needed to remove the protection

Protect Workbook does not encrypt the file or set a password to open it, and it does not protect the cells. Use [Excel Sheet](excel-sheet) _Protect Sheet_ to protect cells.

---

### Unprotect Workbook

Removes the protection from the workbook. Same fields as _Protect Workbook_.

---

### Print Workbook

Prints the workbook on the default printer of the user the Robot Task runs as. Same field as _Activate Workbook_.

---

### Zoom Workbook

Sets the zoom level of the workbook's windows.

![The Zoom Workbook activity, with the Workbook and Zoom fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Zoom.png)

- _Workbook_: the name of the open workbook
- _Zoom_: the zoom percentage

---

### Freeze Workbook Panes

Freezes the panes of the workbook's windows. Same field as _Activate Workbook_.

---

### Unfreeze Workbook Panes

Unfreezes the panes of the workbook's windows. Same field as _Activate Workbook_.

---

### Get Info Workbook

Reads one item of information about the workbook and saves it to a Job or User Variable. The workbook is activated first.

![The Get Info Workbook activity, with the Workbook, Info, Variable type and Variable fields and the Select button](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Workbook/Get%20Info.png)

- _Workbook_: the name of the open workbook
- _Info_: the name of the item to read; type it, or click _Select_ to choose from the supported names
- _Variable type_: "Job" or "User"
- _Variable_: the name of the Variable that receives the value

The supported names are `WorkbookName`, `Author`, `Title`, `Subject`, `Comments`, `Category`, `Keywords`, `Manager`, `Company`, `HyperlinkBase`, `IsProtected`, `SheetCount`, `ZoomPercentage`, `ActiveSheetName` and `ActiveSheetIndex`, and, for the used range of the active sheet, `RowCount`, `ColumnCount`, `FirstRowNumber`, `LastRowNumber`, `FirstColumnNumber`, `LastColumnNumber`, `FirstColumnLetter` and `LastColumnLetter`. Names must be typed exactly as shown; any other name makes the activity fail. `IsProtected` reports whether the workbook's windows are protected, not its structure.

---

### Tips

- Use a Variable in the _File name_ of a _Save as Workbook_ activity so that each run produces a separate file, for example `C:\Logs\{JOB(Active|Name)}_Exceptions_{DATEFORMAT(yyyy-MM-dd)}.xlsx`
- Follow _Save as Workbook_ with _Close Workbook_ and then _Quit Excel_, so that the file is released and no Excel process is left behind
- Use `LastRowNumber` from _Get Info Workbook_ to find the next free row before you append to a sheet
- _Close Workbooks_ inside a _New Excel_ container is a safe cleanup step. Do not use it inside _Attach to Excel_ unless every open workbook can be discarded, because it closes them all without saving
