---
sidebar_label: 'Task IIS - Change Web Site State'
hide_title: 'true'
---

## Task IIS - Change Web Site State

With the Task IIS - Change Web Site State you can start, stop, or restart an existing web site on a local or remote IIS server. This task is useful for automating maintenance windows, controlled deployments, or any workflow that requires managing site availability.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Change%20state%20of%20the%20web%20site.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Web site name**

The name of the existing IIS web site whose state you want to change. Click the *Refresh* button to populate the dropdown with available web sites from the connected server. This field is required.

**Operation**

The state change operation to perform on the web site. Options:

- *Nothing* — No operation is performed. Use this as a placeholder or for testing.
- *Start* — Starts the web site if it is currently stopped. IIS begins accepting requests for the site's bindings.
- *Stop* — Stops the web site. IIS stops accepting new requests for the site's bindings. Active connections may be dropped.
- *Restart* — Stops and then immediately starts the web site. Use this to apply configuration changes or clear transient issues without permanently disabling the site.

:::info Note
Stopping or restarting a web site causes it to be temporarily unavailable. Users accessing the site during this period will receive an HTTP 503 (Service Unavailable) or a connection refused error. Plan maintenance operations accordingly.
:::
