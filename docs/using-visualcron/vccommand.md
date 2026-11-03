---
sidebar_label: 'VCCommand'
hide_title: 'true'
---

## VCCommand

VCCommand is a command-line tool that works with a VisualCron Server without the Client. Use it from scripts, batch files or another scheduler to run a Job or a Task, activate, deactivate or stop a Job, list Jobs and Tasks, or activate and deactivate the license. This page is for administrators who script VisualCron.

VCCommand connects to the Server like the [VisualCron API](visualcron-api) does, either on the same computer or over the network. It acts as the VisualCron user it logs on as, so what it can do depends on that user's permissions (see [Main - User Permissions](../client-user-interface/server/main-user-permissions)).

"VCCommand.exe" is installed in the "VCCommand" folder of the VisualCron installation folder, by default "C:\Program Files (x86)\VisualCron\VCCommand".

### Syntax

```bat
VCCommand.exe --action <action> [--connectionmode local|remote] [--ip <server>] [--port <port>] [--logontype visualcron|ad] [--username <user>] [--password <password>] [--name "<job or task name or Id>"] [--upn <upn> | --spn <spn>] [--activationcode <activation code>]
```

### Switches

| Switch | Short form | Values | Default | Required |
|---|---|---|---|---|
| `--action` | `-a` | One of the actions below | None | Yes |
| `--connectionmode` | `-c` | `local` or `remote` | `local` | No |
| `--ip` | `-i` | Name or IP address of the Server | None | With `remote` |
| `--port` | None | Port number of the Server | `16444` | No |
| `--logontype` | `-l` | `visualcron` or `ad` | `visualcron` | No |
| `--username` | `-u` | VisualCron user name | None | Unless `--logontype ad` |
| `--password` | `-p` | Password of that user | Empty | No |
| `--name` | `-n` | Id or name of the Job, or of the Task for `runtask` | None | For `runjob`, `runtask`, `activatejob`, `deactivatejob` and `stopjob` |
| `--upn` | None | User principal name that identifies the Server | None | No |
| `--spn` | None | Service principal name that identifies the Server | None | No |
| `--activationcode` | `-r` | Activation code of the license | None | For `activate` |

Switch names are not case sensitive, but type the values of `--action`, `--connectionmode` and `--logontype` in lowercase. VCCommand ignores switches it does not recognize, so a misspelled switch has no effect. A `--logontype` value other than `ad` is treated as `visualcron`.

### Actions

| Action | What it does |
|---|---|
| `runjob` | Runs the Job, checks its Conditions, and waits until the Job finishes |
| `runtask` | Runs the Task, checks its Conditions, and waits until the Task finishes. The Task's output is not printed |
| `activatejob` | Activates the Job and prints a status line |
| `deactivatejob` | Deactivates the Job, prints the `--name` value, then prints a status line |
| `stopjob` | Sends a stop request for the Job and prints `Job '<job name>' has been sent a Stop request.` The line does not confirm that the Job was running or has stopped |
| `listjobs` | Prints one line per Job: the Job Id and the Job name, separated by a tab |
| `listtasks` | Prints one line per Task: Job Id, Job name, Task Id and Task name, separated by tabs |
| `activate` | Activates the Server's license online with the code in `--activationcode`, and prints the activation code. When VCCommand runs from a Task, the code is then in the Task output. Stops with an error if the Server is already activated. That error also shows the current activation code |
| `deactivate` | Deactivates the Server's license online. Stops with an error if the Server is not activated |

:::note

The status line that `activatejob` and `deactivatejob` print can show the Job's state from before the change. To confirm the new state, check the Job in the Client.

:::

### Choosing the Job or Task

`--name` takes an Id or a name. VCCommand first looks for a Job with that Id (for `runtask`, a Task with that Id). If there is none, it looks for a name that matches exactly, including case, and uses the first match it finds. For `runtask`, the name search covers the Tasks of every Job. Use `listjobs` and `listtasks` to find the Ids.

:::warning

If two Jobs share a name, or two Tasks in different Jobs share a name, running by name can start the wrong one. Use the Id in scripts.

:::

### Connecting to the Server

