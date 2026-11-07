---
sidebar_label: 'Windows'
hide_title: 'true'
---

## Robot Task Activities - Windows

The Windows activities find application windows and attach to, show, hide, close, maximize, minimize, restore, move or resize them.

![The Windows category in the activity list, with Attach Window, Get Active Window, Close Window, Hide Window, Show Window, Maximize Window, Minimize Window, Restore Window, Resize Window and Move Window](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Windows.png)

Click _Click to select_ on an activity to pick a window in the UI and fill in the search properties. Every activity in this category fails if the window is not found within _WaitForWindow_.

:::note

A window handle changes each time a window is closed and opened again. When the handle in _WindowHandle_ no longer finds the window, the activity searches by _ProcessName_ and _Title_ instead, so fill those in as well.

:::

---

### Attach Window

Finds a window and runs the activities in its _Do_ body against that window. Activities in the body that work on a window or an element use the attached window without searching for it again.

![The Attach Window activity with the Click to select link and the Do body](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Attach.png)

#### Properties

The Windows activities share these properties. Attach Window also has _AttachedWindow_.

![The Properties pane of the Attach Window activity, with ProcessName, Title, WindowHandle, Window, Display name, AttachedWindow, SetFocus, Wait after, Wait before and WaitForWindow](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Attach%20Settings.png)

- _ProcessName_: the name of the process that owns the window
- _Title_: the window title. Supports the wildcards `*`, `?` and `#`
- _WindowHandle_: the handle of the window, when it is known. Default: "0"
- _Window_: a window object, for example the _AttachedWindow_ of another activity, to use instead of searching
- _AttachedWindow_: an output that receives the attached window, for use in a later activity's _Window_ property
- _SetFocus_: give the window focus before the activity acts on it. Default: cleared
- _WaitForWindow_: how long to wait for the window, in milliseconds. Default: "10000"
- _Wait before_ and _Wait after_: the wait in milliseconds before and after the activity runs. When empty, the playback speed from the Robot Task settings is used

At least one of _ProcessName_, _WindowHandle_ and _Window_ must be filled in.

#### How the window is found

Attach Window uses the _Window_ property when it is set. Otherwise it searches: first by _WindowHandle_, then by _ProcessName_ and _Title_. When a _Title_ with wildcards matches several windows, Attach Window uses the first one, and runs its body once.

The other Windows activities find their window in this order:

1. The _Window_ property, when it is set
2. The window of a parent _Attach Window_ or _Get Active Window_ activity
3. A search by _WindowHandle_, then by _ProcessName_ and _Title_

When a _Title_ with wildcards matches several windows, these activities act on every matched window.

---

### Get Active Window

Gets the window that is active and runs the activities in its _Do_ body against it, so the activities in the body do not need to search for a window. The _ActiveWindow_ output receives the window, and _SetFocus_ gives it focus first. The activity fails if no window is active.

![The Get Active Window activity with the Do body](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Get%20Active.png)

---

### Close Window

Finds the window or windows and closes them. The activity fails if a window cannot be closed this way.

![The Close Window activity with the Click to select link](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Close.png)

---

### Hide Window

Finds the window or windows and hides them.

![The Hide Window activity with the Click to select link](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Hide.png)

---

### Show Window

Finds the window or windows and shows them.

![The Show Window activity with the Click to select link](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Show.png)

---

### Maximize Window

Finds the window or windows and maximizes them.

![The Maximize Window activity with the Click to select link](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Maximize.png)

---

### Minimize Window

Finds the window or windows and minimizes them.

![The Minimize Window activity with the Click to select link](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Minimize.png)

---

### Restore Window

Finds the window or windows and restores them to their normal size and position.

---

### Resize Window

Finds the window or windows and resizes them.

![The Resize Window activity with the Click to select link and the Width and Height fields](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Resize.png)

- _Width_: the new window width, in pixels. Default: "0"
- _Height_: the new window height, in pixels. Default: "0"

---

### Move Window

Finds the window or windows and moves them.

![The Move Window activity with the Click to select link and the X and Y fields](../../../../../../../static/img/RPA/Robot%20Tasks/Windows/Move.png)

- _X_: the new horizontal screen position. Default: "0"
- _Y_: the new vertical screen position. Default: "0"

---

### Output and errors

- Close Window, Maximize Window, Minimize Window, Restore Window, Resize Window and Move Window fail if the window does not offer the action at all
- When a window offers resizing or moving but its size or position is fixed, Resize Window and Move Window write a line to the Task output and leave the window as it is, and the Task reports success

---

### Tips

- Put a group of window activities inside one _Attach Window_ activity rather than repeating the search properties on each one. It is faster, and there is only one place to update if the window title changes
- Set _WaitForWindow_ rather than adding a fixed [Wait](other) activity before working with a window that takes time to open. The activity continues as soon as the window is found
- Use wildcards in _Title_ for windows whose title changes, for example `*- Notepad` or `Invoice * - Contoso`. Remember that a wildcard can match more than one window
- Check _SetFocus_ on _Attach Window_ when the body has [Keyboard](keyboard) activities, because those send input to the window that has focus
- Run _Maximize Window_ at the start of a sequence to give the window a known size, which keeps element positions and screenshots the same from run to run
