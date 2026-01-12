---
sidebar_label: 'Global - Time Exceptions'
hide_title: 'true'
---

## Global - Time Exceptions

Time exceptions is a way to skip execution of a Job at a certain time or interval. A time exception collection is a package of one or more time exceptions. For example, a time exception collection may be "American Holidays" and one time exception could be the 4th of July. If you, for example, have a Job that runs every day and you want to skip running that Job on "American holidays", you check the time exception collection "American holidays" for this Job.
 
Collections with time exceptions are managed either from the main menu **Server > Global objects > Time exceptions** dialog or from the Add Job/Edit Job menu under the **Time exceptions** tab. When adding a collection, you can specify a name and a appropriate description. When a collection has been created, time exceptions can be added. Each collection is expandable, and when expanded, the underlying time exceptions are displayed. Setting of time exceptions work the same way as time settings for a Job. Collections and exceptions are managed (add, edit and delete) by mouse right-click in the collection/time exception list. During changes in the time settings, the Next exception time will be calculated at the status bar.
 
Note: Remember that a change of a collection affects all Jobs that use that specific collection.
 
The time exception settings are stored by VisualCron in the "timeexceptions.xml" file, by default stored in the "C:\Program Files\VisualCron\settings" folder.
 
An important feature is the import function, ***Time exceptions* -> Collections -> *Import***. The import function can import collections that you or another person has created. If a collection already exists you'll be asked if you want to replace or skip the import of that collection.
 
**Download time exceptions**

[US Federal Holidays](https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays)

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Time%20Exceptions/Time%20Exceptions.png)

