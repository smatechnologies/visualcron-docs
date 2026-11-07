---
sidebar_label: 'Assembly Resolver - Runtime Download of Components'
hide_title: 'true'
---

## Assembly Resolver - Runtime Download of Components

Some large components are not included in the installation package, to keep it small. When VisualCron needs one of them and it is missing, it can download it from the VisualCron website. Usually these are the OCR language packs for the Scan Document Task. The same mechanism also restores other large libraries if they are missing from the installation folder, for example those used by the PDF Tasks, the Print Document Task, the Web Macro Task, the SAP Tasks and the VMware Tasks.

Both the Client and the Server can download a missing component.

### The Assembly resolver window in the Client

The *Assembly resolver - missing files* window can open when the Client connects to a Server, usually for the OCR language packs. It also opens when the Client needs a missing component while you work.

| Column | Description |
|---|---|
| *Download* | Select to include the file. Every file is selected when it is added |
| *File name* | The name of the missing file |
| *Version* | The version that is needed |
| *Size* | The file size in MB, or "NA" when it is not known |
| *On Client* | "Yes" when the file is in the Client installation folder |
| *On Server* | "Yes" when the file is in the installation folder of the Server. "NA" when the Client is connected locally |
| *Download progress* | The progress of the download to the Client |
| *Transfer progress* | The progress of the copy between the Client and the Server |
| *URL* | The download address of the file |

The *Download* button gets the selected files. For each file, the Client uses the first of these that is available:

1. A copy in the `dll\<version>` subfolder of the Client installation folder
2. The file on the Server, if the Server has it
3. A download from the VisualCron website

Whichever source it uses, the Client saves the file in the Client installation folder itself.

When the Client is connected to a Server on another computer and that Server does not have the file, the Client then copies the file to the Server's installation folder.

*Copy URL list* copies the download addresses of the listed files to the clipboard.

*Download all references* downloads one package of all these components, extracts it to the `dll` subfolder of the Client installation folder, and then starts the download of the selected files.

*Auto close when installation complete* closes the window when the download is finished. It is selected by default.

:::note

The Client saves downloaded files in the Client installation folder. When the Client is installed in "C:\Program Files (x86)\VisualCron", start it with *Run as administrator* before you click *Download* or *Download all references*.

:::

If a file cannot be found on the website, a *Download error* message lists the file name and its address. Send a screenshot of the message to support@visualcron.com.

If the download fails for another reason, for example because the computer has no internet access or a proxy blocks the download, no message appears, and *On Client* can still show "Yes". Add the files by hand, as described in [Servers without internet access](#servers-without-internet-access).

### Auto download on the Server

When a Task on the Server needs a missing component, the Server can download it into its installation folder and load it. This depends on *Auto download missing dependencies*, in the *Assembly resolving options* group on the ***Main settings*** tab of _Server_ -> _Main settings_ -> _Settings_:

- While the option is cleared, the Server downloads the missing component and writes "Downloading missing file" to the Server log. If the download fails, the log shows "Can't download assembly"
- While the option is selected, the Server does not download the component, and the Task that needs it cannot load it

To stop the Server from downloading components, select the option. To let it download them, clear the option.

### Servers without internet access

To add the components by hand, complete the following steps:

1. In the *Assembly resolver - missing files* window, click *Copy URL list*.
2. On a computer with internet access, download each file from the copied addresses.
3. Copy the files to the Client installation folder.
4. Copy the files to the installation folder of the Server that needs them.
5. Restart the Client.
6. Restart the VisualCron service.

For the outbound connections that these downloads need, see [Firewall and network](antivirus-exclusions#firewall-and-network).
