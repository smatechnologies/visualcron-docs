---
sidebar_label: 'List Variable'
hide_title: 'true'
---

## Robot Task Activities - List Variable

The List Variable activities create, load, change and save List Variables, which are User Variables that hold rows and columns.

A List Variable created by these activities appears with the User Variables in the Variables window. List Variables are the usual way a Robot Task processes a data file: load the file into a list, loop through the rows with a [For Each](loops) loop, and write the results back into the list.

![The List Variable category in the activity list, with the List, Column and Row activities](../../../../../../../static/img/RPA/Robot%20Tasks/List/List.png)

Most of these activities are set up in a settings window: click _Click to open settings_ on the activity. Several activities write their outcome to a _Result_ property in the Properties pane. The value is an RPA variable, available while the Robot Task runs, that later activities read as `{RPA(VariableName)}`.

Row numbers start at 1. An activity fails if the list or column it names does not exist, if a row number is out of range, or if the list or column it would create already exists, unless the activity says otherwise below.

---

### List activities

#### List - Create

Creates a new List Variable with the rows and columns set in the ***Create List*** window. The activity fails if a variable with that name already exists.

![The List Variable Create activity with the Click to open settings link](../../../../../../../static/img/RPA/Robot%20Tasks/List/Variable%20Create.png)

![The Create List window, with the Variable name field, the buttons to add and delete rows and columns and to edit a column, and the list grid](../../../../../../../static/img/RPA/Robot%20Tasks/List/Variable%20Setting.png)

- _Variable name_: the name of the new list
- The row buttons add a row and delete the selected row
- The column buttons add a column, delete the selected column and edit the selected column. Adding or editing a column opens the column settings

Drag a column to change the order of the columns.

**Column settings**

![The Add Column window, with the Name and Variable type fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Add%20Column.png)

- _Name_: the column name
- _Variable type_: the data type of the column, for example "Int32" or "String"

---

#### List - Update

Replaces the content of a List Variable with the rows and columns set in the activity. If the variable does not exist, the activity creates it. The settings are the same as for _List - Create_.

:::warning

List - Update replaces all the rows and columns of an existing list. Rows added to the list since it was created are lost.

:::

---

#### List - Delete

Deletes a List Variable. Choose the list in _Variable name_.

:::warning

List Variables are User Variables, so the deleted list is gone for every Job that uses it. To keep a copy, run _List - Duplicate_ or _List - Save_ first.

:::

![The Delete List window, with the Variable name field](../../../../../../../static/img/RPA/Robot%20Tasks/List/Delete%20List.png)

---

#### List - Clear

Removes the content of a List Variable but keeps the variable. The settings are the same as for _List - Delete_.

---

#### List - Set value

Sets the value of one cell of a List Variable.

![The Set value window, with the List name, Row, Column and Value fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Set%20Value.png)

- _List name_: the list to change
- _Row_: the row number
- _Column_: the column
- _Value_: the value to set. For an integer, double or Boolean column, the activity fails if the value cannot be converted to that type

This is the activity that marks a record as processed inside a loop. Set _Row_ to the loop iteration variable and _Column_ to a status column, and place the activity at the very end of the loop body. See [Data Processing & Logging](../data-processing-logging).

---

#### List - Exists

Checks whether a List Variable exists. The settings are the same as for _List - Delete_.

- _Result_: in the Properties pane, the name of the RPA variable that receives "True" or "False"

---

#### List - Duplicate

Copies a List Variable to a new List Variable.

![The Duplicate List window, with the Source variable name and New variable name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Duplicate.png)

- _Source variable name_: the list to copy
- _New variable name_: the name of the new list

---

#### List - Merge

Merges List Variables into a new List Variable.

![The Source list variables list with two lists checked](../../../../../../../static/img/RPA/Robot%20Tasks/List/Merge.png)

![The Merge List window, with the Source list variables and New variable name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Merge%20List.png)

- _Source list variables_: check the lists to merge
- _New variable name_: the name of the new list that receives the merged rows

---

#### List - Rename

Renames a List Variable.

![The Rename List window, with the Source variable name and New variable name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Rename.png)

- _Source variable name_: the list to rename
- _New variable name_: the new name

---

#### List - Reverse

Reverses the order of the rows of a List Variable.

![The Reverse List window, with the Variable name field](../../../../../../../static/img/RPA/Robot%20Tasks/List/Reverse.png)

- _Variable name_: choose a list or type its name. Accepts variables

---

#### List - Shuffle

Puts the rows of a List Variable in random order. The settings are the same as for _List - Reverse_.

---

#### List - Sort

Sorts the rows of a List Variable by one column.

![The Sort List window, with the Variable name, By column and Sort direction fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Sort.png)

