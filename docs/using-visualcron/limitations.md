---
sidebar_label: 'Limitations'
hide_title: 'true'
---

## Limitations

There are some limitations in VisualCron which are listed below:
 
* VisualCron is designed for a set of [System Requirements](../requirements)
* The function "run missed Jobs" doesn't take time exceptions into account. A missed Job will run even if there was a time exception during that time
* Calculation of next run doesn't take time exceptions into account
* In Windows 2000 the Credentials are not fully supported. They work in the execute Task but not in other places like Archive, FTP and Notifications. To come around this you can run the VisualCron service as a certain user and map network drives for that account.