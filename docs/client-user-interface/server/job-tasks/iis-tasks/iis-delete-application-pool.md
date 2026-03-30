---
sidebar_label: 'Task IIS - Delete Application Pool'
hide_title: 'true'
---

## Task IIS - Delete Application Pool

With the Task IIS - Delete Application Pool you can permanently remove an existing application pool from a local or remote IIS server. This is useful for automated cleanup after deployments or when decommissioning web applications.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Delete%20an%20existing%20app%20pool.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Application pool name**

The name of the existing application pool to delete. Click the *Refresh* button to populate the dropdown with available application pools from the connected server. This field is required.

:::info Note
Deleting an application pool that is still assigned to one or more web sites or applications will leave those sites and applications without a valid pool assignment. Ensure that no active sites or applications depend on the pool before deleting it, or reassign them first.
:::