- _Variable name_: choose a list or type its name
- _By column_: the column to sort by
- _Sort direction_: "Asc" or "Desc"

---

#### List - Subtract

Creates a new List Variable from the rows of the first list, without the rows that are also in the second list. A row that appears more than once in the first list appears once in the result.

![The Subtract List window, with the First list variable, Second list variable and Result variable name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Subtract.png)

- _First list variable_: choose a list or type its name
- _Second list variable_: choose the list whose rows are taken away
- _Result variable name_: the name of the new list. The activity fails if it already exists

---

#### List - Distinct

Removes duplicate rows from a List Variable.

![The Distinct List window, with the Variable name and Column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Distinct.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column whose values must be unique. When it is empty, only rows that are the same in every column are removed

When _Column name_ is set, only the first row for each value of that column is kept.

:::warning

The column name must match exactly, including case. If no column has that name, the activity does not fail: it keeps only the first row of the list. Run _List - Duplicate_ first if the original rows are needed.

:::

---

#### List - Save

Saves a List Variable to a file or to the clipboard as delimited text.

![The Save List window, with the Variable name, Include column names, Field separator, Text qualifier, Line break, Save to and File path fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Save.png)

- _Variable name_: choose a list or type its name
- _Include column names_: write the column names as the first line
- _Field separator_: the character between columns, for example "Tab" or "Comma"
- _Text qualifier_: the character around values
- _Line break_: the line break to write, for example "CrLf"
- _Save to_: "File", to write to _File path_, or "Clipboard"
- _File path_: the file the list is written to when _Save to_ is "File". Click _Browse_ to choose it

:::warning

With _Save to_ set to "File", the activity replaces a file that already exists at _File path_ without asking. Include a variable in the path so that each run writes a new file, for example `C:\Testing\RPA\{JOB(Active|Name)}_{DATEFORMAT(yyyy-MM-dd)}.csv`.

:::

---

#### List - Get Info

Gets information about a List Variable and writes it to an RPA variable as text.

![The Get List Info window, with the Variable name, Info type and Column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Get%20List.png)

- _Variable name_: choose a list or type its name
- _Info type_: the information to get:
  - "RowCount": the number of rows
  - "ColumnCount": the number of columns
  - "ColumnType": the data type of the column in _Column name_
- _Column name_: the column, used when _Info type_ is "ColumnType"
- _Result_: in the Properties pane, the name of the RPA variable that receives the information

Read the result in a later activity with `{RPA(VariableName)}`. A common use is setting the end value of a [For](loops) loop from a "RowCount" result. The _For_ loop stops before its _To Y_ value, so add 1 to the row count when the loop starts at 1.

---

#### List - Load

Creates a List Variable from a delimited text file, read as UTF-8. The ***Load List into Variable*** window has these settings:

- _Variable name_: the name of the List Variable to create
- _Recreate if exists_: replace a List Variable with that name if it exists. When cleared, the activity fails if the variable exists
- _File path_: the file to read. Click _Browse_ to choose it
- _Include column names_, _Field separator_ and _Text qualifier_: the format of the file, in the **File format** group. Click _Refresh preview_ to see how the file is read

---

### Column activities

#### Column - Create

Adds a new column to a List Variable.

![The Create Column window, with the List name, Column name and Column type fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Create%20Column.png)

- _List name_: choose a list or type its name
- _Column name_: the name of the new column
- _Column type_: the data type of the column

This is the activity that adds a status column to a loaded data file before it is processed. See [Data Processing & Logging](../data-processing-logging).

---

#### Column - Delete

Deletes a column of a List Variable.

![The Delete Column window, with the Variable name and Column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Delete%20Column.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column to delete

---

#### Column - Duplicate

Copies a column of a List Variable to a new column.

![The Duplicate Column window, with the Variable name, Column name and New column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Duplicate%20Column.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column to copy
- _New column name_: the name of the new column

---

#### Column - Clear

Clears the values of a column of a List Variable.

![The Clear Column window, with the Variable name and Column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Clear%20Column.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column whose values are cleared

---

#### Column - Exists

Checks whether a column exists in a List Variable. The settings window is like the one for _Column - Clear_.

- _Result_: in the Properties pane, the name of the RPA variable that receives "True" or "False"

---

#### Column - Move

Moves a column of a List Variable to a new position.

![The Move Column window, with the Variable name, Column name, Move type, Right of column and Index fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Move%20Column.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column to move
- _Move type_: how the column is moved
  - "Left": to the left of the column in _Left of column_
  - "Right": to the right of the column in _Right of column_
  - "FirstColumn": to the first position
  - "LastColumn": to the last position
  - "Specific": to the position in _Index_
- _Left of column_ or _Right of column_: the column to place it next to, when _Move type_ is "Left" or "Right"
- _Index_: the position to move to, when _Move type_ is "Specific"

![The Move type list, with Left, Right, FirstColumn, LastColumn and Specific](../../../../../../../static/img/RPA/Robot%20Tasks/List/Location.png)

---

#### Column - Rename

Renames a column of a List Variable.

![The Rename Column window, with the Variable name, Column name and New column name fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Rename%20Column.png)

- _Variable name_: choose a list or type its name
- _Column name_: the column to rename
- _New column name_: the new name

---

### Row activities

#### Row - Add

Adds a row at the end of a List Variable.

![The Add Row window, with the Variable name field and a row grid for the values](../../../../../../../static/img/RPA/Robot%20Tasks/List/Add%20Row.png)

- _Variable name_: choose a list or type its name
- _Row_: the values of the new row

---

#### Row - Insert

Inserts a row at a position in a List Variable.

![The Insert Row window, with the Variable name and Row index fields and a row grid for the values](../../../../../../../static/img/RPA/Robot%20Tasks/List/Insert%20Row.png)

- _Variable name_: choose a list or type its name
- _Row index_: the row number to insert at
- _Row_: the values of the new row

---

#### Row - Update

Changes the values of a row of a List Variable.

![The Update Row window, with the Variable name and Row index fields and a row grid for the values](../../../../../../../static/img/RPA/Robot%20Tasks/List/Update%20Row.png)

- _Variable name_: choose a list or type its name
- _Row index_: the row number to change
- _Row_: the new values of the row

---

#### Row - Delete

Deletes a row of a List Variable.

![The Delete Row window, with the Variable name and Row index fields and the rows of the list](../../../../../../../static/img/RPA/Robot%20Tasks/List/Delete%20Row.png)

- _Variable name_: choose a list or type its name
- _Row index_: the row number to delete. Type it, or select the row in _Row_
- _Row_: the rows of the list, to select the row to delete

---

#### Row - Clear

Clears the values of a row of a List Variable. The settings are the same as for _Row - Delete_.

---

#### Row - Move

Moves a row of a List Variable to a new position.

![The Move Row window, with the Variable name, Row index, Move type and Move down to fields](../../../../../../../static/img/RPA/Robot%20Tasks/List/Move%20Row.png)

- _Variable name_: choose a list or type its name
- _Row index_: the row number to move
- _Move type_: how the row is moved
  - "Up": up by the number in _Move up to_
  - "Down": down by the number in _Move down to_
  - "FirstRow": to the first position
  - "LastRow": to the last position
  - "Specific": to the row number in _Move to index_
- _Move up to_ or _Move down to_: the number of positions to move, when _Move type_ is "Up" or "Down"
- _Move to index_: the row number to move to, when _Move type_ is "Specific"

![The Move type list, with Up, Down, FirstRow, LastRow and Specific](../../../../../../../static/img/RPA/Robot%20Tasks/List/Location%20Row.png)

---

### Reading a cell from a List Variable

Outside these activities, a cell is read from a List Variable with the `USERVAR` variable function and its `GetCell` operation:

```text
{USERVAR(ListName|GetCell|RowNumber|ColumnNameOrNumber|IncludeColumns)}
```

Combined with the loop iteration variable, this reads the cell of the record being processed:

```text
{USERVAR(lvDateReformat|GetCell|{RPALOOP(a381|Iterations)}|Date|false)}
```

Variable functions can be nested, so the value can be changed in the same expression. Here the cell is trimmed of surrounding spaces:

```text
{STRING(Trim|{USERVAR(lvDateReformat|GetCell|{RPALOOP(a381|Iterations)}|Date|false)})}
```

The Variables window lists the other List Variable operations, such as row and column counts, minimum and maximum values, and duplicate checks.

---

### Tips

- Name List Variables with an `lv` prefix, for example `lvCustomerRecords`. A Task with dozens of variables is much easier to work with when the kind of variable is visible in the name
- Add a status column with _Column - Create_ right after loading a data file, and mark rows with _List - Set value_ at the end of each loop iteration. That records which rows completed if the Task fails partway through
- Run _List - Save_ at every point where an error can be raised, not only at the end of the Task, so that the status column survives a failure
- Use _List - Get Info_ with "RowCount" to set a [For](loops) loop's end value instead of typing the number of records, and add 1 when the loop starts at 1
- _List - Distinct_ with _Column name_ empty removes rows that are the same in every column. Set a column name to remove duplicates by a key such as an account number
- Use _List - Duplicate_ before a change such as _List - Distinct_ or _List - Sort_ if the original order is needed later
