---
sidebar_label: 'Excel Cell'
hide_title: 'true'
---

## Robot Task Activities - Excel Cell

The Excel Cell activities read, write, copy, merge and clear cells on the active worksheet.

![The Excel Cell category in the activity list, from Activate Cell to Paste to Cell](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Cell/Excel%20Cell.png)

All activities in this category must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel). They act on the active worksheet, so use an [Excel Sheet](excel-sheet) _Activate Sheet_ activity first when the workbook has more than one sheet.

_Address_ fields take a cell or a range of cells, such as `A4` or `A1:B1`. See the [Excel Range reference](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel._application.range). Variables are resolved in every field.

:::warning

With _DisplayAlerts_ cleared on the parent container, which is the default, Excel deletes and overwrites without asking. Save the workbook before you change its structure.

:::

**Selecting a cell:** click the _Click to select Excel element_ link to pick a cell in Excel and fill in the address automatically. Excel must already be running.

---

### Activate Cell

Activates the cell.

![The Activate Cell activity, with the Click to select Excel element link and the Address field](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Cell/Activate.png)

- _Address_: the cell or range of cells

---

### Select Address

Selects the cell or range. Same field as _Activate Cell_.

---

### Select all Cells

Selects all cells in the active worksheet.

---

### Set Cell value

Writes a value to the cell or range.

![The Set Cell value activity, with the Address and Value fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Cell/Set.png)

- _Address_: the cell or range of cells
- _Value_: the value written to the cell, or to every cell of the range

Both fields accept Variables, so the target address and the value can both be set at runtime. This is how a loop writes each record to the next free row.

---

### Get Cell value

Reads the value of the cell or range and saves it to a Job or User Variable.

![The Get Cell value activity, with the Address, Variable type and Variable fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Cell/Get.png)

- _Address_: the cell or range of cells
- _Variable type_: "Job" or "User"
- _Variable_: the name of the Variable that receives the value

For a range, the values are returned as one text value: the cells of a row are separated by tab characters, and each row is on a new line.

---

### Clear Cell

Clears the cell or range: its value, its formula and its formatting. Same field as _Activate Cell_.

---

### Delete Cell

Deletes the cell or range, and shifts the surrounding cells to fill the gap. Same field as _Activate Cell_.

The difference from _Clear Cell_ is that Delete Cell removes the cells and moves the cells around them, whereas Clear Cell empties the cells and leaves the others where they are.

---

### Insert Cell

Inserts a cell or range at the address, and shifts the existing cells to make room. Same field as _Activate Cell_.

---

### Copy Cell

Copies the cell or range to another place.

![The Copy Cell activity, with the Source and Destination fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Cell/Copy.png)

- _Source_: the cell or range to copy
- _Destination_: the cell or range the source is copied to; what was there is overwritten

---

### Cut Cell

Moves the cell or range to another place. Same fields as _Copy Cell_.

---

### Merge Cells

Merges the cells of the block that runs from the _Source_ cell to the _Destination_ cell into one cell. Same fields as _Copy Cell_.

---

### Unmerge Cells

Splits a merged cell back into separate cells.

- _Source_: the merged cell or range

---

### Paste to Cell

Pastes the clipboard content at the cell or range. Same field as _Activate Cell_.

This activity pastes what is on the Windows clipboard, so it pairs with an earlier copy, such as a copy made in Excel. Test it with your data before relying on it for text placed on the clipboard by the [Clipboard](clipboard) _Set Clipboard_ activity.

---

### Tips

- Build the _Address_ from a loop iteration variable to write successive rows, for example `A{RPALOOP(a381|Iterations)}`. See [Loops](loops)
- Write the header row with individual _Set Cell value_ activities at the start of the Task, before the loop begins, so that the exception log has column names. See [Data Processing & Logging](../data-processing-logging)
- Write a range in one _Set Cell value_ activity where the value is the same across the range, rather than one activity per cell
- To put a range into separate Variables, read the cells one at a time with _Get Cell value_
- _Clear Cell_ also removes formatting. To reset a formatted template, write empty values with _Set Cell value_ instead, and avoid _Delete Cell_, which moves the surrounding cells and breaks the layout
