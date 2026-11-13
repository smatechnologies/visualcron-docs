---
sidebar_label: 'Condition - File'
hide_title: 'true'
---

## Condition - File

The _File_ condition checks whether a file exists, or what a file contains, on the Server computer or on a network share the Server can reach. Use it, for example, to run a Job only when an input file has arrived, or to stop when a file contains an error marker.

This page describes the **_File_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "File" -> **_File_** tab

![Add/Edit condition window with the File tab open, showing an empty File path box, the Credential list set to No Credential, and the Match group with File exists selected and set to "True"](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20File.png)

### File information

#### File path

The full path of the file, as the Server sees it: a local path on the Server computer, or a UNC path such as `\\<server>\<share>\<file>`. Click the browse button to the right of the box to select a file. You can use Variables in the path, see [Global - Variables](global-variables). The window does not let you save the condition with an empty path.

The Client can replace a path on a mapped network drive with its UNC path as you type. It does this when the Client runs on the Server computer and the Client setting _Auto translate to UNC path_ is checked, which is the default.

#### Credential

Select a Credential when the Server needs another Windows account to reach the file, for example on a network share. See [Global - Credentials](global-credentials). Leave "No Credential" to check the file with the account the VisualCron service runs under. Use the _Filter.._ box to search the list. To manage Credentials, click the button to the right of the _Filter.._ box.

If the selected Credential no longer exists, or the Server cannot log on with it, the condition returns a Match Error and an error is logged.

### Match

Select one check. The default is _File exists_ with "True".

#### File exists

Select "True" to match when the file exists, or "False" to match when it does not. The file name part of _File path_ can contain the wildcards "\*" and "?". The check then finds the file when at least one file in that folder matches the pattern. Subfolders are not searched.

:::warning

_File exists_ cannot tell a missing file from a path the Server cannot reach. If the share is offline, or the account has no access to it, the check reports that the file does not exist: "True" does not match and "False" matches. Do not rely on "False" alone to decide that a file is absent from a network path. When the file name contains a wildcard, a folder that does not exist, or that the Server cannot reach or read, gives a Match Error instead.

:::

#### File content

Reads the whole file and compares it with the text in the box to the right:

- "Is": the content equals the text
- "Is not": the content differs from the text
- "Contains": the content contains the text
- "Not contains": the content does not contain the text

The comparison is case-sensitive. "Is" and "Is not" compare the entire file, including line breaks at the end, so a file that ends with a line break does not equal the same text without one. The file is read as UTF-8 text. You can use Variables in the text.

If the file does not exist or cannot be read, or if _File path_ contains a wildcard, the condition returns a Match Error and an error is logged. The window asks you to confirm before it saves an empty text.
