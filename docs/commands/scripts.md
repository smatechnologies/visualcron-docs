---
sidebar_label: 'Scripts'
hide_title: 'true'
---

## Scripts

With a script you can automate almost anything in Windows. This page is for anyone who runs scripts from VisualCron. It shows which Task to use for each kind of script, and how to run PHP and VBScript scripts.

Use these Tasks:

- [PowerShell Task](../client-user-interface/server/job-tasks-task-process-powershell): PowerShell code typed in the Task, or a PowerShell file
- [Execute Script Task](../client-user-interface/server/job-tasks-task-process-execute-script): VBScript and JScript files, or VBScript code typed in the Task
- [.NET Code Execute Task](../client-user-interface/server/job-tasks-task-process-dot-net-code-execute): C# or VB.NET code
- [Execute Task](../client-user-interface/server/job-tasks-task-process-execute): any other interpreter, such as PHP or Perl, started with its own program file

To run a script that is on a web server, use the [HTTP Task](../client-user-interface/server/job-tasks/net-tasks/http) to send a GET or POST request to it.

### Using PHP for scripting

PHP is a free scripting language that can, for example, work with databases, read and process files, and send email. You can download it from [php.net](https://www.php.net/).

To run a PHP script, add an [Execute Task](../client-user-interface/server/job-tasks-task-process-execute) and set:

- _Command_: the full path to "php.exe", for example "C:\php\php.exe"
- _Arguments_: `-q` and then the full path to the script, for example `-q "C:\Scripts\report.php"`

`-q` suppresses HTTP header output when PHP runs as CGI. With the command-line "php.exe" it has no effect, but it does no harm. The console window is hidden because _Run in hidden window_ is selected, which is the default.

If the script uses relative paths, select _Working directory_ and enter the folder those paths start from. When _Working directory_ is not selected, the script does not run in its own folder, so its relative paths can point to the wrong place.

![Execute tab of an Execute Task, with Command set to c:\php\php.exe, Arguments set to -q c:\yourscript.php, Working directory selected with no folder, and Run in hidden window selected](../../static/img/Commands%20Scripts%20and%20Third%20Party%20Tools/Scripts.png)

### Using VBScript for scripting

VBScript is a Windows scripting language. Microsoft has deprecated it, so for new scripts consider the [PowerShell Task](../client-user-interface/server/job-tasks-task-process-powershell). VisualCron still runs existing VBScript scripts, as long as VBScript is available on the Server computer.

The easiest way is the [Execute Script Task](../client-user-interface/server/job-tasks-task-process-execute-script). It runs the script with "cscript.exe" in a hidden window. By default, it keeps what the script writes as the Task's output, and the Task fails if the script writes to standard error (see the **_On error_** tab). You have two ways to give it the script:

- Select _Script file_ and enter the full path to the script in _File path_. Put quotes around a path that contains spaces
- Select _Script text_ and type the script

![Execute script tab of an Execute Script Task, with No Credential selected, the Script file and File path fields, and Script text selected with an empty script editor](../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/Execute%20Script.png)

To use the Execute Task instead, set _Command_ to "C:\Windows\System32\cscript.exe" and _Arguments_ to `"C:\Scripts\dosomething.vbs" //NoLogo`.

:::warning

Use "cscript.exe", not "wscript.exe". The "wscript.exe" host shows the script's messages, such as `WScript.Echo`, in message boxes instead of writing them as output. The Task output then stays empty, and a message box that nobody closes keeps the Task running until it is stopped, or until its timeout if one is set.

If you enter a ".vbs" or ".js" file in _Command_ of an Execute Task, the Client offers to move it to _Arguments_ and set _Command_ to "wscript.exe". If you accept, change _Command_ to "C:\Windows\System32\cscript.exe" afterwards.

:::

### Third-party tools

You can use VisualCron to start other programs, for example a backup program at a set time. Use the [Execute Task](../client-user-interface/server/job-tasks-task-process-execute). By default it runs the program in a hidden window, under the account of the VisualCron service or the Credential selected in _Run Task as_. With the default settings, a program that waits for someone to type or click does not get that input. If a program behaves differently than when you start it yourself, see [Windows Command Does Not Execute Correctly](../troubleshooting/windows-command-does-not-execute).

To suggest a tool, see [Commands, Scripts, and Third Party Tools](commands-scripts-third-party-tools).

#### NirCmd

NirCmd is a free command-line utility from NirSoft. It performs many small Windows actions without showing a window, for example changing registry values, creating shortcuts or turning off the monitor. Download it from [nirsoft.net](https://www.nirsoft.net/utils/nircmd.html).