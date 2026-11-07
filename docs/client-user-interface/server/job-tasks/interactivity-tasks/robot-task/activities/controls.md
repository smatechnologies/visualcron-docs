---
sidebar_label: 'Controls'
hide_title: 'true'
---

## Robot Task Activities - Controls

The Controls activities act on UI elements through their Windows automation patterns, rather than by simulating mouse and keyboard input.

![The Controls category in the activity list, with the Invoke, Set Value, Get Value, Selection State, Expand/Collapse and Set Focus activities](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Controls.png)

Because these activities talk to the control directly, they do not depend on the element being visible at a particular screen position. Each activity needs the target control to support the matching automation pattern. If the element is not found, or the control does not support the pattern, the activity fails with an error.

On these activities, use the _Click to select an element_ link to pick the target in the UI and fill in the search properties automatically. Move the mouse over the element, hold `CTRL`, and click.

---

### Invoke

Finds the element and runs its Invoke action. This is the same as activating a control, such as pressing a button or choosing a menu item.

![The Invoke activity, with the Click to select an element link](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Invoke.png)

Fails if the element is not found or does not support the Invoke pattern.

---

### Set Value

Finds the element and sets its value.

![The Set Value activity, with the Click to select an element link and the Value field](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Set%20Value.png)

- _Value_: the value to write to the element; Variables are resolved first

Fails if the element is not found, does not support the Value pattern, or its value is read-only.

---

### Get Value

Finds the element, reads its value, and saves it to a Job or User Variable.

![The Get Value activity, with the Variable type and Variable fields](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Get%20Value.png)

- _Variable type_: "Job" or "User"
- _Variable_: the name of the Variable that receives the value

Fails if the element is not found or does not support the Value pattern.

---

### Selection State

Finds the element and changes whether it is selected.

![The Selection State activity, with the Click to select an element link](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Selection%20State.png)

The _SelectionType_ property, in the Properties pane, sets what happens:

- "Single" (default): clears the existing selection and selects only this element
- "Append": adds this element to the existing selection
- "Deselect": removes this element from the existing selection

Fails if the element is not found or does not support the SelectionItem pattern.

---

### Expand/Collapse

Finds the element and expands or collapses it. Combo box controls and tree view nodes typically support this pattern. In the sequence, the activity is shown as _Set Expand or Collapse_.

![The Set Expand or Collapse activity, with the Click to select an element link](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Expand%20Collapse.png)

The _State_ property, in the Properties pane, is "Expand" or "Collapse". An element that is already in the requested state is left as it is. An element with nothing to expand is also left as it is, and the activity writes a message to the output.

Fails if the element is not found or does not support the ExpandCollapse pattern.

---

### Set Focus

Sets the focus to the element or window provided by the parent activity.

![The Set Focus activity](../../../../../../../static/img/RPA/Robot%20Tasks/Controls%20Group/Set%20Focus.png)

Use Set Focus before [Keyboard](keyboard) activities, which send input to whatever window has the focus.

:::warning

If the focus cannot be set, Set Focus only writes a message to the output, and the sequence continues. The same happens without a message when there is no parent element. The keyboard input that follows then goes to whatever window has the focus, and the Task reports success.

:::

---

### Tips

- Prefer Controls activities over [Mouse](mouse) activities where the control supports the pattern. Set Value writes to a field in one operation and does not depend on window position, scroll state or screen resolution
- Use _Get Value_ to read a value back after writing it, as a check in a workflow that must not fail without notice
- If an activity fails saying that the pattern is not supported, the control does not expose that automation pattern. Use a [Mouse](mouse) or [Keyboard](keyboard) activity instead, or [OCR](ocr) if the control does not expose its content at all
- Use "Append" and "Deselect" rather than "Single" when you build up a multiple selection across several activities, because "Single" clears everything selected so far
