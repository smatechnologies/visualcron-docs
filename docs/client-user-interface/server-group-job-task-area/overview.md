---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

The Server/Group/Job/Task grid fills the main part of the VisualCron Client. It lists every connected Server with its Jobs, grouped by Job group, and the Tasks of each Job.

Under each Server row, the Job rows show the Jobs of that Server, and under each Job the Task rows show its Tasks. Job and Task rows show real-time information, such as the next run and the result of the last run. The Task rows show the status and output of each Task, including error messages.

Jobs are added, edited, cloned and deleted from the toolbar or from the right-click menu of a Job; see [Job List](job-list/overview). Jobs can also be exported and imported, and each Job can be set to active or inactive.

To choose which columns the grid shows, click ***Interface*** -> ***Columns*** -> ***Set columns***; see [Set columns](../interface/columns-set-columns). For Server-wide run figures, see [Server Monitor](../tools/server-monitor).

Every Job run ends with an exit code. A Job that succeeds normally returns exit code 0; a Job that fails returns another exit code.
