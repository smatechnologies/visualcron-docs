---
sidebar_label: 'Connection - Microsoft Graph'
hide_title: 'true'
---

## Connection - Microsoft Graph

The Microsoft Graph Connection uses the Microsoft Graph API to access Microsoft 365 mailboxes. It supports both **app-only** (client credentials) and **delegated** (interactive user sign-in) authentication via OAuth 2.0. Use this connection type for Exchange Online / Microsoft 365 mailboxes as a modern replacement for IMAP4, POP3, and Exchange EWS protocols.

:::tip Note

Microsoft is [retiring Basic Authentication for SMTP AUTH](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-retire-basic-auth-for-client-submission-smtp-auth/4114750) in Exchange Online. Microsoft Graph is the recommended protocol for new integrations with Microsoft 365.

:::

### Supported operations

The Microsoft Graph connection can be used with the following tasks and triggers:

* **Email - Send** — send text and/or HTML emails with attachments, S/MIME, or PGP encryption
* **Email - Get Headers** — retrieve message headers (Subject, Date, To, From)
* **Email - Get Messages** — retrieve one or more full messages with attachments
* **Email - Get Single Message** — retrieve a single message by ID
* **Email - Delete Messages** — delete one or more messages by filter criteria
* **Email - Delete Single Message** — delete a single message by ID
* **Email - Move/Copy Messages** — move or copy messages between folders
* **Event Trigger - Mail** — monitor a mailbox for incoming messages

### Azure app registration

Before creating a Microsoft Graph connection in VisualCron, you must register an application in Azure Active Directory. This app registration provides the Client ID and Client Secret used for authentication.

1. Log into the [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory** > **App registrations**
3. Click **New registration**

**Supported account types:**

* **Single tenant** — accounts in your organization's directory only
* **Multi-tenant** — accounts in any Azure AD directory (requires Microsoft approval)

**Redirect URI:**

Set the platform to **Web** and the URI to `http://localhost:9999`.

4. Note the **Application (client) ID** and **Directory (tenant) ID** from the app overview page
5. Navigate to **Certificates & Secrets** > **New client secret** and create a secret. Copy the secret value immediately — it cannot be revealed again after creation.

### API permissions

Configure permissions under **API permissions** in your app registration.

**For delegated access (interactive sign-in):**

Add **Microsoft Graph** > **Delegated permissions**:
* `Mail.ReadWrite`
* `Mail.Send`
* `User.Read`

**For app-only access (client credentials):**

Add **Microsoft Graph** > **Application permissions**:
* `Mail.ReadWrite`
* `Mail.Send`

Grant admin consent for the permissions after adding them.

### Connection settings

**Manage Connections > Add > Microsoft Graph > Common settings** tab

**Test**

It is possible to test the connection once you have set all settings. Click the Test button to start the test.

**Name**

The unique name for the Connection.

**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time is passed.

**Code page**

The table of values that describes the desired character set. Currently this is overridden by the code page in the Task.

**Manage Connections > Add > Microsoft Graph > Connection settings** tab

**Authentication**

Select the authentication method. OAuth is the recommended method for Microsoft Graph connections.

**Use app-only (client credentials)**

When checked, VisualCron uses the client credentials OAuth flow (no interactive sign-in required). This is suitable for background services and automation scenarios where no user is present. When unchecked, delegated authentication is used which requires an interactive sign-in.

**Username (Application ID)**

The Application (client) ID from your Azure app registration. This is a GUID in the format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

**Password (Client Secret)**

The client secret value from your Azure app registration.

**Email**

The mailbox email address to access (e.g., `user@contoso.com`). For app-only mode, this specifies which user's mailbox to operate on. For delegated mode, this identifies the signed-in user's mailbox.

**Authenticate**

Click to authenticate the connection.

* **App-only mode**: validates that a token can be acquired using the client credentials flow.
* **Delegated mode**: opens an interactive sign-in dialog where the user grants consent to the requested permissions.

**Manage Connections > Add > Microsoft Graph > Cloud App settings** tab

**OAuth Redirect URL**

The redirect URI configured in your Azure app registration. Default: `http://localhost:9999`.

**Tenant ID**

The Azure AD Directory (tenant) ID. If left empty, VisualCron uses the `common` endpoint for multi-tenant scenarios. If provided, authentication is restricted to the specified tenant.

**Tenant Primary Domain**

The primary domain of the tenant (e.g., `contoso.com`). If provided, the sign-in page is redirected to the tenant-specific login endpoint.

**Accept All Certificates**

When checked, SSL/TLS certificate validation is skipped. Leave unchecked for production environments.

**Manage Connections > Add > Microsoft Graph > Encryption** tab

**Cryptographic protocol**

Encryption protocol to use; No encryption, SSL or TLS.

**Allowed SSL/TLS versions**

Check the SSL/TLS versions that are allowed for connections to the Microsoft Graph endpoint.

**Manage Connections > Add > Microsoft Graph > Proxy** tab

**Proxy type**

Select the proxy type to be used.

**Address**

The host name or IP address of the proxy server.

**Port**

The port of the proxy server.

**Use credentials**

The credentials that are associated with the account.

**Domain**

The name of the domain to be created.

**Username**

The user name to access the proxy server.

**Password**

The password to access the proxy server.

### Troubleshooting

**Authentication fails with "insufficient privileges"**

Verify that the correct API permissions have been granted in the Azure app registration and that admin consent has been granted. For app-only mode, ensure **Application permissions** (not Delegated) are configured.

**Token acquisition succeeds but mail operations fail**

For app-only access, ensure `Mail.ReadWrite` and `Mail.Send` application permissions are granted with admin consent. The `User.Read` permission alone is not sufficient for mail operations.

**"AADSTS700016: Application not found" error**

Verify that the Application (client) ID is correct and that the app registration exists in the specified tenant. If using a Tenant ID, confirm it matches the directory where the app is registered.

**Connection works but cannot access a shared mailbox**

For app-only mode, specify the shared mailbox email address in the **Email** field. App-only permissions apply across all mailboxes in the tenant. For delegated mode, the signed-in user must have access to the shared mailbox.
