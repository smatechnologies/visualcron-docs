---
sidebar_label: 'Task PDF - Get Information'
hide_title: 'true'
---

## Task PDF - Get Information

The PDF - Get information Task writes the document properties of PDF files, such as the author, the page count and the signatures, to the Task output.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get information: Main settings tab

![Main settings tab of the Get information Task, with the Password for file(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Information.png)

- _Password for file(s)_: the password that opens the source PDF files, if they are protected

### File filter tab

The ***File filter*** tab selects the PDF files to read; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Get information: Output tab

The ***Output*** tab of the Task window sets the format of the output.

![Output tab of the Get information Task, with the Include field names check box, the Field separator, Text qualifier and Line break lists and the Show information list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Information%20Output.png)

- _Include field names_ (_Output settings_ group): starts each line with the name of the property and _Field separator_; unchecked by default
- _Field separator_: the separator; the default is "Tab"
- _Text qualifier_: the character around each value; none by default
- _Line break_: the line break; the default is "CrLf"
- _Show information_: the properties to return: "CreationDate", "ModificationDate", "Producer", "Keywords", "Subject", "Author", "Creator", "Title", "Trapped", "PagesCount", "IsEncrypted", "Version" and "Signatures"

  All except "Trapped" and "IsEncrypted" are selected by default.

### Output and errors

The Task output has one line for each selected property. A property that has no value in the document is left out. "IsEncrypted" gives "Encrypted" with details of the encryption, or "Decrypted". "Signatures" gives "Signed" with the details of each signature, or "Not signed".

When the Task cannot read the document properties, for example because the password is wrong, it writes the error to standard error and goes on to the encryption and signature information. Unless that second read also fails, the Task reports success.