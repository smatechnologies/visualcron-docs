---
sidebar_label: 'OCR'
hide_title: 'true'
---

## Robot Task Activities - OCR

The OCR activities read text from an area of the screen with optical character recognition, for applications that do not expose their content as UI elements, such as a rendered document, a remote desktop session or a legacy terminal.

![The OCR category in the activity list, with Search Text and Click, Search Text and Hover, Recognize and Get Text and Wait For Text](../../../../../../../static/img/RPA/Robot%20Tasks/OCR/OCR.png)

:::tip

To define the area, click _Click to select a area_ on the activity, then drag with the left mouse button to size the capture box. When the text is inside the box, right-click to save the area.

:::

---

### Search Text and Click

Finds the text in the area and clicks where it was found.

![The Search Text and Click activity with the Click to select a area link, the Search text and OCR language fields and the Is Case Sensitive check box](../../../../../../../static/img/RPA/Robot%20Tasks/OCR/Search.png)

- _Click to select a area_: opens the capture box to define the screen area to search
- _Search text_: the text to find in the area
- _OCR language_: shown on the activity, but recognition always uses English, whatever this field says
- _Is Case Sensitive_: when checked, the case of the text must match
- _CleanBackgroundNoise_: in the Properties pane, cleans background noise from the captured image before recognition

The area is stored as _TextAreaRectangleX_, _TextAreaRectangleY_, _TextAreaRectangleWidth_ and _TextAreaRectangleHeight_ in the Properties pane. The other click properties, such as _MouseButton_ and _PressedKeys_, are the same as for the [Mouse](mouse) _Click_ activity.

:::warning

If the text is not found, the activity clicks the top-left corner of the screen instead, and the Task reports success. Check that the text is on screen first, for example with _Wait For Text_.

:::

---

### Search Text and Hover

Finds the text in the area and moves the mouse to where it was found. The settings are the same as for _Search Text and Click_.

Use this to show hover content, such as a tooltip or a menu that only opens when the mouse is over it.

:::warning

If the text is not found, the activity moves the mouse to the top-left corner of the screen instead, and the Task reports success.

:::

---

### Recognize and Get Text

Reads all the text in the area and saves it to a VisualCron variable.

- _VariableToSave_: the name of the variable that receives the text
- _SaveToVariableType_: "User" or "Job". Default: "User"

The text that was read is also written to the Task output. Use this activity to read a value that has no UI element behind it, such as a total in a rendered report.

---

### Wait For Text

Waits until the text in _Search text_ appears in the area, checking every _PoolingInterval_ milliseconds. Default: "300".

:::warning

Wait For Text has no time limit of its own. If the text never appears, the activity waits until the Task is stopped or the time limit on the Task's ***TimeOut*** tab is reached. See [Job - Tasks](../../../../job-tasks).

:::

Use it instead of a fixed [Wait](other) activity to pause until a screen has finished loading, when there is no UI element to test.

---

### Tips

- Keep the area as small as possible. A small area is faster to read and less likely to pick up similar text elsewhere on the screen
- Use OCR when nothing else works. If the application exposes its content as UI elements, the [Controls](controls) _Get Value_ activity reads it exactly, with no recognition errors. For web pages, use the [Web Macro](web-macro) _Extract Data_ or _Copy Value_ activities
- OCR reads what is drawn on the screen, so the target window must be visible and not covered. Use [Windows](windows) _Show Window_ and _Maximize Window_ first to put the target in a known state
- Screen resolution and display scaling affect recognition. Test OCR activities on the same computer, at the same resolution, that the Job will run on
- Leave _Is Case Sensitive_ cleared unless case is what tells the target apart from other text on the screen. OCR sometimes misreads case
