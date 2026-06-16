---
sidebar_label: 'VisualCron API'
hide_title: 'true'
---

## VisualCron API

The VisualCron API is an easy way to control the VisualCron Server. The .NET API is as powerful as the VisualCron Client. The Client itself uses the API to perform all actions.
 
You can find the API documentation under the main menu **Help > API** selection, which provides two options: *Show documentation* (the API quick start manual) and *API reference* (the full API reference).
 
Basically, you can use these languages:

* [.NET - c# or VB.NET](dot-net-csharp-vbnet)
* [PowerShell](powershell)
 
**Visual Basic 6**

We do no longer support Visual Basic 6.

### Troubleshooting

When using the v13 DLLs, referencing the API (for example, VisualCronAPI.dll) can cause application debugging sessions to terminate with a “Debugger Detected” exception. This can make it difficult to debug personal code while referencing the VisualCron libraries. 

Q. Is this behavior expected in v13?
* Yes, this is expected behavior in v13. The "Debugger Detected" exception is an intentional change introduced in the newer version of the software. We recommend reviewing the v12+ changelog for full details on this change.

Q. How can I debug my code while referencing the v13 libraries?
* To avoid the debugger detection issue, please use the DLLs located in the following directory on your VisualCron installation:

    C:\Program Files (x86)\VisualCron\lib

The libraries in this folder are self-contained and will not trigger the debugger exception, allowing you to debug your own application as expected.

Q. Are there any additional dependencies required?
* No additional dependencies are needed. The two libraries in the directory above are self-contained — you only need those two DLLs to work with the API.

Q. Regarding VisualCron_nat.dll - is this required? 
* No additional dependency file is required. The libraries in the \lib directory are fully self-contained, so you do not need to locate or obtain any additional files to support the API.
