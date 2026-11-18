---
sidebar_label: 'Login'
hide_title: 'true'
---

## Login

This page explains how the VisualCron Client logs on to a Server, and when it asks you for a user name and password.

When the Client starts, it connects to each server connection that has _Auto connect at startup_ checked. Whenever the Client starts and finds no server connections, for example the first time on a computer, it creates one to the Server on the same computer. This is a local connection, which does not use the network port. It logs on with the default user and has _Auto connect at startup_ checked. The Client then connects without asking you to log on.

The login window opens:

- When the connection has _Prompt for login_ checked
- For an Active Directory logon, when the Server no longer accepts the saved logon, for example because it has expired

Other logon failures show a message instead, for example a wrong user name or password, a blocked or inactive user, or a Server that accepts only local connections. If the password of the user that a connection logs on with changes, update the password in the connection in _File_ -> _Servers_ -> _Manage Servers_, or check _Prompt for login_ for it.

In the login window, enter _Username_ and _Password_ and click _Login_. Check _Remember settings_ to save them in the connection. _Always prompt_ shows the connection's _Prompt for login_ setting. For an Active Directory logon, it is always checked when the window opens. With _Remember settings_ checked, the value of _Always prompt_ is saved as the connection's _Prompt for login_. If you check _Remember settings_ and clear _Always prompt_, the login window no longer opens for that connection, except for an Active Directory logon that the Server no longer accepts.

If password rules are enabled on the Server and your password has expired or must be changed, a window asks for a new password after you log on. If you cancel it, the Client disconnects. Password rules are set on the **_Password rules_** tab in _Server_ -> _Main settings_ -> _Settings_.

:::warning

For security, after the first logon give the default user a strong password, or add your own users and then deactivate the default user. You do this in _Server_ -> _Main settings_ -> _User permissions_. The connection that the Client created at start-up logs on with the default user. Before you change that password or deactivate the default user, edit the connection in _File_ -> _Servers_ -> _Manage Servers_: save the new password or your own user in it, or check _Prompt for login_. Otherwise the next logon fails with a message, and the login window does not open. See [Main - User Permissions](../client-user-interface/server/main-user-permissions). To log on with Windows accounts, see [Settings - Users/Logon](../client-user-interface/server/settings-users-logon).

:::

To add connections, for example to Servers on other computers, click _File_ -> _Servers_ -> _Manage Servers_. See [Servers - Manage Servers](../client-user-interface/file/manage-servers).