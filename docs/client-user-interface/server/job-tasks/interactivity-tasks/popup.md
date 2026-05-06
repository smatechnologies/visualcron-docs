---
sidebar_label: 'Task Interactivity - Popup'
hide_title: 'true'
---

## Task Interactivity - Popup

The Popup Task lets you display a message for one or more users. The feedback from the user, button or input, can then be returned back as a result and output for later processing.
 
The Popup Task has a number of purposes:

* Display a simple message
* Display a message and return input in form of buttons
* Display a message and return input in form of text boxes, radio boxes and other controls
 
The actual controls can return user defined values and the result of values can control the result of the Task.
 
**Sample popup**

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Example%20Popup.png)

**Popup > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup.png)

**Popup position**

Where the popup window is displayed.
 
**Icon type**

The icon that is displayed next to the message.

**Popup title**

Title within the popup.

**Popup message**

*(Optional)* - the actual message or description that is shown.
 
**Show message**

If the message should be displayed.
 
**Play sound**

When checked, plays a sound when the popup opens. Select a predefined sound from the dropdown. Click the play button to preview the selected sound.
 
**Blink in task bar**

This makes the item in task bar blinking.
 
**Modal window**

This controls if the window should block other windows in the same application.
 
**Bring to front**

Display the Window top most.
 
**Auto close after**

When checked, automatically closes the popup after the specified number of seconds. When auto closing the dialog result is "Cancel".
 
**Preview popup**

Click this button to test the popup.
 
**Popup > Target** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Target.png)

**VisualCron Client**

When checked, sends the popup to the VisualCron Client.

**Send to specific group(s)**

Select this option to send the popup to specific groups. When selected, a grid lists available groups to choose from. If no groups are specified, the popup is sent to all groups.

**Send to specific user(s)**

Select this option to send the popup to specific users. When selected, a grid lists available users to choose from. If no users are specified, the popup is sent to all users.

**Send to executing user**

When checked, sends the popup to the user that is executing the Task or Job.
 
**Popup > Buttons** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Buttons.png)

You are able to select among common buttons for the popup. In the Result tab you can control how the press of a specific button affect the result of the Task. In the Output tab you control if the button value should be returned as output or if the Input should be returned.
 
You may also set the value that is returned for the specific button.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Pop%20Up%20Button%20Options.png)

**Popup > Input** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Input.png)

The Input tab controls optional input controls that you can use. For example if you want the user to input text or select a radio button, checkbox or combobox. If you want the output from the input control you need to change behavior in the Output tab.

**Allow multiple input**

When enabled in the toolbar, allows the user to select more than one input value.

**Manual source** / **Variable/value list source**

Select how input items are provided. With **Manual source**, add items individually using the Add/Edit/Clone/Delete toolbar buttons; rows are managed in a grid showing Caption, Mask, Value, Selected, and Order. With **Variable/value list source**, populate items from a Variable or text value using the fields below.
 
**Caption**

Use any Variable or text that contains a separation according to *Input separator*. If you want the caption to be based on the value then check *Use value as caption*.
 
**Value**

Use any Variable or text that contains a separation according to *Input separator*. The value property is what is returned when selecting an item.
 
**Use value as caption**

Value array will be used in caption array. Useful if you cannot or don't want to map caption to array (maybe only once source available).
 
**Input separator**

This is the type of character that separates each value.

**Selected value**

The default selected value in the input control.
 
**Mask input**

If you want to display a textbox that the user supplies a password to, for example.
 
**Sort alphabetically**

If checked, items are sorted alphabetically, otherwise in the order they are supplied.
 
You can add input controls by pressing the Add button.

**Popup > Result** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Result.png)

The Result tab controls the result of the Task (if it should fail or not) depending on what you select, write or click.
 
When adding or editing a "Popup Result" you are able to control what happens if, for example, the radio button is checked.

**Popup > Output** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Popup%20Output.png)

In the output settings you control what is returned from the Task.

**Standard output content**

**Dialog result** / **Input values**

Select what is returned as output. **Dialog result** returns the button value that was clicked. **Input values** returns the value(s) entered or selected by the user. When choosing input option "checkbox" each value will be returned in a new row.

**Include caption**

The Caption property is put in front of the value like "captionvalue=inputvalue" when this option is checked. Only available when **Input values** is selected.
