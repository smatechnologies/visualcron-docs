---
sidebar_label: 'Task Event Log - Event Log Read'
hide_title: 'true'
---

## Task Event Log - Event Log Read

The Event log - read Task reads the entries of a Windows event log on the Server computer or on a remote computer that match a filter, and writes chosen fields of them to the output.

![Event log - read tab, with the scope settings and the event log entry filter](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Event%20Log%20Tasks/Event%20Log%20-%20read.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Event log - read tab

**Scope**

- _Local_ (default): reads the event log of the Server computer
- _Remote_: reads the event log of another computer. Enter its host name or IP address in the box next to it, or select it from the list of network computers
- The Credential: the Credential used to read a remote event log. It is used only with _Remote_. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials)

**Event log entry filter**

- _Event log_: the event log to read, "Application" by default
- _Source_, _Entry type_, _Category ID_, _Category_, _Event ID_, _Message_: a condition and a value for each field. "Don't check" (default) leaves the field out of the filter, and its value box is not available

An entry is returned when it matches every condition that is not "Don't check". The conditions are:

- _Entry type_: "Don't check", `Equal (=)` or `Not equal (!=)`, with the entry type "Information" (default), "Any", "Error", "Failure Audit", "Success Audit" or "Warning". With `Equal (=)`, "Any" matches no entry; to read every type, set the condition to "Don't check" and filter on another field
- _Category ID_ and _Event ID_: `Equal (=)`, `Not equal (!=)`, `Larger than (>)`, `Larger than or equal (>=)`, `Smaller than (<)` or `Smaller than or equal (<=)`, with a number
- _Source_, _Category_ and _Message_: the same conditions, and also `Contains (=%)` and `Not contains (!=%)`. Use "Larger than" and "Smaller than" only with numbers: with text, the Task fails

Values may contain Variables.

:::warning

`Not equal (!=)` on _Source_, _Category ID_, _Category_, _Event ID_ or _Message_ matches every entry. For text, use `Not contains (!=%)`.

With every condition set to "Don't check", no entry is returned, the output is empty, and the Task reports success. Set at least one condition.

With _XML object_ selected, no output is written, and the Task reports success.

:::

### Event log - read: Output tab

**Result**

- _Limit result to top row count_: returns only the number of entries entered, "1" by default. The newest entries are read first

**Output format**

- _XML object_: no output is written, and the Task reports success
- _Specific string values_: writes the fields selected in the list, one line for each entry. Select a field and click _Add_; click _Delete selected_ to remove fields. The fields are InstanceID, EventID, CategoryID, Category, Source, EntryType, Message, Username and TimeGenerated
- _Include field names_: writes the field names in the first line
- _Field separator_: the character between fields, "Tab" by default
- _Text qualifier_: an optional character around each value
- _Line break_: the character between entries, "CrLf" by default

### Output and errors

If the event log cannot be read, the Task fails.
