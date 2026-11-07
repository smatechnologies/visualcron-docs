---
sidebar_label: 'Other'
hide_title: 'true'
---

## Robot Task Activities - Other

The Other activities assign workflow values, group activities into a sequence and pause the sequence for a set time.

![The Other category in the activity list, with Assign, Sequence and Wait](../../../../../../../static/img/RPA/Robot%20Tasks/Other/Other.png)

---

### Assign

Sets the value of a workflow variable, declared in the **Variables** pane at the bottom of the Robot designer.

To set a VisualCron Job Variable or User Variable instead, use the [Set variable](variables) activity.

---

### Sequence

Runs its child activities one after another, in order.

![A Sequence activity with an empty Drop activity here area](../../../../../../../static/img/RPA/Robot%20Tasks/Other/Sequence.png)

The outermost container of every Robot Task is a Sequence. Add more Sequence activities inside branches and loop bodies to group related activities. A branch or body that takes a single activity, such as the _Then_ and _Else_ blocks of an If activity, needs a Sequence to hold more than one.

A named Sequence can be collapsed to a single line in the designer, which makes a long sequence easier to read.

---

### Wait

Waits for the time set before running the next activity.

![The Wait activity with the Hours, Minutes, Seconds and Milliseconds fields](../../../../../../../static/img/RPA/Robot%20Tasks/Other/Wait.png)

- _Hours_: the number of hours to wait. Default: "0"
- _Minutes_: the number of minutes to wait. Default: "0"
- _Seconds_: the number of seconds to wait. Default: "0"
- _Milliseconds_: the number of milliseconds to wait. Default: "0"

The four values are added together, so 1 minute and 30 seconds is _Minutes_ "1" and _Seconds_ "30". All four fields accept variables. A total of zero does not wait, and a negative total makes the activity fail.

---

### Tips

- Prefer a targeted wait over a fixed _Wait_. Activities such as [Wait For File](file), [Wait For Folder](folder) and [Wait For Text](ocr), and the _Wait element_ setting of Web Macro activities, continue as soon as the condition is met instead of always waiting the full time
- Many activities also have _Wait before_ and _Wait after_ properties in the Properties pane under **Utils**. Use these for a short pause around one activity rather than adding a separate Wait activity
- Give each nested Sequence a _Display name_ that describes the work it groups, for example `Log Exception And Skip Record`
