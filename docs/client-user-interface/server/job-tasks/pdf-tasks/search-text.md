---
sidebar_label: 'Task PDF - Search Text'
hide_title: 'true'
---

## Task PDF - Search Text

The PDF - Search text Task finds a text or a regular expression in PDF files and writes each match, with the properties you select, to the Task output.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Search text: Main settings tab

![Main settings tab of the Search text Task, with the Find box, the Is regular expression check box, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Search%20text.png)

- _Find_ (_Find ..._ group): the text to find, without quotation marks; required

  Variables are supported.

- _Is regular expression_: treats _Find_ as a regular expression
- _Password for file(s)_: the password that opens the source PDF files, if they are protected
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  A page number larger than the page count raises an error.

### File filter tab

The ***File filter*** tab selects the PDF files to search; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Search text: Output tab

The ***Output*** tab of the Task window sets the format of the output.

![Output tab of the Search text Task, with the Include text info names check box, the Field separator, Text qualifier and Line break lists and the Show text infos list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Search%20text%20output.png)

- _Include text info names_ (_Output settings_ group): starts each line with the name of the property and _Field separator_; unchecked by default
- _Field separator_: the separator between the name and the value; used with _Include text info names_. The default is "Tab"
- _Text qualifier_: the character around each value; none by default
- _Line break_: ends each line; the default is "CrLf"
- _Show text infos_: the properties to return for each match: "Text", "PageNumber", "XIndent", "YIndent", "ForegroundColor", "FontName", "FontSize", "FontIsSubset", "FontIsEmbedded", "FontIsAccessible", "Rectangle", "LineSpacing", "Subscript", "Invisible", "WordSpacing", "HorizontalScaling", "CharacterSpacing", "Superscript" and "HorizontalAlignment"

  "Text" to "FontIsAccessible" are selected by default.

### Output and errors

The Task output has one line for each selected property of each match, with an empty line after each match. A property without a value is left out. When nothing matches, the output is empty.