---
sidebar_label: 'Move a License'
hide_title: 'true'
---

## Move a license

This page explains how to move a VisualCron license from one Server to another, for example when you replace the Server computer. You copy the settings to the new Server, deactivate the license on the old Server, and then activate the same activation code on the new Server.

### Before you start

Make sure you have:

* The *Execute* permission on *License*, to deactivate (see [Supported Permissions](../client-user-interface/server/supported-permissions))
* An active maintenance for a perpetual license, or an active subscription for a subscription license; otherwise the Client shows a message and the license stays on the old Server
* Internet access from the computer where the Client runs to [www.visualcron.com](https://www.visualcron.com) on port 443, when you deactivate
* The activation code, noted before you deactivate, because the old Server no longer shows it afterwards. To copy it, click *Server* -> *Information* -> *License* -> *Copy activation code to clipboard*; this needs the *Read* permission on *License*, and the confirmation message shows the code
* A new Server that is not activated yet and is still in its trial period: *Activate* is available only while a Server is not activated, and after the trial ends the Client can no longer manage the Server until it is activated or its trial is extended

### Copy the settings to the new Server

To copy the settings, complete the following steps:

1. Download and install VisualCron on the new Server.
2. Validate on the My licenses page that you have a Maintenance contract that supports the installed new version for the latest version so you do not run into license problems when trying to activate it later
3. Connect the Client to the old Server.
4. Click *File* -> *Import/Export* -> *Export settings*, and export the settings to a file (see [Import/Export - Export Settings](../client-user-interface/file/export-settings)).
5. Copy the file to the new Server.
6. Connect the Client to the new Server.
7. Click *File* -> *Import/Export* -> *Import settings*, and import the file with *Clear existing* selected, unless you have already created Jobs on the new Server (see [Import/Export - Import Settings](../client-user-interface/file/import-settings)).

The new Server has the settings of the old Server.

### Deactivate the old Server and activate the new Server

:::warning

Before you click *Deactivate*, make sure the computer where the Client runs can reach [www.visualcron.com](https://www.visualcron.com). If it cannot, the old Server still returns to trial and its activation code is cleared, but the code stays registered as in use, and the Client shows no message. The new Server then cannot be activated with it. The *Trial Information* group on the ***Server*** tab does not prove that the code was released. If this has happened, contact [VisualCron support](https://www.visualcron.com/Contact.aspx), or release the code as described in [If the old Server is no longer available](#if-the-old-server-is-no-longer-available).

:::

To move the activation, complete the following steps:

1. Connect the Client to the old Server.
2. Click *Server* -> *Information* -> *License* -> *Deactivate*.
3. Click *Yes* to confirm.
4. Check that the ***Server*** tab shows the *Trial Information* group. This shows that the old Server is in trial, not that the code was released (see the warning above). If the old Server's trial has already ended, the Client also shows the *Trial period has ended* window.
5. Connect the Client to the new Server.
6. Activate the new Server with the same activation code, as described in [License and activation](license-and-activation). The new Server computer does not need Internet access. If the Client computer you use for the new Server cannot reach the website, use offline activation.

The new Server is activated, and the old Server is back in trial. The old Server stops running Jobs if its trial period has already ended.

If you have problems deactivating or activating, contact [VisualCron support](https://www.visualcron.com/Contact.aspx).

### If the old Server is no longer available

If the Server is decommissioned and no longer available please go to [My licenses page](https://www.visualcron.com/Login.aspx?DestinationPageUrl=~%2fMyLicenses.aspx) and click on the Move button next to the activation code.

Deactivation / Move a license requires that you have an active Maintenance.

### Trial licenses

Trial licenses are provided exclusively for evaluation purposes. They may not be used to support production jobs, pre‑cutover testing, environment migrations, or any business‑critical workflows.
