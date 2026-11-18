---
sidebar_label: 'Folder Filter'
hide_title: 'true'
---

## Folder Filter

The folder filter is similar to the file filter but filters out folders only. It is used in various Tasks.
 
**Folder filter > Location** sub tab

![Folder filter Location sub tab in the List folders Task](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Folder%20Filter.png)

**Credentials**

To control a remote computer you may need to use a Credential. Normally that Credential is a remote or AD user with *Local login* unchecked. The Credential must match the user name and password of the user that you want to log in as. Select a Credential in the combo box or click the Settings icon to open *Manage Credentials* in order to add or edit Credentials.
 
**Base folder**

Where the search filter should start finding folders. Click the Folder icon to browse the folder tree.
 
**Include base folder**

If the base folder should be included in the result.
 
**Include sub folders**

Folders directly under the base folder are always searched. Select this option to also search folders at every level below them.
 
**Include folder mask**

A wildcard pattern for folder names, for example `"Archive*"`. Separate several patterns with a semicolon and no spaces, for example `"Archive*;Backup*"`. If you use the *File* icon next to the field, delete the path it inserts and keep only the folder name: a full path does not work as a mask.
 
**Is regex**

If the include folder mask is a regular expression
 
**Case sensitive**

If case sensitive search should be done on the include folder mask.

**Use folder exclusion**

Check this to enable the exclude folder mask below. When unchecked, no exclusion mask is applied.
 
**Exclude folder mask**

When *Is regex* is cleared, a wildcard pattern for the folder names to exclude, for example `"Old*"`. Separate several patterns with a semicolon and no spaces, for example `"Old*;Temp*"`. Unlike the include folder mask, this field also accepts a full folder path, such as `"D:\Data\Old"`, which excludes only that folder, not its sub folders. The *File* icon next to the field opens a folder browser and replaces the field's content with the path you select. If any pattern in the list has no backslash (`\`), every pattern is matched against folder names only, and a full path in the same list matches nothing.
 
**Is regex**

If the exclude folder mask is a regular expression.

:::warning
A regular expression in the exclude folder mask is matched against the path of each folder's parent
folder, not the folder's own name: to exclude the folders in `D:\Data\Old`, the expression must match
`D:\Data\Old`. It uses the *Case sensitive* setting of the include folder mask.
:::

**Case sensitive**

If case sensitive search should be done on the exclude folder mask. Applies when *Is regex* is not
selected.

**Folder filter > Date** sub tab

![Folder filter Date sub tab with the older than and newer than checks](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Folder%20Date.png)

There are two types of checks *Older than* and *Newer than*. These can be combined with AND/OR or used separately. Enter a date Variable or a date. The value is always checked when you save or test the filter. Once you have selected a Variable it can be previewed when hovering over text box (tool tip) or in the group caption.
 
Click on the *Variables* icons to view and select available Date Variables.
 
**Folder filter > Size** sub tab

![Folder filter Size sub tab with the smaller than and larger than checks](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Folder%20Size.png)

**Check if folder is smaller than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the folder is smaller than the value you enter in the numeric box it will return true (=folder will be included).
 
**Check if folder is larger than x size**

Select this to enable size checking. Enter a value in the numeric text box and select the size unit to compare with. Default is kilobyte(s). If the size on the folder is larger than the value you enter in the numeric box it will return true (= folder will be included).
 
The two size checks can be combined with AND or OR. A folder's size is the total size of the files in
it, including files in its sub folders.

:::warning
With OR and only *Check if folder is larger than x size* selected, every folder matches. Select both
checks, or only the smaller-than check.
:::
 
**Folder filter > Result** sub tab

The filtered folders can be sorted and the number of returned rows limited.

**Sort**

Select *Sort* to sort the found folders on *Full path*, *Folder name*, *Modified date*, *Created date* or
*File size*, in *Ascending* or *Descending* order. If *Sort* is cleared, the folders are returned in the
order they are found.

:::warning
*File size* currently sorts by full path, not size, and *Created date* currently always sorts in
ascending order, even with *Descending* selected. If you use *Limit*, check the result on the
**_Test_** sub tab.
:::
 
**Limit**

Check this if you want to limit the number of rows returned. It will be limited according to the number (which could be a Variable) and the current sorting.
 
**Folder filter > Test** sub tab

![Folder filter Test sub tab listing the folders found](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Folder%20Test.png)

**Show filtered folders**

The test will use the selected Credential and lets you test your folder filter - what folders it returns based on the filter. The number of folders found and the elapsed time are shown.
