---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Maintenance and subscription

This page explains what an active maintenance or subscription gives you, what stops when it expires, and where to find renewal and validation information. Read it before your maintenance or subscription ends, or when the Client reports that a feature needs an active maintenance.

See general information about Maintenance and priority support at: [https://www.visualcron.com/maintenance.aspx](https://www.visualcron.com/maintenance.aspx).
 
In order to get the latest version and receive support you need an active Maintenance or Subscription. Each license has an expiration date. Usually, this is one year after purchase and can be renewed here. The expiration date covers any version released within that time period, minor or major version.
 
This is what you get with an active Maintenance:

* Support
* Upgrades (minor or major)
* Ability to deactivate / move a license
* Access to all tasks that require an active maintenance:
 - Reports provides built-in system reporting and task features to track server health, job history, and automation performance. You can view summaries directly in the user interface or automate external reporting tools like Crystal Reports and SQL Server Reporting Services (SSRS).
 - Return on Investment (ROI) is a feature that tracks and calculates the money and time saved by automating scheduled jobs.
 - Server Monitor is a built-in tool in the VisualCron client interface that tracks live performance data, resource usage, and job activity across your automation environments
 - Server Sync allows you to automatically or manually synchronize jobs and global objects between two or more VisualCron servers.
 - You can run VisualCron in a high-availability setup by using the built-in VisualCron Failover Cluster via Windows Server Failover Clustering (WSFC). This ensures your scheduled tasks and automation jobs to keep running if a primary server node fails.
 - Job Report Task generates automatic documents based on job and task execution stats, server health, performance metrics, and log entries. It lets you output data to a file, email, or physical printer as part of a scheduled automation workflow

### Features that need an active maintenance or subscription

This is the complete list of features that need an active maintenance or subscription. They are available only while the maintenance or subscription of the Server is active, and only if its edition includes them:

* Reports, including the *Job Report* Task
* *ROI*
* *Server monitor*
* Server Sync (Master/Slave synchronization)
* *Windows Failover Cluster*
* Load balancing (*Load balancer*)
* Desktop automation (the *Robot* Task)
* *SLA*
* Server Health and Server Health settings

When the maintenance or subscription has expired, the Client no longer opens these features. It shows a *Feature not available* message, or it hides the option: the *Robot* and *Job Report* Tasks are not listed where you add a Task, and the *Settings* tab of the *Server health* window is hidden.

:::warning Jobs and Tasks stop when the maintenance or subscription expires

When the maintenance or subscription of a Server expires, the Server stops these:

* On a subscription license, all Jobs
* On a perpetual license, Jobs whose ***Agent distribution*** tab is set to anything other than *Execute locally only*, and the Server logs that each of these Jobs was not run
* On a perpetual license, *Robot* and *Job Report* Tasks, which fail with the reason in their error output
* Load balancing: Flows, the Broker if the Server acts as Broker, and the connection to a Broker if the Server is a Server Agent

To keep them running, renew before the expiration date shown in the *Expiration* column (see [Maintenance and subscription expiration](maintenance-expiration)). On a perpetual license, you can also set load-balanced Jobs to *Execute locally only* (see [Job - Agent Distribution](../client-user-interface/server/job-agent-distribution)).

:::

### License validation

VisualCron checks each license online regularly, to confirm the activation code and that the maintenance or subscription covers the installed version. For which computers need access and what to do when a check finds a problem, see [License validation](license-validation).

### What happens if I do not renew

This will depend on the license that you have: 

* Subscription licenses: VisualCron will stop executing Jobs.
* Perpetual licenses: The license itself is perpetual so it is forever but it is bound to a specific version. In order to update and get priority support, you need to renew. Also, Perpetual licenses cannot be renewed after they've expired, and a new license would have to be purchased at https://admin.visualcron.com/order.aspx.

On a perpetual license, Jobs keep running after the maintenance expires, except those listed in the warning under [Features that need an active maintenance or subscription](#features-that-need-an-active-maintenance-or-subscription).

:::warning Installing a version your license does not cover

Before you download an update, the Client warns you if your license does not cover the latest version. If you install a version that your license does not cover on a Server with a perpetual license whose maintenance has expired, the Client disconnects from that Server and reports that the license is not valid for this version.

Renew before you install, or install a version your license covers.

:::

For renewal dates and deadlines, see [License renewal coverage dates and deadlines](license-renewal-coverage-dates-and-deadlines).

### Expiration date not refreshing

To see or refresh the expiration date in the Client, see [Maintenance and subscription expiration](maintenance-expiration).
