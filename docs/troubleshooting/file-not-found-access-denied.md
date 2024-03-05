---
sidebar_label: 'File Not Found / Access Denied'
hide_title: 'true'
---

## File Not Found / Access Denied

If you are working with files you may get the above error. Normally when you know a file is there but VisualCron can't find the reason is probably a permission error. What is important to know is that, if you use background execution, everything is being run from the Windows service. The Windows service is normally running as the LOCALSYSTEM user account.
 
Normally, the LOCALSYSTEM account has no network access and might be restricted to certain private folders. There are a couple of ways to come around this:
 
1. Add a [credential](credential) to the Task. With a Credential VisualCron can impersonate as another user. Normally you should create the same Credential as you are logged in as.
2. Change the username of the Service. Even though you can do this we do recommend that you add the Credential instead.