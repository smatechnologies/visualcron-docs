---
sidebar_label: 'Keyboard'
hide_title: 'true'
---

## Robot Task Activities - Keyboard

The Keyboard activities send key presses and key events to the window that has focus.

![The Keyboard category in the activity list, with Key Event and Press Key](../../../../../../../static/img/RPA/Robot%20Tasks/Keyboard/Keyboard.png)

---

### Key Event

Sends one key event: the key goes down or comes up.

![The Key event activity with the Key and Status fields](../../../../../../../static/img/RPA/Robot%20Tasks/Keyboard/Event.png)

- _Key_: the key to send, chosen from the list, for example "Control", "Shift" or "A". Default: "None"
- _Status_: the key state to send: "Down" or "Up". Default: "Down"

Use Key Event to hold a key down across other activities: send "Down", run the activities, then send "Up" for the same key to release it.

---

### Press Key

Presses one key or several keys, either one after another or together as a combination.

![The Press Key activity with the Keys field, the ... button and the Is combination check box](../../../../../../../static/img/RPA/Robot%20Tasks/Keyboard/Press.png)

- _Keys_: the names of the keys to press, separated by commas, for example `Control,C`. Default: "None"
- _Is combination_: when checked, the keys are pressed together. When cleared, they are pressed one after another, in order. Default: cleared
- _KeyPressDelay_: in the Properties pane, the wait in milliseconds before each key when the keys are pressed one after another. Default: "100"

With `Control,C` and _Is combination_ checked, the activity sends Ctrl+C. With _Is combination_ cleared, it presses Control and then C as two separate keys.

**Selecting keys**

Click the _..._ button to open the virtual keyboard and choose the keys there instead of typing their names.

![The virtual keyboard window, with a button for each key](../../../../../../../static/img/RPA/Robot%20Tasks/Keyboard/Input.png)

Click _Detect_ to capture keys from the physical keyboard. In the ***Press any key to detect*** window, press the keys, then click _Set_ to fill in _Keys_, or _Clear_ to start again.

![The Press any key to detect window, with the detected key names and the Clear and Set buttons](../../../../../../../static/img/RPA/Robot%20Tasks/Keyboard/Detect.png)

If a name in _Keys_ is not a known key name, the activity fails without pressing any key. When _Keys_ is empty, the activity presses no key and does not fail.

---

### Tips

- Keyboard activities send input to the window that has focus. Before sending keys, give the target window focus with a [Windows](windows) activity such as _Attach Window_ with _SetFocus_ checked, or with the [Controls](controls) _Set Focus_ activity
- To type text into a field, use the [Text](text) _Send Text_ activity rather than a chain of Press Key activities. Send Text can also find a specific element and decide what happens to existing text
- Use _Detect_ or the virtual keyboard rather than typing key names. The names they fill in are names the activity accepts
- Increase _KeyPressDelay_ if an application misses keys. Some applications cannot keep up with input sent at full speed
