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

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Location%20sub%20tab.png)

**Credentials**

To access a remote computer you may need to use a [Credential](../server/global-credentials). Normally that Credential is a remote or AD user with "Local logon" unchecked. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Folder**

The folder path where the source file(s) reside. You can input several folders by separating with semicolon ";" like this: C:\Temp;C:\test. Click the Folder icon to browse the folder tree.
 
**Include sub folders**

If the file filter should look for files in sub folders then check this option.
 
**Exclude folder(s)**

If the file filter should exclude folder(s) to look for files. Click the Folder icon to browse the folder tree. You can exclude multiple sub folders by separating them with semicolon. Please not that the exclusion is exact to a specific folder. For example:
 
**```C:\subfolder\main2```** - this will exclude files in that folder only.
```C:\subfolder\main2*``` - this will exclude files in this folder and sub folders to this folder.
 
**Include file mask**

Define your file mask for the file name here. When not using the Is regex string, you can use the normal wildcard characters like * or ?. You can input more than one file mask by separating them with semicolon ";" like this: *.doc;*.txt. Click the File icon to browse for files.
 
**Is regex**

If the include file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
 
**Case sensitive**

If the file name search is case sensitive.
 
**Exclude file mask**

It is possible, the same way, to use a exclusion filter. When not using “Is regex” string here you can use the normal wildcard characters like * or ?.
 
**Is regex**

If the exclude file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
 
**File filter > Content**

Makes it possible to check found files for content.

**File filter > Content**

Makes it possible to check found files for content.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Content%20sub%20tab.png)

The default **Content** property is *Don’t check*. Use the drop-down list to select the desired property.
 
**File filter > Date**

Makes it possible to check the created/modified date against a Variable value.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Date%20sub%20tab.png)

There are two types of checks *Older than* and *Newer than*. These can be combined with AND/OR or used separately. Only date variables can be used here. Once you have selected a Variable it can be previewed when hovering over text box (tool tip) or in the group caption.
 
Click the *Variables* icons to view and select available Date Variables.
 
**File filter > Size**

Makes it possible to filter out files based on size. Like the Date filter it can be combined with AND/OR and check can be done on *Larger than* or *Smaller than*.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Size%20sub%20tab.png)

**Check if file is smaller than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the file is smaller than the value you enter in the numeric box it will return true (= file will be included).
 
**Check if file is larger than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the file is larger than the value you enter in the numeric box it will return true (= file will be included).
 
**File filter > Attributes**

All files have different attributes. If you want to check for a specific attribute you can use whether to include or exclude a file based on attribute.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Attributes%20sub%20tab.png)

**Include all attributes**

The default is checked, uncheck if you want to filter on attributes.
 
**Include attribute(s), Exclude attribute(s)**

Check the attributes you want to include or exclude.
 
**File filter > Result**

The filtered files can be presented (in output) in different ways. It is possible to sort the result on various values like name, modified date, created date and size. You can also limit the number of rows returned to, for example, only list the top 3 files according to the current sorting.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Result%20sub%20tab.png)

**Sort**

It is possible to sort the result on various values like name, modified date, created date and size. If sort is unchecked the files will just be presented in the order they are discovered.
 
**Limit**

Check this if you want to limit the number of rows returned. It will be limited according to the number (which could be a Variable) and the current sorting.
 
**File filter > Test**

Makes it possible to test your current file filter - if it matches any existing files

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/File%20Test%20sub%20tab.png)

**Show filtered files**

The test will use the selected Credential. Click to test the filter.