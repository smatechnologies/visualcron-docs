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

Server Launcher is installed with the VisualCron Server. To start it, run `ServerLauncher.exe` from the VisualCron Server installation folder. By default this folder is `C:\Program Files (x86)\VisualCron`.

The main window has a ribbon with two tabs, _VC Server_ and _VC Client_, above a grid of running and configured Server instances. The status bar shows how many of the listed instances are running.

The grid lists two kinds of row:

* Instances configured in the utility, whether they are running or not.
* VisualCron Server processes found running on the computer, including the installed Windows Service and any instance started outside the utility.

On a computer with a standard installation, the grid contains a single row for the installed Server, with _Run mode_ set to _Service_ and the _Name_ column showing the computer name.

The grid updates itself when a Server process starts or stops. Select _Refresh_ on the _VC Server_ tab to re-read the list at any time.

### Reading the Servers grid

The following columns are shown by default:

| Column | Description |
|---|---|
| _(selection)_ | Marks the row for the _Start selected_, _Stop selected_ and _Kill selected_ actions. |
| _(status)_ | A connected icon when the instance is running and a disconnected icon when it is stopped. Point at the icon to see _Running_ or _Stopped_. |
| _ServerId_ | The identifier the instance runs under. For the installed Server this is the identifier from its license. |
| _Run mode_ | _Service_ for the installed Windows Service, _Console_ for an instance added in the utility, and _WinExe_ for a Server started as a window application. |
| _Name_ | The display name. If no Name was entered, the ServerId is shown instead. |
| _Port_ | The port the instance listens on. |
| _Start time_ | When the process started. Empty for a stopped instance. |
| _Username_ | The account the process runs under. |
| _Base folder_ | The folder the program file was started from. |

Select _Show all columns_ to add the remaining columns: _Process ID_, _Process name_, _Command line_, _Thread count_, _Settings folder_ and _Log folder_. The button then changes to _Hide extra columns_.

The _Base folder_, _Settings folder_ and _Log folder_ cells each have a button that opens that folder. If the folder no longer exists, a _Directory not found_ message is shown instead.

### Configuring an additional Server

To add a Server instance, complete the following steps:

1. On the _VC Server_ tab, select _Add server_.
2. In the _VC Server process configuration_ window, confirm that _Path_ points to the VisualCron Server program file. The path to the installed Server is filled in for you.
3. Select the button in the _ServerId_ field to generate an identifier, or enter one manually.
4. Enter a _Name_ for the instance.
5. Enter the _Port_ the instance is to listen on.
6. Select _Save_.

The new instance appears in the grid as a stopped row. To change it later, activate its row and select _Edit_, or double-click the row.

Each configured Server uses the following values:

**Path**

The VisualCron Server program file to start. The file must exist, otherwise the configuration cannot be saved.

**Run mode**

Always _Console_ for an instance added in the utility, and cannot be changed. This is why the installed Windows Service can be started and stopped from the grid but not edited.

**ServerId**

A unique identifier for the instance. Select the button in the input field to generate one automatically, or enter one manually.

If entered manually, the value must be in GUID format, that is `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`, where each `X` is a hexadecimal digit (`0-9`, `A-F`).

Leaving _ServerId_ empty starts the Server with its normal identity and its normal settings, rather than as an additional instance. _Name_ and _Port_ are then unavailable, because both belong to an additional instance.

**Port**

A unique port for the instance. No two running instances can share a port, and none of them can use the port the installed Server is already listening on. The default port of an installed Server is `16444`.

If _Port_ is left empty, the instance uses the port from its own Server settings.

**Name**

An optional display name. If no Name is entered, the Name shown in the grid is the ServerId, which makes instances harder to tell apart. Enter a Name to keep the grid readable.

**Other settings**

Any additional command line arguments to pass to the instance, entered as they would be typed on a command line. Leave this empty unless an argument has been recommended for a specific test.

:::note

The values for an instance can only be edited while that instance is stopped.

:::

The _Run mode_, _ServerId_, _Name_, _Port_ and _Other settings_ values are passed to the Server instance as command line arguments when it starts.

#### Example: a Broker and two Agents on one computer

