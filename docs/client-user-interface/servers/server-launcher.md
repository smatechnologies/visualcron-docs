---
sidebar_label: 'Server Launcher'
hide_title: 'true'
---

## Server Launcher

**Server Launcher** is a utility that runs several VisualCron Server instances from a single installation, each with its own settings. It is used to prepare and test a [Load Balancer](load-balancer) configuration on one computer before the same configuration is applied to production Servers.

Because each instance has its own identifier and port, a Broker and its Server Agents can be set up on a single host. This allows Scheduler role switching, Agent selection and distributed execution to be tried out before any production Server is changed.

:::note

Instances added in the utility run as console applications under the account that started them. They are not Windows Services, so they do not start with the computer and they end when the account signs out. Use the utility for testing and demonstration, not to run a production Server.

:::

### Starting the utility

Server Launcher is installed with the VisualCron Server. To start it, run *ServerLauncher.exe* from the VisualCron Server installation folder. By default this folder is *C:\Program Files (x86)\VisualCron*.

The main window has a ribbon with two tabs, *VC Server* and *VC Client*, above a grid of running and configured Server instances. The status bar shows how many of the listed instances are running.

The grid lists two kinds of row:

* Instances configured in the utility, whether they are running or not.
* VisualCron Server processes found running on the computer, including the installed Windows Service and any instance started outside the utility.

On a computer with a standard installation, the grid contains a single row for the installed Server, with *Run mode* set to *Service* and the *Name* column showing the computer name.

The grid updates itself when a Server process starts or stops. Select *Refresh* on the *VC Server* tab to re-read the list at any time.

### Reading the Servers grid

The following columns are shown by default:

| Column | Description |
|---|---|
| *(selection)* | Marks the row for the *Start selected*, *Stop selected* and *Kill selected* actions. |
| *(status)* | A connected icon when the instance is running and a disconnected icon when it is stopped. Point at the icon to see *Running* or *Stopped*. |
| *ServerId* | The identifier the instance runs under. For the installed Server this is the identifier from its license. |
| *Run mode* | *Service* for the installed Windows Service, *Console* for an instance added in the utility, and *WinExe* for a Server started as a window application. |
| *Name* | The display name. If no Name was entered, the ServerId is shown instead. |
| *Port* | The port the instance listens on. |
| *Start time* | When the process started. Empty for a stopped instance. |
| *Username* | The account the process runs under. |
| *Base folder* | The folder the program file was started from. |

Select *Show all columns* to add the remaining columns: *Process ID*, *Process name*, *Command line*, *Thread count*, *Settings folder* and *Log folder*. The button then changes to *Hide extra columns*.

The *Base folder*, *Settings folder* and *Log folder* cells each have a button that opens that folder. If the folder no longer exists, a *Directory not found* message is shown instead.

### Configuring an additional Server

To add a Server instance, complete the following steps:

1. On the *VC Server* tab, select *Add server*.
2. In the *VC Server process configuration* window, confirm that *Path* points to the VisualCron Server program file. The path to the installed Server is filled in for you.
3. Select the button in the *ServerId* field to generate an identifier, or enter one manually.
4. Enter a *Name* for the instance.
5. Enter the *Port* the instance is to listen on.
6. Select *Save*.

The new instance appears in the grid as a stopped row. To change it later, activate its row and select *Edit*, or double-click the row.

Each configured Server uses the following values:

**Path**

The VisualCron Server program file to start. The file must exist, otherwise the configuration cannot be saved.

**Run mode**

Always *Console* for an instance added in the utility, and cannot be changed. This is why the installed Windows Service can be started and stopped from the grid but not edited.

**ServerId**

A unique identifier for the instance. Select the button in the input field to generate one automatically, or enter one manually.

If entered manually, the value must be in GUID format, that is `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`, where each `X` is a hexadecimal digit (`0-9`, `A-F`).

Leaving *ServerId* empty starts the Server with its normal identity and its normal settings, rather than as an additional instance. *Name* and *Port* are then unavailable, because both belong to an additional instance.

**Port**

A unique port for the instance. No two running instances can share a port, and none of them can use the port the installed Server is already listening on. The default port of an installed Server is `16444`.

If *Port* is left empty, the instance uses the port from its own Server settings.

**Name**

An optional display name. If no Name is entered, the Name shown in the grid is the ServerId, which makes instances harder to tell apart. Enter a Name to keep the grid readable.

