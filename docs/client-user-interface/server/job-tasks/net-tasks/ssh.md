---
sidebar_label: 'Task Net - SSH'
hide_title: 'true'
---

## Task Net - SSH

The SSH Task lets you execute commands on a remote SSH server through the Command Channel of SSH. SSH servers are standard in Linux and exists on all kinds of operating systems. This lets you extend the execution to other operating systems.
 
In computing, Secure Shell or SSH is a set of standards and an associated network protocol that allows establishing a secure channel between a local and a remote computer. It uses public-key cryptography to authenticate the remote computer and (optionally) to allow the remote computer to authenticate the user. SSH provides confidentiality and integrity of data exchanged between the two computers using encryption and message authentication codes (MACs). SSH is typically used to log into a remote machine and execute commands.
 
VisualCron can, with the SSH Task, connect to a remote computer and execute commands securely via SSH. All output is captured and returned to the output of the Task.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/SSH.png)

**Command type**

You can execute one or more commands after each other. When one command is done, the next command in order is executed. The output of each command is added to the output of the Task. If you need to separate the output from the different commands, then add a new Task for each command.
 
Send command: This is a high-level method that connects to server, executes command and gets the entire response. Use this method to execute a simple command which does not require client-server interaction.
Send text: Use SendText to send a string data through the logical connection.
 
**Connection**

Before entering any command you must create a Connection. Click on *Manage Connections* to add a new Connection. Select SSH connection and alter connection settings. There are some specific settings for the SSH connection like if there is support for SSH1 or SSH2.
 
To add a new Command click on Add. Enter the Command in the text field and click on OK to save it.

If you are using Command type *Send command*, the environment variables are not picked up automatically but you can specify them in the text field.

