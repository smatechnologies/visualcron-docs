---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

The Server/Group/Job/Task grid occupies the main part of the VisualCron Client application. This provides an overview where groups of all defined server connections with all their related Tasks and Jobs are shown. Also, most changes of server, Jobs and Tasks may be managed in this grid.
 
For each server, there are two child "tracks", where the first track(s) show the Job(s) defined for the server and the second child track show the Task(s) connected to each Job. The Task and Job tracks provide real time information about next execution and last execution result. Status of each Task, including error messages from Tasks, are showed in the Task list. The output is shown in under the heading columns. The full output is obtained by mouse double-click on the output column.
 
Jobs can be defined, viewed and deleted by *Add, Edit, Clone or Delete*. Furthermore, Jobs can be managed by the *Export and Import* functions. Once a Job is defined, it can be set to active or inactive.
 
By mouse right-click on a Job, some Job related information and statistics are available. General Job information, is included in the **Tools > Explore > Server Monitor**.
 
Jobs can be managed by the Toolbar buttons or the mouse right-click menu for a Job.
 
All Jobs are listed in the Job list grid. The Job list view can be changed by the **Interface > Columns > Set columns** option by filtering the Job list columns.
 
All executed Jobs return an exit code. If a Job runs successfully and exits normally, it will return 0 as exit code which means that it is successful. If any error should occur, a different exit code will be used.
 
Find out more about [Windows exit codes](http://www.hiteksoftware.com/knowledge/articles/049.htm).

