---
sidebar_label: 'Clipboard'
hide_title: 'true'
---

## Robot Task Activities - Clipboard

The Clipboard activities put text on the Windows clipboard, read text from it and clear it.

![The Clipboard category in the activity list, with the Set Clipboard, Get Clipboard and Clear Clipboard activities](../../../../../../../static/img/RPA/Robot%20Tasks/Clipboard/Clipboard.png)

The clipboard is often the only way to move data out of an application that does not expose its content as UI elements. Copy the value in the application with a `Ctrl+C` key press, then read it into a Variable with _Get Clipboard_.

---

### Set Clipboard

Puts text on the clipboard, replacing what it held before.

- _Value_: the text to put on the clipboard; Variables are resolved first

Use this to stage a value before pasting it into an application, for example with a `Ctrl+V` [Press Key](keyboard) activity or an [Excel Cell](excel-cell) _Paste to Cell_ activity.

---

### Get Clipboard

Reads the text on the clipboard and saves it to a Job or User Variable.

- _Variable type_: "Job" or "User"
- _Variable_: the name of the Variable that receives the text

Only text is read. If the clipboard holds something other than text, such as an image, the Variable is set to an empty value.

---

### Clear Clipboard

Removes everything from the clipboard.

---

### Tips

- Clear the clipboard before a copy operation, then check that _Get Clipboard_ returned something. If the copy failed, you would otherwise read a stale value left over from a previous iteration and write the wrong data
- The clipboard is shared by everything in the desktop session the Robot Task runs in. Two Robot Tasks that run at the same time in the same session overwrite each other's clipboard content. Schedule such Jobs so that they do not overlap, or run them in separate sessions or on separate machines
- Add a short delay after the copy keystroke and before _Get Clipboard_. Some applications fill the clipboard asynchronously, and the read can otherwise arrive too early
- Prefer a direct read where one is available. The [Controls](controls) _Get Value_ activity, the [Web Macro](web-macro) _Extract Data_ activity and the [Excel Cell](excel-cell) _Get Cell value_ activity read a value without the clipboard, so nothing else running on the desktop can change it. The Web Macro _Copy Value_ and _Copy Link_ activities, by contrast, copy to the clipboard
- Several activities can write their result to the clipboard, including [List - Save](list-variable) and [Take Screenshot](image). Writing to a file is usually the better choice for anything you need to keep
