---
sidebar_label: 'Task String - JSON Decode'
hide_title: 'true'
---

## Task String - JSON Decode

The JSON Decode Task turns JSON from a file or a value into delimited text, one line for each JSON object, and writes it to the output or to a file.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### JSON Decode tab

![JSON Decode tab, with the Credential, the File and Variable/Value input options, the JSON object field and the column map](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Decode.png)

- _Credentials_: the Credential used to read the file when _File_ is selected
- _File_ (default): the full path of a JSON file. Click the file button to browse for it
- _Variable/Value_: the JSON as text or as a Variable. Click the Variable button to insert a Variable
- _JSON object_: optional. A JSONPath expression that selects the part of the JSON to decode, for example an array inside the document. When it is empty, or matches nothing, the whole JSON is decoded. Click the button next to it to open the JSON browser and select a path
- _Map columns to properties (double click to edit)_: optional. Each row maps an output column (_Name_) to a property (_Value_), given as a path relative to each object, such as `Property1` or `InnerArray[0].Value`. In the _Add/Edit name value_ window, clear _The value is the name of the JObject property_ to enter a value or a Variable instead of a property. Use _Add_, _Edit_ and _Delete_ to change the rows. _Refresh_ removes every row from the map

Without a map, every property of each object becomes a column. If the JSON is an array, each item becomes one line; otherwise there is one line. An array value is written as its items separated by a comma and a space.

### Output tab

![Output tab of the JSON Decode Task, with the output settings and the file output settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Decode%20Output.png)

- _Include field names_: writes the column names in the first line
- _Indent XML_: has no effect on this Task
- _Field separator_: the character between columns, "Tab" by default
- _Text qualifier_: an optional character written around text and date values
- _Line break_: the character between lines, "CrLf" by default
- _Output to standard output_ (default): writes the result to the output of the Task
- _Output to file_: writes the result to the file in _File path_, read and written with the Credential selected above it
  - _Include BOM (if UTF8)_: checked by default. Writes a byte order mark when the Task code page is UTF-8
  - _Append to file_: checked by default. Adds the result to the end of an existing file, after a line break. When cleared, an existing file is replaced without warning

:::warning

With _Output to file_ and _Append to file_ cleared, an existing file at _File path_ is replaced on each run.

:::


With _Output to file_, the output of the Task is the path of the file.

### Example

Input:

```json
[
  {
    "Property1": "Value1",
    "Property2": "Value2",
    "InnerArray": [{ "Value": "item1" }, { "Value": "item2" }]
  },
  {
    "Property1": "Value3",
    "Property2": "Value4",
    "InnerArray": [{ "Value": "item3" }, { "Value": "item4" }]
  }
]
```

With the map _Column1_ = `Property1`, _Column2_ = `Property2` and _ArrayColumn_ = `InnerArray[0].Value`, and _Include field names_ checked, the output is (columns separated by tabs):

```text
Column1   Column2   ArrayColumn
Value1    Value2    item1
Value3    Value4    item3
```

### Output and errors

:::warning

If the file or the value is empty, the Task writes nothing, and the Task reports success.

:::

If the input is not valid JSON, the Task fails.
