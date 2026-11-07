---
sidebar_label: 'Global - Variables'
hide_title: 'true'
---

## Global - Variables

### Introduction

Variables pass information between Jobs, Triggers, Tasks and Notifications. Almost every field in the Client can use a Variable; when the Job, Task or Notification uses the field, the Variable is replaced with its value. To request a Variable that does not exist, contact VisualCron support.
 
### Using variables

The *Variables* window opens from the main menu _Server_ -> _Global objects_ -> _Variables_, or from the *Variables* button in the status bar of each window that can use Variables.
 
Almost all fields in a window with the *Variables* button can use Variables. To check a field, drag a Variable to it: if the field can use it, the field turns pale blue while you hover over it; if not, you cannot drop it there.

![Variables window with the Variable tree, Variable Key and Value Preview](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Variables/Variables.png)

The tree view is a hierarchy of Variables. When you open _VisualCron variables_ -> _Jobs_, the Job you are editing is marked with a blue arrow to the right of its name and its Tasks are shown in the tree. Each Job can be browsed to show the Triggers, Tasks and Variables connected to it.

The toolbar has *Add*, *Edit*, *Clone*, *Delete*, *Go to active Job*, a search box with *Search*, and *Audit log*.
 
**Variable Key**

When you select a Variable in the tree, its key is shown in *Variable Key*, where you can also edit it, for example to change a date format. For a Job or Task Variable, select how the key points to it: *Direct Id (direct pointing Id of Job or Task)*, *Active (current context sensitive Job or Task)* or *PrevTask (previous or last context sensitive Task)*. *Copy to clipboard* copies the key; *Select* puts it in the field you opened the window from.

**Value Preview**

With *Preview Variable value* selected, the current value of the selected Variable is shown in *Value Preview* and updated as you edit the key (see **Local previewing** under Limitations).

**Hierarchy of variables**

VisualCron has several kinds of Variables. The tree, especially the _VisualCron variables_ root, is a hierarchy: the root holds _Jobs_, which lists the Jobs; each Job holds its Job Variables, Loop, Triggers and Tasks Variables as well as its own, and a Trigger may have result Variables that you can browse.
 
**Parameter delimiters**

Separate arguments with a pipe (`|`). If the arguments contain no pipe, a comma (`,`) separates them instead. The check includes the text of Variables nested in the arguments, so use pipes throughout when you nest Variables. Commas and pipes in the value of a nested Variable do not split the arguments.

To use another delimiter, for example when an argument must contain a pipe, start the arguments with it. For example, with @ as the delimiter: ```{FILE(@Content@c:\textfile.txt)}```

Any first character other than a letter, a digit, white space or one of `-` `.` `{` `(` `[` is read as the delimiter. An argument list that starts with another character, such as `+`, `\`, `'` or `%`, is therefore split on that character. `{DATEFORMAT(...)}` is not affected: it always uses the whole text as the format.
 
### Root variables

**Functions**

Functions has string, regular expression and JSON functions, and conversions between value types, such as the number conversions described below. Path functions are under *File variables* and *Folder variables*.

**Number conversion**

Convert a value to a specific numeric type inside a Variable. There are four families: *{INTEGER}* (32-bit integer), *{LONG}* (64-bit integer), *{DECIMAL}* and *{DOUBLE}*. Each family accepts two forms:

```{INTEGER(value|defaultValue)}```

```{INTEGER(value|format|defaultValue)}```

The first argument is the value to convert. The last argument is the default value. The optional middle argument is a standard or custom .NET numeric format string that is applied to the converted result. *{INTEGER}* and *{LONG}* truncate any fractional part toward zero, while *{DECIMAL}* and *{DOUBLE}* keep it.

Values are parsed using the invariant culture, so a period is always the decimal separator and thousand separators are not accepted in the value. Leading zeros are removed, scientific notation such as 1e3 is accepted, and any space before or after the value is ignored.

