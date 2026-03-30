---
sidebar_label: 'Task IIS - Add Application Pool'
hide_title: 'true'
---

## Task IIS - Add Application Pool

With the Task IIS - Add Application Pool you can create a new application pool on a local or remote IIS server. Application pools isolate web applications for better reliability and security by running each pool in its own worker process.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20application%20pool.png)

**Connection**

Select the IIS Connection that defines the target server. Click the *Settings* icon to open *Manage connections* in order to add or edit IIS Connections.

**Application pool name**

The name of the new application pool to create. This field is required.

**Managed pipeline mode**

Sets the pipeline mode for the application pool. Options:

- *Integrated* — The application pool uses the unified IIS and ASP.NET request-processing pipeline. This is the recommended mode for most applications.
- *Classic* — The application pool uses a separate ASP.NET request-processing pipeline, compatible with older applications.

**Managed runtime version**

Specifies the version of the .NET Common Language Runtime (CLR) loaded by the worker process. Options:

- *Without managed code* — The application pool does not load a managed runtime. Use this for native code or non-.NET applications (e.g., PHP, Node.js).
- *v2.0* — Loads the .NET Framework 2.0/3.0/3.5 runtime.
- *v4.0* — Loads the .NET Framework 4.x runtime.

**Start mode**

Controls when the worker process for this application pool is started. Options:

- *On demand* — The worker process starts when the first request is received. This is the default behavior.
- *Always running* — The worker process starts automatically when IIS starts, regardless of incoming requests. Useful for applications that require constant availability (e.g., WCF services, background processing).

**Auto start**

When checked, the application pool starts automatically when IIS starts or when the application pool is created. When unchecked, the pool must be started manually.

**Enable 32-bit applications on 64-bit Windows**

When checked, allows 32-bit applications to run on a 64-bit operating system. Enable this setting only if your application requires a 32-bit environment. When unchecked, 64-bit mode is enforced.

**Queue length**

The maximum number of requests that HTTP.sys will queue for the application pool before returning a 503 (Service Unavailable) response to clients. Leave blank to use the IIS default value (1000).

:::info Note
The IIS Connection account must have sufficient privileges to create application pools on the target server. Typically this requires local Administrator or IIS Manager User role membership.
:::
