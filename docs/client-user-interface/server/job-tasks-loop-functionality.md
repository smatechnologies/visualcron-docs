---
sidebar_label: 'Loop Functionality'
hide_title: 'true'
---

## Loop Functionality

### Summary

“Loops” are introduced in VisualCron version 6.0.0. Loops let you run several Tasks multiple times in three loop types:
1. For
2. For Each
3. While
 
During a loop you are able to access loop runtime Variables. For example, where you are in the current iteration and all related values.
 
### Architecture

:::warning
Loops run only in Jobs that have *Run Tasks in order* selected (see
[Job - Main Settings](job-main-settings)).
:::

Loops are objects that are stored in a Job. On Job can contain a maximum number of loops equal to the maximum number of Tasks. Loops are defined by a start Task and end Task. Anything in between will be looped in Task order. Loops cannot cross each other - you cannot create a loop in a loop.
 
Task Conditions are checked each time before a Task is run, independent of if Task is in loop or not.
 
### Loop types

There are three different loop types:

*For*

A loop type with and x and y value where x and y are numeric values.

*While*

A loop type that can compare two values according to a specific data type (i.e. string, integer)  and comparison method (i.e. larger        than, contains, equal).

*For each*

A loop type that iterates through an existing y value. A list of some sort.
 
### Working with loops
 
**Loop display**

If one or more Tasks belong to a loop you can see that in the loop column. You will see how the loop stretches over itself or more Tasks.

In the *Loop* column, every loop type is shown with the same blue connector. The screenshot below is
from an earlier version, which showed each loop type in a different color.

