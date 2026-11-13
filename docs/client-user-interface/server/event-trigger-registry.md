---
sidebar_label: 'Event Trigger - Registry'
hide_title: 'true'
---

## Event Trigger - Registry

The Registry Trigger fires when a registry key, a key and its subkeys, or a single registry value changes, on the Server computer or on a remote computer. It uses WMI registry events, which Windows sends when the change happens, so *Polling interval* on ***Main settings*** is not used.

To watch the registry of another computer, enter its name or IP address in *Computer name* on ***Main settings***. Select a Credential under *Credentials* only for a remote computer: with *Computer name* ".", a Credential makes the connection fail. To look at registry keys and values, run `regedit.exe`.
 
The settings are on the ***Registry*** tab.

![Registry tab of the Add/Edit event window with Registry key change and HKEY_CLASSES_ROOT selected, an empty Registry key path and the Registry value name field unavailable](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Registry.png)

**Registry event type**

* *Registry key change*: fires on changes to the key itself, not its subkeys (default)
* *Registry tree change*: fires on changes to the key and its subkeys
* *Registry value change*: fires on changes to one value of the key
 
**Hive**

The hive that contains the key: *HKEY_CLASSES_ROOT* (default), *HKEY_CURRENT_USER*, *HKEY_LOCAL_MACHINE*, *HKEY_USERS* or *HKEY_CURRENT_CONFIG*.

:::warning

Windows registry events do not support *HKEY_CLASSES_ROOT* and *HKEY_CURRENT_USER*, and a new Registry Trigger has *HKEY_CLASSES_ROOT* selected. Select *HKEY_LOCAL_MACHINE*, *HKEY_USERS* or *HKEY_CURRENT_CONFIG*. With the other hives, the Trigger fails when it starts and is deactivated. To watch the keys of one user, select *HKEY_USERS* and start *Registry key path* with that user's security identifier (SID).

:::
 
**Registry key path**

The path of the key without the hive, with backslashes between the keys and no backslash at the start, for example `SOFTWARE\Microsoft\DirectX`. Enter single backslashes, as Registry Editor shows them. The field can contain Variables. The value of a Variable is used as it is, so a Variable whose value is a path must contain double backslashes, for example `SOFTWARE\\Microsoft\\DirectX`.
 
**Registry value name**

The name of the value to watch, for example "InstalledVersion" in `SOFTWARE\Microsoft\DirectX`. Required for *Registry value change*; not available for the other event types.

:::warning

If, when the Trigger starts, VisualCron cannot connect to WMI or Windows rejects the query, the Trigger is deactivated; it does not try to reconnect. Check the log, correct the settings and activate the Trigger again.

With a Credential, an error while the Trigger watches the registry also deactivates it. Without a Credential, a WMI connection that is lost after the Trigger has started is not detected: the Trigger still shows as active, but its event no longer fires it (a timeout, if set, still fires), and nothing is logged. If a Registry Trigger that watches a remote computer stops firing, deactivate and activate the Trigger. To notice when the Trigger has gone silent, set a timeout on the ***Timeout*** tab.

:::

### Result Variables

Each time the Trigger fires, it sets result Variables for the change, for example the data of the changed value, `{TRIGGER(Active|LastTrigger|Registry.Result.Value)}`. *Value* is set only for *Registry value change* and only when *Computer name* is "."; for a remote computer it is empty. With *Last trigger* (`Active|LastTrigger`), a Variable reads the result of the firing that started the run. All Registry Trigger result Variables are described in [Variables](global-variables).
