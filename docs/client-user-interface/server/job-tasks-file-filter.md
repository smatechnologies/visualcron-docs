---
sidebar_label: 'File Filter'
hide_title: 'true'
---

## File Filter

The file filter is a part of many Tasks and other objects within VisualCron. The purpose of the file filter is to provide a standardized way of filtering out files for a given Task.

### Evaluation

The file filter is evaluated the following way:

* **Location** AND **Content** AND **Date** AND **Size** AND **Attributes** = filtered files
* **Date** = Date older than AND/OR Date newer than
* **Size** = Size smaller than AND/OR Size larger than
 
**File filter > Location**
Contains the basic properties of finding one or more files.

![File filter Location sub tab with the Browse For Folder window opened from the Folder field](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Location%20sub%20tab.png)

**Credentials**

To access a remote computer you may need to use a [Credential](../server/global-credentials). Normally that Credential is a remote or AD user with *Local login* unchecked. The Credential must match the user name and password of the user that you want to log in as. Select a Credential in the combo box or click the Settings icon to open *Manage Credentials* in order to add or edit Credentials.
 
**Folder**

The folder path where the source file(s) reside. You can input several folders by separating with semicolon ";" like this: C:\Temp;C:\test. Click the Folder icon to browse the folder tree.
 
**Include sub folders**

If the file filter should look for files in sub folders then check this option.
 
**Exclude folder(s)**

If the file filter should exclude folder(s) to look for files. Click the Folder icon to browse the folder tree. To exclude several folders, separate them with a semicolon and no spaces, for example `C:\a;C:\b`. A space is kept as part of the path, so `C:\a; C:\b` does not exclude `C:\b`. Note that the exclusion is exact to a specific folder. For example:
 
`C:\subfolder\main2` - excludes files in `main2` only; its sub folders are still searched.

`C:\subfolder\main2*` - excludes `main2`, its sub folders, and every other folder whose path starts with that
text, such as `main20`.
 
**Include file mask**

Define your file mask for the file name here. When not using the Is regex string, you can use the normal wildcard characters like * or ?. You can input more than one file mask by separating them with semicolon ";" like this: *.doc;*.txt. Click the File icon to browse for files.
 
**Is regex**

If the include file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
 
**Case sensitive**

Makes the match case sensitive for the exclude file mask, and for the include file mask only when *Is regex*
is selected. A wildcard include file mask always ignores case.

**Use file exclusion**

Check this to enable the exclude file mask below. When unchecked, no exclusion mask is applied.
 
**Exclude file mask**

It is possible, the same way, to use a exclusion filter. When not using “Is regex” string here you can use the normal wildcard characters like * or ?.
 
**Is regex**

If the exclude file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
 
**File filter > Content**

Makes it possible to check found files for content.

![File filter Content sub tab set to Contains](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Content%20sub%20tab.png)

The default **Content** property is *Don't check*. Use the list to select the desired check. The available checks are *Contains*, *Not contains*, *Equal*, *Not equal*, *Match RegEx* and *Not match RegEx*.
 
**File filter > Date**

Makes it possible to check the created/modified date against a Variable value.

![File filter Date sub tab with the older than and newer than checks and Validate dates before saving](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Date%20sub%20tab.png)

There are two types of checks *Older than* and *Newer than*. These can be combined with AND/OR or used separately. Enter a date Variable, or a date in the format shown under *Accepted Server format*. Once you have selected a Variable it can be previewed when hovering over text box (tool tip) or in the group caption.
 
Click the *Variables* icons to view and select available Date Variables.

*Validate dates before saving* is selected by default. The date values are checked against the Server date format when you save or test the filter. The check box is not saved with the filter; it is selected again each time you open the filter.
 
**File filter > Size**

Makes it possible to filter out files based on size. Like the Date filter it can be combined with AND/OR and check can be done on *Larger than* or *Smaller than*.

The screenshot is from the Cloud *List item(s)* Task, which has the same size checks.

![Size sub tab with the smaller than and larger than checks](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Size%20sub%20tab.png)

**Check if file is smaller than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the file is smaller than the value you enter in the numeric box it will return true (= file will be included).
 
**Check if file is larger than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the file is larger than the value you enter in the numeric box it will return true (= file will be included).
 
**File filter > Attributes**

All files have different attributes. If you want to check for a specific attribute you can use whether to include or exclude a file based on attribute.

![File filter Attributes sub tab with the Include attribute(s) and Exclude attribute(s) lists](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Attributes%20sub%20tab.png)

**Include all attributes**

The default is checked, uncheck if you want to filter on attributes.
 
**Include attribute(s)**

A file is included only when its full set of attributes is exactly one of the selected items. For
example, a file with both the Archive and ReadOnly attributes is not included when you select
*Archive*, *ReadOnly*, or both.

**Exclude attribute(s)**

:::warning
*Exclude attribute(s)* currently has no effect: files with the selected attributes are not excluded.
:::

**File filter > Result**

The filtered files can be presented (in output) in different ways. It is possible to sort the result on various values like name, modified date, created date and size. You can also limit the number of rows returned to, for example, only list the top 3 files according to the current sorting.

![File filter Result sub tab with the Sort and Limit settings](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Result%20sub%20tab.png)

**Sort**

Select to sort the result on *File name*, *Modified date* (default), *Created date* or *File size*, in
*Ascending* (default) or *Descending* order. If *Sort* is cleared, the files are returned in the order
they are found.

:::warning
Do not sort on *Full path*: with it selected, the search currently fails with an error.
:::

**Limit**

Select to limit the number of files returned (default 10). The limit applies after sorting: with *Sort*
selected and its defaults (*Modified date*, *Ascending*), the oldest files are returned first; select
*Descending* for the newest. If *Sort* is cleared, *Limit* returns the first files in the order they are
found. The number can be a Variable. The number, or the value of the Variable, must be a whole number of 1
or more; otherwise the filter returns no files, and the error appears only in the Server log.

**File filter > Test**

Makes it possible to test your current file filter - if it matches any existing files

![Test sub tab showing the files the filter found](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Test%20sub%20tab.png)

**Show filtered files**

The test will use the selected Credential. Click to test the filter.
