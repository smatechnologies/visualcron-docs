---
sidebar_label: 'Task String - JSON Encode'
hide_title: 'true'
---

## Task String - JSON Encode

The String - JSON Encode Task allows you to encode a JSON string from a file or value/Variable into formatted output.

**JSON Encode** tab

*Map columns to properties*

Optionally, you can configure mapping between object properties (including nested ones) and column names in the input.

If mapping is configured and the "Include field names" checkbox is turned off, then each configured property will correspond to the value index in the input line.

**Input/Output** tab

*Input settings / Include field names*

Specify that the first line in the input contains the column names.

*Output settings / Force JSON array output for single-line input*

Always create a JSON array on the output, even if the input contains only one line of values, or none at all.

**Example input**

```
Column1   Column2   ArrayColumn
Value1    Value2    item1;item2;item3
```

**Example output**

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
