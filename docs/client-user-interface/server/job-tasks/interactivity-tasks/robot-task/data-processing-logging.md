---
sidebar_label: 'Data Processing & Logging'
hide_title: 'true'
---

## Data Processing & Logging

This page describes two logs to plan from the start when a Robot Task loops through a data file or a list of records:

- **Exception logging**: lists the records that could not be processed, so that they can be reviewed and corrected
- **Processing status logging**: tracks which records completed, so that you know exactly where things stand if a run fails partway through

With both in place, the process never has to stop on a single bad record, and you always know what was and was not processed.

---

### Exception logging

An exception log captures the records that fail or contain invalid data during the loop, instead of letting the process stop.

**General approach:**

1. **Create an exceptions workbook at the start of the Task**
   - Use a _New Excel_ activity to start Excel
   - Inside its _Do_ body, use a _Create Workbook_ activity to create a new workbook
   - Use _Set Cell value_ activities to write the column headers to the first row

2. **Inside the loop, put the error-prone steps in an If activity**
   - The If activity acts as the catch: it tests whether the data is valid or an error condition exists
   - In the _Then_ or _Else_ body, whichever represents the error:
     - Use an _Attach to Excel_ activity to return to the exceptions workbook
     - Use _Set Cell value_ activities to write the record's data and the error details to the next row
     - Use a _Continue Loop_ activity as the last step of the body; it skips the rest of the current iteration and moves on to the next record

3. **At the end of the Task, save and close the exceptions workbook**
   - Use an _Attach to Excel_ activity
   - Use a _Save as Workbook_ activity to save the workbook to a file
   - Use a _Close Workbook_ activity
   - Use a _Quit Excel_ activity

:::tip

The _Continue Loop_ activity is what makes exception handling work in a loop. It lets the process skip a problem record, log it and keep going, instead of stopping or retrying the same record.

:::

See [Excel](activities/excel), [Excel Workbook](activities/excel-workbook), [Excel Cell](activities/excel-cell), [Conditions](activities/conditions) and [Loops](activities/loops) for the activities used.

---

### Processing status logging

A status log tracks which records have been fully processed. If the Job fails partway through, you can see exactly which records completed and which did not.

**General approach:**

1. **Add a Status column to the List Variable after loading the data file**
   - After loading the data file as a List Variable, use a _Column - Create_ activity to add a new column, for example `Status`, to the list

2. **At the end of the loop body, mark the record as processed**
   - Use a _List - Set value_ activity to write a value such as `Processed` to the Status column of the current row
   - Because this is the last step of the loop body, a record is marked as processed only if every earlier step of the iteration completed

3. **Save the list regularly**
   - Use a _List - Save_ activity at key points, at the end of each iteration or at the end of the Task, to write the list, including the Status column, to a file
   - This gives you a lasting record of what was processed even if the Task fails before it completes

See [List Variable](activities/list-variable) for these activities.

---

### Combining both approaches

Used together, the two logs give you complete coverage:

- The **exception log** tells you which records had bad data or caused errors
- The **status log** tells you which records ran to completion

Records that appear in neither log after a failure show where the process stopped, and where to resume.
