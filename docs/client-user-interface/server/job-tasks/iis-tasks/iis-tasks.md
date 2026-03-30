---
sidebar_label: 'IIS Tasks'
hide_title: 'true'
---

## IIS Tasks

The IIS Tasks in VisualCron allow you to automate the management of Internet Information Services (IIS) on local or remote servers. Using an IIS Connection, you can create, configure, control, and remove IIS components — including application pools, web sites, web applications, and virtual directories — as part of any automated job workflow.

All IIS Tasks require an **IIS Connection** that defines the target server and credentials used to interact with IIS.

### Available IIS Tasks

| Task | Description |
|------|-------------|
| [Task IIS - Add Application Pool](iis-add-application-pool.md) | Creates a new IIS application pool with configurable pipeline mode, runtime version, and start mode settings. |
| [Task IIS - Add Web Site](iis-add-web-site.md) | Creates a new IIS web site with full control over bindings, logging, connection limits, virtual directory credentials, and failed request tracing. |
| [Task IIS - Add Web Site Application](iis-add-web-site-application.md) | Adds a new application to an existing IIS web site, assigning it an application pool, URL path, physical path, and enabled protocols. |
| [Task IIS - Add App Virtual Directory](iis-add-app-virtual-directory.md) | Adds a virtual directory to an existing application within an IIS web site, mapping a virtual path to a physical folder with optional credentials. |
| [Task IIS - Change Application Pool State](iis-change-application-pool-state.md) | Starts, stops, or recycles an existing IIS application pool. |
| [Task IIS - Change Web Site State](iis-change-web-site-state.md) | Starts, stops, or restarts an existing IIS web site. |
| [Task IIS - Delete Application Pool](iis-delete-application-pool.md) | Permanently removes an IIS application pool from the server. |
| [Task IIS - Delete Web Site](iis-delete-web-site.md) | Permanently removes an IIS web site from the server. |
| [Task IIS - Delete Web Site Application](iis-delete-web-site-application.md) | Removes an application from an existing IIS web site. |
| [Task IIS - Delete App Virtual Directory](iis-delete-app-virtual-directory.md) | Removes a virtual directory from an application within an IIS web site. |
| [Task IIS - Is Application Pool Exists](iis-is-app-pool-exists.md) | Checks whether a named IIS application pool exists on the target server and returns the result to the task output. |

### IIS Connection

All IIS Tasks require a configured **IIS Connection**. The connection defines the target IIS server (local or remote) and the credentials used to authenticate and perform management operations. Connections are managed under *Server > Connections* and can be created or edited using the *Settings* icon available in each task's connection selector.

:::info Note
IIS management operations require that the account used by the IIS Connection has sufficient permissions on the target server (typically local Administrator or IIS Manager privileges).
:::
