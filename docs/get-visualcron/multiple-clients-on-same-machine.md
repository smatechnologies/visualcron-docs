---
sidebar_label: 'Multiple Clients on the Same Machine'
hide_title: 'true'
---

## Multiple Clients on the Same Machine

It is never recommended to install multiple Clients on the same machine, regardless if the Server is also installed on the same machine or not. Normally, Clients work best if the corresponding Server version is the same as the Client version. This is because new features might be introduced in either Client or Server. If the version is not the same across the board, there might be misunderstandings in the communication between Client and Server. This can result in unwanted settings or behavior.
 
VisualCron is built to support one version of the Client installed on a server. If you install both the Client and the Server it is guaranteed that that version is the same.

If you want to install multiple versions of Client on one machine (to be able to Connect to multiple versions of Server) there is one workaround for that*.
 
1. find the corresponding Client version for download [here](https://www.visualcron.com/Login.aspx?DestinationPageUrl=~/OldVersions.aspx) and download it to the Client computer
2. extract the exe file with tool like 7zip into a folder
3. copy that folder to a location where you would like it to be installed
4. right click on the VisualCronClient.exe file and create a shortcut
5. copy that shortcut to desktop and then we recommend that you rename it with the version number like "VisualCron - Client (12.3.1)" or similar

* the above steps work for versions up to v12.1.4 with the Custom Installation. For v12.2.1+, it is recommended to download the custom install, then running the following command within command prompt with elevated permissions: 

msiexec /a "C:\Users\SpecificUser\Desktop\VisualCron.msi" /qb TARGETDIR="C:\Users\SpecificUser\Desktop\Folder"

This is installing the VisualCron software into a specific folder location that's different from the default location. From there, we would follow steps 4 and 5 in the instructions above.

