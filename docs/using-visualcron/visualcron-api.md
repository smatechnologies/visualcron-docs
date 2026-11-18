---
sidebar_label: 'VisualCron API'
hide_title: 'true'
---

## VisualCron API

The VisualCron API is the .NET library that the VisualCron Client uses for every action it performs on a VisualCron Server. Your own programs and scripts can use the same library to connect to a Server and work with Jobs, Tasks, Credentials, Connections and the other objects, and to run Jobs. This page is for developers who build integrations in .NET or PowerShell. To call VisualCron over HTTP without the library, see [VisualCron Web API](visualcron-web-api). To control a Server from the command line, see [VCCommand](vccommand).

### Languages

- [.NET (C# or VB.NET)](dot-net-csharp-vbnet)
- [PowerShell](powershell)

Visual Basic 6 is not supported.

### API documentation and samples

In the Client, go to _Help_ -> _API_:

- _Show documentation_: opens the API quick start (PDF)
- _API reference_: opens the full member reference (CHM)

Both files are installed in the "API\doc" folder of the VisualCron installation folder. The "API\samples" folder holds a C# sample project in "TestClient" and sample scripts in "PowerShell".

### Before you start

- **References:** reference "VisualCronAPI.dll" and "VisualCron.dll" in the installation folder, by default "C:\Program Files (x86)\VisualCron". Both are built for .NET Framework 4.8. The "lib" subfolder holds another build of the same two DLLs that you can debug with (see [Troubleshooting](#troubleshooting))
- **Logon:** your program logs on to the Server as a VisualCron user, with a user name and password or with Active Directory logon, on the Server port (default "16444")
- **Permissions:** the Server checks that user's permissions for most requests. Give each program its own VisualCron user with only the permissions it needs (see [Main - User Permissions](../client-user-interface/server/main-user-permissions))
- **Client-only permissions:** a few permissions are applied only in the desktop Client's own windows, for example _Task manager_ and _Delete_ on _PGP key rings_. A program that uses the API can use these functions whatever they are set to, so do not rely on them to restrict a program
- **Remote logons:** when _Only allow local connections_ is checked on the **_Users/Logon_** tab of the Server settings, the Server refuses API logons from other computers. The logon fails with "Login failed, reason: Only local connections allowed to this Server" (see [Settings - Users/Logon](../client-user-interface/server/settings-users-logon))

### Troubleshooting

#### A debugging session ends with "Debugger Detected"

If your program references "VisualCronAPI.dll" from the installation folder and a debugging session ends with a "Debugger Detected" exception, reference the two DLLs in the "lib" subfolder instead: "C:\Program Files (x86)\VisualCron\lib\VisualCron.dll" and "C:\Program Files (x86)\VisualCron\lib\VisualCronAPI.dll" in a default installation.
