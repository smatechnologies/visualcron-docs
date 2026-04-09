---
sidebar_label: 'Task Image - Profile Conversion'
hide_title: 'true'
---

## Task Image - Profile Conversion

The Image profile conversion Task converts the image from the input color profile to the specified output color profile.
 
**Image profile conversion > File filter > Location** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Settings.png)

In the File filter tab you define the image file to change the profile for. Read more about file filter [here](../../../server/job-tasks-file-filter).
 
**Image profile conversion > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Destination.png)

**Input profile file**

The file path to the ICC color profile of the input image. Click the File icon to browse for a profile file.
 
**Output profile file**

The file path to the ICC color profile to apply to the output image. This field is required. Click the File icon to browse for a profile file.
 
**Filter string for delete profile(s)**

A filter string specifying which embedded profiles to remove from the image during conversion.
 
**Save to**

Select where to save the converted output file:

* _Same file_ - overwrites the original source file with the converted output; the Folder and File mask fields are disabled
* _Same folder but use file mask_ - saves the output to the same folder as the source using a new file name pattern; the Folder field is disabled but the File mask field is enabled
* _Different folder and use file mask_ - saves the output to a different folder with a new file name pattern; both the Folder and File mask fields are enabled
 
**Folder**

The destination folder for the output file. Only enabled when _Different folder and use file mask_ is selected. Click the Folder icon to browse for a folder.
 
**File mask**

The file name pattern to use for the output file. Enabled when _Same folder but use file mask_ or _Different folder and use file mask_ is selected.
