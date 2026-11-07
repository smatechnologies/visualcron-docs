---
sidebar_label: 'Condition - Folder'
hide_title: 'true'
---

## Condition - Folder

The _Folder_ condition checks whether a folder exists on the Server computer or on a network share the Server can reach. Use it, for example, to run a Job only when an output folder is available.

This page describes the **_Folder_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "Folder" -> **_Folder_** tab

![Add/Edit condition window with the Folder tab open, showing an empty Folder path box, the Credentials list set to No Credential, and Folder exists set to "True"](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Folder.png)

### Folder information

#### Folder path

The full path of the folder, as the Server sees it: a local path on the Server computer, or a UNC path such as `\\<server>\<share>\<folder>`. Click the browse button to the right of the box to select a folder. You can use Variables in the path, see [Global - Variables](global-variables). Wildcards are not supported: a path that contains "\*" or "?" is reported as a folder that does not exist, so "True" does not match and "False" matches. The window does not let you save the condition with an empty path.

The Client can replace a path on a mapped network drive with its UNC path as you type. It does this when the Client runs on the Server computer and the Client setting _Auto translate to UNC path_ is checked, which is the default.

#### Credentials

Select a Credential when the Server needs another Windows account to reach the folder, for example on a network share. See [Global - Credentials](global-credentials). Leave "No Credential" to check the folder with the account the VisualCron service runs under. Use the _Filter.._ box to search the list. To manage Credentials, click the button to the right of the _Filter.._ box.

If the selected Credential no longer exists, or the Server cannot log on with it, the condition returns a Match Error and an error is logged.

### Match

#### Folder exists

Select "True" to match when the folder exists, or "False" to match when it does not. The default is "True".

:::warning

_Folder exists_ cannot tell a missing folder from a path the Server cannot reach. If the share is offline, or the account has no access to it, the check reports that the folder does not exist: "True" does not match and "False" matches. Do not rely on "False" alone to decide that a folder is absent from a network path.

:::
