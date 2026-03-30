---
sidebar_label: 'Task IIS - Delete Web Site Application'
hide_title: 'true'
---

## Task IIS - Delete Web Site Application

With the Task IIS - Delete Web Site Application you can remove an existing application from an IIS web site on a local or remote server. This task is useful for automated cleanup of deployed applications, environment teardown, or removing obsolete virtual applications from a site.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/delete%20an%20existing%20application.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site that contains the application to be removed. Click the *Refresh* button to populate the dropdown with available web sites from the connected server. This field is required.

**Application name**

The name (URL path) of the application to delete from the web site (e.g., `/myapp`). After selecting a web site, click the *Refresh* button to populate the dropdown with available applications within that site. This field is required.

:::info Note
Deleting a web site application removes its configuration from IIS but does not delete the physical files on disk. The content folder and its files remain at their original location.

The web site must already exist before this task runs. If the application does not exist on the specified site, the task will fail.
:::
