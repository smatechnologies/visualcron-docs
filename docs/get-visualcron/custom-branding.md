---
sidebar_label: 'Custom Branding'
hide_title: 'true'
---

## Custom Branding

You can change some of the names, email addresses and links that the VisualCron Client shows. The changes go in a file named "custom.xml", which the Client reads when it starts.

The file affects the Windows Client only. The Server, the Tray Client and the Web Client do not read it.

### Create the customization file

The installation folder is under Program Files, so you need administrator rights to save the file there.

To create the customization file, complete the following steps:

1. Open a text editor as administrator.
2. Add the options you want to change, in the format below. Options that you leave out keep their default values.

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <CustomizationClass>
     <ClientAppName>VisualCron - Client</ClientAppName>
     <ProductName>VisualCron</ProductName>
     <SupportEmail>support@visualcron.com</SupportEmail>
     <SalesEmail>sales@visualcron.com</SalesEmail>
     <ShowLinks>true</ShowLinks>
   </CustomizationClass>
   ```

3. Save the file as "custom.xml" in the root of the installation folder, by default "C:\Program Files (x86)\VisualCron" on 64-bit Windows or "C:\Program Files\VisualCron" on 32-bit Windows.
4. Restart the Client.

   The Client shows the values that you set.

If the file cannot be read, the Client uses the default values and shows "Error loading customization settings" in its log window. The message is not written to the Client log file.

:::note

The Client looks for "custom.xml" in the folder it starts in. The shortcuts that the installer creates start the Client in the installation folder. If you start the Client another way, for example from a shortcut that you created, set the shortcut's *Start in* folder to the installation folder. A Client opened from a Tray Client notification may also start in another folder, and then uses the default values.

:::

### Customization options

| Option | What it changes | Default |
|---|---|---|
| `ClientAppName` | The long name in the Client window title and the ribbon caption, and the title of some Client messages | "VisualCron - Client" |
| `ProductName` | The short product name, used as the title of some Client messages | "VisualCron" |
| `SupportEmail` | The address used by the *Email support about any question you may have* link | "support@visualcron.com" |
| `SalesEmail` | The address used by the *Email sales about any license query* link | "sales@visualcron.com" |
| `ShowLinks` | "false" hides the ***About*** tab of the ribbon, the website and email links in the About window, and the forum link in the start guide | "true" |

:::note

The file also accepts the options `ServerAppName` and `SplashRelativePath`, but they currently have no effect. The Server name and the splash image do not change.

:::