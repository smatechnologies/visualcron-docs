---
sidebar_label: 'Connection - Crystal reports'
hide_title: 'true'
---

## Connection - Crystal reports

The Crystal reports Connection stores connect and logon properties for database connections to Crystal reports.
 
The Crystal reports Connection is used in Crystal reports Tasks. In the Task, one or more Connections can be selected depending on how many database connections your report uses.
 
### Runtime binaries

Please note that in order to use the Crystal reports Task from a machine where VisualCron is installed you need to download and install the runtime for Crystal reports. Select the appropriate and latest version below depending on if you have a 32 or 64 bit machine.
[https://wiki.scn.sap.com/wiki/display/BOBJ/Crystal+Reports%2C+Developer+for+Visual+Studio+Downloads](https://wiki.scn.sap.com/wiki/display/BOBJ/Crystal+Reports%2C+Developer+for+Visual+Studio+Downloads)
 
For 8.3.0 and later you need version 21:
[http://downloads.businessobjects.com/akdlm/crnetruntime/clickonce/CRRuntime_32bit_13_0_21.msi](http://downloads.businessobjects.com/akdlm/crnetruntime/clickonce/CRRuntime_32bit_13_0_21.msi)
[http://downloads.businessobjects.com/akdlm/crnetruntime/clickonce/CRRuntime_64bit_13_0_21.msi](http://downloads.businessobjects.com/akdlm/crnetruntime/clickonce/CRRuntime_64bit_13_0_21.msi)
 
For 9.9.7 and later you need version 30:
[https://origin.softwaredownloads.sap.com/public/file/0020000000195592021](https://origin.softwaredownloads.sap.com/public/file/0020000000195592021) (x32)
[https://origin.softwaredownloads.sap.com/public/file/0020000000195602021](https://origin.softwaredownloads.sap.com/public/file/0020000000195602021) (x64)
 
**Manage Connections > Add > Crystal reports > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Crystal%20Reports/Crystal%20Reports.png)

**Name**

Use any name you like to identify this Connection among other Connections

**Group**

The group that the connection is a part of
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Code page**

Code page being used.
 
**Manage Connections > Add > Crystal reports > Connection Settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Crystal%20Reports/Settings.png)

**Address**

This must match the exact name of the ODBC/OLEDB connection name in ODBC administration window. Please note that this ODBC/OLEDB DSN name must exist in the System DSN tab as these are the only DSNs available across users. If your report uses connections from the User DSN you need to copy those to the System DSN. The database that you use is specified in the ODBC/OLEDB DSN.

**Username**

The username must match the same user that you use in the ODBC/OLEDB administration window.
 
**Password**

You need to set the password of the ODBC/OLEDB DSN.
 
**Integrated security**

Check this if you want to use Windows authentication against the database. For username and password use the Windows user.
 
**Debugging**

If you turn on Extended debugging in Server settings->Log you will be able to look at the log after execution and see what went wrong. Usually, it is one of the following problems:
 
1. the Address property does not match the name in System DSN
2. the ODBC/OLEDB DSN has only been created in user DSN and not the required System DSN
3. the Crystal reports document has not been updated to use the System DSN (but only uses User DSN)
4. the username or password do not match the one for the database
5. one or more Connections are missing in VC (if the Crystal report uses more than one)
 
### Troubleshooting

*Could not load file or assembly 'CrystalDecisions.ReportAppServer.ClientDoc, Version=13.0.2000.0'*
In the IIS Manager on the server - set the application pool for my web application to not allow 32-bit assemblies or run the following script: ```C:\inetpub\AdminScripts\adsutil.vbs SET w3svc/AppPools/Enable32bitAppOnWin64 0 –```