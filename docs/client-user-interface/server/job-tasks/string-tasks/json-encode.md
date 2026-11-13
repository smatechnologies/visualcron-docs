---
sidebar_label: 'Task String - JSON Encode'
hide_title: 'true'
---

## Task String - JSON Encode

The JSON Encode Task turns delimited text from a file or a value into JSON, one JSON object for each line, and writes it to the output or to a file.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### JSON Encode tab

![JSON Encode tab, with the Credential, the File and Variable/Value input options and the property map](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Encode.png)

- _Credentials_: the Credential used to read the file when _File_ is selected
- _File_ (default): the full path of a text file. Click the file button to browse for it
- _Variable/Value_: the text as a value or as a Variable. Click the Variable button to insert a Variable
- _Map columns to properties (double click to edit)_: each row maps a JSON property (_Name_) to an input column (_Value_), with a value type (_Type_): "None", "Integer", "Float", "String", "Boolean", "Date", "Object" or "Array". Use a dotted path in _Name_ for a nested property, such as `Address.City`, and `[]` after a name for an array of objects, such as `InnerArray[].Value`. In the _Add/Edit name value_ window, clear _The value is the name of column_ to enter a value or a Variable instead of a column. Use _Add_, _Edit_ and _Delete_ to change the rows. _Refresh_ removes every row from the map

When _Include field names_ is checked on the ***Input/Output*** tab, _Value_ is the column name from the first line. When it is cleared, the rows of the map are matched to the columns by position: the first row to the first column, and so on. A column value that contains `;` becomes an array of values, unless the value is enclosed in the text qualifier.

Without a map, each column becomes a property named after its column. This needs _Include field names_; without it, the objects are empty.

### Input/Output tab

![Input/Output tab of the JSON Encode Task, with the input settings, the output settings and the file output settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/String%20Tasks/JSON%20Encode%20Input-Output.png)

**Input settings**

- _Include field names_: the first line of the input holds the column names
- _Indent XML_: has no effect on this Task
- _Field separator_: the character between columns, "Tab" by default
- _Text qualifier_: an optional character around column values
- _Line break_: the character between lines, "CrLf" by default

**Output settings**

- _Force JSON array output for single-line input_: always writes a JSON array, even when the input has one line of values or none. Without it, one line gives a single JSON object and more lines give an array
- _Output to standard output_ (default): writes the JSON to the output of the Task
- _Output to file_: writes the JSON to the file in _File path_, read and written with the Credential selected above it
  - _Include BOM (if UTF8)_: checked by default. Writes a byte order mark when the Task code page is UTF-8
  - _Append to file_: checked by default. Adds the JSON to the end of an existing file, after a line break. When cleared, an existing file is replaced without warning

:::warning

With _Append to file_ checked, each run adds another JSON document to the same file, and the file as a whole is no longer valid JSON. Clear _Append to file_ to replace the file on each run.

:::

### Example

Input, with _Include field names_ checked (columns separated by tabs):

```text
Column1   Column2   ArrayColumn
Value1    Value2    item1;item2;item3
```

With the map `Property1` = _Column1_, `Property2` = _Column2_ and `InnerArray[].Value` = _ArrayColumn_, the output is (shown indented; the Task writes it on one line):

```json
{
  "Property1": "Value1",
  "Property2": "Value2",
  "InnerArray": [
    { "Value": "item1" },
    { "Value": "item2" },
    { "Value": "item3" }
  ]
}
```

### Output and errors

:::warning

If the file or the value is empty, the Task writes nothing, and the Task reports success.

:::
