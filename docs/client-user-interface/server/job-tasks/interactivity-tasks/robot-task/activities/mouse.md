---
sidebar_label: 'Mouse'
hide_title: 'true'
---

## Robot Task Activities - Mouse

The Mouse activities click, double-click, move the mouse and press or release mouse buttons on a UI element or at a fixed screen position.

![The Mouse category in the activity list, with Click, Double Click, Mouse Move and Mouse Key](../../../../../../../static/img/RPA/Robot%20Tasks/Mouse/Mouse.png)

Unless set to use a fixed screen position, all four activities find the target element first and fail if it is not found within _WaitForElement_.

### Finding the element

Click _Click to select an element_ on the activity to pick the target in the UI and fill in the search properties: move the mouse over the element, hold down Ctrl and click. The search properties are in the Properties pane, under **Find Element**:

- _ProcessName_: the name of the process that owns the window. Required
- _WindowTitle_: the title of the window to search in. Supports the wildcards `*`, `?` and `#`. Default: `*` (any window)
- _Name_, _ClassName_ and _AutomationId_: the element's name, class name and automation ID. At least one is required
- _Text_: the element's text. Supports the wildcards `*`, `?` and `#`
- _WindowHandle_: the handle of the window, when it is known. Default: "0"
- _WaitForElement_ (under **Utils**): how long to wait for the element, in milliseconds. Default: "10000"

Inside an _Attach Window_ or _Get Active Window_ activity, the element is searched for in that window.

---

### Click

Finds the element and clicks it.

![The Click activity with the Click to select an element link](../../../../../../../static/img/RPA/Robot%20Tasks/Mouse/Click.png)

- _OffsetX_ and _OffsetY_: where to click, relative to the element. With "0", the activity clicks the center of the element. Default: "0"
- _ClickManually_: click the screen position in _CursorPointX_ and _CursorPointY_ instead of the element. Default: cleared
- _CursorPointX_ and _CursorPointY_: the screen position used when _ClickManually_ is checked. Default: "0"
- _MouseButton_: the mouse button to use. Default: "Left"
- _PressedKeys_: keys held down during the click, separated by commas, for example `LControl` or `Shift`

If the element is off screen, the activity gives its window and the element focus before clicking. If no click position can be calculated, it invokes the element instead, and fails if the element does not support that. If a name in _PressedKeys_ is not a known key name, the activity fails. Use the key names that the [Press Key](keyboard) virtual keyboard or _Detect_ fills in.

---

### Double Click

Finds the element and double-clicks it. The properties are the same as for _Click_.

---

### Mouse Move

Finds the element and moves the mouse to it.

- _OffsetX_ and _OffsetY_: where to move to, relative to the element. With "0", the mouse moves to the center of the element
- _UseManual_: move to the screen position in _CursorPointX_ and _CursorPointY_ instead of the element. Default: cleared
- _HoverTime_: the wait in milliseconds after the mouse arrives, so that hover menus and tooltips can appear. Default: "300"

---

### Mouse Key

Finds the element and presses or releases a mouse button on it. Check _ClickManually_ to act on a fixed screen position instead.

![The Mouse Key activity with the Click to select an element link and the Key and Status fields](../../../../../../../static/img/RPA/Robot%20Tasks/Mouse/Key.png)

- _Key_: the mouse button, for example "Left", "Right" or "Middle". Default: "Left"
- _Status_: the button state to send: "Down" or "Up". Default: "Down"

Pair a "Down" and an "Up" activity to build actions a single click cannot, such as drag and drop: press "Down" on the source element, use _Mouse Move_ to move to the target, then release with "Up".

---

### Tips

- Prefer element-based clicks over _ClickManually_. Fixed positions stop working when a window is moved or resized, or when the Task runs at a different screen resolution
- To click somewhere other than the center of a control, use _OffsetX_ and _OffsetY_ rather than fixed positions
- For links and buttons on a web page, use the [Web Macro](web-macro) _Click Element_ activity instead. It finds elements by CSS selector or XPath rather than by screen position
- For a standard control such as a button or check box, the [Controls](controls) _Invoke_ activity is often more reliable than a simulated click, because it does not depend on the element being visible on screen
