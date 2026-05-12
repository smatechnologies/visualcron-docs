---
sidebar_label: 'Task Image - Profile Conversion'
hide_title: 'true'
---

## Task Image - Profile Conversion

The Image profile conversion Task converts the image from the input color profile to the specified output color profile.
 
**Image profile conversion > File filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Settings.png)

In the File filter tab you define the image file to change the profile for. Read more about file filter [here](../../../server/job-tasks-file-filter).
 
**Image profile conversion > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Destination.png)

**Profile conversion parameters**

**Input profile file**

The file path to the ICC color profile of the input image. Click the File icon to browse for a profile file.
 
**Output profile file**

The file path to the ICC color profile to apply to the output image. This field is required. Click the File icon to browse for a profile file.
 
**Filter string for delete profile(s)**

A filter string specifying which embedded profiles to remove from the image during conversion.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20Profile%20Settings.png)
 
**Save to**

Select where to save the converted output file:

* **Same file** — Overwrites the original source file.
* **Same folder but use file mask** — Saves to the same folder with a new file name specified in File mask.
* **Different folder and use file mask** — Saves to a different folder with a new file name.

**Folder**

The destination folder path. Only available when **Different folder and use file mask** is selected.

**File mask**

The file name to use for the saved image. Available when **Same folder but use file mask** or **Different folder and use file mask** is selected.