**Other settings**

Any additional command line arguments to pass to the instance, entered as they would be typed on a command line. Leave this empty unless an argument has been recommended for a specific test.

:::note

The values for an instance can only be edited while that instance is stopped.

:::

The *Run mode*, *ServerId*, *Name*, *Port* and *Other settings* values are passed to the Server instance as command line arguments when it starts.

#### Example: a Broker and two Agents on one computer

To try out a Load Balancer configuration on a single computer, add three instances alongside the installed Server, for example:

| Name | ServerId | Port |
|---|---|---|
| Broker | Generated | `16445` |
| Agent 1 | Generated | `16446` |
| Agent 2 | Generated | `16447` |

Start all three instances, then start one VisualCron Client for each and connect them to *localhost* on ports `16445`, `16446` and `16447`. From there the configuration is the same as on separate computers: activate the Broker on the first instance, connect the other two to it as Server Agents, and set the execution mode on a Job. See [Deploying Load Balancing](load-balancing-deployment) for the order of configuration.

The installed Server on port `16444` can be left running as a fourth Server or stopped, as long as its port is not reused by one of the added instances.

### Starting and stopping instances

The *Control* group on the *VC Server* tab acts on the rows marked in the selection column:

* *Start selected*, *Stop selected* and *Kill selected* apply to every marked row. If no row is marked, a *No rows have been selected* message is shown.
* *Stop all & Exit* stops every instance in the grid and then closes the utility.

Use *Select all*, *Deselect all* and *Invert* in the *Selection* group to change the marked rows.

To act on a single instance, right-click its row. The row menu contains *Start*, *Stop*, *Kill*, *Restart*, *Edit* and *Remove*, and only the actions that apply to that instance are available:

| Action | Available when |
|---|---|
| *Start* | The instance is stopped. |
| *Stop*, *Kill*, *Restart* | The instance is running. |
| *Edit* | The instance is stopped and its Run mode is *Console*. |
| *Remove* | The instance is stopped. |

*Stop* asks the instance to shut down and waits up to five seconds for it to end. *Kill* ends the process immediately, without letting the Server shut down. Use *Stop* first and keep *Kill* for an instance that does not respond.

If an action fails, a message with *Abort*, *Retry* and *Ignore* is shown. *Retry* repeats the action on the same instance, *Ignore* continues with the next marked row, and *Abort* stops without processing the remaining rows.

### Starting the VisualCron Client

The VisualCron Client can be started directly from the utility, using *Start new client* on the *VC Client* tab. Start one Client for each instance to be inspected, and connect each of them to *localhost* on that instance's port.

If the Client program file is not found, a message is shown and a file dialog opens so that the correct path can be chosen. The chosen path is remembered for later starts.

When *Auto close client on launcher exit* is active, every Client started from the utility is closed when the utility exits. A close message is sent to the Client main window first, and if the Client has not closed within 3 seconds its process is ended. If a Client cannot be closed, a warning is shown as the utility exits.

### Customizing the Servers grid

Use the column chooser button above the row selectors to choose which columns are displayed, or select *Show all columns* on the ribbon to display all available columns. Select a column header to sort the grid by that column, and hold Shift while selecting further headers to sort by more than one column.

The colour theme of the utility always matches the theme selected in the VisualCron Client.

The window size and position, the configured instances and the state of *Auto close client on launcher exit* are kept between sessions. Select *Reset settings* to return the utility to its defaults and clear the configured instances. A confirmation is requested first. Instances that are running at the time stay in the grid because they are still found on the computer.

### Where instance files are kept

| Item | Location |
|---|---|
| Utility settings | *C:\Users\\[USERNAME]\AppData\Local\VisualCron\settings\settings_serverlauncher.xml* |
| Settings of an instance with a ServerId | A subfolder named after the ServerId, inside the Server settings folder. By default this is *C:\Program Files (x86)\VisualCron\settings\\[SERVERID]*. |
| Log of an instance with a ServerId | *C:\Program Files (x86)\VisualCron\log\\[SERVERID]*, unless another log folder is set in that instance's own Server settings. |

Because each additional instance keeps its settings in its own folder, its Jobs, Credentials and Connections are separate from those of the installed Server and of the other instances. Use the buttons in the *Settings folder* and *Log folder* columns to open these folders for a selected instance.
