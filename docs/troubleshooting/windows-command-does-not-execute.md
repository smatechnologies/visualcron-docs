---
sidebar_label: 'Windows Command Does Not Execute Correctly'
hide_title: 'true'
---

## Windows Command Does Not Execute Correctly

Perhaps your program/Job is running when you double click it but not in VisualCron. Remember that commands in VisualCron are executed under the SYSTEM account, by default, which uses another environment than the ordinary user. When you double click on your command you execute it as the logged in user.
 
To produce the same result in VisualCron you need to connect a user to that Task. A user consists of a username, password and a domain/computer name - this is called a credential in VisualCron. Credentials can be centrally managed in VisualCron. You can add new credentials by choosing "Manage credentials" from the main menu. Be sure to have the right casing as it is case sensitive. Enter the username, password and computer name that you normally use when you execute this command or create a new account in the Control Panel.
 
To connect the added credential you edit your Task and select the credential (in the select box) in the add Task window. Try to execute again. Please contact support if you need further assistance.
 
**Other problems that may appear:**

You can't for example write "ftp.exe" as command line if you don't setup the environment for that.

Solution 1: point directly to the file, like C:\WINDOWS\system32\ftp.exe in the command line.

Solution 2: use C:\WINDOWS\system32\ as Working Directory and ftp.exe in the command line.

Solution 3: activate Use shell execute in the Task Execute settings. However, when using this option you can't redirect output.

_Solution 1 or 2 are the recommended solutions._