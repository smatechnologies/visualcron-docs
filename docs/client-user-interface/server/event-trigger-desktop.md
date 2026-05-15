---
sidebar_label: 'Event Trigger - Desktop'
hide_title: 'true'
---

## Event Trigger - Desktop

The **Desktop trigger** monitors changes in a UI via a locally or remotely runned VC tray. The Trigger reacts on UI events like as opened, closed, focused, appeared, clicked, checked, hovered, changed and many other UI, system, keyboard events. The trigger listens to events for a specific type of controls. It is possible to retrieve the username, hostname, process name, window name, control name, control content, pressed key, event type and other results so you can use it in your Tasks for example.

### Events tab
 
Configured events are listed in a grid showing the **Event type** and the **Watching value** (a summary of the parameters that the event is matching on). Use the toolbar above the grid to **Add**, **Edit**, or **Delete** events, or double‑click a row to edit it.

Events are divided into categories: Process, Application, Window, Control, System, Keyboard.

### Process category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Process.png)

The Process category contains 2 events: 
* Process started
* Process ended

The **Process started** event monitors the running of a specific process that matches the name of the process that the user-specified when adding an event.

The **Process ended** event monitors the ending of a specific process that matches the name of the process that the user-specified when adding an event.

### Application category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Application.png)

The Application category contains 4 events: 
* Application focused 
* Application unfocused
* Application clicked
* Application double clicked

The **Application focused** event monitors the focusing to a specific application that matches the name of the application that the user-specified when adding an event.

The **Application unfocused** event monitors the focus leaving from a specific application that matches the name of the application that the user-specified when adding an event.

The **Application clicked** event monitors the clicking to a specific application that matches the name of the application that the user-specified when adding an event.

The **Application double** clicked event monitors the double clicking to a specific application that matches the name of the application that the user-specified when adding an event.

### Window category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Window.png)

The Window category contains 6 events: 
* Window opened
* Window closed
* Window focused
* Window unfocused
* Window clicked
* Window double clicked

The **Window opened** event monitors the opening of a specific window that matches the name of the application and window that the user-specified when adding an event.

The **Window closed** event monitors the closing of a specific window that matches the name of the application and window that the user-specified when adding an event.

The **Window focused** event monitors the focusing to a specific window that matches the name of the application and window that the user-specified when adding an event.

The **Window unfocused** event monitors the focus leaving from a specific window that matches the name of the application and window that the user-specified when adding an event.

The **Window clicked** event monitors the clicking to a specific window that matches the name of the application and window that the user-specified when adding an event.

The **Window double clicked** event monitors the double clicking to a specific window that matches the name of the application and window that the user-specified when adding an event.

### Control category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Control.png)

The Control category contains 7 child categories: 
* Button 
* Textbox
* Label
* Checkbox 
* Radio button
* Combobox
* Document

The Button, Label categories contains 6 events: 
* Button hovered
* Button clicked
* Button enabled
* Button disabled
* Button appeared
* Button disappeared

The **Button hovered** event monitors the hovering of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Button clicked** event monitors the clicking of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Button enabled** event monitors the enabling of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Button disabled** event monitors the disabling of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Button appeared** event monitors the appearing of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Button disappeared** event monitors the disappearing of a specific button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Texbox, Document** category contains the same events, but has one more additional: **Textbox value changed**.
 
The **Value changed** event monitors the value changing of a specific textbox, document that matches the name of the application, window, button, content that the user-specified when adding an event.

The** Checkbox**, Radio button category contains the same events, but has two more additional: **Checked**, **Unchecked**

The **Checked** event monitors the checking of a specific checkbox or radio button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Unchecked** event monitors the unchecking of a specific checkbox or radio button that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Combobox** category contains the same events, but has three more additional: 
* Combobox value changed
* Combobox opened
* Combobox closed

The **Combobox value changed** event monitors the value changing of a specific combobox that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Combobox opened** event monitors the opening of a specific combobox that matches the name of the application, window, button, content that the user-specified when adding an event.

The **Combobox closed** event monitors the closing of a specific combobox that matches the name of the application, window, button, content that the user-specified when adding an event.

### System category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers//Event%20Trigger%20-%20Desktop%20System.png)

The **System** category contains 4 events: 
* System locked
* System unlocked
* RDP connected
* RDP disconnected.

The **System locked** event monitors the locking of the system. The event fires when the user locks the system session.

The **System unlocked** event monitors the unlocking of the system. The event fires when the user unlocks the system session.

The **RDP connected** event monitors the RDP connecting.The event fires on remote connecting.

The **RDP disconnected** event monitors the RDP disconnecting.The event fires on remote disconnecting.

### Keyboard category

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Keyboard.png)

The Keyboard category contains 3 events: 
* Key pressed
* Hotkey pressed
* Key sequence pressed

The **Key pressed** event monitors the pressing to a specific key.

The **Hotkey pressed** event monitors the pressing to a specific hotkey.

The **Key sequence pressed** event monitors the pressing to a specific key sequence.

### Control selector

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Desktop%20Control.png)

Depending on the event category, the dialog exposes one or more of the following fields:

* **Process name** — the name of the process to match
* **Window name** — the title of the window to match
* **Control name** — the name of the UI control to match
* **Control value** — the content/value of the UI control to match

All fields support wildcards such as: “?”, “*”
“*” - any symbol and any count, “?” - one any symbol.
 
For example, if we enter ‘notep*’ to Process name field, trigger will listen for all processes whose name begins with ‘notep’.

**Match case**

When checked, the values entered in the selector fields are matched case‑sensitively. When unchecked, matching is case‑insensitive.
 
If you don't know the details of the control, you can click on the search button.

Then select the control you need. To select hold down the Ctrl button and click on the control.

The fields will be filled in automatically.

### Keyboard event configuration

For the **Key pressed**, **Hotkey pressed**, and **Key sequence pressed** events, the configuration dialog includes a key capture field that listens for keystrokes as you press them. Captured keys are stored as a comma‑separated list (for example, `ControlKey,L`). Use the **Clear** button to reset the captured keys.

### Connections tab

In the Connections tab, select the **VisualCron Server location** that the trigger should listen on:

* **Local VisualCron Server** — listen for events on the same machine as the VisualCron Server (default)
* **Remote VisualCron Server** — listen for events on a remote VisualCron Server. When selected, choose the [VisualCron Connection](../server/connection-visualcron) to use

Before initializing the trigger, make sure that you have a tray client running, depending on which connection you have selected.

The event from the Process category requires running the tray client as administrator. 
