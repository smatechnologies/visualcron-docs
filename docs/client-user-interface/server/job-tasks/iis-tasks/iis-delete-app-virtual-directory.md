---
sidebar_label: 'Task IIS - Delete App Virtual Directory'
hide_title: 'true'
---

## Task IIS - Delete App Virtual Directory

With the Task IIS - Delete App Virtual Directory you can remove a virtual directory from an existing application within an IIS web site. This task is useful for automated cleanup after deployments or for removing content mappings that are no longer needed.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Delete%20an%20existing%20app%20virtual%20dir.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site that contains the target application. Click the *Refresh* button to populate the dropdown with available web sites from the connected server. This field is required.

**Application name**

The path of the application within the web site that owns the virtual directory to be removed (e.g., `/myapp`). After selecting a web site, click the *Refresh* button to populate the dropdown with available applications. This field is required.

**Virtual directory**

The virtual path of the directory to delete from the application (e.g., `/images`). After selecting a web site and application, click the *Refresh* button to populate the dropdown with available virtual directories. This field is required.

:::info Note
Deleting a virtual directory removes the IIS path mapping only. The physical folder and files it pointed to remain on disk and are not deleted.

Select the web site first, then refresh the application list, then select the application before refreshing the virtual directory list.
:::
