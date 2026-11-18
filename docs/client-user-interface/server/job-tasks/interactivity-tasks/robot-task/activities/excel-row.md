---
sidebar_label: 'Excel Row'
hide_title: 'true'
---

## Robot Task Activities - Excel Row

The Excel Row activities select, set, insert, delete, copy and merge whole rows on the active worksheet.

![The Excel Row category in the activity list, from Select Row to Unmerge Rows](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Row/Row.png)

All activities in this category must be inside a _New Excel_ or _Attach to Excel_ container activity. See [Excel](excel). Variables are resolved in every field.

:::warning

With _DisplayAlerts_ cleared on the parent container, which is the default, Excel deletes and overwrites without asking. Save the workbook before you change its structure.

:::

---

### Select Row

Selects the row.

![The Select Row activity, with the Click to select Excel element link and the Row field](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Row/Select.png)

- _Row_: the row number or range of rows, for example `2` or `1:5`

---

### Set Row value

Writes a value to every cell of the row.

![The Set Row value activity, with the Row and Value fields](../../../../../../../static/img/RPA/Robot%20Tasks/Excel%20Row/Set.png)

- _Row_: the row number or range of rows, for example `2` or `1:5`
- _Value_: the value written to every cell of the row, across to the last column of the worksheet

---

### Clear Row

Clears the row: its values, formulas and formatting. Same field as _Select Row_.

---

### Delete Row

Deletes the row. Same field as _Select Row_.

The difference from _Clear Row_ is that Delete Row removes the row and shifts the rows below it up, whereas Clear Row empties the row and leaves the layout unchanged.

---

### Insert Row

Inserts a row at the given row number, and shifts the existing rows down. Same field as _Select Row_.

---

### Copy Row

Copies the row to another row.

- _Source_: the row number or range of rows to copy, for example `1` or `1:2`
- _Destination_: the row number or range of rows the source is copied to, for example `2` or `4:5`; what was there is overwritten

---

### Cut Row

Moves the row to another row. Same fields as _Copy Row_.

---

### Merge Rows

Merges all rows from the _Source_ row to the _Destination_ row. Same fields as _Copy Row_.

---

### Unmerge Rows

Splits merged cells in the row back into separate cells. Same field as _Select Row_.

---

### Tips

- Deleting rows inside a loop shifts every later row up, so an index captured before the delete no longer points at the record you expect. Either work from the last row upward, or mark rows and delete them in a separate pass
- _Clear Row_ removes formatting as well as values
- Use a range such as `1:5` in _Set Row value_ to write the same value across several rows in one activity
- Use _Insert Row_ at row `1` to add a header row to a sheet that was built without one
- To write different values to the cells of a row, use [Excel Cell](excel-cell) _Set Cell value_ activities. _Set Row value_ writes one value across the whole row
