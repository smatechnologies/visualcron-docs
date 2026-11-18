---
sidebar_label: 'Task PDF - Add Footer/Header'
hide_title: 'true'
---

## Task PDF - Add Footer/Header

The PDF - Add footer/header Task adds a text or an image to the header, the footer or the center of the pages of existing PDF files, or of a new PDF file that it creates.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Add footer/header: Main settings tab

![Main settings tab of the Add footer/header Task, with the PDF location, Vertical alignment, Content type, Page range and Save to.. groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20footer-header%20main.png)

- _Existing file_ (_PDF location_ group): adds the content to every file that the ***File filter*** tab selects
- _New file_: creates a new PDF file at the path in the box below the Credential; click the file button to browse

  With _New file_, the ***File filter*** tab is hidden, the _Save to.._ group is not used, and the Credential in this group is used to write the new file.

- _Password_: the password that opens an existing PDF file

  The password is not applied to a new file: a new file is saved without a password.

- _Vertical alignment_: "Header", "Footer" or "Center"; the default is "Footer"
- _Is background_: places the content behind the page content
- _Content type_: "Text", the default, or "Image"; shows the ***Text*** or the ***Image*** tab
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  For a new file, the Task creates as many pages as the highest number in the _Pages_ box, at least one, even when _All pages_ is selected. The default is "1".

- _Same file_ (_Save to.._ group): saves the result over the source file
- _Same folder but use file mask_: saves the result in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the result in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

### File filter tab

The ***File filter*** tab selects the existing PDF files to change; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Image tab

The ***Image*** tab appears when _Content type_ is "Image".

![Text tab of the Add footer/header Task, with the Text content, Font details and Position groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20footer-header%20image.png)

The screenshot shows the ***Text*** tab; the ***Image*** tab has the fields below.

- _Image location_: the full path of the image file
- _Width_ and _Height_ (_Image dimension_ group): the size of the image on the page; the defaults are "200" and "200"
- _Top (pixel)_ or _Bottom (pixel)_ (_Position_ group): the distance from the top of the page when _Vertical alignment_ is "Header", or from the bottom when it is "Footer"

  The label follows _Vertical alignment_. The value is not used with "Center". The default is "10".

- _Horizontal alignment_: "Left", "Center" or "Right"; the default is "Center"
- _Angle of rotation (in degrees)_: rotates the image; the default is "0"
- _Opacity (0-100)_: "100", the default, is fully opaque

### Text tab

The ***Text*** tab appears when _Content type_ is "Text".

![Text tab of the Add footer/header Task, with the Text content, Font details and Position groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20footer-header%20text.png)

- _Text content_: the text to add

  `#PAGE#` is replaced by the page number and `#NUMPAGES#` by the number of pages. Variables are supported.

- _Font_ and _Font size_ (_Font details_ group): the font of the text; the defaults are "Tahoma" and "11"
- _Text color_ and _Background color_: the defaults are "Black" and "White"
- _Top (pixel)_ or _Bottom (pixel)_ (_Position_ group): the distance from the top of the page when _Vertical alignment_ is "Header", or from the bottom when it is "Footer"

  The label follows _Vertical alignment_. The value is not used with "Center". The default is "10".

- _Horizontal alignment_: "Left", "Center" or "Right"; the default is "Center"
- _Angle of rotation (in degrees)_: rotates the text; the default is "0"
- _Opacity (0-100)_: "100", the default, is fully opaque

### Output and errors

The Task output lists the path of each file it saves. With _Existing file_, the Task raises the File not found error when the File filter matches no file.
