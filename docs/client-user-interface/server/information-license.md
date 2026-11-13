---
sidebar_label: 'Information - License'
hide_title: 'true'
---

## Information - License

The main menu _Server_ -> _Information_ -> _License_ holds the commands for the license of the Server you are connected to: activating and deactivating it, copying the activation code, and refreshing the license information. For an overview of licensing, see [License and Activation](../../using-visualcron/license-and-activation).

_Server_ -> _Information_ -> _License_

![License menu in the Information group of the Server tab of the main menu, with Activate, Deactivate, Copy activation code to clipboard and Refresh license data](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20License/License.png)

### License menu

- _Purchase license_: shown only when the Server is not activated; opens the VisualCron order page in your browser
- _Activate_: opens the _Activation_ window; available only while the Server is not activated
- _Deactivate_: available only when the Server is activated; after you confirm, the activation code is released so you can use it on another computer
- _Copy activation code to clipboard_: available only when the Server is activated; copies the activation code and confirms in a message
- _Refresh license data_: checks the Server's license with VisualCron from the computer running the Client and sends the result to the Server; that computer needs Internet access

_Deactivate_ runs on the computer running the Client, as online activation does, so that computer needs Internet access. If the license has no active maintenance or subscription, the Client shows a message that one is needed to move or deactivate the license.

:::warning

If the computer running the Client cannot reach VisualCron when you click _Deactivate_, the Server is still deactivated and returns to trial, but the activation code is not released, and no message is shown. Check that the computer running the Client can reach VisualCron before you deactivate.

:::

If _Refresh license data_ finds that the license is not valid, the Server's license can be deactivated, or the Client can be disconnected from the Server.

When the end of maintenance or of the subscription is 45 days away or less, a _days left_ button with the number of days can appear next to _License_. During a trial, a _Trial Information_ group on the same tab shows the days left in the trial.

### Permissions

- "License" permission with "Execute": deactivate; activation does not need this permission, because it is possible only while the Server is not activated
- "License" permission with "Read": copy the activation code

See [Main - User Permissions](main-user-permissions).

### Activation window

_Activate_ opens the _Activation_ window, which has four tabs. If the clipboard holds a complete code when the first code field of a tab gets focus, the fields are filled from the clipboard.

#### Online activation

1. On the **_Online activation_** tab, enter your activation code
2. Click _Activate_

The Client validates the code with the VisualCron website from the computer running the Client. It uses the proxy on the _Proxy_ tab of the Client settings (see [Settings - Client Settings](../file/client-settings)). That computer needs Internet access, and its firewall must allow VisualCron to reach the Internet. The Server computer does not need Internet access to be activated from the Client. A message confirms when the activation has succeeded.

The Server also checks its license with VisualCron on its own from time to time, using the proxy on its _Proxy_ tab (see [Settings - Proxy](settings-proxy)). If the Server cannot reach VisualCron, that check is skipped. If VisualCron reports that the activation code does not exist, the Server removes the activation and returns to trial.

#### Offline activation

Use the **_Offline activation_** tab when the computer running the Client cannot reach the Internet.

1. The tab shows _Your server ID_; it is included in the web address in step 3
2. Enter your activation code
3. When the code is complete, the tab shows a web address and copies it to the clipboard; open that address in a browser on a computer that has Internet access, and copy the offline code it returns
4. Paste the offline code into the box at the bottom of the tab
5. Click _Activate_

#### Trial extension

To extend your trial, contact VisualCron support and say why you need more time and until when, as the tab instructs. Support sends you a trial extension code.

1. On the **_Trial extension_** tab, enter the trial extension code
2. Click _Activate_

The computer running the Client must be connected to the Internet. A message shows the new end date of the trial.

#### Offline trial extension

Use the **_Offline trial extension_** tab when the computer running the Client cannot reach the Internet. This tab asks you to contact VisualCron sales instead of support.

1. Click _Copy to clip board_ to copy the code shown on the tab
2. Send the code to VisualCron sales and wait for the answer
3. Enter the code you receive
4. Click _Activate_
