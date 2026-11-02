---
sidebar_label: 'Task PDF - Convert'
hide_title: 'true'
---

## Task PDF - Convert

The PDF - Convert Task converts PDF files to other formats, or converts files in other formats to PDF.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Convert: Main settings tab

![Main settings tab of the Convert Task, with the Convert group, and the Password for file(s) and Page range groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert.png)

- _To PDF from_ (_Convert ..._ group): converts files of the selected format to PDF: "XPS", "PCL", "SVG", "EPUB", "MHT", "HTML", "TeX", "TXT", "CGM", "XML" or "IMAGE"

  Only files with a matching extension are converted: `.xps`, `.pcl`, `.svg`, `.epub`, `.mht` or `.mhtml`, `.html` or `.htm`, `.tex`, `.txt`, `.cgm`, `.xml`, and for "IMAGE" `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tif` or `.tiff`.

- _From PDF to_: converts PDF files to "PDF", "HTML", "DOC", "XLS", "PPT", "XPS", "XML", "TeX", "SVG", "EPUB", "TXT" or "IMAGE"

  A second list sets the variant for some formats: "PDFA_1b", "PDFA_3b", "PDFA_2u" or "PDFA_3u" for "PDF"; "DOC" or "DOCX" for "DOC"; "BMP", "JPEG", "GIF", "PNG", "TIFF" or "EMF" for "IMAGE"; "XML" or "MobiXML" for "XML".

- _Password for file(s)_: the password that opens protected source PDF files; used with _From PDF to_
- _Page range_: _All pages_, or _Pages_ with page numbers and ranges separated by commas, for example `2-4` or `1,3,5-6`. An entry that is not a page number or a valid range is ignored

  Available with _From PDF to_.

:::warning

With _From PDF to_ "PDF", the Task does not save a converted file: it writes any conversion messages to standard error, and the Task reports success.

:::

### File filter tab

The ***File filter*** tab selects the files to convert; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

With _To PDF from_, a file that the filter matches but whose extension does not match the selected format is skipped, and the Task reports success.

### Destination tab

![Destination tab of the Convert Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert%20Destination.png)

The _Save to.._ group is used with _From PDF to_:

- _Same file_ (_Save to.._ group): saves the converted file at the path of the source file
- _Same folder but use file mask_: saves the converted file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the converted file in _Folder_, named by _File mask_
- _Folder_: the destination folder; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name, including its `.pdf` extension. Set a mask that gives the target extension, such as `*.docx`.

:::warning

With _From PDF to_, _Same file_ replaces the source PDF file with the converted content and keeps the `.pdf` name. With the default _File mask_ `*`, _Same folder but use file mask_ does the same to a source file in the File filter folder. Use _Different folder and use file mask_, or a _File mask_ with the target extension.

:::

With _To PDF from_, the _Save to.._ options and _File mask_ are not used. Each PDF file is named after the source file with the `.pdf` extension and saved in _Folder_ when the box has a value, otherwise in the source file's folder.

:::warning

With _To PDF from_, a PDF file that already has the new name is replaced without a prompt.

:::

With _From PDF to_ "IMAGE", each page is saved as a separate image, with ` - page` and the page number added before the extension; the numbering starts at "0" when _All pages_ is selected. A document with one page gives one image without a number. "TIFF" saves all pages in one file.

:::warning

With _From PDF to_ "TXT" and _Pages_, the Task adds the text to the end of an existing file with the same name instead of replacing it.

:::

#### Image parameters

- _Width_, _Height_ and _Quality_ (_Image parameters_ group, _From PDF to_ "IMAGE"): the size of each image, and its quality from "0" to "100"

  The size is used only when both _Width_ and _Height_ are set. A quality outside "0" to "100" is treated as "100". For "TIFF", _Compression_ replaces _Quality_: "LZW", "CCITT4", "CCITT3", "RLE" or "None"; the TIFF settings are used only when _Width_ and _Height_ are set.

#### Text to PDF groups

When _To PDF from_ is set to "TXT", three more groups appear on the ***Destination*** tab: _Page margins (points)_, _Font details_, and _Page orientation and Line fit_.

![Destination tab of the Convert Task for a TXT to PDF conversion, with the Page margins, Font details and Page orientation and Line fit groups](pathname:///img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Convert%20Destination%20TXT.png)

- _Left_, _Right_, _Top_ and _Bottom_ (_Page margins (points)_ group): the margins around the page content, in points

  A blank value, or one that is not a number, gives "50" for a TXT or XML source. The group also appears for "IMAGE", where a blank value gives "5".

- _Font_ (_Font details_ group): the installed font for the text; leave it blank for "Courier New"
- _Font size_: the size of the text in points; leave it blank for "12"
- _Font style_: "Regular", "Bold", "Italic" or "BoldItalic"

  The Task does not currently apply this setting.

- _Orientation_ (_Page orientation and Line fit_ group): "Auto", "Portrait" or "Landscape"

  "Auto" uses landscape when the text is wider than it is tall, otherwise portrait.

- _Line Fit_: scales the text horizontally so that it fits between the page margins

#### Output paper size

An _Output paper size_ group sets the page size of the converted document instead of the size the conversion produces. It is available with _To PDF from_ for every format except "SVG", and with _From PDF to_ for "DOC", "PPT" and "XPS".

- _Paper size_: "Default (auto)", "A3", "A4", "A5", "Letter", "Legal", "Tabloid" or "Custom"

  "Default (auto)" keeps the size the conversion produces; for an image source, the page takes the size of the image. With any other size, an image source is scaled to fit the page and centered.

- _Width_, _Height_ and _Unit_: shown when _Paper size_ is "Custom"

  Enter the page width and height and choose "mm", "in" or "pt". Both values must be greater than "0" and, in points, no larger than "14400"; the Task window does not save the Task until they are.

### Output and errors

With _To PDF from_, the Task output contains the path of each PDF file it writes; the paths are not separated by line breaks. With _From PDF to_, the Task writes nothing to the output.

:::warning

With _From PDF to_ "IMAGE", when _Pages_ selects a single page, no image is saved, and the Task reports success.

:::
