---
sidebar_label: 'Limitations'
hide_title: 'true'
---

## Limitations

There are some limitations in VisualCron which are listed below:
 
* VisualCron is designed for a set of [System Requirements](../requirements)
* The function "run missed Jobs" doesn't take time exceptions into account. A missed Job will run even if there was a time exception during that time
* Calculation of next run doesn't take time exceptions into account
* When accessing/editing files, keep in mind that multiple objects cannot access the same file at the same time. This is due to an OS limitation.

A good thing to keep in mind, if the specific task, job, file etc. is limited in Windows, it is limited in VisualCron. 