To try out a Load Balancer configuration on a single computer, add three instances alongside the installed Server, for example:

| Name | ServerId | Port |
|---|---|---|
| Broker | Generated | `16445` |
| Agent 1 | Generated | `16446` |
| Agent 2 | Generated | `16447` |

Start all three instances, then start one VisualCron Client for each and connect them to _localhost_ on ports `16445`, `16446` and `16447`. From there the configuration is the same as on separate computers: activate the Broker on the first instance, connect the other two to it as Server Agents, and set the execution mode on a Job. See [Deploying Load Balancing](load-balancing-deployment) for the order of configuration.

The installed Server on port `16444` can be left running as a fourth Server or stopped, as long as its port is not reused by one of the added instances.

### Starting and stopping instances

The _Control_ group on the _VC Server_ tab acts on the rows marked in the selection column:

* _Start selected_, _Stop selected_ and _Kill selected_ apply to every marked row. If no row is marked, a _No rows have been selected_ message is shown.
* _Stop all & Exit_ stops every instance in the grid and then closes the utility.

Use _Select all_, _Deselect all_ and _Invert_ in the _Selection_ group to change the marked rows.

To act on a single instance, right-click its row. The row menu contains _Start_, _Stop_, _Kill_, _Restart_, _Edit_ and _Remove_, and only the actions that apply to that instance are available:

| Action | Available when |
|---|---|
| _Start_ | The instance is stopped. |
| _Stop_, _Kill_, _Restart_ | The instance is running. |
| _Edit_ | The instance is stopped and its Run mode is _Console_. |
| _Remove_ | The instance is stopped. |

_Stop_ asks the instance to shut down and waits up to five seconds for it to end. _Kill_ ends the process immediately, without letting the Server shut down. Use _Stop_ first and keep _Kill_ for an instance that does not respond.

If an action fails, a message with _Abort_, _Retry_ and _Ignore_ is shown. _Retry_ repeats the action on the same instance, _Ignore_ continues with the next marked row, and _Abort_ stops without processing the remaining rows.

### Starting the VisualCron Client

The VisualCron Client can be started directly from the utility, using _Start new client_ on the _VC Client_ tab. Start one Client for each instance to be inspected, and connect each of them to _localhost_ on that instance's port.

If the Client program file is not found, a message is shown and a file dialog opens so that the correct path can be chosen. The chosen path is remembered for later starts.

When _Auto close client on launcher exit_ is active, every Client started from the utility is closed when the utility exits. A close message is sent to the Client main window first, and if the Client has not closed within 3 seconds its process is ended. If a Client cannot be closed, a warning is shown as the utility exits.

### Customizing the Servers grid

Use the column chooser button above the row selectors to choose which columns are displayed, or select _Show all columns_ on the ribbon to display all available columns. Select a column header to sort the grid by that column, and hold Shift while selecting further headers to sort by more than one column.

The color theme of the utility always matches the theme selected in the VisualCron Client.

The window size and position, the configured instances and the state of _Auto close client on launcher exit_ are kept between sessions. Select _Reset settings_ to return the utility to its defaults and clear the configured instances. A confirmation is requested first. Instances that are running at the time stay in the grid because they are still found on the computer.

:::warning

_Reset settings_ and _Remove_ delete instance configurations from the utility. _Kill_ ends a Server process without letting it shut down.

:::

### Where instance files are kept

| Item | Location |
|---|---|
| Utility settings | `C:\Users\[USERNAME]\AppData\Local\VisualCron\settings\settings_serverlauncher.xml` |
| Settings of an instance with a ServerId | A subfolder named after the ServerId, inside the Server settings folder. By default this is `C:\Program Files (x86)\VisualCron\settings\[SERVERID]`. |
| Log of an instance with a ServerId | `C:\Program Files (x86)\VisualCron\log\[SERVERID]`, unless another log folder is set in that instance's own Server settings. |

Because each additional instance keeps its settings in its own folder, its Jobs, Credentials and Connections are separate from those of the installed Server and of the other instances. Use the buttons in the _Settings folder_ and _Log folder_ columns to open these folders for a selected instance.
