---
sidebar_label: 'Excel Column'
hide_title: 'true'
---

## Robot Task Activities - Excel Column

The Excel Column activities select, set, insert, delete, copy and merge whole columns on the active worksheet.

![The Excel Column category in the activity list, from Select Column to Unmerge Columns](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Column/Column.png)

All activities in this category must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel). Variables are resolved in every field.

:::warning

With _DisplayAlerts_ cleared on the parent container, which is the default, Excel deletes and overwrites without asking. Save the workbook before you change its structure.

:::

---

### Select Column

Selects the column.

![The Select Column activity, with the Click to select Excel element link and the Column field](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Column/Select.png)

- _Column_: the column or range of columns, for example `B` or `A:C`

---

### Set Column value

Writes a value to every cell of the column.

![The Set Column value activity, with the Column and Value fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Column/Set.png)

- _Column_: the column or range of columns
- _Value_: the value written to every cell of the column, down to the last row of the worksheet

---

### Clear Column

Clears the column: its values, formulas and formatting. Same field as _Select Column_.

---

### Delete Column

Deletes the column. Same field as _Select Column_.

The difference from _Clear Column_ is that Delete Column removes the column and shifts the columns to its right to the left, whereas Clear Column empties the column and leaves the layout unchanged.

---

### Insert Column

Inserts a column at the given column, and shifts the existing columns to the right. Same field as _Select Column_.

---

### Copy Column

Copies the column to another column.

![The Copy Column activity, with the Source and Destination fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Column/Copy.png)

- _Source_: the column or range of columns to copy
- _Destination_: the column or range of columns the source is copied to; what was there is overwritten

---

### Cut Column

Moves the column to another column. Same fields as _Copy Column_.

---

### Merge Columns

Merges all columns from the _Source_ column to the _Destination_ column. Same fields as _Copy Column_.

---

### Unmerge Columns

Splits merged cells in the column back into separate cells. Same field as _Select Column_.

---

### Tips

- Deleting a column shifts every column to its right, so any address hard-coded elsewhere in the Task then points at the wrong data. Prefer _Clear Column_ unless the column really must be removed
- _Clear Column_ removes formatting as well as values
- Use _Insert Column_ to add a status or notes column to a sheet exported from another system, before writing to it in a loop
- Use a range such as `A:C` in _Set Column value_ to apply the same value across several columns in one activity
- To add a column to a [List Variable](list-variable) rather than to a worksheet, use the _Column - Create_ activity of the List Variable category
