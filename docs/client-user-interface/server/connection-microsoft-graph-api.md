---
sidebar_label: 'Connection - Microsoft Graph API'
hide_title: 'true'
---

## Connection - Microsoft Graph API

The Microsoft Graph API Connection uses the Microsoft Graph REST API to send, receive, and manage email in Microsoft 365 and Exchange Online mailboxes. It is the recommended replacement for the [Exchange EWS](connection-exchange-ews) connection, which Microsoft is retiring for Exchange Online on October 1, 2026.

The Microsoft Graph API Connection stores the sign-in and security settings that these Tasks and Triggers use to connect to the mailbox through Microsoft Graph:

- [Email - Send](job-tasks/messaging-tasks/email)
- [Email - Get messages](job-tasks/messaging-tasks/email-get-messages)
- [Email - Get headers](job-tasks/messaging-tasks/email-get-headers)
- [Email - Get single message](job-tasks/messaging-tasks/email-get-single-message)
- [Email - Delete messages](job-tasks/messaging-tasks/email-delete-messages)
- [Email - Delete single message](job-tasks/messaging-tasks/email-delete-single-message)
- Email - Move messages
- The [Email Trigger](event-trigger-mail)

Once the Connection is set up, no sign-in is needed for each run.

Available from VisualCron 13.3.1.

### Choosing an authentication model

The Connection supports two authentication flows and two credential types. Pick the combination that matches your app registration.

_Auth flow_

- "Delegated (interactive)" (default): the Connection signs in as a user. You sign in once in the Connection editor; the sign-in is stored and refreshed for later runs. Use this when your tenant policy requires delegated access or when application permissions cannot be granted
- "App-only (client credentials)": the Connection signs in as the application, with an application permission grant. No user sign-in is needed; the Server gets a token at run time. Use this for unattended automation

_Credential type_

- "Client secret": the client secret of the application
- "Certificate": a VisualCron Certificate with its private key

The editor shows and hides fields based on these two selections. _Redirect URL_ and _Tenant primary domain_ appear only for "Delegated (interactive)".

### Common settings

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

_Test_ opens the _Test Microsoft Graph Connection_ window. _From email_ and _To email_ are filled in with the mailbox of the Connection. Click _Test_ in that window: the Server sends a test message with the subject "Test subject (from VisualCron)" from _From email_ to _To email_. The test does not use the ***Proxy*** tab.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

_Auth flow_ and _Credential type_

