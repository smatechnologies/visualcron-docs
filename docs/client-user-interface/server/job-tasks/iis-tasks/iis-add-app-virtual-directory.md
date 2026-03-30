---
sidebar_label: 'Task IIS - Add App Virtual Directory'
hide_title: 'true'
---

## Task IIS - Add App Virtual Directory

With the Task IIS - Add App Virtual Directory you can add a virtual directory to an existing application within an IIS web site. A virtual directory maps a URL path segment to a physical folder on disk, allowing content from different locations to appear under a single web site.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20app%20virtual%20dir.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site that contains the target application. Click the *Refresh* button to populate the dropdown with available web sites from the connected server.

**Application name**

The path of the application within the web site to which the virtual directory will be added (e.g., `/myapp`). After selecting a web site, click the *Refresh* button to populate the dropdown with available applications. This field is required.

**Virtual directory path**

The virtual URL path of the new directory within the application (e.g., `/images`). This is the URL segment under which the physical path's content will be accessible.

**Physical path**

The local file system path that the virtual directory maps to. Click the folder button to browse for a path.

**Logon method**

The authentication method used when IIS accesses the physical path on behalf of users. Options:

- *Interactive* — Creates an interactive logon. Provides full access to network resources available to the user account.
- *Batch* — Creates a batch logon. Used for background processes.
- *Network* — Creates a network logon. Credentials are not cached locally; suitable for accessing remote network resources.
- *Clear text* — Passes credentials in clear text. Use only when required by downstream systems.

**Credential**

Select a stored VisualCron Credential to use when IIS accesses the physical path. Click the *Settings* icon to open *Manage credentials*. Leave blank to use the application pool identity.

:::info Note
Both the web site and the parent application must already exist on the target IIS server before this task runs. Select the web site first, then refresh the application list to see applications available within that site.
:::
