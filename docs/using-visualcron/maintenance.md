---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

See general information about Maintenance and priority support at: [https://www.visualcron.com/maintenance.aspx](https://www.visualcron.com/maintenance.aspx).
 
In order to get the latest version and receive support you need an active Maintenance or Subscription. Each license has an expiration date. Usually, this is one year after purchase and can be renewed here. The expiration date covers any version released within that time period, minor or major version.
 
This is what you get with an active Maintenance:

* Support
* Upgrades (minor or major)
* Ability to deactivate / move a license
* Access to all tasks that require an active maintenance
    - Reports provides built-in system reporting and task features to track server health, job history, and automation performance. You can view summaries directly in the user interface or automate external reporting tools like Crystal Reports and SQL Server Reporting Services (SSRS).
    - Return on Investment (ROI) is a feature that tracks and calculates the money and time saved by automating scheduled jobs.
    - Server Monitor is a built-in tool in the VisualCron client interface that tracks live performance data, resource usage, and job activity across your automation environments
    - Server Sync allows you to automatically or manually synchronize jobs and global objects between two or more VisualCron servers.
    - You can run VisualCron in a high-availability setup by using the built-in VisualCron Failover Cluster via Windows Server Failover Clustering (WSFC). This ensures your scheduled tasks and automation jobs to keep running if a primary server node fails.
    - Job Report Task generates automatic documents based on job and task execution stats, server health, performance metrics, and log entries. It lets you output data to a file, email, or physical printer as part of a scheduled automation workflow

Read more at: https://help.visualcron.com/
 
**Online/Offline validation**

From time to time, we validate the license. Both that the actual activation code is valid and the Maintenance or Subscription is covering the current version. If our servers cannot be reached you need to do a manual validation from time to time. We strongly recommend that you open firewall to host visualcron.com on port 443 so this can be validated and updated without you having to do a manual validation.
 
If you fail to validate, VisualCron will either stop working or you will not be able to connect to the Server with the Client.
 
 
### Troubleshooting
 
*Maintenance expiration date is not refreshing*

Normally, VisualCron refreshes the Maintenance or Subscription expiration date that you see on the Server row in the main grid of the Client. You can also force this refresh by right clicking on Server row and select Refresh license data. Make sure that VisualCron can connect to Internet against hostname visualcron.com on port 443. If you still have problems with refreshing the maintenance expiration date please follow these steps:
 
1. Close the VisualCron Client
2. Right click on the VisualCron Tray Client and choose Client->Open log folder
3. Move up one folder to the VisualCron folder. Enter the settings folder.
4. Exit the VisualCron Tray Client application
5. Delete the file servers.xml
6. Start the VisualCron Tray Client
7. Start the VisualCron Client.