---
sidebar_label: 'Remote File Filter'
hide_title: 'true'
---

## Remote File Filter

The remote file filter is a limited version of the local [file filter](job-tasks-file-filter). It is used by the FTP Task and, depending on the source or target location, by the Cloud Sync files Task. The Remote file Trigger has its own, smaller filter. The screenshots on this page are from the Remote
file Trigger, so they show fewer settings than the filter in the FTP Task.
 
### Evaluation

The file filter is evaluated the following way:

* Location AND Date AND Size = filtered files
* Date = Date older than AND/OR Date newer than
* Size = Size smaller than AND/OR Size larger than
 
**Remote file filter > Location** sub tab

This tab contains the basic properties of finding one or more files.

![Location sub tab of the remote file filter in the Remote file Trigger](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/remote%20file%20location.png)

**Folder**

The folder path where the source file(s) reside. You can input several folders by separating with semicolon ";" like this:
```C:\Temp;C:\test```
 
**Include sub folders**

If the file filter should look for files in sub folders then check this option.
 
**Treat unknown types as files**

Some servers do not report the correct item type (file or folder) when listing items and instead report an unknown type. When checking this property VisualCron will treat unknown types as files. This setting is used only with SFTP Connections.
 
**Include file mask**

Define your file mask for the file name here. When not using “Is regex” string here you can use the normal wildcard characters like * or ?. You can input more than one file mask by separating them with semicolon ";" like this:
```*.doc```;```*.txt```
 
**Is regex**

If the include file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
 
**Case sensitive**

If the file name search is case sensitive.

**Use file exclusion**

Check this to enable the exclude file mask below. When unchecked, no exclusion mask is applied.
 
**Exclude file mask**

It is possible, the same way, to use a exclusion filter. When not using “Is regex” string here you can use the normal wildcard characters like * or ?.
 
**Is regex**

If the exclude file mask is a regular expression. For more information about regular expressions please look here: [http://www.regular-expressions.info/](http://www.regular-expressions.info/)

**Case sensitive**

If case sensitive search should be done on the exclude file mask.
 
**Remote file filter > Date** sub tab

It is possible to filter files by date. There are two checks, *Older than* and *Newer than*, which can be combined with the *AND/OR* selector or used separately. For each, select which date to check (*Don't check*, *Created date* or *Modified date*) and enter a value or Variable. The value can be a date Variable, or a date in the format shown under
*Accepted Server format*.

:::note
*Created date* currently checks the modified date, so both choices filter on the modified date.
:::

![Date sub tab of the remote file filter in the Remote file Trigger](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/remote%20file%20date.png)

**Validate dates before saving**

*Validate dates before saving* is selected by default. The date values are checked against the Server date format when you save or test the filter. The check box is not saved with the filter; it is selected again each time you open the filter.

**Remote file filter > Size** sub tab

It is possible to filter out files based on size. Like the Date filter it can be combined with AND/OR and check can be done on *Larger than* or *Smaller than*.

:::warning
With OR and only *Check if file is larger than x size* selected, every file matches. Select both
checks, or only the smaller-than check.
:::

![Size sub tab of the remote file filter in the Remote file Trigger](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/remote%20file%20size.png)
 
**Check if file is smaller than x size**

Filter files that are smaller than a value/Variable. Select the unit (*byte(s)*, *kilobyte(s)*, *megabyte(s)*, *gigabyte(s)* or *terabyte(s)*).
 
**Check if file is larger than x size**

Filter files that are larger than a value/Variable. Select the unit (*byte(s)*, *kilobyte(s)*, *megabyte(s)*, *gigabyte(s)* or *terabyte(s)*).
 
**Remote file filter > Result** sub tab

The filtered files can be sorted and the number of returned rows limited.

**Sort**

By checking *Sort* you can sort the found files on values like name, modified date, created date and size, in *Ascending* or *Descending* direction. If sort is unchecked the files are presented in the order they are discovered.
 
**Limit**

Check this if you want to limit the number of rows returned. It will be limited according to the number (which could be a Variable) and the current sorting.

**Remote file filter > Test** sub tab

In the Test tab you can test your current file filter - if it matches any existing files. The test will use the Connection selected for the Task. Click on *Show filtered files* to test the filter; the number of files found and the elapsed time are shown.

:::note
The test always ignores case for the exclude file mask, even when the exclude file mask's *Case sensitive*
option is selected. With that option selected, the test can list fewer files than the Task finds.
:::

![Test sub tab of the remote file filter in the Remote file Trigger](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/remote%20file%20test.png)
