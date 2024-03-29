---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

See general information about Maintenance and priority support at: [https://www.visualcron.com/maintenance.aspx](https://www.visualcron.com/maintenance.aspx).
 
VisualCron licenses are perpetual, but in order to get the latest version and receive support you need an active Maintenance. Each license has a Maintenance expiration date. Usually, this is one year after purchase and can be renewed [here](https://www.visualcron.com/order.aspx). The Maintenance expiration date is covering any version released within that time period, minor or major version.
 
This is what you get with an active Maintenance:

* Support
* Upgrades (minor or major)
* Ability to deactivate / move a license
 
**Online/Offline validation**

From time to time we validate the license. Both that the actual activation code is valid and the Maintenance is covering the current version. If our servers cannot be reached you need to do a manual validation from time to time.We strongly recommend that you open firewall to host visualcron.com on port 443 so this can be validated and updated without you having to do a manual validation.
 
If you fail to validate VisualCron will either stop working or you will not be able to connect to the Server with the Client.
 
 
### Troubleshooting
 
*Maintenance expiration date is not refreshing*

Normally, VisualCron refreshes the Maintenance expiration date that you see on the Server row in the main grid of the Client. You can also force this refresh by right clicking on Server row and select Refresh license data. Make sure that VisualCron can connect to Internet against hostname visualcron.com on port 443. If you still have problems with refreshing the maintenance expiration date please follow these steps:
 
1. Close the VisualCron Client
2. Right click on the VisualCron Tray Client and choose Client->Open log folder
3. Move up one folder to the VisualCron folder. Enter the settings folder.
4. Exit the VisualCron Tray Client application
5. Delete the file servers.xml
6. Start the VisualCron Tray Client
7. Start the VisualCron Client.