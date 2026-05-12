---
sidebar_label: 'Task Image - Get EXIF Data'
hide_title: 'true'
---

## Task Image - Get EXIF Data

The Image get EXIF data Task gets EXIF values from the file according to the user-defined parameter list.
 
**Image get EXIF data > File filter** sub tab

In the File filter tab you define the image file to be checked for EXIF data. Read more about file filter [here](../../../server/job-tasks-file-filter).
 
**Image get EXIF data > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Image%20Tasks/Image%20get%20EXIF%20data.png)

**Selected parameters:**

To add a new parameter, click the empty template row at the bottom of the grid. Use the **Dir** (group) drop-down to select an IFD directory, then use the **Tag** drop-down to select a tag within that group. To delete a parameter row, right-click the row and select **Delete** from the context menu.
 
If the desired tag doesn't exist in the drop-down tag list, it is possible to add a new value using an integer. This solves an issue e.g. based on a new value which has not yet been included the tag list.

**Output settings**

**Include tag name**

When enabled, the tag name is included in the output alongside the tag value.

**Tag value separator**

The separator used between the tag name and its value.

**Text qualifier**

A character used to wrap tag values in the output.

**Tags separator**

The separator used between multiple tag entries in the output.

**Files separator**

The separator used between output blocks when multiple files are processed.

**Add file path into output**

When enabled, the file path of the source image is included in the output.

**Verbose description**

When enabled, a verbose description of the tag is included in the output.

**Include group name**

When enabled, the IFD group name is included in the output alongside the tag name.
