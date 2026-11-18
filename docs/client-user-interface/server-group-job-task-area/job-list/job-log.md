---
sidebar_label: 'Job Log'
hide_title: 'true'
---

## Job Log

The ***Log history*** item opens the ***Job history*** window, which lists the stored runs of the selected Job.

1. Select the Job in the Server/Group/Job/Task grid. To see several Jobs together, select them all.
2. Right-click one of the selected Jobs.
3. Click ***Log history***.

For a Job that uses execution distribution, ***Log history*** is a submenu with ***Local execution history*** and ***Distributed execution history***.

The history is read from the log database. How long entries are kept is set in [Settings - Log Settings](../../server/settings-log-settings). Opening the window requires the Read permission for the Job.

![Job right-click menu with the Log history item highlighted](../../../../static/img/Client%20User%20Interface//Toolbar/Job%20Log%20History.png)

![Job history window listing runs with event time, exit code, execution time and result](../../../../static/img/Client%20User%20Interface//Toolbar/Job%20Log%20History%202.png)

The window has these controls:

- _Job_: the Job to show, with a _Filter.._ field to narrow the list
- The two date fields: the start and end of the period to fetch
- ***Get***: fetches the entries for the period. While it runs, the button changes to ***Abort***
- Result filter: "All", "Failed" or "Success"
- ***Filter...***: more filter options for the list
- ***Export..***: exports the listed entries
- _Search in Output field text_: _Output field type_ ("Output", "Output (error)" or "Result") and _Search text_ search the stored output

The grid shows _Event time_, _Exit code_, _Execution time_ and _Result_ for each run. Double-click the _Result_ cell, or the status icon, of a row to see the result.
