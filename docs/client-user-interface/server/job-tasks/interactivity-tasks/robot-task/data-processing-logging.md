---
sidebar_label: 'Data Processing & Logging'
hide_title: 'true'
---

## Data Processing & Logging

When building a Robot Task that loops through a data file or list of records, two types of logging should be planned from the start:

- **Exception logging** — records that could not be processed so they can be reviewed and corrected
- **Processing status logging** — tracks which records completed successfully so you know exactly where things stand if a failure occurs mid-run

Planning for both means the process never has to stop on a single bad record, and you always have a clear picture of what was and wasn't processed.

---

### Exception Logging

An exception log captures records that fail or contain invalid data during the loop, rather than letting the process halt entirely.

**General approach:**

1. **Create an exceptions Excel workbook at the start of the task**
   - Use a **New Excel** action to open the Excel application
   - Use an **Attach to Excel** action to set the context for subsequent Excel actions
   - Use a **Create Workbook** action to create a new workbook
   - Use **Set Cell Value** actions to write your column headers to the first row

2. **Inside the loop, wrap error-prone steps in an If statement**
   - The If statement acts as a catch — evaluate whether the data is valid or whether an error condition exists
   - In the **Then** or **Else** block (whichever represents the error condition):
     - Use an **Attach to Excel** action to reconnect to the exceptions workbook
     - Use **Set Cell Value** actions to write the record's data and error details to the next row
     - Use a **Continue Loop** action as the last step in the block — this skips the rest of the current iteration and moves to the next record without stopping the process

3. **At the end of the task, save and close the exceptions workbook**
   - Use an **Attach to Excel** action
   - Use a **Save as Workbook** action to save to a file path or clipboard
   - Use a **Close Workbook** action
   - Use a **Quit Excel** action

> The **Continue Loop** action is what makes exception handling work cleanly in a loop. It allows the process to skip a problem record, log it, and keep moving — rather than stopping entirely or retrying the same record.

---

### Processing Status Logging

A status log tracks which records have been fully processed. If the job fails partway through, you can see exactly which records completed and which did not.

**General approach:**

1. **Add a Status column to your List Variable after loading the data file**
   - After loading the data file as a List Variable, use a **Column - Create** action to append a new column (e.g., `Status`) to the list

2. **At the end of the loop body, mark the record as processed**
   - Use a **List - Set Value** action to write a value like `Processed` to the Status column for the current row
   - Because this is the last step in the loop, a record only gets marked as processed if every previous step in the iteration completed successfully

3. **Save the list regularly**
   - Use a **List - Save** action at key points (end of each iteration, or at the end of the task) to write the list — including the Status column — to a file or clipboard
   - This gives you a persistent record of what was processed even if the task fails before completing

---

### Combining Both Approaches

Using both logs together gives you complete coverage:

- The **exception log** tells you which records had bad data or triggered errors
- The **status log** tells you which records ran to completion

Records that appear in neither log after a failure indicate where the process stopped unexpectedly and can be used to determine where to resume.