The default value is returned, exactly as you typed it, when the value is not a number, when it is only spaces, when it is outside the range of the target type, when *{DOUBLE}* would result in an infinite or non numeric value, and when the format cannot be applied. In the three argument form the default value is returned without the format applied.

A format is rejected when it is longer than 64 characters, and a standard format is rejected when its precision is above 99, so a format such as F100000000 returns the default value instead of building a very large string.

An empty value has to reach the function through another Variable, for example ```{INTEGER({STRING(Null)}|0)}```, which returns 0. Writing an empty first argument directly, as in ```{INTEGER(|0)}```, is read as a single argument and reports an invalid number of arguments instead of returning the default value.

Examples:

```{INTEGER(5.9|0)}``` returns 5

```{INTEGER(5.9|000|0)}``` returns 005

```{LONG(9999999999|0)}``` returns 9999999999

```{DECIMAL(5.5|0.00|0)}``` returns 5.50

```{DOUBLE(abc|-1)}``` returns -1, the default value, because the value is not a number

```{INTEGER(2147483648|-1)}``` returns -1, the default value, because 2147483648 is outside the 32-bit integer range (use ```{LONG}``` for larger whole numbers)

```{LONG(2147483648|0)}``` returns 2147483648, which is within the 64-bit integer range

```{DECIMAL(1e3|0)}``` returns 1000, because scientific notation is accepted

```{INTEGER(abc|000|-1)}``` returns -1, the default value, without the 000 format applied to it

```{DOUBLE(1e400|-1)}``` returns -1, the default value, because the value is too large to be a valid number
 
**Logic**

Conditional functions. `{LOGIC(If|<type>|<value 1>|<operator>|<value 2>|<result if true>|<result if false>)}` compares two values and returns one of two results. `<type>` is `String`, `Integer`, `Double` or `Boolean`. For `String`, the operators are `==`, `!=`, `=%` (contains) and `!=%` (does not contain), and the comparison is case-sensitive. For `Integer` and `Double`, they are `==`, `!=`, `<`, `<=`, `>` and `>=`. For `Boolean`, they are `==` and `!=`. For example, `{LOGIC(If|Integer|{TASK(PrevTask|ExitCode)}|==|0|OK|Failed)}` returns `OK` when the previous Task's exit code is 0.
 
**Math**

Math functions. `Add`, `Subtract`, `Multiply` and `Divide` take five arguments: the function, the number type (`Integer` or `Double`), the two values and a .NET numeric output format. The format can be empty, but its delimiter must be there: `{MATH(Add|Integer|5|6|)}` returns `11`, and `{MATH(Add|Integer|5|6|#0.00)}` returns `11.00`. An empty value counts as 0. `Divide` can return a fraction even with `Integer`: `{MATH(Divide|Integer|7|2|)}` returns `3.5`. With `Integer`, each value is rounded to a whole number (halves to the even number, so `2.5` becomes `2`) and must fit in a 32-bit integer; use `Double` for decimals.

The other functions take no output format. `Abs`, `Ceiling`, `Floor`, `Sqrt` and `Exp` take one value, for example `{MATH(Sqrt|16)}` returns `4`. `Pow`, `Max` and `Min` take two, for example `{MATH(Pow|2|10)}` returns `1024`. `Round` takes the value and the number of decimals and rounds halves away from zero: `{MATH(Round|2.5|0)}` returns `3`. `PI` and `E` take none, for example `{MATH(PI)}`. Unlike the number conversions, values are read, and results written, with the regional settings of the VisualCron Server, so on a Server with German settings `{MATH(Divide|Integer|7|2|)}` returns `3,5`.
 
**System variables**

The current user, the computer's name, operating system and start time, memory use, and environment variables.

**Server variables**

Values that describe the VisualCron Server, such as its IP, port, version and activation status, and the settings, backup, temp, log and output cache folders. You can also list the users and groups on the Server.
 
**Date variables**

The current date and time in any format, and date calculations. See [Date/Time Variables](global-date-time-variables).
 
**File variables**

Variables related to files. For example, the Content argument gives the text content of a file.
 
