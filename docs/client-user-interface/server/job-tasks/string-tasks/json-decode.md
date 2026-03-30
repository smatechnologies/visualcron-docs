---
sidebar_label: 'Task String - JSON Decode'
hide_title: 'true'
---

## Task String - JSON Decode

The String - JSON Decode Task allows you to decode a JSON string from a file or value/Variable into formatted output.

**JSON Decode** tab

*Map columns to properties*

Optionally, you can configure mapping between object properties (including nested ones) and column names in the output.

*Output settings / Include field names*

Write the column names in the first line of output.

**Example input**

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

**Example output**

```
Column1   Column2   ArrayColumn
Value1    Value2    item1
Value3    Value4    item3
```
