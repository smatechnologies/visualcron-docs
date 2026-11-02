---
sidebar_label: 'Task File - Touch File'
hide_title: 'true'
---

## Task File - Touch File

The Touch file Task sets the last write time of the files that the file filter finds to the current date and time of the VisualCron Server. If no file matches and the include file mask names a single file, without wildcards, the Task creates that file, empty. Even then, the Task raises a file-not-found error, which its **_On error_** settings handle. The Touch file Task uses the standard [file filter](../../../server/job-tasks-file-filter) to find files that you want to touch.

![Add Task dialog for the Touch file Task, file filter Location tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Touch%20File.png)

**Touch file > File filter** tab

Use the standard [file filter](../../../server/job-tasks-file-filter) to select which files to touch. The file filter includes a Credential field for accessing files on remote or network locations.