**Folder variables**

Paths of the current, system and temp folders, the directory, path and volume separator characters, and path functions (directory name, root and whether a path is rooted).
 
**VisualCron variables**

Variables for the settings and run data of your Jobs, Tasks and Triggers.
 
**User defined variables**

Create your own Variables, each with a name, a description, a type (`String`, `Int32`, `Double`, `Boolean` or `List`) and a value. Use a User Variable with `{USERVAR(<name>)}`. Add, edit and delete User Variables with the toolbar, or in a Job with the [Set User Variable](job-tasks/internal-tasks/set-user-variable), [Remove Variable](job-tasks/internal-tasks/remove-variable) and [Calculate Variable](job-tasks/internal-tasks/calculate-variable) Tasks.

![Edit Variable window for a User Variable](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Variables/Edit%20variables.png)

**Task repository variables**

Variables for accessing items stored in the Task repository.

**The format of a variable**

The text below is an example of a Variable key. It starts with `{`, followed by the kind of root Variable, here a Task. In the *Variables* window, once you select a Variable, its format is shown in the status bar, in this case `{TASK(<taskId>|Name)}`. The parts inside the parentheses are the arguments. The first is the ID of the Task, which VisualCron generates when the Task is created. The second, `Name`, returns the name of that Task.

The function name is 3 to 16 uppercase letters, and there is no space before the parenthesis: with a space, as in `{TASK (…)}`, the text is not replaced.
 
Variable Key example: ```{TASK(7b9a0b42-ec36-482e-bd04-93ef8b655108|Name)}```
 
### Job, Task and Trigger variables

**Active Job/Task vs specific Job/Task**

In the Job list you will see a Job listed as *Active job*, the first entry under _Jobs_. *Active job* stands for the Job that VisualCron is processing when the Variable is replaced, and the Tasks under it for the Task being processed. The Jobs listed below *Active job* each point to one specific Job. For example, when using the Job name Variable (`{JOB(<jobId>|Name)}`) you will always get the same name (unless the name is changed) for that particular Job. With *Active job* (`{JOB(Active|Name)}`) you get the name of the Job being processed when the Variable is replaced.
 
The advantage of using *Active job* is that you can prepare a Notification for example with *Active* Job or Task Variables. In the report from the Notification you will get different results, depending on the Job or Task that is being run. In that way Notifications can be reused.
 
The advantage of using a Variable that points to a specific Job is that you always get the value from that Job or Task.
 
**Current Job/Task**

The current Job or Task is the Job or Task that you currently are editing. It is marked by a blue arrow to the right of the Job or Task name. It is there to help you find the Job or Task currently being edited. A Job that has not been saved does not appear under _Jobs_. When you open the window from a Job you are editing, *Active job* shows that Job, including unsaved changes.
 
**Previous Task**
 
Use the `PrevTask` identifier for the Task that ran before the current one in the same run. If there is none, as in the first Task of a Job, `PrevTask` refers to the current Task:
 
```{TASK(PrevTask|Name)}```

**Output and error output with concurrent Job instances**
 
The Task output Variables (*Output* and *Output (stderr)* in the *Variables* window, for example ```{TASK(PrevTask|StdOut)}``` and ```{TASK(PrevTask|StdErr)}```) are stored per Job and Task, not per running instance. If more than one instance of the same Job runs at the same time, these Variables share a single value across those instances. As a result a Task may read the output produced by a parallel instance instead of its own.
 
For example, if a Job containing an Execute Task followed by a second Task that reads ```{TASK(PrevTask|StdOut)}``` is started twice and both instances run simultaneously, the second Task in one instance may pick up the *Output* written by the other instance.
 
Avoid relying on *Output* and *Output (stderr)* in Jobs that can run concurrently, especially where a later Task depends on the value. If you need output that belongs to one run, write it to a file whose name is unique to the run, or keep *Do not start if job is already running* selected on the Job's **_Main settings_** tab (see [Job main settings](job-main-settings)), so that a second run is skipped or, with *Put Job in queue (does not skip Job - runs Job when running Job is finished)*, queued.
 
