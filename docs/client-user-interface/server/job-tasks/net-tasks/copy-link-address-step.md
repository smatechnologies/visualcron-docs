---
sidebar_label: 'Copy Link Address Step'
hide_title: 'true'
---

## Copy Link Address Step

The Copy link address action of the [Task Net - Web Macro](web-macro) copies the link URL from a web element and saves it to a Variable. The action window is titled _Action - Copy link_.

To add the action while recording, complete the following steps in the _Web recorder_ window:

1. Right-click the element.
2. Click _Add Copy Link Address action_.

### Source tab

Sets the web element to copy the link from; see [Element Path](element-path). _Relative_ and _By search_ are available on this action, and _By position_ is not.

### CopyLink tab

- _Link_: the link URL recorded for the element, stored encrypted

  You can enter a value. To fill the field with a Variable, click the Variables icon next to the field; the Variable replaces the text in the field. To see the available Variables, click _Variables_. Playback copies the link of the element on the ***Source*** tab, and _Link_ holds the value recorded for it.

### Variable tab

Sets where the copied link is saved, in the _Save to_ group. A Variable is required.

- _Job Variable_: selected by default; saves the link to the Job Variable selected in the list
- _User Variable_: saves the link to the User Variable selected in the list
- _Variable type_: the data type used when the value is saved, "String" (default), "Int32", "Double" or "Boolean"

To reload a list of Variables, click the refresh icon next to it.

### Wait tab

Sets how long the action waits before it runs (_Wait before execute_) and after it runs (_Wait after execute_), in milliseconds. Both are "500" by default.
