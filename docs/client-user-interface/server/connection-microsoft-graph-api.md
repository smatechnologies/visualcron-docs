---
sidebar_label: 'Connection - Microsoft Graph API'
hide_title: 'true'
---

## Connection - Microsoft Graph API

The Microsoft Graph API Connection uses the Microsoft Graph REST API to send, receive, and manage email in Microsoft 365 and Exchange Online mailboxes. It is the recommended replacement for the [Exchange EWS](connection-exchange-ews) connection, which Microsoft is retiring for Exchange Online on October 1, 2026.

The connection is reusable across email tasks and the email trigger. Once it is set up, no per-run sign-in is required; the only ongoing maintenance is renewing the client secret or certificate before it expires.

**Manage Connections > Add > Microsoft Graph API**

<!-- Screenshot pending: Microsoft Graph API connection editor (Main settings tab) -->

### Choosing an authentication model

The connection supports two authentication flows and two credential types. Pick the combination that matches how your Azure app registration is set up.

**Auth flow**

* **App-only (client credentials)** — the connection authenticates as the application itself using an application permission grant. No user sign-in is required at any point; the token is acquired automatically at run time and refreshed as needed. Use this for unattended, server-side automation. This is the recommended flow for scheduled jobs.
* **Delegated (interactive)** — the connection authenticates as a signed-in user. You sign in once in the connection editor; the resulting token is stored and refreshed for later runs. Use this when your tenant policy requires delegated access or when app-only permissions cannot be granted.

**Credential type**

* **Client secret** — authenticates with the application (client) secret created in Azure.
* **Certificate** — authenticates with a certificate instead of a secret. Select the certificate in the certificate picker.

The editor shows and hides fields based on these two selections. Client secret and certificate fields are mutually exclusive. Redirect URL and Tenant primary domain appear only for the Delegated flow.

### Main settings

**Auth flow**

Select **App-only (client credentials)** or **Delegated (interactive)**. See [Choosing an authentication model](#choosing-an-authentication-model) above.

**Credential type**

Select **Client secret** or **Certificate**.

**Application (Client) Id**

The Application (client) ID of your Azure app registration. Required. See [How to set up the app in Azure](#how-to-set-up-the-app-in-azure) below.

**Tenant Id**

The Directory (tenant) ID of your Azure app registration. Required.

**Mailbox / Email**

The email address of the mailbox this connection will work with, for example `user@contoso.onmicrosoft.com`. Required.

**Client secret**

The application secret (client secret value) created in Azure. Shown only when **Credential type** is **Client secret**. Required for that credential type. For security, the stored secret is not displayed back after saving; leave the field on its placeholder to keep the existing secret, or type a new value to replace it.

**Certificate**

The certificate used for authentication. Shown only when **Credential type** is **Certificate**. Required for that credential type. Use the picker to select an installed certificate.

**Redirect URL**

The redirect URI registered for your app in Azure. Shown only when **Auth flow** is **Delegated (interactive)**. It must match a redirect URI configured on the app registration exactly, for example `http://localhost`.

**Tenant primary domain**

The primary domain of the tenant, for example `contoso.com`. Shown only when **Auth flow** is **Delegated (interactive)**.

**Authenticate / Test Authentication**

The button label depends on the selected flow:

* In **Delegated** mode the button reads **Authenticate**. Click it to open an interactive Microsoft sign-in. On success the token is stored with the connection and refreshed automatically for later runs.
* In **App-only** mode the button reads **Test Authentication**. Click it to acquire a token from Microsoft using the configured credentials and confirm the connection works. No interactive sign-in occurs.

### Proxy

Configure an HTTP proxy here if outbound access to Microsoft Graph must go through one.

**Proxy type**

Select the proxy type to be used.

**Address**

The host name or IP address of the proxy server.

**Port**

The port of the proxy server.

**Use credentials**

The credentials that are associated with the proxy account.

**Username**

The user name to access the proxy server.

**Password**

The password to access the proxy server.

## How to set up the app in Azure

Both authentication flows require an app registration in Microsoft Entra ID (Azure Active Directory).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) or the Azure portal and open **Microsoft Entra ID > App registrations**.
2. Choose **New registration**, give the app a name, and select the supported account types for your organization. Register the app.
3. On the app **Overview** page, note the **Application (client) ID** and the **Directory (tenant) ID**. You will enter these in the connection.
4. Create a credential:
   * **Client secret:** open **Certificates & secrets > Client secrets > New client secret**. Set an expiry and create it. Copy the secret **Value** immediately; it cannot be retrieved after you leave the page. Enter this value in the connection's **Client secret** field.
   * **Certificate:** upload the public key under **Certificates & secrets > Certificates**, and make sure the matching certificate is installed where the VisualCron server can read it. Select it in the connection's **Certificate** field.
5. Grant Microsoft Graph permissions under **API permissions > Add a permission > Microsoft Graph**:
   * For **App-only (client credentials)**, add **Application permissions**: `Mail.ReadWrite` and `Mail.Send` (add `Mail.ReadWrite.Shared` if you work with shared mailboxes). Application permissions require an administrator to click **Grant admin consent**.
   * For **Delegated (interactive)**, add the equivalent **Delegated permissions** and, under **Authentication**, add a **Redirect URI** (for example `http://localhost`) that matches the **Redirect URL** field in the connection.

Client secrets expire on the schedule you set in Azure. When a secret or certificate expires the connection stops working, so plan to rotate it before the expiry date. VisualCron does not send an automatic expiry notification; you can build an error-triggered job to alert you if a connection begins to fail.

## Migrating from Exchange EWS

Existing email tasks and triggers can be repointed from an [Exchange EWS](connection-exchange-ews) connection to a Microsoft Graph API connection without rebuilding them. Note one exception: folder identifiers are protocol-specific, so any place that references a folder (the email trigger, Move Messages, and similar) must have its folder reselected after switching the connection. Message IDs passed between tasks through variables carry over unchanged.

## Troubleshooting

* **Authentication succeeds but tasks return 4xx errors** — the app registration is missing the required Microsoft Graph permissions, or admin consent has not been granted. Confirm `Mail.ReadWrite` and `Mail.Send` are present and consented for the flow you are using.
* **App-only test fails immediately** — recheck the Application (client) ID, Tenant Id, and that the client secret **Value** (not the secret ID) was entered. Confirm the secret has not expired.
* **Delegated sign-in cannot complete** — the **Redirect URL** in the connection must match a redirect URI on the app registration exactly, including scheme and port.
* **Folder not found after migrating from EWS** — reselect the folder in the trigger or task; EWS and Graph folder identifiers are not interchangeable.
