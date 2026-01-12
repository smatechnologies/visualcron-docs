---
sidebar_label: 'Task Image - Crop'
hide_title: 'true'
---

## Task Image - Crop

The Image crop Task removes the outer parts of an image according to dimensions specified to an existing image.
 
**Image crop  > File filter > Location** sub tab

In the File filter tab you define the image file to be cropped. Read more about file filter [here](../../../server/job-tasks-file-filter).
 
**Image crop > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20crop.png)

**Crop position and dimensions**

Top and Left define the upper left corner of the cropped image.
Width and Height define the size of the cropped image.
 
**Save to**

The destination folder and file mask which the image is saved to.
 
**Folder**

If *Different folder and use file mask* is selected, use manual folder specification or click the *Folder* icon.
 
**File mask**

Save file with different name.
 
:::info Note


Maximum values of Top and Left are related to the original image pixels.
The Width and Height values are applied to the resulting image after Top and Left modification.
If the Width or Height value is 0, the Width or Height value after Left or Top is used.

:::