- `--connectionmode local` connects to the Server on the same computer. `--ip` and `--port` are not used
- `--connectionmode remote` connects over the network to the Server at `--ip`. When VCCommand runs on another computer, the Server must accept remote connections: _Only allow local connections_ must be cleared (see [Settings - Users/Logon](../client-user-interface/server/settings-users-logon)), and the Server's port must be open in any firewall between the two computers
- Without `--connectionmode`, VCCommand uses `local` and prints a message saying so

With `--logontype ad`, VCCommand logs on with the Windows account that runs it, and no user name or password is needed. _Allow Active Directory Logon_ must be selected on the Server (see [Settings - Users/Logon](../client-user-interface/server/settings-users-logon)), and the account must be allowed in [Main - User Permissions](../client-user-interface/server/main-user-permissions) as an AD user or through an AD group.

`--upn` and `--spn` tell Windows which identity to expect for the Server. They apply only together with `--connectionmode remote` and `--logontype ad`. In any other case, VCCommand prints a message and ignores them. If you give both, `--upn` is used.

### Output and exit codes

VCCommand first prints connection details, then the result of the action. When `runjob` or `runtask` runs, the last line is one of:

- `Job '<job name>' ran with success`
- `Job '<job name>' ran with failure (<exit code>)`
- `Job '<job name>' could not be started, reason: <reason>`
- `Task '<task name>' ran with success`
- `Task '<task name>' ran with failure (<exit code>)`
- `Task could not be run.`
- `Task not found.`

The reason can be "Queued": the Job then runs later, and VCCommand does not wait for it. `Task could not be run.` and `Task not found.` mean that the Server did not run the Task it was asked to run. These lines also appear when the user that VCCommand logs on as does not have Execute permission on the Job or Task. For `runjob`, the reason is then "Not started". All of these lines come with exit code "0". When the Server refuses `activatejob` or `deactivatejob` for lack of permission, VCCommand also prints the status line and exits with code "0". To confirm the change, check the Job in the Client.

| Exit code | Meaning |
|---|---|
| "0" | VCCommand performed the action. For `runjob` and `runtask`, the Job or Task may still have failed or not started |
| "1" | VCCommand could not perform the action: a required switch is missing or a value is not recognized, the connection or logon failed, no Job or Task matches `--name`, or an error occurred while the action ran. VCCommand prints example command lines and then the reason |
| Any other code | VCCommand stopped with an unexpected error before it could perform the action |

:::warning

A Job or Task that fails still gives exit code "0". If a script or another scheduler must react to a failure, check the last output line, not only the exit code.

:::

Some messages name a switch differently:

- When a message names `--option`, use `--action`
- When a message names `--ac`, use `--activationcode`
- When `runtask` finds no Task that matches `--name`, the message reads "No Job with that name or Id was found." and the exit code is "1"

To print example command lines, run "VCCommand.exe" without switches. It then stops with exit code "1", because no user name is given.

### Examples

```bat
REM Run, activate, deactivate and stop a Job on the local Server
VCCommand --action runjob --connectionmode local --username admin --password xyz --name "<job name or Id>"
VCCommand --action activatejob --connectionmode local --username admin --password xyz --name "<job name or Id>"
VCCommand --action deactivatejob --connectionmode local --username admin --password xyz --name "<job name or Id>"
VCCommand --action stopjob --connectionmode local --username admin --password xyz --name "<job name or Id>"

REM Run a Task or a Job with the remote connection mode (here to the same computer)
VCCommand --action runtask --ip 127.0.0.1 --connectionmode remote --username admin --password xyz --name "<task name or Id>"
VCCommand --action runjob --ip 127.0.0.1 --connectionmode remote --username admin --password xyz --name "<job name or Id>"

REM List Jobs, and list Tasks with Windows logon
VCCommand --action listjobs --connectionmode local --username admin --password xyz
VCCommand --logontype ad --action listtasks --connectionmode local

REM Windows logon to a remote Server, with the Server identity
VCCommand --logontype ad --upn svc-vc@contoso.com --action listtasks --ip vcserver.contoso.com --connectionmode remote --port 16444
VCCommand --logontype ad --spn HOST/vcserver.contoso.com --action listtasks --ip vcserver.contoso.com --connectionmode remote --port 16444

REM Activate and deactivate the license
VCCommand --action activate --activationcode <activation code> --connectionmode local --username admin --password xyz
VCCommand --action deactivate --connectionmode local --username admin --password xyz
```