---
sidebar_label: 'Image'
hide_title: 'true'
---

## Robot Task Activities - Image

The Image activity captures a screenshot of a screen, a window or an element and saves it to a file, to the clipboard or to both.

![The Image category in the activity list, with the Take Screenshot activity](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Image.png)

---

### Take Screenshot

Takes a screenshot of all screens, the primary screen, a specific screen, the active or a specific window, or the focused or a specific element, either whole or a rectangle of it.

![The Take Screenshot activity in the sequence, with the Click to open settings link](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Take%20Screenshot.png)

#### Properties

The capture target is set in the _Screenshot settings_ property. For a screen capture, the target can be all screens, the primary screen or a specific screen:

![The list of screen choices: All, Primary and Specific](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Option.png)

The output options are in the Properties pane:

- _Screenshot settings_: opens the ***Take screenshot settings*** window, where the capture target is chosen. See [Screenshot Settings](#screenshot-settings)
- _File path_: the full path and file name the image is saved to. The image format follows the extension: ".jpg" or ".jpeg", ".png", ".bmp", ".gif", ".tif" or ".tiff". With no extension, ".jpg" is added and the image is saved as JPEG. With any other extension, the image is saved as JPEG under that name. A missing folder is created
- _Save to clipboard_: copy the image to the clipboard
- _Save to file_: save the image to _File path_. Checked by default

At least one of _Save to file_ and _Save to clipboard_ must be checked, and both can be. With _Save to file_ checked, _File path_ must be a file name, not a folder.

:::warning

_Save to file_ replaces a file that already exists at _File path_ without asking. Include a variable in the file name so that each run writes a new file.

:::

---

### Screenshot Settings

Click _Click to open settings_ on the activity, or click the _..._ button of the _Screenshot settings_ property, to open the ***Take screenshot settings*** window. The Properties pane that holds the _Screenshot settings_ property:

![The Properties pane of the Take Screenshot activity, with Screenshot settings, Display name, File path, Save to clipboard, Save to file, Wait after and Wait before](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Screenshot%20Settings.png)

The _Screenshot of_ list selects the capture target:

![The Screenshot of list, with Screen, Window and Element](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Of.png)

- "Screen": an image of one or all screens
- "Window": an image of the active window or of a specific window
- "Element": an image of the focused element or of a specific element

---

#### Screen options

![The Screen target set to Specific, with the Screen list showing the display names of two screens](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Display.png)

- "All": captures all screens into one image
- "Primary": captures the primary screen only
- "Specific": captures the screen chosen in the _Screen_ list, by its display name, such as `\\.\DISPLAY1`

---

#### Window options

![The Window target with the choices Active and Specific](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Window.png)

- "Active": captures the active window
- "Specific": captures the window found by _Process name_ and _Window title_. Both fields are required. Click _Click to select window_ to pick the window and fill in the fields

![The Window target set to Specific, with the Search window fields Process name and Window title and the Click to select window link](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Window%20Settings.png)

The activity looks for the specific window three times, about a tenth of a second apart, and fails if the window is not found. It sets focus to the window before the capture.

---

#### Element options

![The Element target with the choices Focused and Specific](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Element.png)

- "Focused": captures the element that has focus
- "Specific": captures the element found by the _Search element_ fields: _Process name_ and _Window title_, which are required, and at least one of _Element name_, _Automation id_ and _Class name_. _Element text_ narrows the search. Click _Click to select element_ to pick the element and fill in the fields

![The Part choice with the Relative position and size of rectangle fields X, Y, Width and Height](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Element%20Settings.png)

The activity fails if the element is not found.

---

#### Capturing part of the target

Each target has a size choice. The default, "Full", captures the whole target. "Part" captures a rectangle, set in the _Relative position and size of rectangle_ fields:

![The Take screenshot settings window for a screen capture, with the Screenshot of, screen, size and rectangle fields](../../../../../../../static/img/RPA/Robot%20Tasks/Image/Screenshot%20Settings%20Extra.png)

- _X_: the horizontal offset of the rectangle
- _Y_: the vertical offset of the rectangle
- _Width_: the width of the rectangle
- _Height_: the height of the rectangle

For a window or an element, _X_ and _Y_ are measured from the top-left corner of the window or element. For a screen, they are measured from the top-left corner of the screen. All four values are required when "Part" is selected.

---

### Output and errors

- If the image cannot be copied to the clipboard, the error is written to standard error and the sequence continues. The Task fails when the sequence ends
- If the window or element is not found, the activity fails

---

### Tips

- Take a screenshot in the _Catch_ or _Finally_ block of a [Try Catch](error-handling) activity. A capture of the screen at the moment of failure is often the fastest way to find out why an unattended Robot Task failed
- Include a variable in _File path_ so that each capture gets a unique name, for example `C:\Logs\{JOB(Active|Name)}_{DATEFORMAT(yyyy-MM-dd_HHmmss)}.jpg`
- Prefer a window or element capture over a screen capture when only one application matters. The image is smaller and does not depend on the screen layout
- Use "Part" rather than cropping later when the same region is needed every time, such as a status bar or a total field
- To read text from the screen rather than save an image of it, use the [OCR](ocr) _Recognize and Get Text_ activity
