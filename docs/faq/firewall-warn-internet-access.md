---
sidebar_label: 'Why Does My Firewall Warn / Why Does VisualCron Try to Access the Internet?'
hide_title: 'true'
---

## Why Does My Firewall Warn / Why Does VisualCron Try to Access the Internet?

VisualCron contacts "www.visualcron.com" over the Internet, for example to check for new versions and to activate, deactivate and validate the license. A firewall can warn you the first time this happens. It can also warn you the first time the VisualCron Server listens for connections from Clients.

The Client checks for new versions at startup. To turn off the update check, complete the following steps:

1. Go to *File* -> *Settings* -> *Client settings*.
2. Click the ***Main settings*** tab.
3. Clear *Check for updates at startup*.
4. Click *Apply settings*.

   The Client no longer checks for new versions at startup.

:::warning

A new Server has one user, "admin", with no password. Before you allow inbound TCP "16444" from other computers, set a password for "admin", as described in [Secure the admin user](../get-visualcron/download-install-upgrade-uninstall#secure-the-admin-user). Do not allow all connections on all ports.

:::

If your firewall asks what to allow, allow only what VisualCron needs:

- Inbound TCP "16444" (the default *Server port*, which you can change) on the Server, only from the computers that run a Client or a program that uses the VisualCron API
- The Web API ports, by default "8001" and "8002", and the Web Client port, by default "9000", only if you use them
- Outbound HTTPS (TCP "443") to "www.visualcron.com"

Connecting a Client to another VisualCron Server uses TCP "16444" on that Server and does not need Internet access.

For the full list of ports and addresses, see [Firewall and network](../get-visualcron/antivirus-exclusions#firewall-and-network).