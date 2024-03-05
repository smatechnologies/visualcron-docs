---
sidebar_label: 'Job Does Not Run'
hide_title: 'true'
---

## Troubleshooting

### My Job does not run!

If your Job does not run then check this list, in the following order:
 
1. Is the Job active? If the icon for the Job in the Job list is red, then right click on the row and select Activate.

2. Is the VisualCron Server "On"? If the Start/Stop toolbar icon shows Start, click on the icon/button to Start the server.

3. Can you run the Job manually? Right click on the Job and select _Run Job_. If it does run then look at the time settings. What does next run say? Alter your time settings. If your Job does not run when you select Run Job then the command line or parameters might be wrong, please check.

4. Log in the server log and the output column if the Task. Perhaps you can find the error there.

5. Is your command and argument correct? You need to separate the argument from the command in the two fields. You can not write ```"C:\php\php.exe -q myscript.php"``` in the command line, in this case the command line must be ```"C:\php\php.exe"``` and the argument ```"-q myscript.php".```
 
You can turn on debug for the server, see [show log](showlog) and [log to file](logtofile) for more information. 

Run the Job manually again and the open the log file. 

Open the log file with the corresponding date. This log file may say something about the error. 

If you believe that the error is in VisualCron itself then send the log file to [support@visualcron.com](support@visualcron.com). 

Remember to turn debug off after turning it on because an activated debug option slows down VisualCron.