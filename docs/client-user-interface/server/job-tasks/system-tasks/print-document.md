---
sidebar_label: 'Task System - Print Document'
hide_title: 'true'
---

## Task System - Print Document

The Print document Task prints files on a printer of the VisualCron Server computer. It prints PDF, Word, Excel, PowerPoint, HTML, image and text files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Print document tab

The ***Print document*** tab has two sub tabs:

- ***File filter***: selects the files to print; see [File filter](../../job-tasks-file-filter). Every file that the filter returns is printed
- ***Print settings***: the printer and the print options below

![Print document tab with the File filter sub tab open](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Print%20Document.png)

- _Select printer_: the printer to use. The list shows the printers of the VisualCron Server computer

![Print settings sub tab, with the Select printer, Printer settings and Document groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Print%20Document%20Settings.png)

- _Paper source_ (_Printer settings_ group): the paper tray. Used for image, PDF and text files only
- _All Pages_ (_Page range_ group): prints the whole file. Selected by default
- _Page Range_: prints only the pages entered in the field below it, as page numbers and ranges separated by commas, for example `1,3,5-12`

  For Excel files, enter one range, for example `1-3`. For PowerPoint files, the options are _All Slides_ and _Slides_, and the field takes slide numbers. For text files, only _All Pages_ is available.

- _Number of copies_ (_Pages_ group): the number of copies. The default is "1"
- _Auto_, _Portrait_ or _Landscape_ (_Orientation_ group): the page orientation. The default is "Portrait". _Auto_ is used for PDF files only, where it follows the shape of the first page; other files print in portrait with _Auto_
- _Left_, _Right_, _Top_ and _Bottom_ (_Margin_ group): the page margins. The default is "2" for each
- _Auto detect document type from extension_ (_Document_ group): selected by default. The Task chooses the document type from the file extension:

  - `.pdf`: PDF
  - `.doc` and `.docx`: Word
  - `.xls` and `.xlsx`: Excel
  - `.ppt` and `.pptx`: PowerPoint
  - `.htm` and `.html`: HTML
  - `.jpg`, `.png`, `.gif` and `.bmp`: image
  - `.txt` and every other extension: text

  Because any other extension is printed as text, check that the extensions are correct.

- _Specify document type_: prints every file as the type selected in the list: "Word" (default), "Excel", "PowerPoint", "Image", "Text", "HTML", "PDF" or "Other". With "Other", the Task uses the Print command that Windows associates with the file type
- _Password_: the password of password-protected PDF files
- _Use fallback method_: for PDF files only, prints with a second PDF print method. Try it when a PDF file does not print correctly, for example in landscape

:::note

Word, Excel and PowerPoint files are printed through Microsoft Office, which must be installed on the VisualCron Server computer.

:::

### Output and errors

The output lists the path of each printed file, one per line.

### Troubleshooting

**The printer is not in the list**

The list shows the printers of the VisualCron Server computer. By default, the VisualCron Server service runs as the SYSTEM account, and that account must have access to the printer. Check the sharing permissions of the printer.

**Landscape mode is not working**

For PDF files, select _Use fallback method_.
