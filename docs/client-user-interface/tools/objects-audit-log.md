---
sidebar_label: 'Objects - Audit Log'
hide_title: 'true'
---

## Objects - Objects - Audit Log

The main menu **Tools > Objects > Audit log** option is used to track changes among objects within VisualCron. These type of changes are logged an internal database - the same database where Job and Task logs are stored.
 
**Tools > Objects > Audit log**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Audit%20Log.png)

The audit log is displaying the following information:

* Event date - when did the change ocur
* User - who did the change
* Type - what kind of object that was changed
* Job - the related Job name, if available
* Object - the name of the object
* Event type - what kind of event type (add/update/delete etc)
* Diff - if the object contains any changes to previous object
* Summary - a short, description of what was changed
 
The amount of data stored (history) is controlled by the [Server > Settings > Log > Database](../server/settings-log-settings).
 
By default, if you open the audit log from the Tools menu, the audit log is opened with no filters, displaying the events of today.  The audit log can be opened from various places and use different filters by default. For example, if you right click on a Job, it will show you events for this specific Job only. If you open the audit log from the Credentials window (and do not click on a specific Credential) changes to all Credentials are listed.
 
Double clicking on a row opens the Versions window, see [Audit log > Versions](audit-log-versions) for details.