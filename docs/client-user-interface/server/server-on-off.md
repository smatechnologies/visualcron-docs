---
sidebar_label: 'Main - Server On/Off'
hide_title: 'true'
---

## Main - Server On/Off

In the main menu ***Server*** -> ***Main settings***, the button ***Server [On]*** or ***Server [Off]*** shows the VisualCron server status. Click it to switch the status between "On" and "Off".

The status "Server [Off]" means that the service is running but Time Triggers do not start Jobs and Event Triggers are inactive, except Event Triggers with _Ignore Server Off (always run)_ checked, which still start their Jobs. The _Next run_ column of every active Job with a Time Trigger shows "Server off". You can still run Jobs manually. Switching to "Server [Off]" is not an emergency stop. Jobs and Tasks that are already running continue until they finish, and their Flow can still start other Jobs. To stop a running Job, use ***Stop Job*** in the Client. See [VisualCron Server](../../using-visualcron/visualcron-server#server-on-and-off).

:::warning

Runs that Time Triggers would have started while the Server was "Off" are not made up when you switch it back to "On". Check which Jobs should have run in that time and run them manually if needed.

:::

When you switch the Server to "Off", the Client asks you to confirm, unless _Show Server Stop confirmation dialog_ is unchecked in the Client settings (see [Settings - Client Settings](../file/client-settings)). Switching the status needs the "Server Settings" permission with "Edit". Every switch is written to the Audit log with the user who made it (see [Objects - Audit Log](../tools/objects-audit-log)).

Once you have changed the server status, the status will be saved and VisualCron will use that status the next time the server computer is started.
