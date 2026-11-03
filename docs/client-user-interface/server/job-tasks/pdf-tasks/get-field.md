---
sidebar_label: 'Task PDF - Get Field'
hide_title: 'true'
---

## Task PDF - Get Field

The PDF - Get field(s) Task writes the names, values and properties of form fields in PDF files to the Task output.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get field(s): Main settings tab

![Main settings tab of the Get field(s) Task, with the Fields grid listing four text box fields, the Get field names button, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Fields.png)

- _Name_ (_Fields ..._ grid): the names of the fields to return

  When the grid is empty, the Task returns every field. Click _Get field names_ to load the field names of the files that the File filter matches, and then select names in the grid. A name can contain wildcards, such as `*`, and Variables. To delete a field, select its row and press Delete.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  Only the fields on those pages are returned.

### File filter tab

The ***File filter*** tab selects the PDF files to read; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Get field(s): Output tab

The ***Output*** tab of the Task window sets the format of the output.

![Output tab of the Get field(s) Task, with the Include field names check box, the Field separator, Text qualifier and Line break lists and the Show field infos list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Fields%20Output.png)

- _Include field names_ (_Output settings_ group): starts the output of each file with a row of the selected info names; unchecked by default
- _Field separator_: the separator; the default is "Tab"
- _Text qualifier_: the character around each value; none by default
- _Line break_: the line break; the default is "CrLf"
- _Show field infos_: the properties to return for each field, in this order: "Name", "Type", "PageNumber", "Left", "Top", "Width", "Height", "Length", "Value", "ReadOnly" and "Required"

  All are selected by default. "Length" is the number of items of a combo box field, the maximum length of a text field, or `-`. "ReadOnly" gives "ReadOnly" or "Enabled", and "Required" gives "Required" or "Unrequired".

### Output and errors

The Task output has one row for each field, with the selected properties separated by _Field separator_. For a file without fields, the output is "The document has no fields".