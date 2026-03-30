---
sidebar_label: 'Task IIS - Add Web Site Application'
hide_title: 'true'
---

## Task IIS - Add Web Site Application

With the Task IIS - Add Web Site Application you can add a new application to an existing IIS web site. A web application is a logical unit within a site that has its own application pool assignment, physical path, and URL entry point.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20application.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site to which the application will be added. Click the *Refresh* button to populate the dropdown with available web sites from the connected server.

**Application URL**

The virtual URL path within the web site at which the application is mounted (e.g., `/myapp`). This becomes the application's root within the site.

**Application pool name**

The name of the application pool to assign to this application. Click the *Refresh* button to populate the dropdown with available application pools from the connected server. This field is required.

**Enabled protocols**

A comma-separated list of protocols enabled for this application (e.g., `http`, `https`, `net.tcp`). Leave blank to inherit the site's default protocol.

**Physical path**

The local file system path to the root folder of the application's content. Click the folder button to browse for a path.

**Logon method**

The authentication method used when IIS accesses the physical path. Options:

- *Interactive* — Creates an interactive logon. Provides full access to network resources available to the user account.
- *Batch* — Creates a batch logon. Used for background processes.
- *Network* — Creates a network logon. Credentials are not cached locally; suitable for accessing remote network resources.
- *Clear text* — Passes credentials in clear text. Use only when required by downstream systems.

**Credential**

Select a stored VisualCron Credential to use when IIS accesses the physical path. Click the *Settings* icon to open *Manage credentials*. Leave blank to use the application pool identity.

:::info Note
The application pool name is required. The web site name must already exist on the target IIS server before this task runs.
:::
