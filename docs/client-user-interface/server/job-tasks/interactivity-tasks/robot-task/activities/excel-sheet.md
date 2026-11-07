---
sidebar_label: 'Excel Sheet'
hide_title: 'true'
---

## Robot Task Activities - Excel Sheet

The Excel Sheet activities create, select, rename, protect, move and copy worksheets in the active workbook.

![The Excel Sheet category in the activity list, from Activate Sheet to Set page orientation](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Sheet.png)

All activities in this category must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel). Sheet names are matched exactly, and an activity fails if the sheet it names is not found. Variables are resolved in every field.

:::warning

With _DisplayAlerts_ cleared on the parent container, which is the default, Excel deletes and overwrites without asking. Save the workbook before you change its structure.

:::

**Selecting a sheet:** click the _Click to select Excel element_ link, then select the sheet, hold `CTRL` and click any cell in the sheet. The sheet name is filled in automatically. Excel must already be running.

![The prompt shown in Excel while picking a sheet, asking to select the sheet and press CTRL while clicking](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Sample.png)

---

### Activate Sheet

Makes the sheet the active sheet.

![The Activate Sheet activity, with the Click to select Excel element link and the Sheet field](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Activate.png)

- _Sheet_: the name of the worksheet

---

### Select all Sheets

Selects all sheets in the active workbook.

---

### Select Sheet

Selects the sheet. Same field as _Activate Sheet_.

---

### Create Sheet

Creates a sheet with the name in _Sheet_, after the active sheet. Fails if a sheet with that name already exists.

---

### Delete Sheet

Deletes the sheet. Same field as _Activate Sheet_.

---

### Hide Sheet

Hides the sheet. Same field as _Activate Sheet_.

---

### Show Sheet

Shows a hidden sheet. Same field as _Activate Sheet_.

---

### Copy Sheet

Copies the sheet.

![The Copy Sheet activity, with the Source and Destination fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Copy.png)

- _Source_: the name of the worksheet to copy
- _Destination_: the name of the new worksheet, which is placed right after the source; fails if a sheet with that name already exists

If _Destination_ is empty, Excel copies the sheet into a new workbook instead.

---

### Move Sheet

Moves the sheet to a new position.

![The Move Sheet activity, with the Sheet and After sheet fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Move.png)

- _Sheet_: the name of the worksheet to move
- _After sheet_: the name of the worksheet after which it is placed

If _After sheet_ is empty, Excel moves the sheet into a new workbook instead.

---

### Rename Sheet

Renames the sheet.

![The Rename Sheet activity, with the Sheet and New name fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Rename.png)

- _Sheet_: the name of the worksheet to rename
- _New name_: the new name; fails if it is empty or a sheet with that name already exists

---

### Protect Sheet

Protects the sheet against changes, optionally with a password.

![The Protect Sheet activity, with the Sheet and Password fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Protect.png)

- _Sheet_: the name of the worksheet to protect
- _Password_: the password needed to remove the protection; leave it empty to protect without a password

---

### Unprotect Sheet

Removes the protection from the sheet.

- _Sheet_: the name of the worksheet to unprotect
- _Password_: the password the sheet was protected with

---

### Set page orientation

Sets the print page orientation of the sheet.

![The Set page orientation activity, with the Sheet and Orientation fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Sheet/Set.png)

- _Sheet_: the name of the worksheet
- _Orientation_: "Portrait" or "Landscape"

---

### Tips

- Add an _Activate Sheet_ activity before a group of [Excel Cell](excel-cell), [Excel Row](excel-row) or [Excel Column](excel-column) activities. Those activities act on the active sheet, so being explicit avoids writing to whichever sheet happened to be active
- Use a Variable in the _New name_ of a _Rename Sheet_ activity to stamp sheets with a date or a record identifier
- _Unprotect Sheet_ must run before any activity that writes to a protected sheet, otherwise the write fails
- Use _Copy Sheet_ to duplicate a formatted template sheet rather than rebuilding headers and formatting with individual _Set Cell value_ activities