**Triggers**

A Trigger starts a Job. Its Variables give information about it.
 
**Last trigger and specific Trigger**

*Last trigger* is always in a Job's Trigger tree. It stands for the Trigger that fired last, so that a Job with several Triggers can use one Variable for all of them, without pointing to a specific Trigger.
 
When a Trigger starts a run, the *Last trigger* result Variables read the result of that firing for the whole run. Other *Last trigger* values, such as the description, follow the Trigger that fired most recently, and so does the Trigger type used to read results: if another Trigger of the Job fires during the run, even one whose run is skipped or queued, they change. In a run that no Trigger started, for example a manual run, *Last trigger* reads the result of whichever of the Job's Triggers fired last. A Variable that points to a specific Trigger always reads that Trigger's latest result, which a later firing can replace while the Job is still running.
 
Values that every Trigger has, such as the description, work with any Trigger. A result Variable of one Trigger type, for example the file name of a File Trigger, returns an error message in square brackets instead of a value when the Trigger that fired last is of another type.
 
**Trigger result variables**

Some Variables exist when a Trigger has been added, for example a Trigger description, or the folder and file mask of a File Trigger. Other Variables are result Variables, which are set each time the Trigger fires.
 
Now, suppose you are monitoring for changes in ```*.txt``` files. Because of the file mask, you may not know which file changed; the result Variables tell you. They are kept in memory when the Trigger fires and are available before the Job starts.
 
Event Triggers in particular have many result Variables. The result Variables of the main Event Triggers are described below.
 
Result Variables are not saved. A Trigger's result is replaced each time the Trigger fires and is lost when the VisualCron service restarts.
 
### File event result variables

**Folder path**

The folder path that the event is watching.
 
**File mask**

The file mask that was used when watching.
 
**Type of change**

The kind of change: "Created", "Changed", "Deleted" or "Renamed".
 
**Path**

Full path of the affected file or folder.
 
**Name**

Name of the affected file or folder.

**Path of triggered folder**

The folder that contains the affected file. When *Include subfolders* is selected, this can be a subfolder of the watched folder.
 
**Old Name**

The previous name of the affected file or folder (available on rename).
 
**Old full Path**

The previous full path of the affected file or folder (available on rename).
 
**New text**

Available only for a change event with *Trailing Trigger* selected (see [File Trigger](event-trigger-file)). The text added to the file since the previous change. For the first change the Trigger sees in a file, or when the file became shorter, it is the whole content. A change that does not change the file's length does not fire the Trigger.
 
