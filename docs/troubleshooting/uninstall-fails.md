---
sidebar_label: 'Uninstall Fails - Cannot Find Package VisualCron.msi'
hide_title: 'true'
---

## Uninstall Fails - Cannot Find Package VisualCron.msi

### Symptom

When you uninstall VisualCron, Windows Installer reports that it cannot find the package "VisualCron.msi".

### Cause

Windows Installer is asking for the original installation package. The *Uninstall VisualCron* shortcut in the Start menu asks Windows Installer to check the installation first, which can need that package. The setup program extracts "VisualCron.msi" to a temporary folder, "%TEMP%\VisualCron", of the user who ran it. That copy may no longer exist.

### Fix

If the message appears when you use *Uninstall VisualCron* in the Start menu, uninstall from Windows instead. To uninstall from Windows, complete the following steps:

1. Open Windows *Settings* -> *Apps* -> *Installed apps*, or *Control Panel* -> *Programs and Features*.
2. Find the entry `VisualCron <version>`.
3. Select *Uninstall*.

   VisualCron is uninstalled. Your settings folder stays in place.

If that also fails, remove VisualCron with the MSI package of the same version, from the custom installation package.

To uninstall VisualCron with the MSI package, complete the following steps:

1. Go to *File* -> *Import/Export* -> *Export settings*.
2. Export your settings to a file outside the VisualCron installation folder. See [Import/Export - Export Settings](../client-user-interface/file/export-settings).
3. Copy the settings folder, by default "C:\Program Files (x86)\VisualCron\settings", to a safe location.
4. In Windows *Settings* -> *Apps* -> *Installed apps*, or in *Control Panel* -> *Programs and Features*, find the entry `VisualCron <version>`, and note the version.
5. Download the custom installation package (.zip) for that version. See [Get VisualCron](../get-visualcron/get-visualcron.md).
6. Extract the .zip file to a folder.

   "VisualCron.msi" is in the version folder inside the extracted package.

7. Double-click "VisualCron.msi".

   The setup wizard asks whether you want to repair or remove VisualCron.

8. Select the option that starts with *Remove VisualCron*.
9. Complete the wizard.

   VisualCron is uninstalled. Your settings folder stays in place.

The MSI package of a different version cannot remove the installed version.