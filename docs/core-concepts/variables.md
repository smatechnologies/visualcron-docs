---
sidebar_label: 'Variables'
sidebar_position: 4
description: Use variables in VisualCron to pass dynamic values between tasks, format dates, and reference system data.
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Variables

**Variables** allow you to insert dynamic values into almost any field in VisualCron — task settings, email bodies, file paths, conditions, and more.

Variables are accessed from **Server > Global Objects > Variables**, or via the **Variables** button in the status bar of any supporting window.

---

## Variable Syntax

```
{VARIABLETYPE(argument1,argument2)}
```

Example: `{TASK(taskId,Output)}` — retrieves the standard output of a specific task.

Parameters are separated by `|` or `,` by default. If your value contains those characters, see [Parameter Delimiters](#parameter-delimiters) below.

---

## Using Variables

**Drag and drop** — In the Variables window, drag a variable directly into any compatible field. The field turns light blue when it can accept a variable.

**Type directly** — Type or paste the variable key (e.g. `{TASK(id,Output)}`) into any supporting text field.

**Value preview** — Clicking a variable in the Variables window shows its current resolved value in the yellow *Value Preview* box.

---

## Parameter Delimiters

By default, parameters use `|` or `,` as separators. If your path or value already contains those characters, choose a custom delimiter by placing it as the first character inside the parentheses:

```
{FILE(@Content@C:\my,folder\file.txt)}
```

Here `@` is used as the delimiter so the comma inside the path is not misread as a parameter separator. Any character can be used as the alternate delimiter.

---

## Variable Categories

| Category | What it gives you |
|---|---|
| **Date & Time** | Current date/time in any format |
| **File** | File content, size, and properties |
| **Path & String** | Path encoding, text manipulation, escape sequences |
| **Job** | Job name and properties |
| **Task** | Task output, exit code, name, and timing |
| **Trigger** | Values from the trigger that fired the job |
| **User Defined** | Your own static or runtime-calculated variables |

---

## Creating User-Defined Variables

1. Go to **Server > Global Objects > Variables > User Defined**
2. Click **Add** and configure name, type, and value
3. Or set them at runtime using tasks: [Set Variable](../tasks/variables/set-remove-calculate), [Environment Variables](../tasks/variables/environment-variables)

Reference them anywhere with `{USERVAR(YourVariableName)}`.

---

## Limitations

- **Variable depth** — VisualCron resolves variables to a maximum depth of 2 levels. A variable that points to a field containing another variable will resolve both, but no deeper.
- **Variables cannot be used as arguments** — You cannot nest a variable inside another variable's argument.
- **Tree view is a snapshot** — The Variables browser shows the state at the time you opened it. Variables added after opening are not visible until you reopen it.
- **Local vs server paths** — File variable previews in the client use client-side paths. If the file exists only on the server, the preview may show "file not found" even though it resolves correctly at runtime.

---

## Variable Reference

For the full live list, open the **Variables** browser inside VisualCron — it shows every available variable for your current jobs, tasks, and triggers in real time, including dynamic IDs. The tables below document all confirmed static syntax.

<Tabs>

<TabItem value="datetime" label="Date & Time">

Use `{DATETIME(format)}` where `format` is any combination of the tokens below.

**Shorthand formats**

| Name | Variable Key | Example Output |
|---|---|---|
| Short date | `{DATETIME(d)}` | `08/17/2000` |
| Long date | `{DATETIME(D)}` | `Thursday, August 17, 2000` |
| Full date short time | `{DATETIME(f)}` | `Thursday, August 17, 2000 16:32` |
| Full date long time | `{DATETIME(F)}` | `Thursday, August 17, 2000 16:32:32` |
| General short time | `{DATETIME(g)}` | `08/17/2000 16:32` |
| General long time | `{DATETIME(G)}` | `08/17/2000 16:32:32` |
| Month and day | `{DATETIME(m)}` | `August 17` |
| RFC 1123 | `{DATETIME(r)}` | `Thu, 17 Aug 2000 23:32:32 GMT` |
| Sortable | `{DATETIME(s)}` | `2000-08-17T16:32:32` |
| Short time | `{DATETIME(t)}` | `16:32` |
| Long time | `{DATETIME(T)}` | `16:32:32` |
| Universal sortable | `{DATETIME(u)}` | `2000-08-17 23:32:32Z` |
| Universal full | `{DATETIME(U)}` | `Thursday, August 17, 2000 23:32:32` |
| Year and month | `{DATETIME(y)}` | `August, 2000` |

**Custom format tokens**

| Name | Variable Key | Example Output |
|---|---|---|
| Day, no zero | `{DATETIME(d)}` | `7` |
| Day, leading zero | `{DATETIME(dd)}` | `07` |
| Day, abbreviated | `{DATETIME(ddd)}` | `Wed` |
| Day, full name | `{DATETIME(dddd)}` | `Wednesday` |
| Fractions of second | `{DATETIME(fff)}` | `321` |
| Hour, 12-hour | `{DATETIME(h)}` / `{DATETIME(hh)}` | `4` / `04` |
| Hour, 24-hour | `{DATETIME(H)}` / `{DATETIME(HH)}` | `16` / `16` |
| Minutes | `{DATETIME(m)}` / `{DATETIME(mm)}` | `5` / `05` |
| Month, numeric | `{DATETIME(M)}` / `{DATETIME(MM)}` | `8` / `08` |
| Month, abbreviated | `{DATETIME(MMM)}` | `Aug` |
| Month, full name | `{DATETIME(MMMM)}` | `August` |
| Seconds | `{DATETIME(s)}` / `{DATETIME(ss)}` | `4` / `04` |
| AM/PM indicator | `{DATETIME(t)}` / `{DATETIME(tt)}` | `A` / `AM` |
| Year, 2 digits | `{DATETIME(yy)}` | `00` |
| Year, 4 digits | `{DATETIME(yyyy)}` | `2000` |
| UTC offset | `{DATETIME(zzz)}` | `+01:00` |
| Month name only | `{DATE(Month.Name)}` | `August` |

**Time span tokens**

| Name | Variable Key | Example Output |
|---|---|---|
| Elapsed milliseconds | `{DATETIME(totalmilliseconds)}` | `86400000` |
| Elapsed seconds | `{DATETIME(totalseconds)}` | `86400` |
| Elapsed minutes | `{DATETIME(totalminutes)}` | `1440` |
| Elapsed hours | `{DATETIME(totalhours)}` | `24` |
| Elapsed days | `{DATETIME(totaldays)}` | `1` |

**Single-part extraction** — prefix with `%` to isolate one unit:

| Name | Variable Key | Example Output |
|---|---|---|
| Minutes only | `{DATEFORMAT(%M)}` | `32` |
| Day only | `{DATEFORMAT(%d)}` | `17` |

**Common custom examples**

| Name | Variable Key | Example Output |
|---|---|---|
| ISO date | `{DATETIME(yyyy-MM-dd)}` | `2000-08-17` |
| Time only | `{DATETIME(HH:mm:ss)}` | `16:32:32` |
| Full readable | `{DATETIME(dddd, MMMM dd yyyy)}` | `Thursday, August 17 2000` |
| European short | `{DATETIME(dd-MM-yy)}` | `17-08-00` |
| Month/year | `{DATETIME(M/yy)}` | `8/00` |

</TabItem>

<TabItem value="file" label="File & Path">

**File variables**

| Name | Variable Key | Example Output |
|---|---|---|
| File content | `{FILE(Content,C:\path\file.txt)}` | Full text content of the file |
| File size | `{FILE(Size,C:\path\file.txt)}` | `2048` |
| File content (alternate delimiter) | `{FILE(@Content@C:\my,folder\file.txt)}` | Full text content when path contains commas |

**Path variables**

| Name | Variable Key | Example Output |
|---|---|---|
| Encode filename | `{PATH(EncodeFileName\|value\|MASK)}` | Safe filename string |
| New unique name | `{NEWNAME()}` | `file_20250317_143201` |

**File trigger result variables**

These are populated when a **File Trigger** fires.

| Name | Variable Key | Example Output |
|---|---|---|
| Triggered file name | `{TRIGGER(FileName)}` | `report.csv` |
| Triggered file full path | `{TRIGGER(FileFullPath)}` | `C:\Drop\report.csv` |
| Last trigger file name | `{TRIGGER(Active\|LastTrigger\|File.Result.Name)}` | `report.csv` |
| Last trigger new text | `{TRIGGER(Active\|LastTrigger\|File.Result.NewText)}` | Contents added on change |
| Monitored folder | `{TRIGGER(Active\|LastTrigger\|File.Result.TriggerFolder)}` | `C:\Drop\` |

</TabItem>

<TabItem value="job" label="Job">

Reference any job by its ID (visible in the Variables browser under **VisualCron variables → Jobs**). Use `Active` in place of an ID to always refer to the currently executing job.

| Name | Variable Key | Example Output |
|---|---|---|
| Job name | `{JOB(id,Name)}` | `Daily Cleanup Script` |
| Active job name | `{JOB(Active,Name)}` | `Daily Cleanup Script` |
| Job variable | `{USERVAR(VariableName)}` | Value of the named job-scoped variable |

:::tip Active Job
Using `Active` instead of a hard-coded ID makes notifications and templates reusable across multiple jobs.
:::

</TabItem>

<TabItem value="task" label="Task">

Reference any task by its ID (visible in the Variables browser under **VisualCron variables → Jobs → Tasks**). Use `PrevTask` or `Active` as special references.

| Name | Variable Key | Example Output |
|---|---|---|
| Task standard output | `{TASK(id,Output)}` | `Success — logged to C:\VC-Logs\hello-world.txt` |
| Task error output | `{TASK(id,OutputError)}` | `Access denied` |
| Task name | `{TASK(id,Name)}` | `PowerShell` |
| Task exit code | `{TASK(id,ExitCode)}` | `0` |
| Task exit code description | `{TASK(id,ExitCodeDesc)}` | `The operation completed successfully` |
| Previous task name | `{TASK(PrevTask,Name)}` | `PowerShell` |
| Active task exit code description | `{TASK(Active,ExitCodeDesc)}` | `The operation completed successfully` |
| Active task last exited | `{TASK(Active\|LastExited\|dd/MM/yyyy HH:mm)}` | `25/03/2026 07:00` |

:::tip PrevTask
`PrevTask` always refers to the task that ran immediately before the current one — useful for chaining logic without hard-coding task IDs.
:::

</TabItem>

<TabItem value="trigger" label="Trigger Results">

Trigger result variables are populated after a trigger fires. Properties depend on the trigger type.

**File trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| Monitored folder | *(via Variables browser → File trigger → Folder path)* | `C:\Drop\` |
| File mask | *(via Variables browser → File trigger → File mask)* | `*.csv` |
| Type of change | *(via Variables browser → File trigger → Type of change)* | `Created` |
| Affected file path | *(via Variables browser → File trigger → Path)* | `C:\Drop\report.csv` |
| Affected file name | *(via Variables browser → File trigger → Name)* | `report.csv` |

**Event Log trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| Host | *(via Variables browser)* | `MYSERVER` |
| Category | *(via Variables browser)* | `Disk` |
| Event code | *(via Variables browser)* | `7036` |
| Event id | *(via Variables browser)* | `1074` |
| Event type | *(via Variables browser)* | `Information` |
| Date created | *(via Variables browser)* | `2026-03-25 07:00:00` |
| Log file | *(via Variables browser)* | `System` |
| Message | *(via Variables browser)* | `The service entered the running state.` |
| Record number | *(via Variables browser)* | `48291` |
| Source | *(via Variables browser)* | `Service Control Manager` |
| User name | *(via Variables browser)* | `SYSTEM` |

**Process trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| Process name | *(via Variables browser)* | `notepad.exe` |
| Description | *(via Variables browser)* | `Notepad` |
| Created date | *(via Variables browser)* | `2026-03-25 07:00:00` |
| Executable path | *(via Variables browser)* | `C:\Windows\System32\notepad.exe` |
| Command line | *(via Variables browser)* | `"C:\Windows\System32\notepad.exe" report.txt` |
| Process ID | *(via Variables browser)* | `4821` |

**Service trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| Service name | *(via Variables browser)* | `wuauserv` |
| Display name | *(via Variables browser)* | `Windows Update` |
| Binary path | *(via Variables browser)* | `C:\Windows\System32\svchost.exe` |
| State | *(via Variables browser)* | `Running` |
| Status | *(via Variables browser)* | `OK` |
| Exit code | *(via Variables browser)* | `0` |
| Service-specific exit code | *(via Variables browser)* | `0` |

**Registry trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| Hive | *(via Variables browser)* | `HKEY_LOCAL_MACHINE` |
| Key path | *(via Variables browser)* | `SOFTWARE\Microsoft\WBEM` |
| Value name | *(via Variables browser)* | `Default Namespace` |
| Value | *(via Variables browser)* | `root\cimv2` |

**Network / HTTP REST trigger**

| Name | Variable Key | Example Output |
|---|---|---|
| HTTP REST query parameter | `{TRIGGER(Active\|LastTrigger\|HTTPREST.Result.QueryParameters.Value\|name)}` | `Philadelphia` |
| TCP text body | `{TRIGGER(...\|TCP.Result.TCP.TextBody)}` | `PING` |

</TabItem>

<TabItem value="uservar" label="User Defined">

User-defined variables are created in **Server > Global Objects > Variables > User Defined**, or set at runtime using tasks.

| Name | Variable Key | Example Output |
|---|---|---|
| Any user variable | `{USERVAR(VariableName)}` | Value you assigned |
| Named example | `{USERVAR(CustomerName)}` | `Acme Corp` |
| Version variable | `{USERVAR(VCVersion)}` | `10.0.1` |

**Variable types**

| Type | Use case | Example value |
|---|---|---|
| String | Any text | `Acme Corp` |
| Integer | Whole numbers | `42` |
| Decimal | Floating-point | `3.14` |
| Boolean | True/False flags | `True` |
| DateTime | Date and time | `2026-03-25 07:00:00` |

**Setting variables at runtime**

| Name | Variable Key | Example Output |
|---|---|---|
| Set variable | [Set Variable task](../tasks/variables/set-remove-calculate) | Creates or updates a user variable |
| Remove variable | [Remove Variable task](../tasks/variables/set-remove-calculate) | Deletes a user variable |
| Calculate variable | [Calculate Variable task](../tasks/variables/set-remove-calculate) | Performs arithmetic on a numeric variable |

</TabItem>

<TabItem value="string" label="String Functions">

| Name | Variable Key | Example Output |
|---|---|---|
| Print with escapes | `{STRING(Print\|Hello\nWorld)}` | `Hello` (newline) `World` |
| Print newline | `{STRING(Print\|\n)}` | *(newline character)* |
| Replace text | `{STRING(Replace\|original\|new)}` | Replaced string |

**Escape sequences** inside `STRING(Print|...)`

| Name | Variable Key | Example Output |
|---|---|---|
| New line | `\n` | Line break |
| Carriage return | `\r` | CR character |
| Tab | `\t` | Tab character |

Full reference: [.NET character escapes](https://docs.microsoft.com/en-us/dotnet/standard/base-types/character-escapes-in-regular-expressions)

</TabItem>

</Tabs>

---

## Related

- [Set/Remove/Calculate Variable task](../tasks/variables/set-remove-calculate)
- [Environment Variables task](../tasks/variables/environment-variables)
- [Conditions](conditions) — variable-based conditions
- [Output and Results](output-and-results)