More information:
[Microsoft file system event arguments](https://learn.microsoft.com/en-us/dotnet/api/system.io.filesystemeventargs)
 
### EventLog event result variables

**Host**

Name of the computer that logged the event.
 
**Category**

The event's task category number.
 
**Event code**

The event's task category number (the same as *Category*). For the event ID shown in Event Viewer, use *Event id*.
 
**Event id**

The event ID shown in Event Viewer.
 
**Event type**

The event's level as a number: 0 (Log always), 1 (Critical), 2 (Error), 3 (Warning), 4 (Information) or 5 (Verbose). Many events that Event Viewer shows as Information, such as security audit events, have level 0.
 
**Date created**

When the event was logged.
 
**Log file**

Name of the event log, for example "Application".
 
**Message**

The first data value of the event, not the full message text. Use *XML* for all of the event's data.
 
**Record number**

The event's record number in the log.
 
**Source**

The provider that logged the event.
 
**Username**

Currently always empty.
 
**Type**

The event's opcode name, for example "Info", "Start" or "Stop".

**XML**

The raw XML representation of the event.
 
**Keywords**

The event's keyword names, one per line, for example "Audit Success" or "Audit Failure".
 
More information:
[Microsoft: EventRecord properties](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventing.reader.eventrecord)
 
### Process event result variables

**Process name**

Name of the process that was started/stopped.
 
**Description**

Description of the process, usually the executable name.
 
**Created date**

Date the process began executing.
 
**Path**

Full path to the executable file of the process. Example: ```C:\WINDOWS\explorer.exe```.
 
**Command line**

The command line that started the process.
 
**Process id**

Global process identifier that you can use to identify a process.

If Windows does not report the name, command line, description or path of a new process, the Job still runs, but for that run the Process result Variables return an error message in square brackets instead of a value.
 
More information:
[Microsoft process info](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process)
 
### Service event result variables

**Name**

The service name, for example "Spooler" (not the display name).
 
**Display name**

Display name of the service.
 
**Path**

Path of the service executable as registered in Windows; it can include arguments.
 
**State**

Current state of the base service: "Stopped", "Running" or "Paused".

:::warning

The Service Trigger fires only for the Stopped, Running and Paused states. It does not fire for Start pending, Stop pending, Continue pending or Pause pending, even if they are selected in the Trigger.

:::
 
**Status**

The status Windows reports for the service, for example "OK", "Degraded" or "Error". This is not the same as *State*.
 
Values include the following:

* "OK"
* "Error"
* "Degraded"
* "Unknown"
* "Pred Fail"
* "Starting"
* "Stopping"
* "Service"
 
**Exit code**

The Windows error code for a problem starting or stopping the service, or 0 if there was none. 1066 means the service reported its own error code; see *Service specific exit code*.
 
**Service specific exit code**

The service's own error code. Set only when *Exit code* is 1066.

**Process Id**

Process ID of the service, or 0 when the service is stopped.
 
**Description**

Description of the service.
 
More information:
[Microsoft service info](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-service)
 
### Registry event result variables

**Hive**

Name of the hive (subtree) that contains the key (or keys) that is changed. For example, ```HKEY_LOCAL_MACHINE```.
 
**Registry key path**

Path to the registry key. For example, ```"SOFTWARE\Microsoft\WBEM\Scripting"```.
 
**Registry value name**

Name of the value in the registry key. For example, in the registry key ```HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WBEM\Scripting``` you can detect changes in the value Default Namespace.
 
**Value**

The data of the changed value, read when VisualCron processes the event. Available only for the *Registry Value Change* event when the Trigger's computer is `.` (the default). For binary and multi-string values it returns the .NET type name, such as `System.Byte[]`; if the value cannot be read, it returns the error message.
 
More information:
[Microsoft registry info](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/regprov/registryevent)
 
### Custom event result variables

Currently no result Variables exist for this event type.
 
### Other Event Triggers

Most other Event Triggers also have result Variables. They are listed in the *Variables* window under the Job's Triggers and described on each Trigger's page.
 
### Special characters

`{STRING(Print|<text>)}` replaces `\r`, `\n`, `\t` and `\f` in the text with a carriage return, a line break, a tab and a form feed, for example `{STRING(Print|line1\nline2)}`. `\n` already produces a Windows line break (carriage return and line feed), so write `\n`, not `\r\n`. With the pipe as delimiter, the text cannot contain a pipe; to include one, use another delimiter (see **Parameter delimiters**), for example `{STRING(~Print~a|b\nc)}`. Other Variables and fields do not replace these characters.
 
### Limitations

**Current state of tree view**

The tree view shows the current state. It shows the Variables that exist when you open the *Variables* window. Jobs and Tasks added after you open the window appear the next time you open it.
 
**Local previewing**

*Value Preview* is computed in the Client, not on the VisualCron Server. Date and time, computer, user, environment, memory and file Variables show the values of the computer the Client runs on. When the Job runs, they have the Server's values. If the preview says a file does not exist, the file may still exist on the Server.
 
**Nested and chained Variables**

Variables can be nested in another Variable's arguments, for example ```{INTEGER({STRING(Null)}|0)}```; the inner Variables are resolved first. A value that contains another Variable is resolved again. After 1,000 levels of nesting and re-resolution, the Variable is replaced with an error message in square brackets that says a possible infinite loop was detected.
