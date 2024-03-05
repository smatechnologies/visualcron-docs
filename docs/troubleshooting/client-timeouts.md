---
sidebar_label: 'VisualCron Client Timeouts When Connecting'
hide_title: 'true'
---

## VisualCron Client Timeouts When Connecting

### Problem 1 

This can happen when you have stopped or started the VisualCron service manually or installed a new version. If VisualCron has started a Job before you did this and the Job is still running, then VisualCron still has a connection to that Job.
 
Exit the running Job. On the computer where the VisualCron server is installed, open the Windows _Control Panel -> Administrative Tools -> Services_. Mark the "VisualCron Service" in the list, right click and select "Restart service".
 
### Problem 2 

This can also happen if the default port 16444 is already used by the client or it could be any else reason.
 
To determine this you have to stop the VisualCron service in _Control Panel -> Administrative Tools -> Services_. Locate the server_settings.xml located in c:\program files\VisualCron\settings\. Open the file with notepad and change Debug to "True" instead of "False". Start the VisualCron service and try to login. Locate the log file in C:\Program files\VisualCron\log\ named log_serverXXXXXX.txt (current date) and send it to support.