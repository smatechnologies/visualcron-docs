---
sidebar_label: 'Connection - IIS'
hide_title: 'true'
---

## Connection - IIS

The IIS Connection stores the host and authentication properties required for VisualCron to connect to and manage Internet Information Services (IIS) on a local or remote Windows server.

### About IIS

Internet Information Services (IIS) is Microsoft's web server platform built into Windows Server. It hosts web sites, web applications, and web services, and is managed through the IIS Manager console or programmatically via the `Microsoft.Web.Administration` API. VisualCron uses this API over the connection you define here to perform IIS management tasks such as creating application pools, managing web sites, and controlling site and pool state.

### IIS Connection settings

**Manage Connections > Add > IIS > Main** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/IIS.png)

**Name**

A descriptive name for the connection used to identify it in the connection list and within tasks.

**Group**

The group this connection belongs to. Groups help organize connections when many exist.

**Timeout**

The connection timeout in seconds. The operation will fail if the target does not respond within this time.

**Manage Connections > Add > IIS > Connection Settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/Settings.png)

**Address**

The hostname or IP address of the Windows server running IIS. Use `localhost` or leave blank to target the local machine. For remote servers, enter the server's hostname or IP address (e.g., `webserver01` or `192.168.1.100`).

**Username**

The Windows user account used to authenticate against the target IIS server. The account must have sufficient permissions to perform IIS management operations (typically local Administrator or IIS Manager User role membership on the target server).

**Password**

The password for the specified Windows user account. Credentials are stored encrypted within VisualCron.

:::info Note
For remote IIS management, ensure that Windows Remote Management (WinRM) or the appropriate firewall rules allow the connection from the VisualCron server to the target machine. The account used must have the necessary IIS management permissions on the remote server.
:::

### Troubleshooting

**Access is denied**

The user account specified in the connection does not have sufficient permissions on the target IIS server. Ensure the account is a member of the local Administrators group or has been granted IIS Manager User access on the target server.

**Cannot connect to remote server**

Verify that the target hostname or IP address is correct and reachable from the VisualCron server. Confirm that Windows Firewall or network firewall rules allow the required traffic between the two machines.

**IIS management operations fail on a remote server**

Remote IIS management requires the IIS Management Service (`WMSVC`) to be running and configured to allow remote connections on the target server. Enable this in IIS Manager under **Management Service** feature settings.
