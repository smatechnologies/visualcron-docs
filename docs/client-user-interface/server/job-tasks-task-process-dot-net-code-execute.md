---
sidebar_label: 'Task Process - .NET Code Execute'
hide_title: 'true'
---

## Task Process - .NET Code Execute

The Process - .NET code execute Task is able to execute .NET code using languages C# or VB.NET.
 
You are able to use Variables wherever in the code and parameters. The output of the method is converted to string. The purposes of this Task could be many but you could use it to solve a specific problem for you (when no existing Task can do that for you).
 
The code is compiled in real time for each execution.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/NET%20Code%20Execute.png)0896

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Language**

Select either C# or VB.NET language. The syntax editor and compile methods will alter depending on selected language.
 
**Edit references..**

Add/remove any dll that you want to use as a reference to make our code work or be more compact.
 
**Code**

In this text box you insert your code. It is important that:

* The code exists in a class
* That you use static/shared methods only

Any return value will be converted to a string.
 
**Method selection**

Select the method you want to use. After you have added new code please press "Refresh methods" button.
 
**Compile**

This button tests if the code can compile and will return a popup with error if not.
 
**Refresh methods**

This button compiles the codes and add all existing static methods into the method combo box.
 
**Run**

This button compiles and runs the code so you can test it.
 
**Parameters**

If the selected method contains any parameter can double click on the row to add your own parameter value.
 
**Troubleshooting**
 
**An error occured: Could not find a part of the path 'local path to tmp file'**

Try closing the application. Go to VisualCron installation folder. Right click on VisualCronClient.exe and select "Run as administrator". Then try again.