---
sidebar_label: 'Jobs - Failed Jobs'
hide_title: 'true'
---

## Jobs - Failed Jobs

The _Failed Jobs_ window lists the Job runs that failed recently, so you can find and review failures in one place. Each row is one failed run, newest first. Expand a row to see that run's Tasks.

To open it, click the main menu _Server_ -> _Jobs_ -> _Failed Jobs_. When there are failures you have not looked at yet, the _Failed Jobs_ button shows how many.

_Server_ -> _Jobs_ -> _Failed Jobs_

![Failed Jobs window opened from the Jobs group of the Server tab of the main menu, whose Failed Jobs button shows a count; the toolbar has Days back, Refresh and Mark all as read, and the grid lists failed runs with Event time, Name, Exit code, Execution time and Result](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Jobs%20-%20Failed%20Jobs.png)

### Toolbar

- _Days back_: how many days of failures to list, from "1" to "7"; default "1". This is the same setting as _Days to track failed Jobs_ in [Settings - Client Settings](../file/client-settings). A changed value takes effect when you click _Refresh_.
- _Refresh_: clears the list and loads it again from the Job log for the _Days back_ period
- _Mark all as read_: marks every listed failure as read

### Columns

- _Event time_: when the run started
- _Name_: the Job
- An icon showing the result
- _Exit code_: the Job's exit code
- _Execution time_: how long the run took
- _Result_: "Double click for result" when the run has a Job result to show, otherwise "No result"; double-click the cell to open the result

The Task rows under a Job show each Task's result, exit code, execution time and output. Double-click an output cell to open that output.

### Read and unread failures

Failures you have not looked at yet are shown in bold. Selecting a row marks it as read, and _Mark all as read_ marks them all. The count on the _Failed Jobs_ button is the number of unread failures. The read state is kept by your Client only, and only until you close the Client; after the Client starts again, all listed failures are unread.

### Where the failures come from

- When your Client connects, and when you click _Refresh_, failures are read from the Job log in the Server's log database for the _Days back_ period. They are found only when _Log to database_ is on in [Settings - Log Settings](settings-log-settings), and only as far back as the Job log is kept.
- Failures that happen while your Client is connected are added as they occur, also when _Log to database_ is off. _Refresh_ replaces them with what the Job log holds.

There is no command to clear or delete failed Jobs.