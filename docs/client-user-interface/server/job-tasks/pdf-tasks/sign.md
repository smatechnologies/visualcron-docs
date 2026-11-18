---
sidebar_label: 'Task PDF - Sign'
hide_title: 'true'
---

## Task PDF - Sign

The PDF - Sign Task signs PDF files with a Certificate, and can show the signature as a widget on the pages.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Sign: Main settings tab

![Main settings tab of the Sign Task, with the Certificate list, the Show signature widget check box, the Signature type list, the Author, Reason, Contact info and Location boxes, and the Password for file(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Sign%20Settings.png)

- _Certificate_ (_Sign ..._ group): the Certificate to sign with; required

  See [Global - Certificates](../../global-certificates).

- _Show signature widget_: makes the signature visible on the pages and shows the ***Signature widget*** tab

  When it is unchecked, the signature is invisible.

- _Signature type_: "Pkcs1" (the default), "Pkcs7" or "Pkcs7_detached"

  :::note

  The signature uses the SHA-1 digest.

  :::

- _Author_, _Reason_, _Contact info_ and _Location_: stored in the signature

  Variables are supported.

- _Password for file(s)_: not used by this Task

  The Task cannot sign an encrypted file; see [Output and errors](#output-and-errors).

### File filter tab

The ***File filter*** tab selects the PDF files to sign; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Sign Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Sign%20Destination.png)

- _Same file_ (_Save to.._ group): saves the signed file over the source file
- _Same folder but use file mask_: saves the signed file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the signed file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, _Same folder but use file mask_ saves every result in the File filter folder, not in the subfolder the source file came from.

### Signature widget tab

The ***Signature widget*** tab appears when _Show signature widget_ is checked.

#### Properties

- _No rotate_: the widget does not rotate when the document is rotated; checked by default
- _No zoom_: the widget keeps its size when the document is zoomed; checked by default
- _Print_: the widget is printed; unchecked by default
- _Locked_: the widget cannot be moved; checked by default
- _Locked contents_: the content of the widget is locked; unchecked by default
- _ReadOnly_: the widget does not respond to the user; checked by default
- _No view_: the widget is not shown when the document is viewed; unchecked by default
- _Toggle no view_: the widget is shown only when the pointer is over it; unchecked by default
- _Signature widget background image_: a JPEG file shown as the background of the widget

  When it is empty, a built-in image is used.

- _Auto stretch background_: stretches the background image to fit the widget; checked by default
- _Stretch width_ and _Stretch height_: the size of the background image, used when _Auto stretch background_ is unchecked

#### Signature position and dimension

- _AutoPos_: places the widget automatically; checked by default

  When it is unchecked, _Left_ and _Top_ set the position; the defaults are "10" and "10".

- _AutoSize_: sizes the widget automatically; checked by default

  When it is unchecked, _Width_ and _Height_ set the size; the defaults are "300" and "400".

#### Show signature in page range

- _All pages_: shows the widget on every page; this is the default
- _Pages_: shows the widget on page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

#### Default text

The ***Default text*** tab sets the texts in the widget.

- _AutoText_: builds the widget texts from the Certificate; checked by default

  When it is unchecked, the widget uses _Header_, _Algorithm caption_, _Algorithm info_, _Signer caption_ and _Signer info_, and the texts on the ***Custom texts*** tab.

- _Hide default text_: hides the default texts of the widget, such as the signature algorithm and signing time; unchecked by default
- _Show timestamp_: shows the signing time; checked by default
- _AutoFontSize_, _Title font size_, _Timestamp font size_, _Section title font size_ and _Section text font size_: the Task does not currently apply these settings
- _Font name_: the name of a font to add to the widget

#### Custom texts

The ***Custom texts*** tab lists more texts for the widget, used when _AutoText_ is unchecked.

- _Text_: the text to add

  Variables are supported.

- _Left_ and _Top_: the position of the text in the widget
- _FontSize_: the size of the text

### Output and errors

The Task output contains "Success" for each file it signs. An encrypted file raises an error.

:::warning

When the selected Certificate no longer exists, the file is not signed, and the Task reports success. With _Same folder but use file mask_ or _Different folder and use file mask_, the Task copies the source file to the destination before it signs it, so an unsigned copy stays there.

:::
