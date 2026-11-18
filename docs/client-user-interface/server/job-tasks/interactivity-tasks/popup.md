---
sidebar_label: 'Task Interactivity - Popup'
hide_title: 'true'
---

## Task Interactivity - Popup

The Popup Task shows a message in the VisualCron Client of one or more users and returns the user's reply, the button they clicked or the values they entered, as the Task output and result.

Use it to:

- show a simple message
- show a message and return the button the user clicks
- show a message and return input from text boxes, check boxes, radio buttons or a combo box

A popup as a user sees it:

![Example popup with a title, a message, OK and Cancel buttons and an auto close countdown](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Example%20Popup.png)

:::warning

_Mask input_ hides typed text in the popup only. When the ***Output*** sub tab is set to "Input values", the Task output contains the text as the user typed it. With Task debugging on, the values are also written to the log. Do not use the Popup Task to collect passwords.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Popup tab

The ***Popup*** tab has the sub tabs ***Main settings***, ***Target***, ***Buttons***, ***Input***, ***Result*** and ***Output***.

#### Popup: Main settings sub tab

![Popup Main settings sub tab with the position, icon, title, message and display options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup.png)

- _Popup position_: Where the popup window opens: "CenterParent" (the default), "CenterScreen", "WindowsDefaultBounds" or "WindowsDefaultLocation"
- _Icon type_: The icon next to the message: "Information" (the default), "Exclamation", "Question" or "Error"
- _Popup title_: The title shown in the popup; "Popup title" by default
- _Popup message_: Optional; the message shown in the popup
- _Show message_: When selected, the message is shown
- _Play sound_: When selected, the popup plays the selected sound, "Sound1" or "Sound2", when it opens. Click the button next to the list to hear the sound
- _Blink in task bar_: When selected, the popup's button in the Windows task bar flashes
- _Modal window_: When selected, the popup blocks the other windows of the VisualCron Client until it is closed
- _Bring to front_: When selected, the popup is shown on top of other windows
- _Auto close after_: When selected, the popup closes after the number of seconds set, "60" by default. A popup that closes this way returns the "Cancel" dialog result
- _Preview popup.._: Shows the popup in your own Client, to test it

All check boxes on this sub tab are selected by default. [Variables](../../global-variables) are resolved in _Popup title_ and _Popup message_.

#### Popup: Target sub tab

![Popup Target sub tab with the group and user lists](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Target.png)

- _Server desktop (specify user/session in Foreground execution)_: Shown, but not available
- _VisualCron Client_: Sends the popup to VisualCron Clients
- _Send to specific group(s)_: Sends the popup to every connected Client whose user is a member of a group selected in the list
- _Send to specific user(s)_: Sends the popup to every connected Client of a user selected in the list
- _Send to executing user_: Also sends the popup to the Client connection that started the Job

Select at least one group or user, or _Send to executing user_. The Client does not save the Task without a target, although the list captions say that the popup goes to all when none is selected.

The popup reaches only users whose Client is connected to the Server when the Task runs. If none of the targets is connected, the Task fails with "No target Connection found". When the popup goes to several users, the Task uses the first reply it receives and ignores the others.

#### Popup: Buttons sub tab

![Popup Buttons sub tab with the button set and the value of each button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Buttons.png)

- _Buttons_: The set of buttons in the popup: "Ok", "Ok Cancel" (the default), "Abort Retry Ignore", "Retry Cancel", "Yes No" or "Yes No Cancel"
- _Edit_: Opens _Edit button value_ for the selected button, where you set the _Value_ the button returns

A button's value is its name by default. The ***Result*** sub tab decides whether a button makes the Task succeed or fail. With "Dialog result" on the ***Output*** sub tab, the value of the clicked button is the Task output.

![Edit button value window for one button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Pop%20Up%20Button%20Options.png)

#### Popup: Input sub tab

![Popup Input sub tab with the input type, the manual source list and the Variable/value list source fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Input.png)

The ***Input*** sub tab adds optional input controls to the popup. To return what the user enters, set the ***Output*** sub tab to "Input values".

- _Input type_: The kind of control: "Text", "Check Box", "Combo Box" or "Radio Button" (the default)
- _Manual source_: Add the items one by one with _Add_, _Edit_ and _Delete_. The list shows each item's Order, Caption, Value, Mask and Selected. In _Add/Edit input_ you set the item's _Caption_, _Value_, _Mask input_ and _Selected_
- _Variable/value list source_: Build the items from a list of values in a Variable or in text:
  - _Caption_: The captions, separated by the _Input separator_. Not used when _Use value as caption_ is selected
  - _Value_: The values, separated by the _Input separator_. The value of an item is what the Task returns when the item is chosen
  - _Use value as caption_: When selected, each value is also its caption. Selected by default
  - _Input separator_: The character between the items; ";" by default
  - _Selected value_: The value that is selected when the popup opens
  - _Mask input_: For "Text" only; the popup shows each typed character as `*`
  - _Sort alphabetically_: For check boxes, radio buttons and combo boxes; sorts the items by caption instead of the order supplied

#### Popup: Result sub tab

![Popup Result sub tab with result rows and the Add/Edit popup result window](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Result.png)

The ***Result*** sub tab decides whether the Task succeeds or fails, based on how the popup was closed and what the user chose or typed. Each row sets one check; click _Add_ or _Edit_ to open _Add/Edit popup result_:

- _Control to validate_: What the row checks: "Message Button", "Input Control", "Close Button", "Auto Close" or "Timeout"
- _Control name/caption_: For "Input Control", the input item to check
- _Validation value type_: For a text input, how the values are compared. With "String", larger and smaller compare the length of the text
- _Condition_: How the value is compared, for example "Equal"
- _Value_: The value to compare with
- _Return result_: "Success" or "Failure"

When the popup closes and a row that applies returns "Failure", the Task fails.

#### Popup: Output sub tab

![Popup Output sub tab with Dialog result, Input values and Include caption](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Output.png)

- _Dialog result_: The output is the value of the button the user clicked. The default
- _Input values_: The output is the values the user entered or selected, one per line for check boxes and text boxes; for radio buttons, the selected item only
- _Include caption_: With "Input values", puts the caption in front of each value, as `caption=value`. Selected by default

### Output and errors

- The Task waits until a user replies, the popup closes itself (_Auto close after_), or the time on the ***TimeOut*** tab runs out. With _Auto close after_ cleared and no time-out, the Task waits until a user replies
- If no target Client is connected, the Task fails with "No target Connection found"
- If a row on the ***Result*** sub tab returns "Failure", the Task fails
