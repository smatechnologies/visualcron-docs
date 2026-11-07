---
sidebar_label: 'Task String - JSON Filter'
hide_title: 'true'
---

## Task String - JSON Filter

The JSON filter Task runs a JSONPath or JQ query against JSON from a file or a value, and writes the result to the output of the Task.

JQ filter manual: [https://stedolan.github.io/jq/manual/](https://stedolan.github.io/jq/manual/)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### JSON filter tab

![JSON filter tab, with the Credential, the File and Variable/Value input options, the PreFormatting options, the filter engine and the filter expression](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Filter.png)

- _Credentials_: the Credential used to read the file when _File_ is selected. Select a Credential in the combo box, or click the settings button to open _Manage credentials_
- _File_ (default): the full path of a JSON file. Click the file button to browse for it
- _Variable/Value_: the JSON as text or as a Variable. Click the Variable button to insert a Variable
- _PreFormatting_: formatting applied to the JSON before it is filtered:
  - "None" (default): no formatting
  - "Single line": the JSON on one line
  - "Indented": the JSON indented
- _JSONPath_ (default) or _JQ_: the filter engine
- The filter expression field below the engine: the JSONPath expression or the JQ program. Click the button next to it to open the JSON browser, which shows the input as a tree and lets you select a path. The button is available once a file or a value is entered

### Output tab

![Output tab of the JSON filter Task, with the output settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Filter%20Output.png)

The ***Output*** tab applies to "JSONPath" only; it is hidden when "JQ" is selected. A JQ program writes its own result.

- _Include value path_: writes the JSONPath location of each value before the value. Applies to "MultiValue"
- _Name value separator_: the separator between the path and the value, "Colon" by default: "None", "Blankspace", "Colon", "Equal", "Tab", "Cr", "CrLf" or "Lf". Available when _Include value path_ is checked
- _Value qualifier_: an optional character around each value: none, a double quote (`"`) or a single quote (`'`). Applies to "MultiValue"
- _Output value type_: how the matches are written:
  - "SingleValue" (default): the first match only
  - "MultiValue": every match, separated by _Value separator_
  - "JSONObject": a single match as JSON, or several matches as a JSON array
- _Value separator_: the separator between matches for "MultiValue", "CrLf" by default: "Comma", "Cr", "CrLf", "Lf", "CommaWithCr", "CommaWithCrLf", "CommaWithLf", "Pipe", "SemiColon", "Tab" or "None"

### Output and errors

:::warning

If a JSONPath expression matches nothing, the output is empty, and the Task reports success. To treat an empty result as an error, add an error condition on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::

If the input is empty or not valid JSON, or a JQ program fails, the Task fails.
