---
sidebar_label: 'Health - Server Health'
hide_title: 'true'
---

## Health - Server Health

The _Server health_ window shows how the Server's health level has changed recently, which conditions the current level matches, and the latest level changes. Use it to find out why the Server reports a level and, if needed, to adjust the thresholds.

To open it, click the health button in the main menu _Server_ -> _Health_. The button shows the current level, for example "Excellent", so its caption changes with the level. Not every edition includes this window; if yours does not, the Client shows a "Feature not available" message instead.

_Server_ -> _Health_ -> `<current health level>`

![Server health window, Overview tab: a line chart of recent health levels from Excellent to Very bad, the Condition state grid with the conditions of the current level, and the Health events grid with Event date, Result, Health, Server name and Reason for change](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Health%20Server%20Health/Server%20Health.png)

### Overview tab

The **_Overview_** tab contains:

- A chart of the recent changes in the Server health level
- _Condition state_: the conditions of the current health level
- _Health events_: the latest level changes, with the columns _Event date_, _Result_, _Health_, _Server name_ and _Reason for change_; the window loads the 20 most recent changes

:::warning

Health events are read from the log database, and a change is recorded only when the level actually changes. If _Log to database_ is turned off in [Settings - Log Settings](settings-log-settings), or the log database holds no health events yet, the _Health events_ section stays empty, the chart has no history, and the **_Settings_** tab lists no levels, so you cannot change conditions in this window.

:::

### Settings tab

The **_Settings_** tab lists the five health levels and their conditions. Not every edition includes this tab.

Select a level to see its _Current_ and _Default_ conditions side by side.

To change the conditions of a level:

1. Double-click the level
2. Change the conditions in the editor that opens
3. Click _OK_

_Reset to default_ opens the same editor with the default conditions of the selected level filled in. The level changes only when you click _OK_.

Changing conditions requires the "Health levels" permission with "Edit" and the "Server settings" permission with "Edit" (see [Main - User Permissions](main-user-permissions)). With both, the change is saved to the Server immediately, and the health level is evaluated again with the new conditions.

:::warning

With the "Health levels" permission but without the "Server settings" permission with "Edit", the editor accepts your change and the tab shows it, but the Server does not store or use it, and no message is shown. The tab keeps showing your change, also after you close and reopen the window, until the Client receives the Server settings again. To see the conditions the Server uses, disconnect from the Server and connect again.

:::

### Server health levels

Abbreviations used in the conditions:

- `OSCPU`: total CPU use of the whole computer (%), across all processes
- `VCCPU`: CPU use of the VisualCron Server process (%), divided by the number of logical processors, so it expresses VisualCron's share of the whole computer's CPU capacity, not of a single core; it can therefore be much lower than the process's "% Processor Time" counter in Performance Monitor, which counts each core as 100%
- `OSRAM`: physical memory in use on the whole computer (%), across all processes, calculated as total physical memory minus available physical memory; this is not the memory used by VisualCron

:::note

The memory used by the VisualCron Server process itself is not part of any default health level. A separate _VC Server memory (%)_ condition type is available if you want to add it, but by default a Bad or Very bad level caused by memory always refers to the memory usage of the whole computer.

:::

| Level | Name | Conditions |
|:-----:| ---- | ---------- |
| ![Five green bars](../../../static/img/bar_516.png) | Excellent | `OSCPU <= 25% and VCCPU <= 10%` |
| ![Four green bars](../../../static/img/bar_416.png) | Good | `OSCPU > 25% or VCCPU > 10%` |
| ![Three bars, red to yellow](../../../static/img/bar_316.png) | Ok | `OSCPU > 50% or VCCPU > 20% or OSRAM > 80%` |
| ![Two bars, red and orange](../../../static/img/bar_216.png) | Bad | `OSCPU > 80% or VCCPU > 60% or OSRAM > 90%` |
| ![One red bar](../../../static/img/bar_116.png) | Very bad | `OSCPU > 90% or VCCPU > 80% or OSRAM > 95%` |

:::warning

When the built-in default conditions change in a new VisualCron version, customized health conditions are automatically reset to the new defaults. If you have tuned your thresholds, review the **_Settings_** tab after upgrading.

:::

### How the health level is decided

- Server statistics are sampled approximately once per second while a Client is subscribed to Server statistics, and once every three seconds otherwise. The health level is re-evaluated on every sample.
- By default each level is evaluated against a single, instantaneous sample. There is no averaging and no minimum duration, so a brief CPU spike is enough to change the level, and the level can change back on the very next sample. This is why the diagram often shows the level alternating between two neighboring levels.
- Levels are evaluated from worst to best, and the first level whose conditions match is the one reported. The level therefore reflects the worst matching condition, not a combined score.
- Because the _Good_ level is defined on CPU only, a computer with low CPU usage but high memory usage moves directly between _Ok_ and _Excellent_ and never reports _Good_. This is expected behavior.
- Each of the OSCPU, VCCPU and OSRAM conditions can optionally be given a _Duration_ and an _Average value_ option in the **_Settings_** tab. Adding a duration prevents momentary spikes from changing the level.

### Troubleshooting a Bad or Very bad level

The health level reports the state of the computer, so a level that stays at Bad or Very bad for a long period means the underlying value really is above the threshold, and not that the indicator is stale.

To find the cause:

1. In the _Health events_ section, read the _Reason for change_ column of the newest row. It contains the condition that matched, together with the measured values, for example:

   `OSCPU > 90% or VCCPU > 80% or OSRAM > 95% : OSCPUStatus:7.70 > 90 OR VCServerCPUStatus:0.13 > 80 OR OSRAMStatus:95.08 > 95`

   In this example both CPU values are far below their thresholds and only OSRAM is over the limit, so the cause is the memory usage of the computer.

2. Open [Server Monitor](../tools/server-monitor) to see the current _Total memory used_, _Total memory available_ and _VisualCron memory usage_ values side by side.

3. Open [Task Manager](../tools/task-manager), select the **_System processes_** tab and sort by the _Working set_ column to find the process that holds the memory. Sort by _CPU_ if a CPU condition is the one that matched.

4. Run the _Server: Computer_ report from the [Reports](../reports) menu to see the history of memory and CPU use and confirm whether the value is climbing over time.

:::note

The health level is informational. No Job or Task run is prevented, delayed or throttled because of it. The health level is acted upon only in a load balancing setup, where it can be used to select the best Server Agent or as a [load balancing condition](../servers/load-balancing-conditions).

:::

Raising the thresholds in the **_Settings_** tab makes the indicator report a better level, but it does not change the resource usage that triggered it. Where the reported values are genuinely high, address the resource usage on the computer instead.
