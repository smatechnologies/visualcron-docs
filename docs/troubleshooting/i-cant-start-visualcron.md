---
sidebar_label: 'I Cannot Start VisualCron'
hide_title: 'true'
---

## I Cannot Start VisualCron

### Symptom

A part of VisualCron does not start, or stops with an error.

### Fix

First find out which part does not start:

- **The Client does not open, or shows an error before the login:** note the exact error message
- **The Client opens but cannot connect:** see [I Cannot Connect to the VisualCron Server](i-cant-connect-to-visualcron-server)
- **The service does not start:** open `services.msc` and try to start *VisualCron*. If it stops again, open "server_startup.txt" in the log folder (default "C:\Program Files (x86)\VisualCron\log") and check the Windows *Application* event log. See also [VisualCron Service Does Not Start Automatically](visualcron-service-does-not-start-automatically)

If the problem remains, email [support@visualcron.com](mailto:support@visualcron.com) and include:

- the Windows version
- the VisualCron version
- the exact error message
- how far it gets, for example whether the login appears
- "server_startup.txt" and the latest `log_server<yyyyMMdd>.txt`

Review the log files for user names, paths and server names before you send them.