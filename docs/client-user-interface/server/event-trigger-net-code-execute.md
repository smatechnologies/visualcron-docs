---
sidebar_label: 'Event Trigger - .NET Code Execute'
hide_title: 'true'
---

## Event Trigger - .NET Code Execute

![](../../../static/img/triggereventnetexecutecode.png)

The composition and purpose of all the parameters that are available inside the Trigger sub tab fully corresponds to the description of the parameters from the topic, which describes the [.NET code execute Task](../server/job-tasks-task-process-dot-net-code-execute).
 
.**NET code execute** tab > **Condition** sub tab

![](../../../static/img/triggereventnetexecutecondition.png)

**Output**

**Remove all leading and trailing white-space characters from the result**

All leading and trailing white-space characters are removed from the .NET code execution output before the condition is checked. This option is enabled by default.
 
**Data type**

Select the data type that the .NET code execution result should be interpreted as. The available comparison methods in the _Condition_ dropdown change depending on the selected data type:

* **String**
* **Boolean**
* **Int32**
* **Int64**
* **Decimal**
* **Double**

**Condition**

Select the comparison method that should be applied between the result and the _Value to compare with_. The list of available methods depends on the selected _Data type_:

* **Boolean** — _Equal_, _Not equal_
* **String** — _Equal_, _Not equal_, _Contains_, _Not contains_, _RegEx match_, _RegEx no match_
* **Int32 / Int64 / Decimal / Double** — _Equal_, _Not equal_, _Larger_, _Larger or equal_, _Smaller_, _Smaller or equal_, _Contains_
 
**Value to compare with**

Enter a value/Variable to compare the result with. Click the Variables icon to open the the Variables list.
 
**If value is the same as last time**

Choose how the Trigger should behave when the new result matches the previous result:

* **Fire Trigger** — fire the Trigger every time the Condition is met (default)
* **Do not fire Trigger** — skip firing when the result is the same as last time
* **Disable Trigger** — disable the Trigger after a repeated identical match
 
 
**.NET code execute Trigger Result Variables**
 
**MatchedValue**

The string representation of the matched value from the .NET code execution output.
