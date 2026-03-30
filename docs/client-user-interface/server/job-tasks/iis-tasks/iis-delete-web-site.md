---
sidebar_label: 'Task IIS - Delete Web Site'
hide_title: 'true'
---

## Task IIS - Delete Web Site

With the Task IIS - Delete Web Site you can permanently remove an existing web site from a local or remote IIS server. This task is useful for automated environment teardown, cleanup after testing, or decommissioning a site as part of a deployment pipeline.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Delete%20an%20existing%20web%20site.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site to delete. This field is required.

:::info Note
Deleting a web site removes the site configuration from IIS but does not delete the physical files on disk. The content folder and its files remain at their original location and must be removed separately if required.

The site name comparison is case-insensitive.
:::
