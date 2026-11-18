---
sidebar_label: 'Task File - Archive - Compress'
hide_title: 'true'
---

## Task File - Archive - Compress

The *Archive - compress* Task compresses files into an archive in one of these formats: 7z, BZip2, GZip, Tar, Tar+GZip, Xz, Zip or Zipx.
 
The different formats provides different functionality and compatibility across different operating systems. The Tar and GZip formats can be used to read or write archives between Windows and Linux/Unix. The **Zip** format is the most versatile and the most common in Windows workstations. It allows you to encrypt your archive with a password and select a compression level.
 
**Tar** and **GZip** are usually used together. Tar is an archive; it gathers a collection of files or folders into a single file, while preserving file system information (such as permissions, dates and the folder structure). However, Tar does not compress the files in any way. The GZip format on the other hand is typically used to compress single files.
 
Using these two formats together, Tar to create an archive and then compressing it with GZip, can potentially attain greater compression ratios than using a compressing archiver such as ZIP. The ZIP format compresses the individual files and then archives them into a single .zip file. With a GZip Tar file, files are first archived into a .tar file and then the complete archive is compressed. The advantage is that the compression engine searches for similar patterns across the entire archive, rather than just within each individual file, thereby increasing the chances of finding the patterns for this kind of compression. When used together, the resulting files typically have a .tar.gz extension. For the Tar+GZip format in this Task, end the archive path in `".tar.gz"`.

:::note NTFS long paths in Windows
 
By default, the [maximum path length limit in Windows](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry) is 260 characters. However, it is possible to remove the limitation on Windows 10 (v. 1607 or later) so that VisualCron will support the paths that are longer than 260 characters. In the context of the current Task, this feature allows to archive files within folders of unlimited depth, ensuring correct extraction at any nesting level of the target folder.
To turn this on, see [Enable long paths in Windows](#enable-long-paths-in-windows).

:::

When the *Archive - compress* Task is selected in the Task window you are presented with a set of sub tabs within the *Archive - compress* tab.
 
**Archive - compress > Archive settings** sub tab

![Add Task dialog for the Archive - compress Task, Archive settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Archive%20-%20Compress.png)

The archive settings sub tab controls the main settings, including the archive format and what happens when the archive already exists.
 
**Archive type**

Select one of *7z*, *BZip2*, *GZip*, *Tar*, *Tar+GZip*, *Xz*, *Zip* and *Zipx*.
 
**Credential**

Optional Credential for accessing the archive path when it is on a remote or network location.
 
**Archive path**

The archive path is the full path where your archive is stored. You can choose any name for your archive but the following names are recommended:

* 7z: `"myarchive.7z"`
* Zip: `"myarchive.zip"`
* Zipx: `"myarchive.zipx"`
* Tar: `"myarchive.tar"`
* Tar+GZip: `"myarchive.tar.gz"`
* GZip: `"myarchive.gz"`
* BZip2: `"myarchive.bz2"`
* Xz: `"myarchive.xz"`
 
**Use password**

Available for the 7z, Zip and Zipx formats. Enter the password that protects the archive.
 
**Compression level**

Available for the 7z, Zip and Zipx formats. A higher level is slower and produces a smaller file.
Levels: *Ultra compression*, *High compression*, *Normal compression* (default) and *Low compression*.
 
**Encryption method**

Available for 7z, Zip and Zipx archives when *Use password* is selected. For Zip and Zipx archives:

- *WinZipAES* (default): AES encryption. Use it unless the recipient's software cannot open AES
  archives
- *Compatible*: traditional Zip encryption, which is weak; use it only for compatibility
 
**Encryption strength**

Available when *Encryption method* is *WinZipAES*. Select 128, 192 or 256 bits (default 256). Use 256
unless the recipient cannot open it.
 
**Overwrite archive if existing**

When this option is selected, the archive will be overwritten (if existing).
 
**Append to archive**

If the archive exists it will be appended with new items.

**Always create archive**

When checked, an empty archive file is created even if no files match the content filter. When unchecked, no archive is written if there are no matching files.
 
**Archive - compress > Content** sub tab

![Archive - compress Task, Content sub tab, with the Add/Edit archive item dialog open on its file filter](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Archive%20-%20Compress%20Content.png)

This sub tab contains a list of items/objects to be compressed. Use the Add, Edit, Clone, and Delete toolbar buttons to manage items.

The Archive item dialog uses the standard [file filter](../../../server/job-tasks-file-filter) to select which files to add to the archive.

**Archive item > Item settings** tab

These settings decide what happens to the archive's existing contents when the archive already exists:
because *Append to archive* is selected on the **_Archive settings_** sub tab, or because an earlier
item in this Task has already added files to it.

- *Overwrite if existing* (default): entries already in the archive that match the files this item
  adds are removed, and then the item's files are added
- *Append to archive*: the item's files are added, and no existing entry is removed first

These settings are not used for the Tar+GZip format.

**Delete source file after**

When checked, the source file is deleted after it has been successfully added to the archive.
 
:::info Note 

When you are accessing a network drive (a folder on a remote computer) as source or destination folder you must specify the path in UNC format and not the letter of the logical drive. For example `Y:\remotefolder\` must be specified as `\\remoteservername\remotefolder\`.

:::

### Enable long paths in Windows

This changes a Windows setting for the whole computer, not only for VisualCron.

To enable long paths by using the registry (Windows Home), complete the following steps:

1. Press the _Windows_ key and _R_ together. The _Run_ dialog opens.
2. In the _Open_ field, enter `"regedit"`.
3. Select the _OK_ button. The _Registry Editor_ window opens.
4. Go to `"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem"`.
5. Create a DWORD (32-bit) value named `"LongPathsEnabled"`.
6. Set the value of `"LongPathsEnabled"` to `"1"`.
7. Restart the computer.

After the restart, Windows accepts paths longer than 260 characters.

To enable long paths by using Group Policy (Windows Pro and Enterprise, and Windows Server 2016 or later), complete the following steps:

1. Press the _Windows_ key and _R_ together. The _Run_ dialog opens.
2. In the _Open_ field, enter `"gpedit.msc"`.
3. Select the _OK_ button. The _Local Group Policy Editor_ window opens.
4. Go to _Local Computer Policy_ -> _Computer Configuration_ -> _Administrative Templates_ -> _System_ -> _Filesystem_.
5. Open the _Enable Win32 long paths_ setting.
6. Select the _Enabled_ option.
7. Select the _OK_ button.
8. Restart the computer.

After the restart, Windows accepts paths longer than 260 characters.
