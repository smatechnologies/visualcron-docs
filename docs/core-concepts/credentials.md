---
sidebar_label: 'Credentials'
sidebar_position: 6
description: Manage Windows user credentials in VisualCron for running tasks as specific users.
---

# Credentials

**Credentials** store Windows usernames and passwords centrally. They are used when a task needs to run as a specific user — for example, to access a network drive, a protected folder, or a trusted SQL connection.

Credentials are managed at **Server > Global Objects > Credentials**.

:::info Why credentials are needed

By default, all VisualCron tasks run under the **LOCALSYSTEM** account of the VisualCron Server service. That account typically cannot access network shares, user-profile paths, or domain resources. Assigning a credential to a task runs it as a different Windows user with the appropriate access.

:::

## Creating a credential

1. Go to **Server > Global Objects > Credentials**.
2. Click **Add**.
3. Fill in the fields:

| Field | Description |
|-------|-------------|
| **Username** | Windows username |
| **Password** | Windows password (stored encrypted) |
| **Domain** | Domain or computer name/IP |
| **Local login** | Check when authenticating against the local machine |
| **Load profile** | Loads the user's registry profile (`HKEY_USERS`). Only available with Local login. Use when tasks need access to `HKEY_CURRENT_USER` or user-specific network resources. |

4. Click **OK**.

## Login types

### With profile (Local login checked)
Loads the full user profile. Use when tasks need `HKEY_CURRENT_USER` or user-profile paths. Slower than network-only.

### Network credentials only (Local login unchecked)
Uses the credentials only for network access — does not load the local profile. Faster. Requires UNC paths (e.g., `\\server\share\file.bat`) instead of drive letters.

:::tip Network drives

To access a network drive from a task, use **Network credentials only** with the UNC path of the resource. Drive letters (e.g., `Y:\`) are not available to the service account — use `\\server\folder\` instead.

:::

## Using credentials in tasks

In any task that supports impersonation, a **Credentials** dropdown appears in the task settings. Select the stored credential, or create one inline.

## Security

Credentials are encrypted when stored in the VisualCron configuration. Access to credentials is controlled by VisualCron user permissions.

## Related

- [User Permissions](../server/security/user-permissions)
- [Connections](connections) — connection-level authentication (separate from task-level credentials)
