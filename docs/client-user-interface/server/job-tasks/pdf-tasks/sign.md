---
sidebar_label: 'Task PDF - Sign'
hide_title: 'true'
---

## Task PDF - Sign

The PDF - Sign Task signs existing PDF files with a Certificate and optionally adds a watermark image with details about the Certificate.
 
**Sign > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Sign%20Settings.png)

**Certificate**

Select an existing Certificate you have created/imported in [Certificates manager](../../global-certificates.md).
 
**Show signature widget**

If a watermark should be added or not to the document.
 
**Signature type**

What type of signature
 
**Author**

Author property for the widget.
 
**Reason**

Reason property for the widget.
 
**Contact info**

Contact info property for the widget.
 
**Location**

Location property for the widget.
 
**Password for file(s)**

If any of the specified PDF files contains a password it should be entered here
 
**Sign > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter.md) to filter out the files that should be processed in this Task.
 
**Sign > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Sign%20Destination.png)

**Save to**

The destination folder and file mask which the output file is saved to.
 
**Folder**

If *Different folder and use file mask* is selected, use manual folder specification or click the *Folder* icon.
 
**File mask**

Save file with different name.
 
**Properties->No rotate**

If this property value is checked signature widget will not be rotated when document is rotated in browser.
 
**Properties->No zoom**

If this property is checked signature widget size will not be changed during zooming.
 
**Properties->Print**

If this property is checked the signature widget will be printed on paper.
 
**Properties->Locked**

If this property is checked signature widget can't be moved by the user.
 
**Properties->Locked contents**

Set this property to checked if widget's contents should be locked.
 
**Properties->ReadOnly**

If this property is checked the signature widget will not interact with the user (will not react on mouse, etc.)
 
**Properties->No view**

If this property is checked signature widget will not be displayed when document is viewed.
 
**Properties->Toggle no view**

If this property is checked the signature widget will be displayed only when user is moving mouse over it.
 
**Properties->Signature widget background image**

This image should be in jpeg format and will be displayed as a background image.
 
**Properties->Auto stretch background**

If this property is checked the background picture will be automatically stretched to fit the signature widget.
 
**Properties->Stretch width**

Specify the horizontal size of the stretched background picture.
 
**Properties->Stretch height**

Specify the vertical size of the stretched background picture.
 
**Signature position and dimensions->AutoPos**

If this property is checked signature widget will be placed to the upper right corner. If not checked Left and Top properties will be used as widget coordinates (from bottom left corner).
 
**Signature position and dimensions->AutoSize**

The signature will be auto-sized if checked. If not checked please set the Width/Height properties.
 
**Show signature in page range->All pages**

The signature stamp will be added to all pages.
 
**Show signature in page range->Pages**

The signature stamp will be added to the specified range of pages. Specify a range like 2-4 or specific pages 1,3,5-6.
 
**Default text**

This tab contains the properties that set the texts inside the widget
 
**Default text->Auto text**

If this property is checked texts to be displayed on the signature widget will be generated automatically on the grounds of information from the certificate. Otherwise texts will be taken from Algorithm caption, Algorithm Info, Signer caption, Signer Info and Header properties.
 
**Default text->Hide default text**

Set this property to cheched to hide the default text of the signature widget (signature algorithm, signing time, etc.).
 
**Default text->AutoFontSize**

If this property is cheked then the following values will be assigned to different font sizes: Title font size = 8.77, Timestamp font size = 4.89, Section title font size = 7, Section text font size = 5. Otherwise values will be used from defined values.
 
**Default text->Font name**

Add font name to use in widget
 
**Custom texts**

Use this property to specify any custom text to be added to the widget.
 
**Custom texts->Text**

The text to be added.
 
**Custom texts->Left**

Horizontal offset of the displayed text.
 
**Custom texts->Top**

Vertical offset of the displayed text.
 
**Custom texts->FontSize**

The font size of the text