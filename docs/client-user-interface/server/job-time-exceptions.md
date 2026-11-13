---
sidebar_label: 'Job - Time Exceptions'
hide_title: 'true'
---

## Job - Time Exceptions

A time exception blocks a Job from running during the periods it defines. Time exceptions are defined in collections under [Global - Time Exceptions](global-time-exceptions), and any Job can use a collection.

On the Job's **_Time exceptions_** tab, select the check box beside each collection the Job should use.

While a selected time exception is in effect, the Job's Time Triggers and Event Triggers do not start it, and a missed run that falls inside it is skipped. Time exceptions are checked only when a Trigger fires or a missed run is found: a run started manually, by another Job or a Task, or by *Trigger on existing files* on a File, Cloud File or SharePoint File Trigger, is not blocked.
