---
sidebar_label: 'Task Net - WebDAV - Upload'
hide_title: 'true'
---

## Task Net - WebDAV - Upload

The WebDAV - Upload Task lets you upload documents based on a file filter. Web-based Distributed Authoring and Versioning (WebDAV) is a set of methods based on the Hypertext Transfer Protocol (HTTP) that facilitates collaboration between users in editing and managing documents and files stored on World Wide Web servers.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Upload%20.png)

**File filter** tab

The WebDAV - Upload Task uses the [standard file filter](client-user-interface/server/job-tasks-file-filter.md) to select which local files to upload.

**Upload settings** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Upload%20Settings.png)

**Connection**

All WebDAV Tasks use connection settings from a Connection. In Connections you can create a new WebDAV connection with all other details like Proxy. In the combo box you select the Connection after creation.

**Target URL folder**

The URL of the remote folder to upload files to. Use the folder browse button to select a folder from the server (a Connection must be selected first).

**Save files to destination folder**

When selected, all matched files are uploaded directly into the target URL folder, regardless of their original folder structure. This is the default.

**Save files to destination relative to source path**

When selected, the relative path of each source file is preserved under the target URL folder.