![Loop column in a Job's Task list, showing loop connectors next to the Tasks each loop covers](../../../static/img/image00.png)

**Add/Edit loop**

In the Task list, in main window or Task list of add/edit Job you can double click in the “Loop” column in each Task row. This will open up existing or new Loop settings window.

**Add loop option**

![Add Task Loop window, Main settings tab, opened with Add loop on the Job's Tasks tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20Main%20Settings.png)

**Add loop > Main settings**

In the main settings you enter the descriptive name of the Loop. You also set which Task the loop should start and end with.

**Add loop > Loop settings**

In the loop settings you control the loop type by clicking on one of the three radio buttons.
You can click on the Variable button next to each text field to find and insert a Variable that can be used in the field.

![Add Task Loop window, Loop settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20Settings.png)

**For x to y**

Enter two numerical values or Variables that contain numerical values.

![Loop settings tab with For x to y selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20For.png)
 
**While x**

Depending on type comparison you enter different kind of values/Variables.

![Loop settings tab with While x selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20While.png)
 
**For each x in y**

Enter a Variable that contains a list. You may need to alter *Use column*, *Field separator*, *Text qualifier*, *Line break* or *Start row* depending on the format of the Variable list. *Use column* is the number of the column that the x value is taken from; the first column is 0 (the
default). *Start row* is the number of the first row to use (default 1); enter `"2"` to skip one header
row. Rows are counted from 1 and columns from 0. Empty lines in the list are ignored.

![Loop settings tab with For each x in y selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20For%20each%20x%20in%20y.png)

#### Referencing columns in For Each loops

When a For Each loop goes through multi-column data, such as a CSV file, you can read a column of the
current row by number or by name.

By column number (the first column is 0):

```
{LOOP(CurrentValueXArray|0)}    first column
{LOOP(CurrentValueXArray|8)}    ninth column
```

By column name (available in VisualCron 13.3.1 and later):

```
{LOOP(CurrentValueByColumnName|Email)}
{LOOP(CurrentValueByColumnName|CustomerID)}
```

VisualCron uses the row just above *Start row* as the header row. If your data has one header row, set
*Start row* to `"2"`. Column names are not case sensitive.

:::warning
With *Start row* at `"1"` (the default) there is no row above it, so every column-name reference returns
an empty value.
:::

A name reference keeps working when the columns are reordered. A number reference returns whatever column
is now in that position, without an error. These references are equivalent:

| Column number | Column name |
|---|---|
| `{LOOP(CurrentValueXArray\|0)}` | `{LOOP(CurrentValueByColumnName\|CustomerID)}` |
| `{LOOP(CurrentValueXArray\|3)}` | `{LOOP(CurrentValueByColumnName\|Email)}` |
| `{LOOP(CurrentValueXArray\|7)}` | `{LOOP(CurrentValueByColumnName\|Department)}` |

**Sleep/Wait in each iteration**

Sets the wait time between each iteration. This is especially interesting if you are using a While loop because you might want to save resources and not check _all_ the time.
 
**Limitations**

Sets the maximum number of iterations (default 1000).

:::warning
When the loop reaches the limit, it stops: the remaining iterations are not run, an error is logged, and
the Job continues with the Task after the loop. Set the limit higher than the number of iterations you
expect.
:::

**Validate values when saving**

When checked, the loop values are validated when the loop settings are saved.
 
**Add loop > Loop settings > Loop Variables**

Any Variable can be used in the settings of the actual loop to provide dynamic x and y values. Also, a set of dynamic, loop context sensitive Variables exist. You find them in the Variables browser:

![Loop settings tab with the Variables window opened from a Variable button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Loop%20Variables.png)

**Loop Id**

Each loop in a Job has an internal Id.
 
**Loop name**

You are able to set a name of a loop which can be accessed through this Variable.
 
**Loop type**

Returns the loop type: `ForLoop`, `ForEachLoop` or `WhileLoop`.
 
**Preset X value**

The original left hand value that you used in a For or While loop.
 
**Preset Y value**

The original right hand value in For, While or For Each loop.
 
**Current X value**

The value of the position in the loop. This value is interesting when using For or For Each loop.

**Current X line**

The current line of the X value when using a For Each loop.
 
**Current line in X - specify column index**

The value of a column in the current X line, by column number (the first column is 0).
 
**Current line in X - specify column name**

The value of a column in the current X line, by column name, for example
`{LOOP(CurrentValueByColumnName|Email)}`. See
[Referencing columns in For Each loops](#referencing-columns-in-for-each-loops).
 
**Current Y value**

The current right hand value in a For or While loop. It is not used in For Each loops.
 
**Current Y position in list**

A numeric value of the position in the y list. Used when using a For Each loop type.
 
**Y value list**

A list containing all rows in y.
 
**Id of Task that loops starts with**

Task Id for the selected start Task in the loop.
 
**Id of Task that loops ends with**

Task Id for the selected end Task in the loop.
 
**Column position that is used in For Each loop**

The *Use column* number: the column that the x value is taken from in a For Each loop (the first column is
0). To read a column by name, see
[Referencing columns in For Each loops](#referencing-columns-in-for-each-loops).

**Field separator**

The character that is used to separate fields in For Each loop.
 
**Text qualifier**

The surrounding character of each column.
 
**New line character**

The line break character that is used in each column.
 
**Number of loop iterations so far**

Number of loop “laps”/iterations that has been done so far.
 
**Maximum allowed iterations before exiting loop**

A limit that prevents loop for going on forever. Default 1000. This value is showed here.
 
**Deleting a loop**

To delete a loop you open the Add/Edit Job window and go to Tasks tab. Right click/select a Task row that contains a loop and click on Delete loop. This will only delete the related loop - not the Tasks in it.

![Delete loop button on the Job's Tasks tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Loop%20Settings/Delete%20Loop.png)

**Changing Task order**

A change of Task order (clicking up/down in the numeric box in the Task list) affects any existing loop.
 
If a loop covers 3 Tasks and the first Task is moved up it will include any Task that becomes number two in the list.
 
**Deleting Tasks**

If a start or end Task is deleted VisualCron will attempt to shift start or end Task, if loops covers more than one Task. If all Tasks that a loop covers are deleted the loop itself will be deleted.
