---
sidebar_label: 'Text'
hide_title: 'true'
---

## Robot Task Activities - Text

The Text activity types text into an application, either into the window that has focus or into a window or element it finds first.

![The Text category in the activity list, with the Send Text activity](../../../../../../../static/img/RPA/Robot%20Tasks/Text/Text.png)

---

### Send Text

Types the text in _InputText_ one character at a time. What the activity does first depends on which search properties are filled in:

- Only _ProcessName_: the activity checks that the process is running, then types into the window that has focus. It does not give the process focus
- _ProcessName_ and _WindowTitle_ or _WindowHandle_: the activity waits for the window, gives it focus and types into it
- _ProcessName_, _WindowTitle_ and one of _Name_, _ClassName_ and _AutomationId_: the activity waits for the element, gives it focus and types into it
- None of these: the activity types into the window that has focus

If the process, window or element is not found, the activity fails.

![The Send Text activity with the Click to select an element link and the Text field](../../../../../../../static/img/RPA/Robot%20Tasks/Text/Send%20Text.png)

Click _Click to select an element_ to pick the target in the UI and fill in the search properties.

#### Properties

![The Properties pane of the Send Text activity, with the Find Element, Input, Misc and Utils groups](../../../../../../../static/img/RPA/Robot%20Tasks/Text/Settings.png)

**Find Element**

- _AutomationId_: the automation ID of the element
- _ClassName_: the class name of the element
- _Name_: the name of the element
- _ProcessName_: the name of the process that owns the window
- _Text_: the text of the element. Supports the wildcards `*`, `?` and `#`
- _WindowHandle_: the handle of the window, when it is known. Default: "0"
- _WindowTitle_: the title of the window. Supports the wildcards `*`, `?` and `#`. Default: `*` (any window)

**Input**

- _Case_: changes the case of the text before it is typed: "None", "UpperCase" or "LowerCase". Default: "None"
- _InputText_: the text to type. The _Text_ field on the activity sets the same value. A line break is typed as Enter
- _Mode_: what happens before the text is typed. Default: "None"
  - "Overwrite": presses Ctrl+A and then Delete, which clears the field
  - "Append": presses Ctrl+End, which moves to the end
  - "InsertInFront": presses Ctrl+Home, which moves to the start
  - "None": types at the current position
- _TypingDelay_: the wait in milliseconds before each character. Default: "100"

**Utils**

- _WaitForElement_: how long to wait for the window or element, in milliseconds. Default: "10000"
- _Wait before_ and _Wait after_: the wait in milliseconds before and after the activity runs. When empty, the playback speed from the Robot Task settings is used

---

### Tips

- Use "Overwrite" when filling in a field that may already hold a value, such as a form that is reused in each loop iteration. With "None", the text is typed at the current position next to whatever is there
- Raise _TypingDelay_ for applications that check or reformat input as it is typed. Text sent too fast can lose characters
- Identify the target by _AutomationId_ where the application has one. It is the most stable identifier and does not change when the window is resized or the layout changes
- Fill in _WindowTitle_ as well as _ProcessName_ when the text must go to a specific window. With only _ProcessName_, the text goes to whichever window has focus
- For text fields on a web page, use the [Web Macro](web-macro) _Populate Field_ activity instead, which finds elements by CSS selector or XPath. See [Web Input - Element Path](../web-input-element-path)