See [Choosing an authentication model](#choosing-an-authentication-model).

_Application (Client) Id_

The _Application (client) ID_ of your app registration. Required. See [How to set up the app in Azure](#how-to-set-up-the-app-in-azure).

_Tenant Id_

The _Directory (tenant) ID_ of your app registration. Required.

_Mailbox / Email_

The email address of the mailbox that the Connection works with, for example `<user>@<tenant>.onmicrosoft.com`. Required.

_Client secret_

The client secret value of the application. Shown and required for "Client secret". After saving, the stored secret is not displayed, and leaving the placeholder keeps the stored secret.

_Certificate_

Shown and required for "Certificate". Select a VisualCron [Certificate](global-certificates) that was imported as a ".pfx" file with its private key. The Windows certificate store is not used.

_Redirect URL_

Shown for "Delegated (interactive)". It has no default. Enter an address that matches a redirect URI of the app registration exactly, with a free port on the computer where the Client runs, for example `http://localhost:<port>`. The Client listens on that port during the sign-in.

_Tenant primary domain_

Shown for "Delegated (interactive)". The primary domain of the tenant, for example `<tenant>.onmicrosoft.com`. When it is empty, the Server refreshes the sign-in through the multi-tenant sign-in address, which an app registered for a single tenant does not accept. Fill it in for a single-tenant app.

_Authenticate_ / _Test Authentication_

- For "Delegated (interactive)", the button reads _Authenticate_. Click it to open a Microsoft sign-in on the Client computer. The Connection requests the delegated permissions _Mail.ReadWrite_, _Mail.Send_ and _User.Read_. On success, the sign-in is stored with the Connection and refreshed for later runs
- For "App-only (client credentials)", the button reads _Test Authentication_. Click it to open the same _Test Microsoft Graph Connection_ window as _Test_. Click _Test_ in that window to have the Server get a token and send a test message from _From email_ to _To email_. No sign-in window opens

### Proxy

The Email Tasks that read, delete or move messages, and the Email Trigger, send their mail requests through the proxy on this tab, with the "HTTP Proxy", "SOCKS4" or "SOCKS5" type.

:::warning

Email - Send, the _Test_ button, and the sign-in and token requests to Microsoft do not use the ***Proxy*** tab. Make sure that the Server can reach Microsoft Graph and the Microsoft sign-in addresses without the proxy on this tab.

:::

### How to set up the app in Azure

Both authentication flows need an app registration in Microsoft Entra ID, a credential and Microsoft Graph permissions.

To register the app, complete the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Open _Microsoft Entra ID_ -> _App registrations_.
3. Click _New registration_.
4. Enter a name for the app.
5. Select the supported account types for your organization.
6. Click _Register_.
7. On the _Overview_ page, copy the _Application (client) ID_ into _Application (Client) Id_ in the Connection.
8. Copy the _Directory (tenant) ID_ into _Tenant Id_ in the Connection.

The app is registered.

#### Create a client secret

For the "Client secret" credential type, complete the following steps:

1. In the app registration, open _Certificates & secrets_ -> _Client secrets_.
2. Click _New client secret_.
3. Set an expiry.
4. Click _Add_.
5. Copy the secret value. It cannot be shown again.
6. Enter the value in _Client secret_ in the Connection.

The Connection can now sign in with the client secret.

#### Use a certificate

For the "Certificate" credential type, complete the following steps:

1. In the app registration, open _Certificates & secrets_ -> _Certificates_.
2. Upload the public key of the certificate.
3. In the Client, import the certificate with its private key as a ".pfx" file. See [Global - Certificates](global-certificates).
4. Select the imported Certificate in _Certificate_ in the Connection.

The Connection can now sign in with the certificate.

#### Add the Microsoft Graph permissions

To add the permissions, complete the following steps:

1. In the app registration, open _API permissions_ -> _Add a permission_ -> _Microsoft Graph_.
2. Add the permissions for the _Auth flow_ of the Connection:
   - For "App-only (client credentials)", the application permissions _Mail.ReadWrite_ and _Mail.Send_
   - For "Delegated (interactive)", the delegated permissions _Mail.ReadWrite_, _Mail.Send_ and _User.Read_, and _Mail.ReadWrite.Shared_ if you work with shared mailboxes
3. For "App-only (client credentials)", have an administrator click _Grant admin consent_.
4. For "Delegated (interactive)", open _Authentication_.
5. For "Delegated (interactive)", add a redirect URI that matches _Redirect URL_ in the Connection.

The app can now be used by the Connection.

:::tip

Application permissions such as _Mail.ReadWrite_ and _Mail.Send_ give the app access to every mailbox in the tenant. _Mailbox / Email_ does not limit that. To limit the app to the mailboxes it needs, ask your Exchange Online administrator to scope it with RBAC for Applications.

:::

When the client secret or certificate expires, the Connection stops working.

### Migrating from Exchange EWS

Existing email Tasks and Triggers can be pointed from an [Exchange EWS](connection-exchange-ews) Connection to a Microsoft Graph API Connection without rebuilding them, with two exceptions:

- Folder IDs are protocol-specific. Reselect the folder anywhere one is referenced, such as the Email Trigger and Email - Move messages
- Message IDs are protocol-specific too. A message ID that an EWS-based Task wrote to a variable does not work in a Task that uses the Graph Connection, so switch every Task in the Job that passes message IDs

### Troubleshooting

#### Authentication succeeds but Tasks return 4xx errors

The app registration is missing the Microsoft Graph permissions, or admin consent has not been granted. Check that _Mail.ReadWrite_ and _Mail.Send_ are present and consented for the flow that you use.

#### App-only test fails at once

Check the application ID, _Tenant Id_, and that the client secret value (not the secret ID) was entered. Check that the secret has not expired.

#### Delegated sign-in cannot complete

_Redirect URL_ must match a redirect URI of the app registration exactly, including scheme and port. If the redirect port is in use or reserved on the Client computer, the Client reports that it cannot bind to the address. Change _Redirect URL_ to a free port, and update the redirect URI of the app.

#### Delegated Jobs fail after a successful sign-in, with a single-tenant app

Fill in _Tenant primary domain_.

#### Email - Send fails on a network that needs a proxy, while Get messages works

Email - Send does not use the ***Proxy*** tab. See [Proxy](#proxy).

#### Folder not found after migrating from EWS

Reselect the folder in the Trigger or Task. EWS and Graph folder IDs are not interchangeable.
