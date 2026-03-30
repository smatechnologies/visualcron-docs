---
sidebar_label: 'Task IIS - Add Web Site'
hide_title: 'true'
---

## Task IIS - Add Web Site

With the Task IIS - Add Web Site you can create a new web site on a local or remote IIS server. The task provides full control over site bindings, logging configuration, connection limits, virtual directory credentials, and failed request tracing.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20web%20site.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Site name**

The name of the new web site. This field is required and must be unique within the IIS instance.

**Application pool name**

The name of the existing application pool to assign to this web site. Click the *Refresh* button to populate the dropdown with available application pools from the connected server.

**Physical path**

The local file system path to the root folder of the web site's content. Click the folder button to browse for a path.

### Binding

The binding defines how IIS listens for incoming requests for this site.

**Protocol**

The protocol used for the binding, typically `http` or `https`. When set to `https`, the Certificate field becomes available.

**IP address**

The IP address on which the site listens. Use `*` to bind to all IP addresses on the server.

**Port**

The TCP port number the site listens on. This field is required. Common values: `80` for HTTP, `443` for HTTPS.

**Host name**

An optional host header value (e.g., `www.example.com`) used for name-based virtual hosting. Leave blank to accept requests for any host name on the bound IP and port.

**Certificate**

When the protocol is `https`, select the SSL/TLS certificate to use for the binding. The certificate must already be installed on the target server.

### Logging

**Log file enabled**

When checked, IIS will write access logs for this site. When unchecked, logging is disabled.

**Log file directory**

The folder path where IIS writes log files for this site. Click the folder button to browse for a path.

**Log file format**

The format used for log files. Options:

- *Iis* — Microsoft IIS format (fixed ASCII text fields).
- *Ncsa* — NCSA Common Log File format.
- *W3c* — W3C Extended Log File format (default). Allows customizable fields.
- *Custom* — Custom log format.

**Log file rollover period**

Controls how often IIS creates a new log file. Options:

- *Max Size* — A new log file is created when the current file reaches the size specified in *Log file truncate size*.
- *Daily* — A new log file is created each day.
- *Weekly* — A new log file is created each week.
- *Monthly* — A new log file is created each month.
- *Hourly* — A new log file is created each hour.

**Log file truncate size**

The maximum log file size (in bytes) before IIS rolls over to a new file. Only used when *Log file rollover period* is set to *Max Size*.

**Log file local time rollover**

When checked, log file rollovers are based on local server time. When unchecked, UTC time is used.

**Log fields (W3C)**

A multi-select list of fields to include in W3C-format log entries. Available fields include: Date, Time, Client IP, User name, Site name, Computer name, Server IP, Method, Uri Stem, Uri Query, Http Status, Win32 Status, Bytes Sent, Bytes Recv, Time Taken, Server Port, User Agent, Cookie, Referer, Protocol Version, Host, Http SubStatus.

**Log target (W3C)**

Specifies where W3C log data is written. Options:

- *File* — Log entries are written to a log file on disk.
- *ETW* — Log entries are sent to the Windows Event Tracing for Windows (ETW) subsystem.

Both options can be selected simultaneously.

### Virtual Directory

**Logon method**

The authentication method used when IIS accesses the physical path on behalf of users. Options:

- *Interactive* — Creates an interactive logon. Provides full access to network resources available to the user account.
- *Batch* — Creates a batch logon. Used for background processes.
- *Network* — Creates a network logon. Credentials are not cached locally; suitable for accessing remote network resources.
- *Clear text* — Passes credentials in clear text. Use only when required by downstream systems.

**Credential**

Select a stored VisualCron Credential to use when IIS accesses the physical path. Click the *Settings* icon to open *Manage credentials*. Leave blank to use the application pool identity.

### Limits

**Connection timeout**

The time (in seconds) that IIS keeps an idle connection open before closing it. Leave blank to use the IIS default.

**Max bandwidth**

The maximum network bandwidth (in bytes per second) that the site may use. Leave blank to set no limit.

**Max connections**

The maximum number of simultaneous connections allowed for the site. Leave blank to set no limit.

**Max URL segments**

The maximum number of URL path segments that IIS accepts in a request URL. Leave blank to use the IIS default.

### Trace failed requests logging

**Enabled**

When checked, IIS will log detailed trace information for failed requests to assist with troubleshooting.

**Directory**

The folder path where failed request trace log files are written. Click the folder button to browse for a path.

**Max log files**

The maximum number of failed request trace log files to retain. Older files are deleted when the limit is reached.

:::info Note
The site name and binding port are the minimum required fields. A physical path is also required. All other settings are optional and fall back to IIS defaults when left blank.
:::
