---
sidebar_label: 'Task Internal - Report'
hide_title: 'true'
---

## Task Internal - Report

The Report Task creates a report on Jobs, Tasks, logs, Notifications, Connections or the Server, and prints it, saves it as a PDF, HTML or CSV file, or writes it to the Task's output. The settings are on the ***Report*** tab.

***Main settings*** **sub tab**

![Report Task, Main settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/Job%20Report%20setting.png)

**Report type**

Select the report; see [Reports](../../../reports). Defaults to *Job - Overview*. The reports are:

* *Job - Overview*, *Job - List*, *Job - Results*, *Job - Execution*, *Job - ROI*, *Job - Time Distribution*, *Job - Next Execution*
* *Tasks - Overview*
* *Logs - Event log*, *Logs - Server log*, *Logs - Transfer log*
* *Notifications - Overview*
* *Connections - Overview*, *Connections - Executions*
* *Server - Health*, *Server - SLA*, *Server - Computer*, *Server - Overview*, *Server - Optimization*

**Date range**

Select the start and end dates. A new Task uses the last 7 days. The dates are saved with the Task and do not change, so for a range that moves with each run, select *Use Variables to specify a date range*.

**Use Variables to specify a date range**

When selected, the date pickers are unavailable and the ***Date range*** sub tab is shown, with *From* and *To*. Both accept Variables and are required: *From* defaults to `{DATENOWADD(Days|-7|yyyy-MM-dd)}` and *To* to `{DATEFORMAT(yyyy-MM-dd)}`. If a value is not a date when the Task runs, the Task fails.

**Output type**

*To printer* (default), *To PDF file*, *To HTML file*, *To CSV file* or *To output (CSV format)*. The two CSV options are available only for the *Job - List* report. *To output (CSV format)* writes the report to the Task's output, which a later Task can read, for example with `{TASK(PrevTask|StdOut)}`.

**Theme**

*Dark blue*, *Light grey* or *Dark grey*; defaults to the Client's current theme. Available for printer, PDF and HTML output.

***PDF***, ***HTML*** **and** ***CSV*** **sub tabs**

The sub tab for the chosen file output has:

**Credentials**

Optional. The Server writes the file as this Credential, for example to a network share. The user who saves the Task needs the *Execute* permission on the Credential.

**File**

The full path of the report file on the VisualCron Server. Required; Variables can be used, and an existing file is replaced.

***Job range*** **sub tab**

Shown for the *Job - List* report. *All Jobs* / *Specific Job groups* / *Specific Jobs*; for the last two, select the groups or Jobs on the ***Groups*** or ***Jobs*** sub tab.

***Content*** **sub tab**

Shown for the *Job - List* report. Under *Job and Task column selection*, select and order the columns. For CSV output, select at least one column; values are separated by semicolons.

***Print*** **sub tab**

![Report Task, Print sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/report%20print.png)

These settings apply when *Output type* is *To printer*.

**Select printer**

Select a printer installed on the VisualCron Server. Required for printer output.

**Printer settings**

**Number of copies**

Enter the number of copies to print. Defaults to 1.

**Orientation**

*Portrait* / *Landscape*

Select the page orientation. Defaults to *Portrait*.

**Page range**

*All pages* / *Pages*

Select whether to print all pages or enter one page or one range, for example "2-4". An empty range makes the Task fail.
