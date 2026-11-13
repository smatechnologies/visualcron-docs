---
sidebar_label: 'Job Folders'
hide_title: 'true'
---
## Job Folders

Job folders let you sort Jobs into a folder structure of your own. A Job can be in several folders. When you click a folder, the main grid shows only the Jobs in that folder; ***All Jobs*** shows every Job. The ***Favorites*** folder is always there and cannot be deleted.

The Job folders pane is at the left of the main window. To show or hide it, use _Show Job folders_ on the ***Grid*** tab of [Client settings](file/client-settings), or right-click the pane and click ***Hide Job folders***.

![The Job folders pane with the Favorites, All Jobs and user-created folders](../../static/img/Client%20User%20Interface/Status%20Bar/Folders.png)

### Manage folders

Right-click in the Job folders pane. The menu items name the folder you right-clicked:

- ***Add folder to root***, or `Add folder to folder '<folder name>'` on a folder: creates a folder, or a subfolder in that folder, on the current Server
- `Rename folder '<folder name>'`: renames the folder
- `Delete folder '<folder name>' and all sub folders`: deletes the folder and its subfolders at once, without a confirmation
- ***Delete all folders***: deletes all Job folders, after a confirmation

On ***Favorites*** and ***All Jobs***, rename and delete are unavailable.

:::warning

Renaming or deleting a folder applies to every Server the Client is connected to, not only the current one. Deleting a folder does not delete its Jobs; they are only removed from the folder, and the folder assignments are lost.

:::

You need permission to edit the Server settings.

### Add Jobs to a folder

To add one Job, right-click it in the main grid, click ***Add to folder*** and select a folder. The folders the Job is already in are shown with a check mark. You can also drag a Job from the main grid onto a folder in the Job folders pane.

To add a whole Job group, right-click the Job group row, click ***Add to folder*** and select a folder. Every Job in the group is added. The group menu shows no check marks, because the Jobs in a group can be in different folders.

### Remove Jobs from a folder

- While a folder is selected in the Job folders pane, right-click the Job, or several selected Jobs, and click `Remove from folder '<folder name>'`
- Or right-click the Job, click ***Add to folder*** and click a checked folder to clear it. This is also how you remove a Job from ***Favorites***

To remove all Jobs in a Job group from a folder, right-click the Job group row and click ***Select all Jobs***. Then right-click one of the selected Jobs, click ***Add to folder*** and click the checked folder.
