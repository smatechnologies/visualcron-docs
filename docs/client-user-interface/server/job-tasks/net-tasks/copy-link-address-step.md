---
sidebar_label: 'Copy Link Address Step'
hide_title: 'true'
---

## Copy Link Address Step

The Copy link address step copies the link URL from a web element.

**Source tab**

Defines the web element to copy the link from. Uses the standard element selection interface.

**CopyLink tab**

**Link**

The link URL to copy. You can enter a value manually or click the Variables button to insert a variable.

**Variable tab**

Defines where to save the copied link value.

**Variable type**

Select whether to save the result to a Job Variable or a User Variable:

* _Job Variable_ - saves to the selected job variable; enables the Job Variable dropdown
* _User Variable_ - saves to the selected user variable; enables the User Variable dropdown

**Job Variable / User Variable**

Select the variable to save the copied link into. Click the Refresh button to reload the list of available variables.

**Variable type** (data type)

The data type to use when saving the value. Available options: _String_, _Int32_, _Double_, _Boolean_. Default is _String_.

**Wait tab**

The wait tab controls how long the step should wait before performing the step and after performing the step (in milliseconds).
