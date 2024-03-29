---
sidebar_label: 'Debug and Logging'
hide_title: 'true'
---

## Debug and Logging

Additional debug entries may be written into the client/server log files or sent by email.
 
See below for more information.

### Debug

 Settings for debug log entries are found in the main menu _Manage -> Manage server settings -> Log settings_ tab.
 
Additional debug and log information is available for the [server](../client-user-interface/server/main-settings) and [log function](../client-user-interface/server/information-log).

### Send Email

The main email settings are found in the main menu Manage -> Manage server settings -> Email settings. Additional [email setting](../client-user-interface/server/main-settings) information is available.
 
For each Job that shall use the Notification email feature, the Notification options are checked for the specific Job/Task in the Edit/Add Job -> Notifications or the Edit/Add Task -> Notifications tabs.

### Technical Information

#### Some Important VisualCron Related Folders and Their Usage

| Folder Name | Usage |
|-------------|-------|
| C:\WINDOWS\system 32\ | See [Remote and Customized Installation](../get-visualcron/remote-silent-customized-installation) |
| C:\Program Files\VisualCron\ | VisualCron Default Installation Folder |
| C:\Program Files\VisualCron\backup\VC-Settings.zip | Default File Name For Exported Settings |
| C:\Program Files\Program Files\VisualCron\data\triggers\mail\\{MailId}\\{MailID}.eml | Default File Name For a Saved Email |
| C:\Program Files\VisualCron\log\ | Default Log File Folder, See [Settings](../client-user-interface/server/main-settings) For More Information |
| C:\Program Files\VisualCron\settings\jobs.xml | Default Job Settings File |
| C:\Program Files\VisualCron\settings\timeexceptions.xml | Default File Name For Time Exceptions|
| C:\Program Files\VisualCron\settings\users.xml | Default Users File Name, See "[Forgot My Password](../troubleshooting/forgot-my-password)" for more information |
| C:\php\php.exe | Normal PHP File Name, See [PHP Scripting](../commands/scripts) For More Information |